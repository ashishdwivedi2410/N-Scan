from scapy.all import sniff
from analyzer import analyze_packet

def start_sniffing():
    sniff(prn=analyze_packet, store=False)
