"""Defines physical port classes and related items."""

# System imports

# Local source tree imports
from pyof.foundation.base import Enum, GenericBitMask, GenericStruct
from pyof.foundation.basic_types import (
    Char, FixedTypeList, HWAddress, Pad, UBInt16, UBInt32)
from pyof.foundation.constants import OFP_MAX_PORT_NAME_LEN

# Third-party imports

__all__ = ('ListOfPortDescProperties', 'ListOfPorts', 'OPFPort',
           'OPFPortConfig', 'OPFPortFeatures', 'OPFPortNo',
           'OPFPortState')


class OPFPortNo(Enum):
    """Port numbering.

    Ports are numbered starting from 1.
    """

    #: Maximum number of physical and logical switch ports.
    OFPP_MAX = 0xffffff00
    # Reserved OpenFlow port (fake output "ports")
    #: Send the packet out the input port. This reserved port must be
    #: explicitly used in order to send back out of the input port.
    OFPP_IN_PORT = 0xfffffff8
    #: Submit the packet to the first flow table
    #: NB: This destination port can only be used in packet-out messages.
    OFPP_TABLE = 0xfffffff9
    #: Process with normal L2/L3 switching.
    OFPP_NORMAL = 0xfffffffa
    #: All physical ports in VLAN, except input port and thos blocked or link
    #: down.
    OFPP_FLOOD = 0xfffffffb
    #: All physical ports except input port
    OFPP_ALL = 0xfffffffc
    #: Send to controller
    OFPP_CONTROLLER = 0xfffffffd
    #: Local openflow "port"
    OFPP_LOCAL = 0xfffffffe
    #: Wildcard port used only for flow mod (delete) and flow stats requests.
    #: Selects all flows regardless of output port (including flows with no
    #: output port).
    OFPP_ANY = 0xffffffff


class OPFPortDescPropType(Enum):
    """Port description property types."""

    # Ethernet property
    OFPPDPT_ETHERNET = 0
    # Optical property
    OFPPDPT_OPTICAL = 1
    # Experimenter property
    OFPPDPT_EXPERIMENTER = 0xfff


class OPFOpticalPortFeatures(GenericBitMask):
    """Features of optical ports available in switch."""

    # Receiver is tunable.
    OFPOPF_RX_TUNE = 1 << 0
    # Transmit is tunable.
    OFPOPF_TX_TUNE = 1 << 1
    # Power is configurable.
    OFPOPF_TX_PWR = 1 << 2
    # Use Frequency, not wavelength
    OFPOPF_USE_FREQ = 1 << 3


class OPFPortConfig(GenericBitMask):
    """Flags to indicate behavior of the physical port.

    These flags are used in :class:`Port` to describe the current
    configuration. They are used in the
    :class:`~pyof.v0x05.controller2switch.port_mod.PortMod`
    message to configure the port's behavior.

    The :attr:`OFPPC_PORT_DOWN` bit indicates that the port has been
    administratively brought down and should not be used by OpenFlow. The
    :attr:`~OFPPC_NO_RECV` bit indicates that packets received on that port
    should be ignored. The :attr:`OFPPC_NO_FWD` bit indicates that OpenFlow
    should not send packets to that port. The :attr:`OFPPC_NO_PACKET_IN` bit
    indicates that packets on that port that generate a table miss should never
    trigger a packet-in message to the controller.

    In general, the port config bits are set by the controller and not changed
    by the switch. Those bits may be useful for the controller to implement
    protocols such as STP or BFD. If the port config bits are changed by the
    switch through another administrative interface, the switch sends an
    :attr:`OFPT_PORT_STATUS` message to notify the controller of the change.
    """

    #: Port is administratively down.
    OFPPC_PORT_DOWN = 1 << 0
    #: Drop all packets received by port.
    OFPPC_NO_RECV = 1 << 2
    #: Drop packets forwarded to port.
    OFPPC_NO_FWD = 1 << 5
    #: Do not send packet-in msgs for port.
    OFPPC_NO_PACKET_IN = 1 << 6


class OPFPortFeatures(GenericBitMask):
    """Physical ports features.

    The curr, advertised, supported, and peer fields indicate link modes
    (speed and duplexity), link type (copper/fiber) and link features
    (autonegotiation and pause).

    Multiple of these flags may be set simultaneously. If none of the port
    speed flags are set, the max_speed or curr_speed are used.

    The curr_speed and max_speed fields indicate the current and maximum bit
    rate (raw transmission speed) of the link in kbps. The number should be
    rounded to match common usage. For example, an optical 10 Gb Ethernet port
    should have this field set to 10000000 (instead of 10312500), and an OC-192
    port should have this field set to 10000000 (instead of 9953280).

    The max_speed fields indicate the maximum configured capacity of the link,
    whereas the curr_speed indicates the current capacity. If the port is a LAG
    with 3 links of 1Gb/s capacity, with one of the ports of the LAG being
    down, one port auto-negotiated at 1Gb/s and 1 port auto-negotiated at
    100Mb/s, the max_speed is 3 Gb/s and the curr_speed is 1.1 Gb/s.
    """

    #: 10 Mb half-duplex rate support.
    OFPPF_10MB_HD = 1 << 0
    #: 10 Mb full-duplex rate support.
    OFPPF_10MB_FD = 1 << 1
    #: 100 Mb half-duplex rate support.
    OFPPF_100MB_HD = 1 << 2
    #: 100 Mb full-duplex rate support.
    OFPPF_100MB_FD = 1 << 3
    #: 1 Gb half-duplex rate support.
    OFPPF_1GB_HD = 1 << 4
    #: 1 Gb full-duplex rate support.
    OFPPF_1GB_FD = 1 << 5
    #: 10 Gb full-duplex rate support.
    OFPPF_10GB_FD = 1 << 6
    #: 40 Gb full-duplex rate support.
    OFPPF_40GB_FD = 1 << 7
    #: 100 Gb full-duplex rate support.
    OFPPF_100GB_FD = 1 << 8
    #: 1 Tb full-duplex rate support.
    OFPPF_1TB_FD = 1 << 9
    #: Other rate, not in the list
    OFPPF_OTHER = 1 << 10

    #: Copper medium.
    OFPPF_COPPER = 1 << 11
    #: Fiber medium.
    OFPPF_FIBER = 1 << 12
    #: Auto-negotiation.
    OFPPF_AUTONEG = 1 << 13
    #: Pause.
    OFPPF_PAUSE = 1 << 14
    #: Asymmetric pause.
    OFPPF_PAUSE_ASYM = 1 << 15


class OPFPortState(GenericBitMask):
    """Current state of the physical port.

    These are not configurable from the controller.

    The port state bits represent the state of the physical link or switch
    protocols outside of OpenFlow. The :attr:`~PortConfig.OFPPS_LINK_DOWN` bit
    indicates the the physical link is not present. The
    :attr:`~PortConfig.OFPPS_BLOCKED` bit indicates that a switch protocol
    outside of OpenFlow, such as 802.1D Spanning Tree, is preventing the use of
    that port with :attr:`~PortConfig.OFPP_FLOOD`.

    All port state bits are read-only and cannot be changed by the controller.
    When the port flags are changed, the switch sends an
    :attr:`v0x05.common.header.Type.OFPT_PORT_STATUS` message to notify the
    controller of the change.
    """

    #: Not physical link present.
    OFPPS_LINK_DOWN = 1 << 0
    #: Port is blocked.
    OFPPS_BLOCKED = 1 << 1
    #: Live for Fast Failover Group.
    OFPPS_LIVE = 1 << 2


# Classes
class OPFPortDescPropHeader(GenericStruct):
    """Common header for all port description properties."""

    # One of OFPPDPT_*
    port_desc_type = UBInt16()
    # Length in bytes of this property
    length = UBInt16()

    def __init__(self, port_desc_type=None, length=None):
        """Create the Header for Port Description Properties.

        Args:
            port_desc_type (int): The Port Description property type.
            length (int): The property's length.
        """
        super().__init__()
        self.port_desc_type = port_desc_type
        self.length = length


class ListOfPortDescProperties(FixedTypeList):
    """List of Port Description Properties.

    Represented by instances of PortDescPropHeader objects.
    """

    def __init__(self, items=None):
        """Create a ListOfActions with the optional parameters below.

        Args:
            items (~pyof.v0x05.common.action.ActionHeader):
                Instance or a list of instances.
        """
        super().__init__(pyof_class=OPFPortDescPropHeader, items=items)


class OPFPort(GenericStruct):
    """Description of a port.

    The port_no field uniquely identifies a port within a switch. The hw_addr
    field typically is the MAC address for the port;
    :data:`.OFP_MAX_ETH_ALEN` is 6. The name field is a null-terminated string
    containing a human-readable name for the interface.
    The value of :data:`.OFP_MAX_PORT_NAME_LEN` is 16.

    :attr:`curr`, :attr:`advertised`, :attr:`supported` and :attr:`peer` fields
    indicate link modes (speed and duplexity), link type (copper/fiber) and
    link features (autonegotiation and pause). They are bitmaps of
    :class:`PortFeatures` enum values that describe features.
    Multiple of these flags may be set simultaneously. If none of the port
    speed flags are set, the :attr:`max_speed` or :attr:`curr_speed` are used.
    """

    port_no = UBInt32()

    length = UBInt16()
    pad = Pad(2)
    hw_addr = HWAddress()
    pad2 = Pad(2)                               # Align to 64 bits
    name = Char(length=OFP_MAX_PORT_NAME_LEN)   # Null terminated
    config = UBInt32(enum_ref=OPFPortConfig)       # Bitmap of OFPPC_* flags
    state = UBInt32(enum_ref=OPFPortState)         # Bitmap of OFPPS_* flags

    properties = ListOfPortDescProperties()

    def __init__(self, port_no=None, hw_addr=None, name=None, config=None,
                 state=None, properties=ListOfPortDescProperties):
        """Create a Port with the optional parameters below.

        Args:
            port_no (int): Port number.
            hw_addr (HWAddress): Hardware address.
            name (str): Null-terminated name.

            config (~pyof.v0x05.common.port.PortConfig):
                Bitmap of OFPPC* flags.
            state (~pyof.v0x05.common.port.PortState): Bitmap of OFPPS* flags.
            properties (ListOfPortDescProperties): Port description property
             list - 0 or more properties.

        """
        super().__init__()
        self.port_no = port_no
        self.hw_addr = hw_addr
        self.name = name
        self.config = config
        self.state = state
        self.properties = properties
        self.length = UBInt16(self.__sizeof__())


class OPFPortDescPropEthernet(OPFPortDescPropHeader):
    """Ethernet port description property."""

    # Align to 64 bits
    pad4 = Pad(4)
    # Current features.
    curr = UBInt32(enum_ref=OPFPortFeatures)
    # Feature being advertised by port.
    advertised = UBInt32(enum_ref=OPFPortFeatures)
    # Features supported by the port.
    supported = UBInt32(enum_ref=OPFPortFeatures)
    # Features advertised by peer.
    peer = UBInt32(enum_ref=OPFPortFeatures)
    # Current port bitrate in kbps.
    curr_speed = UBInt32()
    # Max port bitrate in kbps.
    max_speed = UBInt32()

    def __init__(self, curr=OPFPortFeatures, advertised=OPFPortFeatures,
                 supported=OPFPortFeatures, peer=OPFPortFeatures,
                 curr_speed=None, max_speed=None):
        """Create the Port Description Property for Ethernet.

        Args:
            curr (int): Current features.
            advertised (int): Feature being advertised by port.
            supported (int): Features supported by the port.
            peer (int): Features advertised by peer.
            curr_speed (int): Current port bitrate in kbps.
            max_speed (int): Max port bitrate in kbps.
        """
        super().__init__(OPFPortDescPropType.OFPPDPT_ETHERNET)
        self.curr = curr
        self.advertised = advertised
        self.supported = supported
        self.peer = peer
        self.curr_speed = curr_speed
        self.max_speed = max_speed
        self.length = UBInt16(self.__sizeof__())


class PortDescPropOptical(OPFPortDescPropHeader):
    """Optical port description property."""

    # Align to 64 bits.
    pad4 = Pad(4)

    # Features supported by the port.
    supported = UBInt32()
    # Minimum TX Frequency/Wavelength.
    tx_min_freq_lmda = UBInt32()
    # Maximum TX Frequency/Wavelength.
    tx_max_freq_lmda = UBInt32()
    # TX Grid Spacing Frequency/Wavelength.
    tx_grid_freq_lmda = UBInt32()
    # Minimum RX Frequency/Wavelength.
    rx_min_freq_lmda = UBInt32()
    # Maximum RX Frequency/Wavelength.
    rx_max_freq_lmda = UBInt32()
    # RX Grid Spacing Frequency/Wavelength
    rx_grid_freq_lmda = UBInt32()
    # Minimum TX power
    tx_pwr_min = UBInt16()
    # Maximun TX power
    tx_pwr_max = UBInt16()

    def __init__(self, supported=None, tx_min_freq_lmda=None,
                 tx_max_freq_lmda=None, tx_grid_freq_lmda=None,
                 rx_min_freq_lmda=None, rx_max_freq_lmda=None,
                 rx_grid_freq_lmda=None, tx_pwr_min=None,  tx_pwr_max=None):
        """Create the Port Description Property for Optical.

        Args:
            supported (int): Features supported by the port.
            tx_min_freq_lmda (int): Minimum TX Frequency/Wavelength.
            tx_max_freq_lmda (int): Maximum TX Frequency/Wavelength.
            tx_grid_freq_lmda (int): TX Grid Spacing Frequency/Wavelength.
            rx_min_freq_lmda (int): Minimum RX Frequency/Wavelength.
            rx_max_freq_lmda (int): Maximum RX Frequency/Wavelength.
            rx_grid_freq_lmda (int): RX Grid Spacing Frequency/Wavelength.
            tx_pwr_min (int): Minimum TX power.
            tx_pwr_max (int): Maximun TX power.
        """
        super().__init__(OPFPortDescPropType.OFPPDPT_OPTICAL)
        self.supported = supported
        self.tx_min_freq_lmda = tx_min_freq_lmda
        self.tx_max_freq_lmda = tx_max_freq_lmda
        self.tx_grid_freq_lmda = tx_grid_freq_lmda
        self.rx_grid_freq_lmda = rx_grid_freq_lmda
        self.rx_min_freq_lmda = rx_min_freq_lmda
        self.rx_max_freq_lmda = rx_max_freq_lmda
        self.tx_pwr_min = tx_pwr_min
        self.tx_pwr_max = tx_pwr_max
        self.length = UBInt16(self.__sizeof__())


class PortDescPropExperimenter(OPFPortDescPropHeader):
    """Experimenter port description property."""

    # Experimenter ID which takes the same form as in ExperimenterHeader.
    experimenter = UBInt16()
    # Experimenter defined.
    exp_type = UBInt16()
    experimenter_data = UBInt32()

    def __init__(self, experimenter=None, exp_type=None,
                 experimenter_data=None):
        """Create the Port Description Property for Experimenter.

        Args:
            experimenter (int): Experimenter ID which takes the same
             form as in ExperimenterHeader.
            exp_type (int): Experimenter defined.
            experimenter_data (int): Experimenter Data.
            Followed by:
            - Exactly (length - 12) bytes containing the experimenter
             data, then
            - Exactly (length + 7) / 8 * 8 - (length) (between 0 and 7)
             bytes of all-zero bytes.
        """
        super().__init__(OPFPortDescPropType.OFPPDPT_EXPERIMENTER)
        self.experimenter = experimenter
        self.exp_type = exp_type
        self.experimenter_data = experimenter_data


class ListOfPorts(FixedTypeList):
    """List of Ports.

    Represented by instances of :class:`Port` and used on

    :class:`~pyof.v0x05.controller2switch.features_reply.FeaturesReply`/
    :class:`~pyof.v0x05.controller2switch.features_reply.SwitchFeatures`
    objects.
    """

    def __init__(self, items=None):
        """Create a ListOfPort with the optional parameters below.

        Args:

            items (:class:`list`, :class:`~pyof.v0x05.common.port.Port`):
                One :class:`~pyof.v0x04.common.port.Port` instance or list.

        """
        super().__init__(pyof_class=OPFPort,
                         items=items)
