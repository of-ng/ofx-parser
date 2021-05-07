"""Defines an Error Message."""

# System imports

from pyof.foundation import exceptions
from pyof.foundation.base import Enum, GenericMessage
from pyof.foundation.basic_types import BinaryData, UBInt16, UBInt32
from pyof.v0x05.common.header import Header, Type

# Third-party imports


__all__ = ('OPFBadActionCode', 'OPFBadInstructionCode', 'OPFBadMatchCode',
           'OPFErrorType', 'OPFFlowModFailedCode', 'OPFGroupModFailedCode',
           'OPFHelloFailedCode', 'OPFMeterModFailedCode',
           'OPFPortModFailedCode', 'OPFQueueOpFailedCode',
           'OPFRoleRequestFailedCode', 'OPFSwitchConfigFailedCode',
           'OPFTableFeaturesFailedCode', 'OPFTableModFailedCode',
           'OPFGenericFailedCode', 'OPFBadPropertyCode',
           'OPFAsyncConfigFailedCode', 'OPFFlowMonitorFailedCode',
           'OPFBundleFailedCode')

# Enums


class OPFGenericFailedCode(Enum):
    """Error_msg 'code' values for OFPET_BAD_ACTION.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unknown error
    GENERIC_ERROR = 0


class OPFBadActionCode(Enum):
    """Error_msg 'code' values for OFPET_BAD_ACTION.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unknown action type.
    OFPBAC_BAD_TYPE = 0
    #: Length problem in actions.
    OFPBAC_BAD_LEN = 1
    #: Unknown experimenter id specified.
    OFPBAC_BAD_EXPERIMENTER = 2
    #: Unknown action for experimenter id.
    OFPBAC_BAD_EXP_TYPE = 3
    #: Problem validating output port.
    OFPBAC_BAD_OUT_PORT = 4
    #: Bad action argument.
    OFPBAC_BAD_ARGUMENT = 5
    #: Permissions error.
    OFPBAC_EPERM = 6
    #: Can’t handle this many actions.
    OFPBAC_TOO_MANY = 7
    #: Problem validating output queue.
    OFPBAC_BAD_QUEUE = 8
    #: Invalid group id in forward action.
    OFPBAC_BAD_OUT_GROUP = 9
    #: Action can’t apply for this match, or Set-Field missing prerequisite.
    OFPBAC_MATCH_INCONSISTENT = 10
    #: Action order is unsupported for the action list in an Apply-Actions
    #:  instruction.
    OFPBAC_UNSUPPORTED_ORDER = 11
    #: Actions uses an unsupported tag/encap.
    OFPBAC_BAD_TAG = 12
    #: Unsupported type in SET_FIELD action.
    OFPBAC_BAD_SET_TYPE = 13
    #: Length problem in SET_FIELD action.
    OFPBAC_BAD_SET_LEN = 14
    #: Bad argument in SET_FIELD action.
    OFPBAC_BAD_SET_ARGUMENT = 15


class OPFBadInstructionCode(Enum):
    """Error_msg 'code' values for OFPET_BAD_INSTRUCTION.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unknown instruction.
    OFPBIC_UNKNOWN_INST = 0
    #: Switch or table does not support the instruction.
    OFPBIC_UNSUP_INST = 1
    #: Invalid Table-ID specified.
    OFPBIC_BAD_TABLE_ID = 2
    #: Metadata value unsupported by datapath.
    OFPBIC_UNSUP_METADATA = 3
    #: Metadata mask value unsupported by datapath.
    OFPBIC_UNSUP_METADATA_MASK = 4
    #: Unknown experimenter id specified.
    OFPBIC_BAD_EXPERIMENTER = 5
    #: Unknown instruction for experimenter id.
    OFPBIC_BAD_EXP_TYPE = 6
    #: Length problem in instructions.
    OFPBIC_BAD_LEN = 7
    #: Permissions error.
    OFPBIC_EPERM = 8
    #: Duplicate instruction.
    OFPBIC_DUP_INST = 9


class OPFBadMatchCode(Enum):
    """Error_msg 'code' values for OFPET_BAD_MATCH.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unsupported match type specified by the match
    OFPBMC_BAD_TYPE = 0
    #: Length problem in match.
    OFPBMC_BAD_LEN = 1
    #: Match uses an unsupported tag/encap.
    OFPBMC_BAD_TAG = 2
    #: Unsupported datalink addr mask - switch does not support arbitrary
    #: datalink address mask.
    OFPBMC_BAD_DL_ADDR_MASK = 3
    #: Unsupported network addr mask - switch does not support arbitrary
    #: network address mask.
    OFPBMC_BAD_NW_ADDR_MASK = 4
    #: Unsupported combination of fields masked or omitted in the match.
    OFPBMC_BAD_WILDCARDS = 5
    #: Unsupported field type in the match.
    OFPBMC_BAD_FIELD = 6
    #: Unsupported value in a match field.
    OFPBMC_BAD_VALUE = 7
    #: Unsupported mask specified in the match, field is not dl-address or
    #: nw-address.
    OFPBMC_BAD_MASK = 8
    #: A prerequisite was not met.
    OFPBMC_BAD_PREREQ = 9
    #: A field type was duplicated.
    OFPBMC_DUP_FIELD = 10
    #: Permissions error.
    OFPBMC_EPERM = 11


class OPFBadRequestCode(Enum):
    """Error_msg 'code' values for OFPET_BAD_REQUEST.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: ofp_header.version not supported.
    OFPBRC_BAD_VERSION = 0
    #: ofp_header.type not supported.
    OFPBRC_BAD_TYPE = 1
    #: ofp_multipart_request.type not supported.
    OFPBRC_BAD_MULTIPART = 2
    #: Experimenter id not supported (in ofp_experimenter_header or
    #:  ofp_multipart_request or * ofp_multipart_reply).
    OFPBRC_BAD_EXPERIMENTER = 3
    #: Experimenter type not supported.
    OFPBRC_BAD_EXP_TYPE = 4
    #: Permissions error.
    OFPBRC_EPERM = 5
    #: Wrong request length for type.
    OFPBRC_BAD_LEN = 6
    #: Specified buffer has already been used.
    OFPBRC_BUFFER_EMPTY = 7
    #: Specified buffer does not exist.
    OFPBRC_BUFFER_UNKNOWN = 8
    #: Specified table-id invalid or does not * exist.
    OFPBRC_BAD_TABLE_ID = 9
    #: Denied because controller is slave.
    OFPBRC_IS_SLAVE = 10
    #: Invalid port.
    OFPBRC_BAD_PORT = 11
    #: Invalid packet in packet-out.
    OFPBRC_BAD_PACKET = 12
    #: ofp_multipart_request overflowed the assigned buffer.
    OFPBRC_MULTIPART_BUFFER_OVERFLOW = 13   # pylint: disable=invalid-name
    #: Timeout during multipart request.
    OFPBRC_MULTIPART_REQUEST_TIMEOUT = 14   # pylint: disable=invalid-name
    #: Timeout during multipart reply
    OFPBRC_MULTIPART_REPLY_TIMEOUT = 15     # pylint: disable=invalid-name


class OPFErrorType(Enum):
    """Values for ’type’ in ofp_error_message.

    These values are immutable: they will not change in future versions of the
    protocol (although new values may be added).
    """

    #: Hello protocol failed
    OFPET_HELLO_FAILED = 0
    #: Request was not understood
    OFPET_BAD_REQUEST = 1
    #: Error in action description
    OFPET_BAD_ACTION = 2
    #: Error in instruction list.
    OFPET_BAD_INSTRUCTION = 3
    #: Error in match.
    OFPET_BAD_MATCH = 4
    #: Problem modifying flow entry.
    OFPET_FLOW_MOD_FAILED = 5
    #: Problem modifying group entry.
    OFPET_GROUP_MOD_FAILED = 6
    #: Port mod request failed.
    OFPET_PORT_MOD_FAILED = 7
    #: Table mod request failed.
    OFPET_TABLE_MOD_FAILED = 8
    #: Queue operation failed.
    OFPET_QUEUE_OP_FAILED = 9
    #: Switch config request failed.
    OFPET_SWITCH_CONFIG_FAILED = 10
    #: Controller Role request failed.
    OFPET_ROLE_REQUEST_FAILED = 11
    #: Error in meter.
    OFPET_METER_MOD_FAILED = 12
    #: Setting table features failed.
    OFPET_TABLE_FEATURES_FAILED = 13
    #: Some property is invalid.
    OFPET_BAD_PROPERTY = 14
    #: Asynchronous config request failed
    OFPET_ASYNC_CONFIG_FAILED = 15
    #: Setting flow monitor failed.
    OFPET_FLOW_MONITOR_FAILED = 16
    #: Bundle operation failed
    OFPET_BUNDLE_FAILED = 17
    #: Experimenter error messages.
    OFPET_EXPERIMENTER = 0xffff

    def get_class(self):
        """Return a Code class based on current ErrorType value.

        Returns:
            enum.IntEnum: class referenced by current error type.

        """
        classes = {'OFPET_HELLO_FAILED': OPFHelloFailedCode,
                   'OFPET_BAD_REQUEST': OPFBadRequestCode,
                   'OFPET_BAD_ACTION': OPFBadActionCode,
                   'OFPET_BAD_INSTRUCTION': OPFBadInstructionCode,
                   'OFPET_BAD_MATCH': OPFBadMatchCode,
                   'OFPET_FLOW_MOD_FAILED': OPFFlowModFailedCode,
                   'OFPET_GROUP_MOD_FAILED': OPFGroupModFailedCode,
                   'OFPET_PORT_MOD_FAILED': OPFPortModFailedCode,
                   'OFPET_QUEUE_OP_FAILED': OPFQueueOpFailedCode,
                   'OFPET_SWITCH_CONFIG_FAILED': OPFSwitchConfigFailedCode,
                   'OFPET_ROLE_REQUEST_FAILED': OPFRoleRequestFailedCode,
                   'OFPET_METER_MOD_FAILED': OPFMeterModFailedCode,
                   'OFPET_TABLE_MOD_FAILED': OPFTableModFailedCode,
                   'OFPET_TABLE_FEATURES_FAILED': OPFTableFeaturesFailedCode,
                   'OFPET_BAD_PROPERTY': OPFBadPropertyCode,
                   'OFPET_ASYNC_CONFIG_FAILED': OPFAsyncConfigFailedCode,
                   'OFPET_FLOW_MONITOR_FAILED': OPFFlowMonitorFailedCode,
                   'OFPET_BUNDLE_FAILED': OPFBundleFailedCode}
        return classes.get(self.name, OPFGenericFailedCode)


class OPFFlowModFailedCode(Enum):
    """Error_msg 'code' values for OFPET_FLOW_MOD_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unspecified error.
    OFPFMFC_UNKNOWN = 0
    #: Flow not added because table was full.
    OFPFMFC_TABLE_FULL = 1
    #: Table does not exist
    OFPFMFC_BAD_TABLE_ID = 2
    #: Attempted to add overlapping flow with CHECK_OVERLAP flag set.
    OFPFMFC_OVERLAP = 3
    #: Permissions error.
    OFPFMFC_EPERM = 4
    #: Flow not added because of unsupported idle/hard timeout.
    OFPFMFC_BAD_TIMEOUT = 5
    #: Unsupported or unknown command.
    OFPFMFC_BAD_COMMAND = 6
    #: Unsupported or unknown flags.
    OFPFMFC_BAD_FLAGS = 7
    #: Problem in table synchronisation
    OFPFMFC_CANT_SYNC = 8
    #: Unsupported priority value
    OFPFMFC_BAD_PRIORITY = 9
    #: Synchronised flow entry is read only.
    OFPFMFC_IS_SYNC = 10


class OPFGroupModFailedCode(Enum):
    """Error_msg 'code' values for OFPET_GROUP_MOD_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Group not added because a group ADD attempted to replace an
    #: already-present group.
    FPGMFC_GROUP_EXISTS = 0
    #: Group not added because Group specified is invalid.
    OFPGMFC_INVALID_GROUP = 1
    #: Switch does not support unequal load sharing with select groups.
    OFPGMFC_WEIGHT_UNSUPPORTED = 2
    #: The group table is full.
    OFPGMFC_OUT_OF_GROUPS = 3
    #: The maximum number of action buckets for a group has been exceeded.
    OFPGMFC_OUT_OF_BUCKETS = 4
    #: Switch does not support groups that forward to groups.
    OFPGMFC_CHAINING_UNSUPPORTED = 5
    #: This group cannot watch the watch_port or watch_group specified.
    OFPGMFC_WATCH_UNSUPPORTED = 6
    #: Group entry would cause a loop.
    OFPGMFC_LOOP = 7
    #: Group not modified because a group MODIFY attempted to modify a
    #: non-existent group.
    OFPGMFC_UNKNOWN_GROUP = 8
    #: Group not deleted because another group is forwarding to it.
    OFPGMFC_CHAINED_GROUP = 9
    #: Unsupported or unknown group type.
    OFPGMFC_BAD_TYPE = 10
    #: Unsupported or unknown command.
    OFPGMFC_BAD_COMMAND = 11
    #: Error in bucket.
    OFPGMFC_BAD_BUCKET = 12
    #: Error in watch port/group.
    OFPGMFC_BAD_WATCH = 13
    #: Permissions error.
    OFPGMFC_EPERM = 14


class OPFHelloFailedCode(Enum):
    """Error_msg 'code' values for OFPET_HELLO_FAILED.

    'data' contains an ASCII text string that may give failure details.
    """

    #: No compatible version
    OFPHFC_INCOMPATIBLE = 0
    #: Permissions error
    OFPHFC_EPERM = 1


class OPFMeterModFailedCode(Enum):
    """Error msg 'code' values for OFPET_METER_MOD_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unspecified error.
    OFPMMFC_UNKNOWN = 0
    #: Meter not added because a Meter ADD * attempted to replace an existing
    #: Meter.
    OFPMMFC_METER_EXISTS = 1
    #: Meter not added because Meter specified * is invalid.
    OFPMMFC_INVALID_METER = 2
    #: Meter not modified because a Meter MODIFY attempted to modify a
    #: non-existent Meter.
    OFPMMFC_UNKNOWN_METER = 3
    #: Unsupported or unknown command.
    OFPMMFC_BAD_COMMAND = 4
    #: Flag configuration unsupported.
    OFPMMFC_BAD_FLAGS = 5
    #: Rate unsupported.
    OFPMMFC_BAD_RATE = 6
    #: Burst size unsupported.
    OFPMMFC_BAD_BURST = 7
    #: Band unsupported.
    OFPMMFC_BAD_BAND = 8
    #: Band value unsupported.
    OFPMMFC_BAD_BAND_VALUE = 9
    #: No more meters available.
    OFPMMFC_OUT_OF_METERS = 10
    #: The maximum number of properties * for a meter has been exceeded.
    OFPMMFC_OUT_OF_BANDS = 11


class OPFPortModFailedCode(Enum):
    """Error_msg 'code' values for OFPET_PORT_MOD_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Specified port number does not exist.
    OFPPMFC_BAD_PORT = 0
    #: Specified hardware address does not * match the port number.
    OFPPMFC_BAD_HW_ADDR = 1
    #: Specified config is invalid.
    OFPPMFC_BAD_CONFIG = 2
    #: Specified advertise is invalid.
    OFPPMFC_BAD_ADVERTISE = 3
    #: Permissions error.
    OFPPMFC_EPERM = 4


class OPFQueueOpFailedCode(Enum):
    """Error msg 'code' values for OFPET_QUEUE_OP_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Invalid port (or port does not exist)
    OFPQOFC_BAD_PORT = 0
    #: Queue does not exist
    OFPQOFC_BAD_QUEUE = 1
    #: Permissions error
    OFPQOFC_EPERM = 2


class OPFRoleRequestFailedCode(Enum):
    """Error msg 'code' values for OFPET_ROLE_REQUEST_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Stale Message: old generation_id.
    OFPRRFC_STALE = 0
    #: Controller role change unsupported.
    OFPRRFC_UNSUP = 1
    #: Invalid role.
    OFPRRFC_BAD_ROLE = 2


class OPFSwitchConfigFailedCode(Enum):
    """Error msg 'code' values for OFPET_SWITCH_CONFIG_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Specified flags is invalid.
    OFPSCFC_BAD_FLAGS = 0
    #: Specified len is invalid.
    OFPSCFC_BAD_LEN = 1
    #: Permissions error.
    OFPQCFC_EPERM = 2


class OPFTableFeaturesFailedCode(Enum):
    """Error msg 'code' values for OFPET_TABLE_FEATURES_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Specified table does not exist.
    OFPTFFC_BAD_TABLE = 0
    #: Invalid metadata mask.
    OFPTFFC_BAD_METADATA = 1
    #: Permissions error.
    OFPTFFC_EPERM = 5


class OPFTableModFailedCode(Enum):
    """Error_msg 'code' values for OFPET_TABLE_MOD_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Specified table does not exist.
    OFPTMFC_BAD_TABLE = 0
    #: Specified config is invalid.
    OFPTMFC_BAD_CONFIG = 1
    #: Permissions error.
    OFPTMFC_EPERM = 2


class OPFBadPropertyCode(Enum):
    """Error_msg 'code' values for OFPET_BAD_PROPERTY.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unknown property type.
    OFPBPC_BAD_TYPE = 0
    #: Length problem in property.
    OFPBPC_BAD_LEN = 1
    #: Unsupported property value.
    OFPBPC_BAD_VALUE = 2
    #: Can't handle this many properties.
    OFPBPC_TOO_MANY = 3
    #: A property type was duplicated.
    OFPBPC_DUP_TYPE = 4
    #: Unknown experimenter id specified.
    OFPBPC_BAD_EXPERIMENTER = 5
    #: Unknown exp_type for experimenter id.
    OFPBPC_BAD_EXP_TYPE = 6
    #: Unknown value for experimenter id.
    OFPBPC_BAD_EXP_VALUE = 7
    #: Permissions error
    OFPBPC_EPERM = 8


class OPFAsyncConfigFailedCode(Enum):
    """Error_msg 'code' values for OFPET_ASYNC_CONFIG_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: One mask is invalid.
    OFPACFC_INVALID = 0
    #: Requested configuration not supported.
    OFPACFC_UNSUPPORTED = 1
    #: Permissions error.
    OFPACFC_EPERM = 2


class OPFFlowMonitorFailedCode(Enum):
    """Error_msg 'code' values for OFPET_FLOW_MONITOR_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unspecified error.
    OFPMOFC_UNKNOWN = 0
    #: Monitor not added because a Monitor ADD attempted to replace
    #: and existing Monitor.
    OFPMOFC_MONITOR_EXISTS = 1
    #: Monitor not added because Monitor specified is invalid.
    OFPMOFC_INVALID_MONITOR = 2
    #: Monitor not modified because a Monitor MODIFY attempted to modify
    # a non-existent Monitor.
    OFPMOFC_UNKNOWN_MONITOR = 3
    #: Unsupported or unknown command.
    OFPMOFC_BAD_COMMAND = 4
    #: Flag configuration unsupported.
    OFPMOFC_BAD_FLAGS = 5
    #: Specified table does not exist.
    OFPMOFC_BAD_TABLE_ID = 6
    #: Error in output port/group.
    OFPMOFC_BAD_OUT = 7


class OPFBundleFailedCode(Enum):
    """Error_msg 'code' values for OFPET_BUNDLE_FAILED.

    'data' contains at least the first 64 bytes of the failed request.
    """

    #: Unspecified error.
    OFPBFC_UNKNOWN = 0
    #: Permissions error.
    OFPBFC_EPERM = 1
    #: Bundle ID doesn't exist.
    OFPBFC_BAD_ID = 2
    #: Bundle ID already exist.
    OFPBFC_BUNDLE_EXIST = 3
    #: Bundle ID is closed.
    OFPBFC_BUNDLE_CLOSED = 4
    #: Too many bundles IDs.
    OFPBFC_OUT_OF_BUNDLES = 5
    #: Unsupported or unknown message control type
    OFPBFC_BAD_TYPE = 6
    #: Unsupported, unknown, or inconsistent flags.
    OFPBFC_BAD_FLAGS = 7
    #: Length problem in included message.
    OFPBFC_MSG_BAD_LEN = 8
    #: Inconsistent or duplicate XID.
    OFPBFC_MSG_BAD_XID = 9
    #: Unsupported message in this bundle.
    OFPBFC_MSG_UNSUP = 10
    #: Unsupported message combination in this bundle.
    OFPBFC_MSG_CONFLICT = 11
    #: Can't handle this many messages in bundle.
    OFPBFC__MSG_TOO_MANY = 12
    #: One message in bundle failed.
    OFPBFC_MSG_FAILED = 13
    #: Bundle is taking too long.
    OFPBFC_TIMEOUT = 14
    #: Bundle is locking the resources.
    OFPBFC_BUNDLE_IN_PROGRESS = 15


# Classes

class OPFErrorMsg(GenericMessage):
    """OpenFlow Error Message.

    This message does not contain a body in addition to the OpenFlow Header.
    """

    #: :class:`~.header.Header`: OpenFlow Header
    header = Header(message_type=Type.OFPT_ERROR)
    #: ErrorType enum item
    error_type = UBInt16(enum_ref=OPFErrorType)
    #: Error code associated with ErrorType
    code = UBInt16()
    #: Variable-length data interpreted based on the type and code.
    # No padding.
    data = BinaryData()

    def __init__(self, xid=None, error_type=None, code=None, data=b''):
        """Assign parameters to object attributes.

        Args:
            xid (int): To be included in the message header.
            error_type (ErrorType): Error type.
            code (Enum): Error code.
            data: Its content is specified in the error code documentation.
                Unless specified otherwise, the data field contains at least
                64 bytes of the failed request that caused the error message
                 to be generated, if the failed request is shorter than 64
                 bytes it should be the full request without any padding.
        """
        super().__init__(xid)
        self.error_type = error_type
        self.code = code
        self.data = data

    def unpack(self, buff, offset=0):
        """Unpack binary data into python object."""
        super().unpack(buff, offset)
        code_class = OPFErrorType(self.error_type).get_class()
        self.code = code_class(self.code)


class OPFErrorExperimenterMsg(GenericMessage):
    """OFPET_EXPERIMENTER: Error message (datapath -> controller).

    The experimenter field is the Experimenter ID, which takes the same form
     as in :class:`~.symmetric.experimenter.ExperimenterHeader
    """

    # :class:`~.header.Header`: OpenFlow Header
    header = Header(message_type=Type.OFPT_ERROR)
    #: OFPET_EXPERIMENTER.
    error_type = UBInt16(OPFErrorType.OFPET_EXPERIMENTER,
                         enum_ref=OPFErrorType)
    #: Experimenter Defined
    exp_type = UBInt16()
    #: Experimenter ID which takes the same form as in
    #:   :class:`~.symmetric.experimenter.ExperimenterHeader`.
    experimenter = UBInt32()
    #: Variable-length data interpreted based on the type and code.
    # No padding.
    data = BinaryData()

    def __init__(self, xid=None, exp_type=None, experimenter=None, data=b''):
        """Assign parameters to object attributes.

        Args:
            xid (int): To be included in the message header.
            exp_type (int): Experimenter defined.
            experimenter (int): Experimenter ID which takes the same form as
             in :class:`~.symmetric.experimenter.ExperimenterHeader`.
            data: Variable-length data interpreted based on the type and code.
                No padding.
        """
        super().__init__(xid)
        self.exp_type = exp_type
        self.experimenter = experimenter
        self.data = data

    def unpack(self, buff, offset=0):
        """Unpack binary data into python object."""
        raise exceptions.MethodNotImplemented("'Unpack' method not "
                                              "implemented on ErrorMsg class")
