dict1 = {"hostname":"R1", "mgmt-ip":"10.1.1.1", "username": "rohit", "password": "cisco"}
dict2 = {"hostname":"R2", "mgmt-ip":"10.1.1.2", "username":"rohit", "password":"cisco"}
interfaces_r1 = {"interface":"G1", "ip_address":"192.168.1.1"}
interfaces_r2 = {"interface":"G1", "ip_address":"192.168.1.1"}

# dict1["interfaces"] = interfaces_r1
# dict2["interfaces"] = interfaces_r2
# data_center = []
# data_center.append(dict1)
# data_center.append(dict2)
#print (data_center)

data_center = []
data_center.append(dict1)
data_center.append(dict2)
data_center[0]["interfaces"] = interfaces_r1
data_center[1]["interfaces"] = interfaces_r2

import json 
print(json.dumps(data_center, indent=4))


