#####################################
############ VPN Checker ############
###### Dan Duran - GetCyber.Me ######
#####################################

import sys
import ipaddress

def load_ip_list(file_path):
    """Load IP lists from any given file path."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def is_ip_in_list(ip, ip_list):
    """Check if an IP address is within any CIDR block in the list."""
    for cidr in ip_list:
        if ip in ipaddress.IPv4Network(cidr):
            return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 vnp.py <input.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    vpn_list = load_ip_list('known-vpn/vpn-list.txt')
    manual_list = load_ip_list('known-vpn/vpn-manual.txt')

    with open(input_file, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                try:
                    ip_obj = ipaddress.IPv4Address(ip)
                    if is_ip_in_list(ip_obj, vpn_list) or is_ip_in_list(ip_obj, manual_list):
                        print(ip)
                    else:
                        with open('/dev/null', 'a') as devnull:
                            devnull.write(f"{ip}\n")
                except ipaddress.AddressValueError:
                    with open('/dev/null', 'a') as devnull:
                        devnull.write(f"{ip}\n")

if __name__ == "__main__":
    main()
