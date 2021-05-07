"""Match strucutre and related enums.

An OpenFlow match is composed of a flow match header and a sequence of zero or
more flow match fields.
"""
# System imports
from enum import IntEnum
from math import ceil

# Local source tree imports
from pyof.foundation.base import GenericBitMask, GenericStruct
from pyof.foundation.basic_types import (
    BinaryData, FixedTypeList, Pad, UBInt8, UBInt16, UBInt32)
from pyof.foundation.exceptions import PackException, UnpackException

__all__ = ('Ipv6ExtHdrFlags', 'ListOfOxmHeader', 'OPFMatch', 'OPFMatchType',
           'OPFOxmClass', 'OxmExperimenterHeader', 'OPFOxmMatchFields',
           'OPFOxmOfbMatchField', 'OPFOxmTLV', 'VlanId')


class Ipv6ExtHdrFlags(GenericBitMask):
    """Bit definitions for IPv6 Extension Header pseudo-field."""

    #: "No next header" encountered.
    OFPIEH_NONEXT = 1 << 0
    #: Encrypted Sec Payload header present.
    OFPIEH_ESP = 1 << 1
    #: Authentication header present.
    OFPIEH_AUTH = 1 << 2
    #: 1 or 2 dest headers present.
    OFPIEH_DEST = 1 << 3
    #: Fragment header present.
    OFPIEH_FRAG = 1 << 4
    #: Router header present.
    OFPIEH_ROUTER = 1 << 5
    #: Hop-by-hop header present.
    OFPIEH_HOP = 1 << 6
    #: Unexpected repeats encountered.
    OFPIEH_UNREP = 1 << 7
    #: Unexpected sequencing encountered.
    OFPIEH_UNSEQ = 1 << 8


class OPFOxmOfbMatchField(IntEnum):
    """OXM Flow match field types for OpenFlow basic class.

    A switch is not required to support all match field types, just those
    listed in the Table 10. Those required match fields don’t need to be
    implemented in the same table lookup. The controller can query the switch
    about which other fields it supports.
    """

    #: Switch input port.
    OFPXMT_OFB_IN_PORT = 0
    #: Switch physical input port.
    OFPXMT_OFB_IN_PHY_PORT = 1
    #: Metadata passed between tables.
    OFPXMT_OFB_METADATA = 2
    #: Ethernet destination address.
    OFPXMT_OFB_ETH_DST = 3
    #: Ethernet source address.
    OFPXMT_OFB_ETH_SRC = 4
    #: Ethernet frame type.
    OFPXMT_OFB_ETH_TYPE = 5
    #: VLAN id.
    OFPXMT_OFB_VLAN_VID = 6
    #: VLAN priority.
    OFPXMT_OFB_VLAN_PCP = 7
    #: IP DSCP (6 bits in ToS field).
    OFPXMT_OFB_IP_DSCP = 8
    #: IP ECN (2 bits in ToS field).
    OFPXMT_OFB_IP_ECN = 9
    #: IP protocol.
    OFPXMT_OFB_IP_PROTO = 10
    #: IPv4 source address.
    OFPXMT_OFB_IPV4_SRC = 11
    #: IPv4 destination address.
    OFPXMT_OFB_IPV4_DST = 12
    #: TCP source port.
    OFPXMT_OFB_TCP_SRC = 13
    #: TCP destination port.
    OFPXMT_OFB_TCP_DST = 14
    #: UDP source port.
    OFPXMT_OFB_UDP_SRC = 15
    #: UDP destination port.
    OFPXMT_OFB_UDP_DST = 16
    #: SCTP source port.
    OFPXMT_OFB_SCTP_SRC = 17
    #: SCTP destination port.
    OFPXMT_OFB_SCTP_DST = 18
    #: ICMP type.
    OFPXMT_OFB_ICMPV4_TYPE = 19
    #: ICMP code.
    OFPXMT_OFB_ICMPV4_CODE = 20
    #: ARP opcode.
    OFPXMT_OFB_ARP_OP = 21
    #: ARP source IPv4 address.
    OFPXMT_OFB_ARP_SPA = 22
    #: ARP target IPv4 address.
    OFPXMT_OFB_ARP_TPA = 23
    #: ARP source hardware address.
    OFPXMT_OFB_ARP_SHA = 24
    #: ARP target hardware address.
    OFPXMT_OFB_ARP_THA = 25
    #: IPv6 source address.
    OFPXMT_OFB_IPV6_SRC = 26
    #: IPv6 destination address.
    OFPXMT_OFB_IPV6_DST = 27
    #: IPv6 Flow Label
    OFPXMT_OFB_IPV6_FLABEL = 28
    #: ICMPv6 type.
    OFPXMT_OFB_ICMPV6_TYPE = 29
    #: ICMPv6 code.
    OFPXMT_OFB_ICMPV6_CODE = 30
    #: Target address for ND.
    OFPXMT_OFB_IPV6_ND_TARGET = 31
    #: Source link-layer for ND.
    OFPXMT_OFB_IPV6_ND_SLL = 32
    #: Target link-layer for ND.
    OFPXMT_OFB_IPV6_ND_TLL = 33
    #: MPLS label.
    OFPXMT_OFB_MPLS_LABEL = 34
    #: MPLS TC.
    OFPXMT_OFB_MPLS_TC = 35
    #: MPLS BoS bit.
    OFPXMT_OFP_MPLS_BOS = 36
    #: PBB I-SID.
    OFPXMT_OFB_PBB_ISID = 37
    #: Logical Port Metadata.
    OFPXMT_OFB_TUNNEL_ID = 38
    #: IPv6 Extension Header pseudo-field
    OFPXMT_OFB_IPV6_EXTHDR = 39

    #: PBB UCA header field.
    OFPXMT_OFB_PBB_UCA = 41


class OPFMatchType(IntEnum):
    """Indicates the match structure in use.

    The match type is placed in the type field at the beginning of all match
    structures. The "OpenFlow Extensible Match" type corresponds to OXM TLV
    format described below and must be supported by all OpenFlow switches.
    Extensions that define other match types may be published on the ONF wiki.
    Support for extensions is optional
    """

    #: Deprecated
    OFPMT_STANDARD = 0
    #: OpenFlow Extensible Match
    OFPMT_OXM = 1


class OPFOxmClass(IntEnum):
    """OpenFlow Extensible Match (OXM) Class IDs.

    The high order bit differentiate reserved classes from member classes.
    Classes 0x0000 to 0x7FFF are member classes, allocated by ONF.
    Classes 0x8000 to 0xFFFE are reserved classes, reserved for
    standardisation.
    """

    #: Backward compatibility with NXM
    OFPXMC_NXM_0 = 0x0000
    #: Backward compatibility with NXM
    OFPXMC_NXM_1 = 0x0001
    #: Basic class for OpenFlow
    OFPXMC_OPENFLOW_BASIC = 0x8000
    #: Experimenter class
    OFPXMC_EXPERIMENTER = 0xFFFF


class VlanId(IntEnum):
    """Indicates conditions of the Vlan.

    The VLAN id is 12-bits, so we can use the entire 16 bits to indicate
    special conditions.
    """

    #: Bit that indicate that a VLAN id is set.
    OFPVID_PRESENT = 0x1000
    #: No VLAN id was set
    OFPVID_NONE = 0x0000


# Classes

class OPFOxmTLV(GenericStruct):
    """Oxm (OpenFlow Extensible Match) TLV."""

    oxm_class = UBInt16(enum_ref=OPFOxmClass)
    oxm_field_and_mask = UBInt8()
    oxm_length = UBInt8()
    oxm_value = BinaryData()

    def __init__(self, oxm_class=OPFOxmClass.OFPXMC_OPENFLOW_BASIC,
                 oxm_field=None, oxm_hasmask=False, oxm_value=None):
        """Create an OXM TLV struct with the optional parameters below.

        Args:
            oxm_class (OxmClass): Match class: member class or reserved class
            oxm_field (OxmMatchFields, OxmOfbMatchField): Match field within
                the class
            oxm_hasmask (bool): Set if OXM include a bitmask in payload
            oxm_value (bytes): OXM Payload

        """
        super().__init__()
        self.oxm_class = oxm_class
        self.oxm_field_and_mask = None
        self.oxm_length = None
        self.oxm_value = oxm_value
        # Attributes that are not packed
        self.oxm_field = oxm_field
        self.oxm_hasmask = oxm_hasmask

    def unpack(self, buff, offset=0):
        """Unpack the buffer into a OxmTLV.

        Args:
            buff (bytes): The binary data to be unpacked.
            offset (int): If we need to shift the beginning of the data.

        """
        super().unpack(buff, offset)
        # Recover field from field_and_hasmask.
        try:
            self.oxm_field = self._unpack_oxm_field()
        except ValueError as exception:
            raise UnpackException(exception)

        # The last bit of field_and_mask is oxm_hasmask
        self.oxm_hasmask = (self.oxm_field_and_mask & 1) == 1  # as boolean

        # Unpack oxm_value that has oxm_length bytes
        start = offset + 4  # 4 bytes: class, field_and_mask and length
        end = start + self.oxm_length
        self.oxm_value = buff[start:end]

    def _unpack_oxm_field(self):
        """Unpack oxm_field from oxm_field_and_mask.

        Returns:
            :class:`OxmOfbMatchField`, int: oxm_field from oxm_field_and_mask.

        Raises:
            ValueError: If oxm_class is OFPXMC_OPENFLOW_BASIC but
                :class:`OxmOfbMatchField` has no such integer value.

        """
        field_int = self.oxm_field_and_mask >> 1
        # We know that the class below requires a subset of the ofb enum
        if self.oxm_class == OPFOxmClass.OFPXMC_OPENFLOW_BASIC:
            return OPFOxmOfbMatchField(field_int)
        return field_int

    def _update_length(self):
        """Update length field.

        Update the oxm_length field with the packed payload length.

        """
        payload = type(self).oxm_value.pack(self.oxm_value)
        self.oxm_length = len(payload)

    def pack(self, value=None):
        """Join oxm_hasmask bit and 7-bit oxm_field."""
        if value is not None:
            return value.pack()

        # Set oxm_field_and_mask instance attribute
        # 1. Move field integer one bit to the left
        try:
            field_int = self._get_oxm_field_int()
        except ValueError as exception:
            raise PackException(exception)
        field_bits = field_int << 1
        # 2. hasmask bit
        hasmask_bit = self.oxm_hasmask & 1
        # 3. Add hasmask bit to field value
        self.oxm_field_and_mask = field_bits + hasmask_bit

        self._update_length()
        return super().pack(value)

    def _get_oxm_field_int(self):
        """Return a valid integer value for oxm_field.

        Used while packing.

        Returns:
            int: valid oxm_field value.

        Raises:
            ValueError: If :attribute:`oxm_field` is bigger than 7 bits or
                should be :class:`OxmOfbMatchField` and the enum has no such
                value.

        """
        if self.oxm_class == OPFOxmClass.OFPXMC_OPENFLOW_BASIC:
            return OPFOxmOfbMatchField(self.oxm_field).value
        elif not isinstance(self.oxm_field, int) or self.oxm_field > 127:
            raise ValueError('oxm_field above 127: "{self.oxm_field}".')
        return self.oxm_field


class OPFOxmMatchFields(FixedTypeList):
    """Generic Openflow EXtensible Match header.

    Abstract class that can be instantiated as Match or OxmExperimenterHeader.

    """

    def __init__(self, items=None):
        """Initialize ``items`` attribute.

        Args:
            items (OxmHeader): Instance or a list of instances.
        """
        super().__init__(pyof_class=OPFOxmTLV, items=items)


class OPFMatch(GenericStruct):
    """Describes the flow match header structure.

    These are the fields to match against flows.

    The :attr:`~type` field is set to :attr:`~MatchType.OFPMT_OXM` and

    :attr:`length` field is set to the actual length of match structure
    including all match fields. The payload of the OpenFlow match is a set of
    OXM Flow match fields.

    """

    # One of OFPMT_*
    match_type = UBInt16(enum_ref=OPFMatchType)
    # Length of Match (excluding padding)
    length = UBInt16()
    # 0 or more OXM match fields.
    oxm_match_fields = OPFOxmMatchFields()
    # Zero bytes - see above for sizing
    pad = Pad(4)

    def __init__(self, match_type=OPFMatchType.OFPMT_OXM,
                 length=None, oxm_match_fields=None):
        """Describe the flow match header structure.

        Args:
            match_type (MatchType): One of OFPMT_* (MatchType) items.
            length (int): Length of Match (excluding padding) followed by
                          Exactly (length - 4) (possibly 0) bytes containing
                          OXM TLVs, then exactly ((length + 7)/8*8 - length)
                          (between 0 and 7) bytes of all-zero bytes.
            oxm_match_fields (OxmMatchFields): Sample description.

        """
        super().__init__()
        self.match_type = match_type
        self.length = length
        self.oxm_match_fields = oxm_match_fields or OPFOxmMatchFields()
        self._update_match_length()

    def _update_match_length(self):
        """Update the match length field."""
        self.length = super().get_size()

    def pack(self, value=None):
        """Pack and complete the last byte by padding."""
        if isinstance(value, OPFMatch):
            return value.pack()
        elif value is None:
            self._update_match_length()
            packet = super().pack()
            return self._complete_last_byte(packet)
        raise PackException(f'Match can\'t unpack "{value}".')

    def _complete_last_byte(self, packet):
        """Pad until the packet length is a multiple of 8 (bytes)."""
        padded_size = self.get_size()
        padding_bytes = padded_size - len(packet)
        if padding_bytes > 0:
            packet += Pad(padding_bytes).pack()
        return packet

    def get_size(self, value=None):
        """Return the packet length including the padding (multiple of 8)."""
        if isinstance(value, OPFMatch):
            return value.get_size()
        elif value is None:
            current_size = super().get_size()
            return ceil(current_size / 8) * 8
        raise ValueError(f'Invalid value "{value}" for Match.get_size()')

    def unpack(self, buff, offset=0):
        """Discard padding bytes using the unpacked length attribute."""
        begin = offset
        size = 0
        for name, value in list(self.get_class_attributes())[:-1]:
            size = self._unpack_attribute(name, value, buff, begin)
            begin += size
        self._unpack_attribute('oxm_match_fields',
                               type(self).oxm_match_fields,
                               buff[:offset+self.length - len(Pad(4))],
                               begin - size)

    def get_field(self, field_type):
        """Return the value for the 'field_type' field in oxm_match_fields.

        Args:

            field_type (~pyof.v0x05.common.flow_match.OxmOfbMatchField,
                        ~pyof.v0x05.common.flow_match.OxmMatchFields):

                The type of the OXM field you want the value.

        Returns:
            The integer number of the 'field_type' if it exists. Otherwise
            return None.

        """
        for field in self.oxm_match_fields:
            if field.oxm_field == field_type:
                return field.oxm_value

        return None


class OxmExperimenterHeader(GenericStruct):
    """Header for OXM experimenter match fields."""

    #: oxm_class = OFPXMC_EXPERIMENTER
    oxm_header = UBInt32(OPFOxmClass.OFPXMC_EXPERIMENTER,
                         enum_ref=OPFOxmClass)
    #: Experimenter ID which takes the same form as in struct
    #:     ofp_experimenter_header
    experimenter = UBInt32()

    def __init__(self, experimenter=None):
        """Initialize ``experimenter`` attribute.

        Args:
            experimenter (int): Experimenter ID which takes the same form as
              in struct ofp_experimenter_header

        """
        super().__init__()
        self.experimenter = experimenter


class ListOfOxmHeader(FixedTypeList):
    """List of Openflow Extensible Match header instances.

    Represented by instances of OxmHeader.

    """

    def __init__(self, items=None):
        """Initialize ``items`` attribute.

        Args:
            items (OxmHeader): Instance or a list of instances.

        """
        super().__init__(pyof_class=OPFOxmTLV, items=items)
