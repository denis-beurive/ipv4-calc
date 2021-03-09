import sys
import re
from typing import List, Tuple, Pattern, Match, Optional


def ip2int(in_ip: str) -> Tuple[int, int, int, int, int]:
    tokens: List[str] = in_ip.split(".")
    return int(tokens[0]) << 24 | int(tokens[1]) << 16 | int(tokens[2]) << 8 | \
           int(tokens[3]), int(tokens[0]), int(tokens[1]), int(tokens[2]), \
           int(tokens[3])


def split_cidr(in_cidr: str) -> Optional[Tuple[str, str]]:
    p: Pattern = re.compile('^([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,'
                            '3})/([0-9]{1,2})')
    m: Optional[Match] = p.match(in_cidr)
    if m is None:
        return None, None
    return m.group(1), m.group(2)


def int2ip(in_int: int) -> str:
    n3 = (in_int & 0xFF000000) >> 24
    n2 = (in_int & 0x00FF0000) >> 16
    n1 = (in_int & 0x0000FF00) >> 8
    n0 = in_int & 0x000000FF
    return f"{n3:d}.{n2:d}.{n1:d}.{n0:d}"


def int2ip_bin(in_int: int) -> str:
    n3 = (in_int & 0xFF000000) >> 24
    n2 = (in_int & 0x00FF0000) >> 16
    n1 = (in_int & 0x0000FF00) >> 8
    n0 = in_int & 0x000000FF
    return f"{n3:08b}.{n2:08b}.{n1:08b}.{n0:08b}"


if len(sys.argv) != 2:
    print("Usage: ip <cidr>")
    sys.exit(1)

cidr: str = sys.argv[1]
ip_net = split_cidr(cidr)
if ip_net is None:
    print(f"Invalid CIDR \"{cidr:s}\"\n")
    sys.exit(1)

ip: str = ip_net[0]
net_len = int(ip_net[1])
ip_num, n3, n2, n1, n0 = ip2int(ip)
net_mask = (0xFFFFFFFF << (32 - net_len)) & 0xFFFFFFFF
host_mask = net_mask ^ 0xFFFFFFFF
net_part = ip_num & net_mask
host_part = ip_num & host_mask

print(f"ip={ip:s} len={net_len:d}\n")
print(f'network mask: 0x{net_mask:08X} ({int2ip_bin(net_mask):s}) '
      f'{int2ip(net_mask):s}')
print(f'host mask:    0x{host_mask:08X} ({int2ip_bin(host_mask):s})')
print(f'network part: 0x{net_part:08X} ({int2ip(net_part):s})')
print(f'IP count:     {host_mask+1:d}')
print(f'min IP:       {int2ip(net_part):s}')
print(f'max IP:       {int2ip(net_part | host_mask):s}')



