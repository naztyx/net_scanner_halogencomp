from scapy.all import ARP
from scapy.all import Ether
from scapy.all import srp
import argparse


def unauthorized_devices_filter(ip_to_scan):

    ## set the ip address of the router or gateway device with the notation /24 or /16 depending
    ## on the ip range you wish to scan
    target_net = ip_to_scan + '/24'

    #arp packets
    arp = ARP(pdst=target_net)

    #create packet to be broadcast by Ether
    eth = Ether(dst='ff:ff:ff:ff:ff:ff')

    packet_stack = eth/arp

    #srp is used tro send out the packets
    #set verbose to 0 to reduce unnecessary print out on screen,
    #set timeout to 2 to prevent the script from freezing or malfunctioning
    output = srp(packet_stack,timeout=2,verbose=0)[0] 

    #create an empty list of clients (ip and mac) to be populated later from the output
    list_of_connected_devices = []

    for sent_packets, received_packets in output:
        #print(received_packets.psrc)

        #append each mac to corresponding ip
        list_of_connected_devices.append({'mac_address': received_packets.hwsrc,
                                        'ip_address': received_packets.psrc})

    ## read a list of whitleisted mac adresses and create an empty filtered list
    mac_whitelist = open('whitelist.txt').readlines()
    clean_macs = []
    ## strip newline \n from the mac strings
    for i in mac_whitelist:
        clean_macs.append(i.rstrip())
    #print(clean_macs)

    ## SORT AND PRINT LIST OF ALL CONNECTED DEVICES
    print('>>> List of Connected Devices...')
    print('>>> '+'Ip'+ ' '*18 + 'Mac')
    for device in list_of_connected_devices:
        print('>>> {:16}    {}'.format(device['ip_address'], device['mac_address']))

    ## SORT AND PRINT LIST OF UNAUTHORIZED CONNECTIONS
    print('>>> \nList of Unauthorized Connected Devices...')
    print('>>> '+'Ip'+ ' '*18 + 'Mac')
    for device in list_of_connected_devices:
        if device['mac_address'] in clean_macs:
            return
        else:
            print('>>> {:16}    {}'.format(device['ip_address'], device['mac_address']))

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Python Script to Scan and Filter Unauthorized Connected Devices.')
    parser.add_argument('target_ip', help='Target Ip to scan.')

    args =parser.parse_args()
    target = args.target_ip

    unauthorized_devices_filter(target)
