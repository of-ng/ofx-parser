"""Defines actions that may be associated with flows packets."""
# System imports
from enum import IntEnum
from math import ceil

# Local source tree imports
from pyof.foundation.base import GenericStruct
from pyof.foundation.basic_types import (
    FixedTypeList, Pad, UBInt8, UBInt16, UBInt32)
from pyof.v0x05.common.flow_match import OPFOxmTLV

# Third-party imports

__all__ = ('OPFActionExperimenterHeader', 'OPFActionGroup', 'OPFActionHeader',
           'OPFActionCopyTTLIn', 'OPFActionCopyTTLOut', 'OPFActionDecMPLSTTL',
           'OPFActionSetMPLSTTL', 'OPFActionDecNWTTL', 'OPFActionSetNWTTL',
           'OPFActionOutput', 'OPFActionPopMPLS', 'OPFActionPopPBB',
           'OPFActionPopVLAN', 'OPFActionPush', 'OPFActionSetField',
           'OPFActionSetQueue', 'OPFActionType', 'ControllerMaxLen',
           'ListOfActions')

# Enums


class OPFActionType(IntEnum):
    """Actions associated with flows and packets."""

    #: Output to switch port.
    OFPAT_OUTPUT = 0
    #: Copy TTL "outwards" -- from next-to-outermost to outermost
    OFPAT_COPY_TTL_OUT = 11
    #: Copy TTL "inwards" -- from outermost to next-to-outermost
    OFPAT_COPY_TTL_IN = 12
    #: MPLS TTL
    OFPAT_SET_MPLS_TTL = 15
    #: Decrement MPLS TTL
    OFPAT_DEC_MPLS_TTL = 16
    #: Push a new VLAN tag
    OFPAT_PUSH_VLAN = 17
    #: Pop the outer VLAN tag
    OFPAT_POP_VLAN = 18
    #: Push a new MPLS tag
    OFPAT_PUSH_MPLS = 19
    #: Pop the outer MPLS tag
    OFPAT_POP_MPLS = 20
    #: Set queue id when outputting to a port
    OFPAT_SET_QUEUE = 21
    #: Apply group.
    OFPAT_GROUP = 22
    #: IP TTL.
    OFPAT_SET_NW_TTL = 23
    #: Decrement IP TTL.
    OFPAT_DEC_NW_TTL = 24
    #: Set a header field using OXM TLV format.
    OFPAT_SET_FIELD = 25
    #: Push a new PBB service tag (I-TAG)
    OFPAT_PUSH_PBB = 26
    #: Pop the outer PBB service tag (I-TAG)
    OFPAT_POP_PBB = 27
    #: Experimenter type
    OFPAT_EXPERIMENTER = 0xffff


class ControllerMaxLen(IntEnum):
    """A max_len of OFPCML_NO_BUFFER means not to buffer.

    The packet should be sent.
    """

    #: Maximum max_len value which can be used to request a specific byte
    #: length.
    OFPCML_MAX = 0xffe5
    #: indicates that no buffering should be applied and the whole packet is
    #: to be sent to the controller.
    OFPCML_NO_BUFFER = 0xffff


# Classes


class OPFActionHeader(GenericStruct):
    """Action header that is common to all actions.

    The length includes the header and any padding used to make the action
    64-bit aligned.
    NB: The length of an action *must* always be a multiple of eight.
    """

    #: One of OFPAT_*.

    action_type = UBInt16(enum_ref=OPFActionType)
    #: Length of action, including this header. This is the length of actions,
    #: including any padding to make it 64-bit aligned.
    length = UBInt16()

    _allowed_types = ()

    def __init__(self, action_type=None, length=None):
        """Create an ActionHeader with the optional parameters below.

        Args:
            action_type (~pyof.v0x05.common.action.ActionType):
                The type of the action.
            length (int): Length of action, including this header.
        """
        super().__init__()
        self.action_type = action_type
        self.length = length

    def get_size(self, value=None):
        """Return the action length including the padding (multiple of 8)."""
        if isinstance(value, OPFActionHeader):
            return value.get_size()
        elif value is None:
            current_size = super().get_size()
            return ceil(current_size / 8) * 8
        raise ValueError(f'Invalid value "{value}" for Action*.get_size()')

    def unpack(self, buff, offset=0):
        """Unpack a binary message into this object's attributes.

        Unpack the binary value *buff* and update this object attributes based
        on the results.

        Args:
            buff (bytes): Binary data package to be unpacked.
            offset (int): Where to begin unpacking.

        Raises:
            Exception: If there is a struct unpacking error.

        """
        self.action_type = UBInt16(enum_ref=OPFActionType)
        self.action_type.unpack(buff, offset)

        for cls in OPFActionHeader.__subclasses__():
            if self.action_type.value in cls.get_allowed_types():
                self.__class__ = cls
                break

        super().unpack(buff, offset)

    @classmethod
    def get_allowed_types(cls):
        """Return allowed types for the class."""
        return cls._allowed_types


class OPFActionExperimenterHeader(OPFActionHeader):
    """Action structure for OFPAT_EXPERIMENTER."""

    # Experimenter ID
    experimenter = UBInt32()

    _allowed_types = (OPFActionType.OFPAT_EXPERIMENTER, )

    def __init__(self, length=None, experimenter=None):
        """Create ActionExperimenterHeader with the optional parameters below.

        Args:
            experimenter (int): The experimenter field is the Experimenter ID,
            which takes the same form as in struct ofp_experimenter.
        """
        super().__init__(action_type=OPFActionType.OFPAT_EXPERIMENTER)
        self.length = length
        self.experimenter = experimenter


class OPFExperimenterStruct(GenericStruct):
    """Typical Experimenter structure."""

    # Experimenter ID:
    # - MSB 0: low-order bytes are IEEE OUI
    # - MSB != 0: defined by ONF
    experimenter = UBInt32()
    # Experimenter defined
    exp_type = UBInt32()

    experimenter_data = UBInt8()


class OPFActionGroup(OPFActionHeader):
    """Action structure for OFPAT_GROUP."""

    # Group identifier.

    group_id = UBInt32()

    _allowed_types = (OPFActionType.OFPAT_GROUP, )

    def __init__(self, group_id=None):
        """Create an ActionGroup with the optional parameters below.

        Args:
            group_id (int): The group_id indicates the group used to process
                this packet. The set of buckets to apply depends on the group
                type.
        """
        super().__init__(action_type=OPFActionType.OFPAT_GROUP, length=8)
        self.group_id = group_id


class OPFActionDecMPLSTTL(OPFActionHeader):
    """Action structure for OFPAT_DEC_MPLS_TTL."""

    # Pad to 64 bits

    pad = Pad(4)

    _allowed_types = (OPFActionType.OFPAT_DEC_MPLS_TTL, )

    def __init__(self):
        """Create an ActionDecMPLSTTL."""
        super().__init__(action_type=OPFActionType.OFPAT_DEC_MPLS_TTL,
                         length=8)


class OPFActionSetMPLSTTL(OPFActionHeader):
    """Action structure for OFPAT_SET_MPLS_TTL."""

    # MPLS TTL
    mpls_ttl = UBInt8()

    pad = Pad(3)

    _allowed_types = (OPFActionType.OFPAT_SET_MPLS_TTL, )

    def __init__(self, mpls_ttl=None):
        """Create an ActionSetMPLSTTL with the optional parameters below.

        Args:
            mpls_ttl (int): The mpls_ttl field is the MPLS TTL to set.
        """
        super().__init__(action_type=OPFActionType.OFPAT_SET_MPLS_TTL,
                         length=8)
        self.mpls_ttl = mpls_ttl


class OPFActionCopyTTLIn(OPFActionHeader):
    """Action structure for OFPAT_COPY_TTL_IN."""

    pad = Pad(4)

    _allowed_types = (OPFActionType.OFPAT_COPY_TTL_IN, )

    def __init__(self):
        """Create an ActionCopyTTLIn."""
        super().__init__(action_type=OPFActionType.OFPAT_COPY_TTL_IN,
                         length=8)


class OPFActionCopyTTLOut(OPFActionHeader):
    """Action structure for OFPAT_COPY_TTL_OUT."""

    pad = Pad(4)

    _allowed_types = (OPFActionType.OFPAT_COPY_TTL_OUT, )

    def __init__(self):
        """Create an ActionCopyTTLOut."""
        super().__init__(action_type=OPFActionType.OFPAT_COPY_TTL_OUT,
                         length=8)


class OPFActionPopVLAN(OPFActionHeader):
    """Action structure for OFPAT_POP_VLAN."""

    pad = Pad(4)

    _allowed_types = (OPFActionType.OFPAT_POP_VLAN, )

    def __init__(self):
        """Create an ActionPopVLAN."""
        super().__init__(action_type=OPFActionType.OFPAT_POP_VLAN, length=8)


class OPFActionPopPBB(OPFActionHeader):
    """Action structure for OFPAT_POP_PBB."""

    pad = Pad(4)

    _allowed_types = (OPFActionType.OFPAT_POP_PBB, )

    def __init__(self):
        """Create an ActionPopPBB."""
        super().__init__(action_type=OPFActionType.OFPAT_POP_PBB, length=8)


class OPFActionDecNWTTL(OPFActionHeader):
    """Action structure for OFPAT_DEC_NW_TTL."""

    pad = Pad(4)

    _allowed_types = (OPFActionType.OFPAT_DEC_NW_TTL, )

    def __init__(self):
        """Create a ActionDecNWTTL."""
        super().__init__(action_type=OPFActionType.OFPAT_DEC_NW_TTL, length=8)


class OPFActionSetNWTTL(OPFActionHeader):
    """Action structure for OFPAT_SET_NW_TTL."""

    # IP TTL
    nw_ttl = UBInt8()

    pad = Pad(3)

    _allowed_types = (OPFActionType.OFPAT_SET_NW_TTL, )

    def __init__(self, nw_ttl=None):
        """Create an ActionSetNWTTL with the optional parameters below.

        Args:
            nw_ttl (int): the TTL address to set in the IP header.

        """
        super().__init__(action_type=OPFActionType.OFPAT_SET_NW_TTL, length=8)
        self.nw_ttl = nw_ttl


class OPFActionOutput(OPFActionHeader):
    """Action structure for OFPAT_OUTPUT.

    When the ’port’ is the OFPP_CONTROLLER, ’max_len’ indicates the max
    number of bytes to send. A ’max_len’ of zero means no bytes of the
    packet should be sent. A ’max_len’ of OFPCML_NO_BUFFER means that
    the packet is not buffered and the complete packet is to be sent to
    the controller.

    """

    # Extend the ActionHeader.
    # Output port.
    port = UBInt32()
    # Max length to send to controller.
    max_length = UBInt16()
    # Pad to 64 bits.

    pad = Pad(6)

    _allowed_types = (OPFActionType.OFPAT_OUTPUT, )

    def __init__(self, port=None,
                 max_length=ControllerMaxLen.OFPCML_NO_BUFFER):
        """Create a ActionOutput with the optional parameters below.

        Args:
            port (:class:`Port` or :class:`int`): Output port.
            max_length (int): Max length to send to controller.
        """
        super().__init__(action_type=OPFActionType.OFPAT_OUTPUT, length=16)
        self.port = port
        self.max_length = max_length


class OPFActionPopMPLS(OPFActionHeader):
    """Action structure for OFPAT_POP_MPLS."""

    # Ethertype
    ethertype = UBInt16()

    pad = Pad(2)

    _allowed_types = (OPFActionType.OFPAT_POP_MPLS, )

    def __init__(self, ethertype=None):
        """Create an ActionPopMPLS with the optional parameters below.

        Args:
            ethertype (int): indicates the Ethertype of the payload.
        """
        super().__init__(action_type=OPFActionType.OFPAT_POP_MPLS)
        self.ethertype = ethertype


class OPFActionPush(OPFActionHeader):
    """Action structure for OFPAT_PUSH_[VLAN/MPLS/PBB]."""

    # Ethertype
    ethertype = UBInt16()

    pad = Pad(2)

    _allowed_types = (OPFActionType. OFPAT_PUSH_VLAN,
                      OPFActionType.OFPAT_PUSH_MPLS,
                      OPFActionType.OFPAT_PUSH_PBB, )

    def __init__(self, action_type=None, ethertype=None):
        """Create a ActionPush with the optional parameters below.

        Args:
            action_type (:class:`ActionType`): indicates which tag will be
                pushed (VLAN, MPLS, PBB).
            ethertype (int): indicates the Ethertype of the new tag.
        """
        super().__init__(action_type, length=8)
        self.ethertype = ethertype


class OPFActionSetField(OPFActionHeader):
    """Action structure for OFPAT_SET_FIELD."""

    # <editor-fold desc="Description">
    # </editor-fold>

    # OXM TLV - Make compiler happy

    field = OPFOxmTLV()

    _allowed_types = (OPFActionType.OFPAT_SET_FIELD, )

    def __init__(self, length=None, field=None):
        """Create a ActionSetField with the optional parameters below.

        Args:
            length (int): length padded to 64 bits, followed by exactly
                          oxm_len bytes containing a single OXM TLV, then
                          exactly ((oxm_len + 4) + 7)/8*8 - (oxm_len + 4)
                          (between 0 and 7) bytes of all-zero bytes
            field (:class:`OxmTLV`): OXM field and value.
        """
        super().__init__(action_type=OPFActionType.OFPAT_SET_FIELD,
                         length=length)
        self.field = OPFOxmTLV() if field is None else field

    def pack(self, value=None):
        """Pack this structure updating the length and padding it."""
        self._update_length()
        packet = super().pack()
        return self._complete_last_byte(packet)

    def _update_length(self):
        """Update the length field of the struct."""
        action_length = 4 + len(self.field.pack())
        overflow = action_length % 8
        self.length = action_length
        if overflow:
            self.length = action_length + 8 - overflow

    def _complete_last_byte(self, packet):
        """Pad until the packet length is a multiple of 8 (bytes)."""
        padded_size = self.length
        padding_bytes = padded_size - len(packet)
        if padding_bytes > 0:
            packet += Pad(padding_bytes).pack()
        return packet


class OPFActionSetQueue(OPFActionHeader):
    """Action structure for OFPAT_SET_QUEUE."""

    # Queue id for packets.

    queue_id = UBInt32()

    _allowed_types = (OPFActionType.OFPAT_SET_QUEUE, )

    def __init__(self, queue_id=None):
        """Create an ActionSetQueue with the optional parameters below.

        Args:
            queue_id (int): The queue_id send packets to given queue on port.
        """
        super().__init__(action_type=OPFActionType.OFPAT_SET_QUEUE, length=8)
        self.queue_id = queue_id


class ListOfActions(FixedTypeList):
    """List of actions.

    Represented by instances of ActionHeader and used on ActionHeader objects.
    """

    def __init__(self, items=None):
        """Create a ListOfActions with the optional parameters below.

        Args:
            items (~pyof.v0x05.common.action.ActionHeader):
                Instance or a list of instances.
        """
        super().__init__(pyof_class=OPFActionHeader, items=items)
