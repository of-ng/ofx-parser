"""Defines a Request Forward Header."""

#: System imports.

from pyof.foundation.base import Enum, GenericStruct
from pyof.v0x05.common.header import Header, Type

#: Third-party imports.


__all__ = ('RequestForwardHeader', 'RequestForwardReason')


# Enums

class RequestForwardReason(Enum):
    """Request forward reason."""

    #: Forward group mod requests.
    OFPRFR_GROUP_MOD = 0
    #: Forward meter mod requests.
    OFPRFR_METER_MOD = 1


class RequestForwardHeader(GenericStruct):
    """Group/Meter request forwarding."""

    # :class:`~.header.Header`: OpenFlow Header
    # :class:`~.header.Type`: OpenFlow Type
    header = Header(Type.OFPT_REQUESTFORWARD)
    # :class:`~.header.Header`: OpenFlow Header
    request = Header()

    def __init__(self, header=Header(Type.OFPT_REQUESTFORWARD),
                 request=Header):
        """Create an instance of the header.

        Args:
            header (:class: `~pyof.v0x05.common.header.Header`):
            :class: `~pyof.v0x05.common.header.Type` OFPT_REQUESTFORWARD.
            request (:class: `~pyof.v0x05.common.header.Header`):
            Request being forwarded.
        """
        super().__init__()
        self.header = header
        self.request = request
