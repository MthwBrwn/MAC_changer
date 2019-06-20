#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option('-i', '--interface', dest='interface', help='This is the interface (eth, wlan, etc) whose MAC will be changed')
parser.add_option('-m', '--mac', dest='new_mac', help='The new MAC address')

(options, args) = parser.parse_args()

interface = options.interface
new_mac =  options.new_mac

print('[+] changing MAC address for ' + interface + ' to ' + new_mac)


subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])

subprocess.call(['ifconfig', interface])





