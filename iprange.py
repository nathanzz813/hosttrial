import ipaddress

def generate_ipv4_addresses(start_ip, end_ip):
    start_ip = ipaddress.IPv4Address(start_ip)
    end_ip = ipaddress.IPv4Address(end_ip)

    if start_ip > end_ip:
        raise ValueError("Start IP must be less than or equal to End IP")

    ip_list = []
    current_ip = start_ip
    while current_ip <= end_ip:
        ip_list.append(str(current_ip))
        current_ip += 1

    return ip_list

# Example usage:
start_ip_address = "192.168.0.1"
end_ip_address = "192.168.0.10"

result = generate_ipv4_addresses(start_ip_address, end_ip_address)
for ip in result:
    print(ip)
