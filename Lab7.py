from dbus import Interface


ip_address = "10.1.5.5"
interface = "G0/0/0/0"
description = "connected vi Python"

List = []
List.append(interface)
List.append(ip_address)
List.append(description)
List.append("shut")

print(List[0])
print(List[1])
print(List[2])
print(List[3])
print(List)

List[3] = "no shut"

message = "The IP address of the route is {} and the management interface is {} "
print(message.format(ip_address,interface))
