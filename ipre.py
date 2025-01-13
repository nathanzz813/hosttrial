import re
import ipaddress

ippattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

def is_bogon(ip_address_str):#is_bogon(x):returns true or false
    # Define regex patterns for bogon IP address ranges
    bogon_patterns = [
        re.compile(r'^0\.'),                    # 0.0.0.0/8
        re.compile(r'^10\.'),                   # 10.0.0.0/8
        re.compile(r'^100\.'),                  # 100.64.0.0/10 (Carrier-grade NAT)
        re.compile(r'^127\.'),                  # 127.0.0.0/8 (Loopback)
        re.compile(r'^169\.254\.'),             # 169.254.0.0/16 (Link-local)
        re.compile(r'^192\.168\.'),             # 192.168.0.0/16 (Private-use)
        re.compile(r'^172\.(1[6-9]|2[0-9]|3[0-1])\.'),  # 172.16.0.0/12 (Private-use)
        re.compile(r'^224\.'),                  # 224.0.0.0/4 (Multicast)
        re.compile(r'^240\.'),                  # 240.0.0.0/4 (Reserved for future use)
    ]

    try:
        ip = ipaddress.ip_address(ip_address_str)
        for pattern in bogon_patterns:
            if pattern.match(ip_address_str):
                return True
        return False
    except ValueError:
        # Invalid IP address format
        return False
