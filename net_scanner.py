from scapy.all import ARP
from scapy.all import Ether
from scapy.all import srp
import socket

target_net = '192.168.0.1/24'

#arp packets
arp = ARP(pdst=target_net)

#create packet to be broadcast by Ether
eth = Ether(dst='ff:ff:ff:ff:ff:ff')

packet_stack = eth/arp

output = srp(packet_stack,timeout=2,verbose=0)[0] #set verbose to 0 to reduce unnecessary print out on screen

#create an empty list of clients to be populated later
list_of_users_on_network = []

for sent_packets, received_packets in output:
    #append each mac to corresponding ip
    list_of_users_on_network.append({'mac_address': received_packets.hwsrc,
                                    'ip_address': received_packets.psrc})

#print list of connected devices on the network
print('>>> Printing list of connected devices on the network: \n')

print('>>> '+'Ip'+ ' '*18 + 'Mac')
for users in list_of_users_on_network:
    print('>>> {:16}    {}'.format(users['ip_address'], users['mac_address']))

