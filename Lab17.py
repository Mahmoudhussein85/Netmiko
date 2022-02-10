import netmiko

from netmiko import ConnectHandler

print("You have two deivces R1, R2")

def device_connect(cmd,dev,dev_username,dev_password):
    
    if dev.lower() == "r1":
        dev_connect = ConnectHandler(ip = "11.11.11.102", username = dev_username, password = dev_password, device_type = "cisco_ios" )
        hostname = dev_connect.send_command("show run | in hostname").split()[1]
        print(f'Connecting to {hostname}:{str(dev_connect.is_alive())}')
        dev_connect.enable()
        dev_connect.send_command("terminal length 0")
        cmd_out = dev_connect.send_command(cmd)
        dev_connect.disconnect()
        return cmd_out
    elif dev.lower() == "r2":
        dev_connect = ConnectHandler(ip = "11.11.11.103", username = dev_username, password = dev_password, device_type = "cisco_ios" )
        hostname = dev_connect.send_command("show run | in hostname").split()[1]
        print(f'Connecting to {hostname}:{str(dev_connect.is_alive())}')
        dev_connect.enable()
        dev_connect.send_command("terminal length 0")
        cmd_out = dev_connect.send_command(cmd)
        dev_connect.disconnect()
        return cmd_out
    else:
        print("Invalid Device")

dev = input("Enter the router show command you want to display? ")
dev_username = input(f'Enter the username of the {dev}: ')
dev_password = input(f'Enter the password of the {dev}: ')
cmd =input("Enter the command: ")
dev_output = device_connect(cmd,dev,dev_username=dev_username, dev_password=dev_password)
print(f'Executing {cmd} on {dev}:')
print(dev_output)