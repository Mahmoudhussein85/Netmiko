import netmiko

from netmiko import ConnectHandler

r1 = ConnectHandler(ip = "11.11.11.102", username = "Raya", password = "cisco123", device_type = "cisco_ios" )
r2 = ConnectHandler(ip = "11.11.11.103", username = "Raya", password = "cisco123", device_type = "cisco_ios" )

devices = [r1, r2]
hostnames = [] 
for dev in devices:  
    hostname = dev.send_command("show run | in hostname").split()[1]
    hostnames.append(hostname)
    print(f'Connecting to {hostname}:{str(dev.is_alive())}')

device = input("Which routing table do you want to see? ")
show_cmd  = input("Desired Command to execute? ")

if device.lower() == hostnames[0].lower() :
    r1.enable()
    r1.send_command("terminal length 0")
    print(f'This is the oute of {show_cmd} executing on {hostnames[0]}')
    output = r1.send_command(show_cmd)
    print(output)
    r1.disconnect()
elif device.lower() == hostnames[1].lower():
    r2.enable()
    r2.send_command("terminal length 0")
    print(f'This is the oute of {show_cmd} executing on {hostnames[1]}')
    output = r2.send_command(show_cmd)
    print(output)
    r2.disconnect()
else:
    print("Invalid Device")