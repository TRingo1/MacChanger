#!/usr/bin/env python

import subprocess

interface = "eth0"
newmac = "00:11:22:33:44:55"
print("[+] Changing Mac address for " + interface + " to " + newmac)


subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + newmac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
