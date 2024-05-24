import sys
import os
import ipaddress
import hashlib
import urllib.request

def download_file(url, local_path):
    """Download a file from the GIT URL if it has changed."""
    try:
        print("Downloading latest VPN list")
        response = urllib.request.urlopen(url)
        new_content = response.read()

        if os.path.exists(local_path):
            with open(local_path, 'rb') as local_file:
                existing_content = local_file.read()
                if hashlib.md5(existing_content).hexdigest() == hashlib.md5(new_content).hexdigest():
                    print(f"No changes detected in {local_path}. Using the existing file.")
                    return

        with open(local_path, 'wb') as local_file:
            local_file.write(new_content)
        print(f"Updated {local_path} with the latest version.")
    except urllib.error.URLError as e:
        print(f"Failed to download {url}: {e}")
        sys.exit(1)

def load_ip_list(file_path):
    """Load IP lists from a given file path."""
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
        print("Usage: python3 vpn.py <input.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    vpn_list_url = 'https://raw.githubusercontent.com/Dan-Duran/vpn-checker/main/known-vpn/vpn-list.txt'
    vpn_list_path = 'known-vpn/vpn-list.txt'
    manual_list_path = 'known-vpn/vpn-manual.txt'

    # Ensure the known-vpn directory exists
    os.makedirs('known-vpn', exist_ok=True)

    # Download the latest VPN list
    download_file(vpn_list_url, vpn_list_path)

    vpn_list = load_ip_list(vpn_list_path)
    manual_list = load_ip_list(manual_list_path)

    print("Checking input against VPN list")
    matches = []

    with open(input_file, 'r') as file:
        for line in file:
            ip = line.strip()
            if ip:
                try:
                    ip_obj = ipaddress.IPv4Address(ip)
                    if is_ip_in_list(ip_obj, vpn_list) or is_ip_in_list(ip_obj, manual_list):
                        matches.append(ip)
                except ipaddress.AddressValueError:
                    continue

    if matches:
        print("The following IP addresses are a match:")
        for match in matches:
            print(match)
    else:
        print("No matches")

if __name__ == "__main__":
    main()
