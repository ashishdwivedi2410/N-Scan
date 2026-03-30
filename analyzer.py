from scapy.layers.inet import IP, TCP, UDP
from ml_model import predict_anomaly
from database import log_data

def analyze_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src
        dst = packet[IP].dst
        size = len(packet)

        port = 0
        if packet.haslayer(TCP):
            port = packet[TCP].dport
        elif packet.haslayer(UDP):
            port = packet[UDP].dport

        prediction = predict_anomaly(size, port)

        log_data(src, dst, port, size, prediction)

        print(f"{src} → {dst} | Port: {port} | {prediction}")
