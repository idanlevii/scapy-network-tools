# Scapy Network Tools
A collection of lightweight Python scripts designed for network reconnaissance and security testing using the Scapy library. This project was developed as part of a cybersecurity learning milestone.
## Tools Included
 1. Network Scanner (network_scanner.py)
   Performs a live ARP scan on the local subnet to map connected devices, discovering active IP and MAC addresses dynamically.
 2. ARP Spoofing Tool (arp_spoofing.py)
   Demonstrates a Man-in-the-Middle (MitM) / Denial of Service (DoS) mechanism by poisoning ARP tables between a target host and the local gateway.
## Usage
Ensure you have Scapy installed:
pip install scapy
Run the tools using administrative privileges (Required for raw packet manipulation):
python network_scanner.py
python arp_spoofing.py
## Disclaimer
This project is created strictly for educational purposes, academic research, and authorized security testing. Do not run these tools on networks without explicit, prior permission from the owner. The author is not responsible for any misuse or damage caused by this software.
