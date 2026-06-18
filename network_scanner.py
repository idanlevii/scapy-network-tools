import scapy.all as scapy
import sys

def scan_wifi_network(ip_range):
    """
    Performs an ARP Scan on the specified IP range to discover active devices.
    """
    print(f"[*] Initializing ARP Scan on range: {ip_range}")
    print("[*] Sending ARP Requests to all hosts... Please wait.\n")
    
    # 1. Create the ARP Request packet
    arp_request = scapy.ARP(pdst=ip_range)
    
    # 2. Create the Ethernet Broadcast layer (Sends to everyone)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # 3. Combine them together
    arp_request_packet = broadcast / arp_request
    
    # 4. Send the packets and capture the responses
    # timeout=3 means wait 3 seconds for devices to answer before moving on
    answered_list = scapy.srp(arp_request_packet, timeout=3, verbose=False)[0]
    
    # 5. Process and display the results
    print("=" * 55)
    print("IP Address\t\tMAC Address")
    print("=" * 55)
    
    discovered_devices = []
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        discovered_devices.append(device_info)
        # Print each found device beautifully
        print(f"{device_info['ip']}\t\t{device_info['mac']}")
        
    print("=" * 55)
    print(f"[+] Scan completed. Found {len(discovered_devices)} active devices.")

# ========================================================================
# --- Execution ---
# ========================================================================

print("=== Cyber Security Project: WiFi ARP Scanner ===")

# Ask the user for the network gateway to target (e.g., 192.168.11.254)
target_gateway = input("[?] Enter Gateway IP to deduce network range: ")

# Automatically format the IP to scan the whole range (e.g., 192.168.11.0/24)
# /24 means scan all numbers from 1 to 254 in the last section
network_range = ".".join(target_gateway.split(".")[:-1]) + ".0/24"

try:
    scan_wifi_network(network_range)
except KeyboardInterrupt:
    print("\n[-] Scan interrupted by user. Exiting.")
    sys.exit(0)