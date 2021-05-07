"""Defines Hello message."""

# System imports

from pyof.foundation.base import Enum, GenericMessage, GenericStruct
from pyof.foundation.basic_types import BinaryData, FixedTypeList, UBInt16
from pyof.foundation.exceptions import PackException
from pyof.v0x05.common.header import Header, Type

# Third-party imports

__all__ = ('Hello', 'HelloElemType',
           'HelloElemVersionBitmap', 'ListOfHelloElements',
           'OPFHelloElemHeader')

# Enums


class HelloElemType(Enum):
    """Hello element types."""

    #: Bitmap of version supported.
    OFPHET_VERSIONBITMAP = 1


# Classes

class OPFHelloElemHeader(GenericStruct):
    """Common header for all Hello Elements."""

    hello_element_type = UBInt16()
    # Length in bytes of element, including this header, excluding padding.
    length = UBInt16()
    # This variable does NOT appear in 1.4 specification
    # content = BinaryData()

    def __init__(self, hello_element_type=None, length=None):
        """Create a HelloElemHeader with the optional parameters below.

        Args:
            hello_element_type: One of OFPHET_*.
            length: Length in bytes of the element, including this header,
                excluding padding.
        """
        super().__init__()
        self.hello_element_type = hello_element_type
        self.length = length

    def pack(self, value=None):
        """Update the length and pack the message into binary data.

        Returns:
            bytes: A binary data that represents the Message.

        Raises:
            Exception: If there are validation errors.

        """
        if value is None:
            self.update_length()
            return super().pack()
        elif isinstance(value, type(self)):
            return value.pack()
        else:
            msg = "{} is not an instance of {}".format(value,
                                                       type(self).__name__)
            raise PackException(msg)

    def update_length(self):
        """Update length attribute."""
        self.length = self.get_size()

    def unpack(self, buff=None, offset=0):
        """Unpack *buff* into this object.

        This method will convert a binary data into a readable value according
        to the attribute format.

        Args:
            buff (bytes): Binary buffer.
            offset (int): Where to begin unpacking.

        Raises:
            :exc:`~.exceptions.UnpackException`: If unpack fails.

        """
        # length = UBInt16()
        self.length.unpack(buff, offset=offset+2)

        super().unpack(buff[:offset+self.length.value], offset)


class ListOfHelloElements(FixedTypeList):
    """List of Hello elements.

    Represented by instances of HelloElemHeader and used on Hello
    objects.
    """

    def __init__(self, items=None):
        """Create a ListOfHelloElements with the optional parameters below.

        Args:
            items (HelloElemHeader): Instance or a list of instances.
        """
        super().__init__(pyof_class=OPFHelloElemHeader, items=items)


class Hello(GenericMessage):
    """OpenFlow Hello Message OFPT_HELLO.

    This message includes zero or more hello elements having variable size.
    Unknown element types must be ignored/skipped, to allow for future
    extensions.
    """

    header = Header(Type.OFPT_HELLO)

    #: Hello element list
    elements = ListOfHelloElements()

    def __init__(self, xid=None, elements=None):
        """Create a Hello with the optional parameters below.

        Args:
            xid (int): xid to be used on the message header.
            elements: List of elements - 0 or more
        """
        super().__init__(xid)
        self.elements = elements


class HelloElemVersionBitmap(OPFHelloElemHeader):
    """Version bitmap Hello Element.

    The bitmaps field indicates the set of versions
    of the OpenFlow switch protocol a device supports,
    and may be used during version negotiation.
    """

    bitmaps = BinaryData()

    def __init__(self, length=None, bitmaps=None):
        """Initialize the class with the needed values.

        Args:
            length(int): Followed by:
            - Exactly (length - 4) bytes containing the bitmaps, then
            - Exactly (length + 7) / 8 * 8 - (length) (Between 0 and 7)
            bytes of all-zero bytes.

            bitmaps(binary): List of bitmaps - supported versions.
        """
        super().__init__(HelloElemType.OFPHET_VERSIONBITMAP, length)
        self.bitmaps = bitmaps
