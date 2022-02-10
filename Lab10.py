vlans = []
vlans.append({"id":"10", "name":"DATA"})
vlans.append({"id":"20", "name":"VOICE"})
vlans.append({"id":"30", "name":"MGMT"})

modify_vlans = open("vlans.cfg", "w")

content = "vlan" + vlans[0]["id"] + "\n" + "\tname"+ vlans[0]["name"] + "\n" 
modify_vlans.write(content)

content = "vlan" + vlans[1]["id"] + "\n" + "\tname"+ vlans[1]["name"] + "\n" 
modify_vlans.write(content)

content = "vlan" + vlans[2]["id"] + "\n" + "\tname"+ vlans[2]["name"] + "\n" 
modify_vlans.write(content)

modify_vlans.close()

import os 

os.chdir("/home/vm-ubuntu/scripts")
os.system("cat vlans.cfg")