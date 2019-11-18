#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, newmac):
  print("[+] Changing Mac address for " + interface + " to " + newmac)

  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
  subprocess.call(["ifconfig", interface, "up"])

parser = optparse.Optionparser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="newmac", help="New MAC address")

(options, arguements) = parser.parse_args()

change_mac(options.interface, options.newmac)
