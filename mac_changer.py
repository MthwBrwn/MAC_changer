#!/usr/bin/env python

import subprocess
import optparse
import re

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
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error('please input interface. see --help for info. ')
    if not options.new_mac:
        parser.error('please input new MAC value. see --help for info. ')
    return options

options = get_args()
# change_mac(options.interface, options.new_mac)

check = subprocess.check_output(['ifconfig', options.interface])
search_result = re.search(r'([0-9A-F]{2}[:-]){5}([0-9A-F]{2})', check)

print(check)
print(search_result.group(0))









