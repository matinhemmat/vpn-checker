# VPN Checker

This script checks your list of IP addresses against known VPN IP addresses to determine if they are VPNs. This is not a complete list of VPNs, but it is a good starting point. The script will output any IP addresses that are part of the VPNs CIDR blocks. If IPs are not then they will get diregarded via `/dev/null`.

Everytime the script is ran, it will check for the latest updates to the known-vpn/vpn-list.txt. Thus way we can maintain a current list.

This script is useful for identifying VPNs in logs or other data sources. For your convenience, new VPN IP addresses can be added to the `known-vpn/vpn-manual.txt` file.

All contributions to the known-vpn/vpn-list.txt file must include IP addresses in CIDR notation to precisely define the network range. This can range from specific single IP addresses noted as /32 to broader network ranges, potentially as expansive as /0. This ensures that our matching logic accurately identifies VPN traffic by covering the correct network segments. When adding IP addresses, please use the appropriate CIDR block that best represents the network scope of the VPN service. 

## Installation
Clone the repository:

```bash
git clone https://github.com/Dan-Duran/vpn-checker.git
cd vpn-checker
```
## Usage
The input.txt file is juat a placeholder where you can put your list of IP addresses to be checked. The script will work with any file and files extension (ex python3 vpn.py input.csv or python3 vpn.py my-ip-list.txt)

### Linux & MacOS
```bash
python3 vpn.py input.txt
```
### Windows
```bash
python vpn.py input.txt
```

## Requierements

- Python 3.3 and above (The ipaddress module is part of the Python standard library and does not need to be installed separately)
  
## Directory Structure
```
vpn-checker/
├── known-vpn/
│   ├── vpn-list.txt
│   └── vpn-manual.txt
├── input.txt
├── vpn.py
└── README.md
```

## License
This project is licensed under the MIT License - see the LICENSE file for details. 

## Disclaimer

This script is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the script or the use or other dealings in the script.

