TC_TM_SEQ_SPACKET = 0x03
ECSS_VER_NUMBER = 0
ECSS_DATA_FIELD_HDR_FLG = 1
TC = 1
TM = 0
ECSS_HEADER_SIZE = 6
ECSS_DATA_HEADER_SIZE = 4
ECSS_CRC_SIZE = 2
ECSS_DATA_OFFSET = ECSS_HEADER_SIZE + ECSS_DATA_HEADER_SIZE
MIN_PKT_SIZE = 5
MAX_COMMS_PKT_SIZE = 210
MAX_PKT_SIZE = 2048 + ECSS_HEADER_SIZE + ECSS_DATA_HEADER_SIZE + ECSS_CRC_SIZE
ECSS_PUS_VER = 1
ECSS_SEC_HDR_FIELD_FLG = 0

SATR_PKT_ILLEGAL_APPID = 0
SATR_PKT_INV_LEN = 1
SATR_PKT_INC_CRC = 2
SATR_PKT_ILLEGAL_PKT_TP = 3
SATR_PKT_ILLEGAL_PKT_STP = 4
SATR_PKT_ILLEGAL_APP_DATA = 5
SATR_OK = 6
SATR_ERROR = 7
SATR_EOT = 8
SATR_CRC_ERROR = 9
SATR_PKT_ILLEGAL_ACK = 10
SATR_ALREADY_SERVICING = 11
SATR_MS_MAX_FILES = 12
SATR_PKT_INIT = 13
SATR_INV_STORE_ID = 14
SATR_INV_DATA_LEN = 15
SATR_LAST = 16

OBC_APP_ID = 1
EPS_APP_ID = 2
ADCS_APP_ID = 3
COMMS_APP_ID = 4
IAC_APP_ID = 5
GND_APP_ID = 6
DBG_APP_ID = 7
LAST_APP_ID = 8

upsat_app_ids = {
    "1": "OBC",
    "2": "EPS",
    "3": "ADCS",
    "4": "COMMS",
    "5": "IAC",
    "6": "GND",
    "7": "DBG"
}

upsat_store_ids = {
    "1": "SU_SCRIPT_1",
    "2": "SU_SCRIPT_2",
    "3": "SU_SCRIPT_3",
    "4": "SU_SCRIPT_4",
    "5": "SU_SCRIPT_5",
    "6": "SU_SCRIPT_6",
    "7": "SU_SCRIPT_7",
    "8": "SU_LOG",
    "9": "WOD_LOG",
    "10": "EXT_WOD_LOG",
    "11": "EVENT_LOG"
}

SCRIPT_REPORT_SU_OFFSET = 9
SCRIPT_REPORT_LOGS_OFFSET = 22

SU_LOG_SIZE = 196
WOD_LOG_SIZE = 228

LOGS_LIST_SIZE = 10

SERVICES_VERIFICATION_TC_TM = [
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_VERIFICATION_SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [1, 0], [0, 0], [0, 0]],  # TC_HOUSEKEEPING_SERVICE 3
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [1, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_EVENT_SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_FUNCTION_MANAGEMENT_SERVICE
    [[0, 0], [1, 1], [1, 1], [0, 1], [0, 1], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TIME MANAGEMENT SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 0], [0, 1], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_SCHEDULING_SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [1, 0], [1, 0], [1, 0], [1, 0], [0, 1], [0, 1], [1, 0], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [1, 0], [1, 0], [1, 0], [1, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_LARGE_DATA_SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 1], [0, 1],
    [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_MASS_STORAGE_SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 1], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],  # TC_TEST_SERVICE
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],
    [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
]

TC_ACK_NO = 0x00
TC_ACK_ACC = 0x01
TC_ACK_EXE_START = 0x02
TC_ACK_EXE_PROG = 0x04
TC_ACK_EXE_COMP = 0x08
TC_ACK_ALL = 0x0F

FRAME_RECEIVER_IP = '127.0.0.1'
FRAME_RECEIVER_PORT = 16886

SAT_RETURN_STATES = {
    0: "SATR_PKT_ILLEGAL_APPID",
    1: "SATR_PKT_INV_LEN",
    2: "SATR_PKT_INC_CRC",
    3: "SATR_PKT_ILLEGAL_PKT_TP",
    4: "SATR_PKT_ILLEGAL_PKT_STP",
    5: "SATR_PKT_ILLEGAL_APP_DATA",
    6: "SATR_OK",
    7: "SATR_ERROR",
    8: "SATR_EOT",
    9: "SATR_CRC_ERROR",
    10: "SATR_PKT_ILLEGAL_ACK",
    11: "SATR_ALREADY_SERVICING",
    12: "SATR_MS_MAX_FILES",
    13: "SATR_PKT_INIT",
    14: "SATR_INV_STORE_ID",
    15: "SATR_INV_DATA_LEN",
    17: "SATR_SCHEDULE_FULL",
    18: "SATR_SSCH_ID_INVALID",
    19: "SATR_NMR_OF_TC_INVALID",
    20: "SATR_INTRL_ID_INVALID",
    21: "SATR_ASS_INTRL_ID_INVALID",
    22: "SATR_ASS_TYPE_ID_INVALID",
    23: "SATR_RLS_TIMET_ID_INVALID",
    24: "SATR_DEST_APID_INVALID",
    25: "SATR_TIME_INVALID",
    26: "SATR_TIME_SPEC_INVALID",
    27: "SATR_INTRL_LOGIC_ERROR",
    28: "SATR_SCHEDULE_DISABLED",
    29: "SATRF_OK",
    30: "SATRF_DISK_ERR",
    31: "SATRF_INT_ERR",
    32: "SATRF_NOT_READY",
    33: "SATRF_NO_FILE",  # (4) Could not find the file */
    34: "SATRF_NO_PATH",  # (6) The path name format is invalid */
    35: "SATRF_INVALID_NAME",  # (6) The path name format is invalid */
    36: "SATRF_DENIED",  # (7) Access denied due to prohibited access or directory full */
    37: "SATRF_EXIST",  # (8) Access denied due to prohibited access */
    38: "SATRF_INVALID_OBJECT",  # (9) The file/directory object is invalid */
    39: "SATRF_WRITE_PROTECTED",  # (10) The physical drive is write protected */
    40: "SATRF_INVALID_DRIVE",  # (11) The logical drive number is invalid */
    41: "SATRF_NOT_ENABLED",  # (12) The volume has no work area */
    42: "SATRF_NO_FILESYSTEM",  # (13) There is no valid FAT volume */
    43: "SATRF_MKFS_ABORTED",  # (14) The f_mkfs() aborted due to any parameter error */
    44: "SATRF_TIMEOUT",  # (15) Could not get a grant to access the volume within defined period */
    45: "SATRF_LOCKED",  # (16) The operation is rejected according to the file sharing policy */
    46: "SATRF_NOT_ENOUGH_CORE",  # (17) LFN working buffer could not be allocated */
    47: "SATRF_TOO_MANY_OPEN_FILES",  # (18) Number of open files > _FS_SHARE */
    48: "SATRF_INVALID_PARAMETER",  # (19) Given parameter is invalid */
    49: "SATRF_DIR_ERROR",
}

HLDLC_START_FLAG = 0x7E
HLDLC_CONTROL_FLAG = 0x7D
UART_BUF_SIZE = 4096

# Service Types
TC_VERIFICATION_SERVICE = 1
TC_HOUSEKEEPING_SERVICE = 3
TC_EVENT_SERVICE = 5
TC_FUNCTION_MANAGEMENT_SERVICE = 8
TC_TIME_MANAGEMENT_SERVICE = 9
TC_SCHEDULING_SERVICE = 11
TC_LARGE_DATA_SERVICE = 13
TC_MASS_STORAGE_SERVICE = 15
TC_TEST_SERVICE = 17
TC_SU_MNLP_SERVICE = 18

# Service Subtypes
TM_VR_ACCEPTANCE_SUCCESS = 1
TM_VR_ACCEPTANCE_FAILURE = 2
TC_HK_REPORT_PARAMETERS = 21
TM_HK_PARAMETERS_REPORT = 23

TM_EV_NORMAL_REPORT = 1
TM_EV_ERROR_REPORT = 4

TC_FM_PERFORM_FUNCTION = 1

TC_SC_ENABLE_RELEASE = 1
TC_SC_DISABLE_RELEASE = 2
TC_SC_RESET_SCHEDULE = 3
TC_SC_INSERT_TC = 4
TC_SC_DELETE_TC = 5
TC_SC_TIME_SHIFT_SPECIFIC = 7
TC_SC_TIME_SHIFT_SELECTED_OTP = 8
TC_SC_TIME_SHIFT_ALL = 15

TM_LD_FIRST_DOWNLINK = 1
TC_LD_FIRST_UPLINK = 9
TM_LD_INT_DOWNLINK = 2
TC_LD_INT_UPLINK = 10
TM_LD_LAST_DOWNLINK = 3
TC_LD_LAST_UPLINK = 11
TC_LD_ACK_DOWNLINK = 5
TM_LD_ACK_UPLINK = 14
TC_LD_REPEAT_DOWNLINK = 6
TM_LD_REPEAT_UPLINK = 15
TM_LD_REPEATED_DOWNLINK = 7
TC_LD_REPEATED_UPLINK = 12
TM_LD_ABORT_SE_DOWNLINK = 4
TC_LD_ABORT_SE_UPLINK = 13
TC_LD_ABORT_RE_DOWNLINK = 8
TM_LD_ABORT_RE_UPLINK = 16

TC_MS_ENABLE = 1
TC_MS_DISABLE = 2
TM_MS_CONTENT = 8
TC_MS_DOWNLINK = 9
TC_MS_DELETE = 11
TC_MS_REPORT = 12
TM_MS_CATALOGUE_REPORT = 13
TC_MS_UPLINK = 14
TC_MS_FORMAT = 15
TM_MS_CATALOGUE_LIST = 17

TC_CT_PERFORM_TEST = 1
TM_CT_REPORT_TEST = 2

# mNLP science unit sub-service definitions
TC_SU_ON = 1
TC_SU_OFF = 2
TC_SU_RESET = 3
TC_SU_LOAD_P = 4  # subservice 4
TM_SU_LOAD_P = 5
TC_SU_HC = 6  # subservice 5
TM_SU_HC = 7
TC_SU_CAL = 8  # subservice 6
TM_SU_CAL = 9
TC_SU_SCI = 10  # subservice 7
TM_SU_SCI = 11
TC_SU_HK = 12  # subservice 8
TM_SU_HK = 13
TC_SU_STM = 14  # subservice 9
TM_SU_STM = 15
TC_SU_DUMP = 16  # subservice 10
TM_SU_DUMP = 17
TC_SU_BIAS_ON = 18  # subservice 11
TC_SU_BIAS_OFF = 19  # subservice 12
TC_SU_MTEE_ON = 20  # subservice 13
TC_SU_MTEE_OFF = 21  # subservice 14
TM_SU_ERR = 22  # subservice 15
TM_OBC_SU_ERR = 23  # subservice 16
TC_OBC_EOT = 24  # subservice 17
TC_SU_SCHE_ON = 25  # subservice 24
TC_SU_SCHE_OFF = 26  # subservice 25

# TIME MANAGEMENT SERVICE
TM_TIME_SET_TIME_UTC = 1  # subservice 1
TM_TIME_SET_TIME_QB50 = 2  # subservice 2
TM_REPORT_TIME_IN_UTC = 3   # Asking time in UTC
TM_REPORT_TIME_IN_QB50 = 4   # Asking time in QB50
TM_TIME_REPORT_IN_UTC = 5  # Reporting time in UTC
TM_TIME_REPORT_IN_QB50 = 6  # Reporting time in QB50

SU_SCRIPT_1 = 1
SU_SCRIPT_2 = 2
SU_SCRIPT_3 = 3
SU_SCRIPT_4 = 4
SU_SCRIPT_5 = 5
SU_SCRIPT_6 = 6
SU_SCRIPT_7 = 7
SU_LOG = 8
WOD_LOG = 9
EXT_WOD_LOG = 10
EVENT_LOG = 11
FOTOS = 12
SCHS = 13
SRAM = 14

EV_inc_pkt = 1
EV_pkt_ack_er = 2
EV_sys_boot = 3
EV_pwr_level = 4
EV_comms_tx_off = 5
EV_sys_timeout = 6
EV_sys_shutdown = 7
EV_assertion = 8
EV_su_error = 9
EV_su_scr_start = 10
EV_pkt_pool_timeout = 11
EV_ms_err = 12

HEALTH_REP = 1
EX_HEALTH_REP = 2
EVENTS_REP = 3
WOD_REP = 4
EXT_WOD_REP = 5
SU_SCI_HDR_REP = 6
ADCS_TLE_REP = 7
EPS_FLS_REP = 8

# Housekeeping EX WOD offsets and sizes
OBC_EXT_WOD_SIZE = 50
OBC_EXT_WOD_OFFSET = 1
COMMS_EXT_WOD_SIZE = 29
COMMS_EXT_WOD_OFFSET = 51
ADCS_EXT_WOD_SIZE = 83
ADCS_EXT_WOD_OFFSET = 80
EPS_EXT_WOD_SIZE = 34
EPS_EXT_WOD_OFFSET = 163
