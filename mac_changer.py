#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):

    print('[+] changing MAC address for ' + interface + ' to ' + new_mac)

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

    subprocess.call(['ifconfig', interface])

def get_args():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='This is the interface (eth, wlan, etc) whose MAC will be changed')
    parser.add_option('-m', '--mac', dest='new_mac', help='The new MAC address')
    return parser.parse_args()

(options, args) = get_args()
change_mac(options.interface, options.new_mac)








