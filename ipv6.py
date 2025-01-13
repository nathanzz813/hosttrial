import re

# Regular expressions
ipv6_pattern = r'^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$|^([0-9a-fA-F]{1,4}:){1,7}:$|^(?:[0-9a-fA-F]{1,4}:){1,6}(:[0-9a-fA-F]{1,4}){1,2}$|^(?:[0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,3}$|^(?:[0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,4}$|^(?:[0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,5}$|^(?:[0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,6}$|^[0-9a-fA-F]{1,4}:((?:[0-9a-fA-F]{1,4}:){1,7}|::)$'
bogon_ipv6_pattern = r'^(::|fe80:(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4}|ff00::(?:[0-9a-fA-F]{1,4}:){0,7}[0-9a-fA-F]{1,4}|::ffff(:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|2001:db8::[0-9a-fA-F]{1,4})$'

dns_hostname_regex = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z0-9-]{1,63})*$')

# Test IPv6 addresses
test_ipv6_addresses = [
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334",  # valid
    "fe80::1",  # bogon (link-local)
    "ff00::",  # bogon (multicast)
    "2001:db8::",  # bogon (documentation)
    "::",  # valid (empty address)
    "::ffff:192.168.1.1",  # bogon (IPv4-mapped)
    "abcd:efgh:ijkl:mnoo:0:0:0:1"  # invalid
]

# Function to check if address is a valid IPv6 address
def is_valid_ipv6(address):
    return bool(re.match(ipv6_pattern, address))

# Function to check if address is a bogon IPv6 address
def is_bogon_ipv6(address):
    return bool(re.match(bogon_ipv6_pattern, address))

# Test the addresses
#for address in test_ipv6_addresses:
    #print(f"Address: {address}")
    #print(f"  Valid IPv6? {'Yes' if is_valid_ipv6(address) else 'No'}")
    #print(f"  Bogon IPv6? {'Yes' if is_bogon_ipv6(address) else 'No'}")
    #print("-" * 50)
