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

def get_current_mac(interface)
  ifconfig_result = subprocess.check_output(["ifconfig" , options.interface])
  mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
  
  if mac_address_search_result:
    return mac_address_search_result.group(0)
  else
    print("[-] Could not read MAC address)

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
change_mac(options.interface, options.newmac)
current_mac = get_current_mac(options.interface)
if current_mac == options.newmac
   print("[+] MAC address was successfully changed to " + current_mac)
    
