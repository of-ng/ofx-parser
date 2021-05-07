"""Defines Header classes and related items."""

# System imports
from enum import IntEnum

# Local source tree imports
from pyof.foundation.base import GenericStruct
from pyof.foundation.basic_types import UBInt8, UBInt16, UBInt32
from pyof.v0x05.common.constants import OFP_VERSION

# Third-party imports

__all__ = ('Header', 'Type')

# Enums


class Type(IntEnum):
    """Enumeration of Message Types."""

    # Symmetric/Immutable messages

    OFPT_HELLO = 0
    OFPT_ERROR = 1
    OFPT_ECHO_REQUEST = 2
    OFPT_ECHO_REPLY = 3
    OFPT_EXPERIMENTER = 4

    # Switch configuration messages
    # Controller/Switch messages
    OFPT_FEATURES_REQUEST = 5
    OFPT_FEATURES_REPLY = 6
    OFPT_GET_CONFIG_REQUEST = 7
    OFPT_GET_CONFIG_REPLY = 8
    OFPT_SET_CONFIG = 9

    # Async messages
    OFPT_PACKET_IN = 10
    OFPT_FLOW_REMOVED = 11
    OFPT_PORT_STATUS = 12

    # Controller command messages
    # Controller/Switch message
    OFPT_PACKET_OUT = 13
    OFPT_FLOW_MOD = 14
    OFPT_GROUP_MOD = 15
    OFPT_PORT_MOD = 16
    OFPT_TABLE_MOD = 17

    # Multipart messages.
    # Controller/Switch message
    OFPT_MULTIPART_REQUEST = 18
    OFPT_MULTIPART_REPLY = 19

    # Barrier messages
    # Controller/Switch message
    OFPT_BARRIER_REQUEST = 20
    OFPT_BARRIER_REPLY = 21

    # Queue Configuration messages
    # Controller/Switch message

    # OFPT_QUEUE_GET_CONFIG_REQUEST = 22
    # OFPT_QUEUE_GET_CONFIG_REPLY = 23

    # Controller role change request message
    # Controller/Switch message
    OFPT_ROLE_REQUEST = 24
    OFPT_ROLE_REPLY = 25

    # Asynchronous message configuration
    # Controller/Switch message
    OFPT_GET_ASYNC_REQUEST = 26
    OFPT_GET_ASYNC_REPLY = 27
    OFPT_SET_ASYNC = 28

    # Meters and rate limiters configuration messages
    # Controller/Switch message
    OFPT_METER_MOD = 29

    # Controller role change event messages
    # Async message
    OFPT_ROLE_STATUS = 30

    # Asynchronous message
    # Async message
    OFPT_TABLE_STATUS = 31

    # Request forwarding by switch
    # Async message
    OFPT_REQUESTFORWARD = 32

    # Bundle operations (Multiple messages as a single operation)
    # Controller/Switch message
    OFPT_BUNDLE_CONTROL = 33
    OFPT_BUNDLE_ADD_MESSAGE = 34


# Classes

class Header(GenericStruct):
    """Representation of an OpenFlow message Header."""

    version = UBInt8(OFP_VERSION)
    message_type = UBInt8(enum_ref=Type)
    length = UBInt16()
    xid = UBInt32()

    def __init__(self, message_type=None, length=None, xid=None):
        """Create a Header with the optional parameters below.

        Args:
            message_type (~pyof.v0x05.common.header.Type):
                One of the OFPT_* constants.
            length (int): Length including this ofp_header.
            xid (int): Transaction id associated with this packet. Replies use
                the same id as was in the request to facilitate pairing.
        """
        super().__init__()
        self.message_type = message_type
        self.length = length
        self.xid = xid
