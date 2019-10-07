import struct

LOCAL_HOST = "0.0.0.0"
BCAST_HOST = "255.255.255.255"

DISCOVERY_PORT = 50000
CODE_RECV_PORT = DISCOVERY_PORT + 1
TERMINAL_PORT = CODE_RECV_PORT + 1

RECEIVE_POLL_MS = DISCOVERY_POLL_MS = 1_000
MAX_TCP_CONNECTIONS = 10

UDP_MAX_SIZE = 1024  # 1 KB
TCP_MAX_SIZE = 1024_0  # 10KB

UINT_FMT = ">L"
UINT_SIZE = struct.calcsize(UINT_FMT)
TCP_MAX_PAYLOAD_SIZE = TCP_MAX_SIZE - UINT_SIZE
