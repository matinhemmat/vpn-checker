# VPN Checker

This script checks your list of IP addresses against known VPN IP addresses to determine if they are VPNs. This is not a complete list of VPNs, but it is a good starting point. The script will output any IP addresses that are part of the VPNs CIDR blocks. If IPs are not then they will get diregarded via `/dev/null`.

This script is useful for identifying VPNs in logs or other data sources. For your convenience, new IP addresses can be added to the `known-vpn/vpn-manual.txt` file.

Contributions are welcome! Please submit a pull request with any updates to the code or additions to the known-vpn/vpn-list.txt file. Please include the source of the IP addresses in the comments.

## Usage
### Linux & MacOS
```bash
python3 vpn.py input.txt
```
### Windows
```bash
python vpn.py input.txt
```

## Installation
Clone the repository:

```bash
git clone https://github.com/Dan-Duran/vpn-checker.git
cd vpn-checker
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

