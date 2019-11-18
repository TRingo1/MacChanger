#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
  parser = optparse.Optionparser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
  parser.add_option("-m", "--mac", dest="newmac", help="New MAC address")
  (options, arguments) = parcer.parse_args()
  if not options.interface:
    parser.error("[-] Please specify an interface, use --help for more info.")
  elif not options.newmac:
    parser.error("[-] Please specify a new mac, use --help for more info.")
  return options

 def change_mac(interface, newmac):
  print("[+] Changing Mac address for " + interface + " to " + newmac)
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
  subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.newmac)

ifconfig_result = subprocess.check_output(["ifconfig" , options.interface])
print(ifconfig_result)

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
if mac_address_search_result:
  print(mac_address_search_result.group(0))
else
  print("[-] Could not read MAC address)
