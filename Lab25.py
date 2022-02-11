from netmiko import ConnectHandler
import textfsm

dev_username="Raya"
dev_password="cisco123"

R1 = ConnectHandler(ip = "11.11.11.102", username = dev_username, password = dev_password, device_type = "cisco_ios" )
R2 = ConnectHandler(ip = "11.11.11.103", username = dev_username, password = dev_password, device_type = "cisco_ios" )

devices = [R1, R2]

#Function to get the hostname
def device_config(device):
    device.establish_connection()
    device.enable()
    hostname = device.send_command("show run | in hostname").split()[1]
    print(f'Connecting to {hostname}:{str(device.is_alive())}')
    device.send_command("terminal length 0")

    if "fw" in hostname.lower():
        output = device.send_command("show int ip brief")
    else:
        output = device.send_command("show ip int brief")    
    
    print(f'Connnectiong to device: {hostname}')

    with open("interface_brief.template") as temp:
        fsm = textfsm.TextFSM(temp)
        result = fsm.ParseText(output)
        print(fsm.header)
        print(result)

for item in devices:
    device_config(item)