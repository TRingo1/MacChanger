#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.Optionparser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="newmac", help="New MAC address")

parser.parse_args()


interface = raw_input("Interface you want to update mac address, ie: eth0, wlan0 > ")
newmac = raw_input("New MacAddress x:x:x:y:y:y > ")
print("[+] Changing Mac address for " + interface + " to " + newmac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
subprocess.call(["ifconfig", interface, "up"])
