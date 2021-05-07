"""Defines Experimenter message."""

# System imports

# Third-party imports

from pyof.foundation.base import GenericMessage
from pyof.foundation.basic_types import BinaryData, UBInt32
from pyof.v0x05.common.header import Header, Type

__all__ = ('OPFExperimenterHeader',)

# Classes


class OPFExperimenterHeader(GenericMessage):
    """OpenFlow Experimenter message.

    The experimenter field is a 32-bit value that uniquely identifies the
    experimenter. If the most significant byte is zero, the next three bytes
    are the experimenter’s IEEE OUI. If the most significant byte is not zero,
    it is a value allocated by the Open Networking Foundation. If experimenter
    does not have (or wish to use) their OUI, they should contact the Open
    Networking Foundation to obtain an unique experimenter ID.

    The rest of the body is uninterpreted by standard OpenFlow processing and
    is arbitrarily defined by the corresponding experimenter.

    If a switch does not understand an experimenter extension, it must send an
    OFPT_ERROR message with a OFPBRC_BAD_EXPERIMENTER error code and
    OFPET_BAD_REQUEST error type.
    """

    header = Header(message_type=Type.OFPT_EXPERIMENTER)
    experimenter = UBInt32()
    exp_type = UBInt32()
    experimenter_data = BinaryData()

    def __init__(self, xid=None, experimenter=None, exp_type=None,
                 experimenter_data=b''):
        """Create a ExperimenterHeader with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            experimenter (int): Vendor ID:
                MSB 0: low-order bytes are IEEE OUI.
                MSB != 0: defined by ONF.
            exp_type (int): Experimenter defined.
            experimenter_data (Binary): Experimenter-defined arbitrary
             additional data.
        """
        super().__init__(xid)
        self.experimenter = experimenter
        self.exp_type = exp_type
        self.experimenter_data = experimenter_data
