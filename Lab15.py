import os 
os.chdir("/home/vm-ubuntu/scripts")

from netmiko import ConnectHandler

r1 = ConnectHandler(ip = "11.11.11.102", username = "Raya", password = "cisco123", device_type = "cisco_ios" )
r2 = ConnectHandler(ip = "11.11.11.103", username = "Raya", password = "cisco123", device_type = "cisco_ios" )
fw1 = ConnectHandler(ip = "11.11.11.104", username = "Raya", password = "cisco123", device_type = "cisco_ios" )

devices = [r1, r2, fw1] 

def devices_configs (dev):
    dev.establish_connection()
    dev.enable()
    hostname = dev.send_command("show run | in hostname").split()[1]
    if "fw" in hostname.lower():
        dev.send_command("terminal page 0")
    else:
        dev.send_command("terminal length 0")
    print(f'Connecting to device: {hostname}')
    dev.send_command("wr")
    print(f'Backing configs of device: {hostname}')
    temp = dev.send_command("show run")

    with open(f'{hostname}.cfg', "w") as dev_file:
        dev_file.write(temp)
    
    dev.disconnect()

for device in devices:
    devices_configs(device)