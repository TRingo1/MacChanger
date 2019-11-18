#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
  parser = optparse.Optionparser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
  parser.add_option("-m", "--mac", dest="newmac", help="New MAC address")
  return parser.parse_args()

def change_mac(interface, newmac):
  print("[+] Changing Mac address for " + interface + " to " + newmac)
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
  subprocess.call(["ifconfig", interface, "up"])

(options, arguements) = get_arguments()
change_mac(options.interface, options.newmac)
