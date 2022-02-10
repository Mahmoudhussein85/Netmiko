from netmiko import ConnectHandler
import getpass
import readline


print("You have two deivces R1, R2")

def device_connect(cmd,devices):

    for device in devices:
        device.enable()
        hostname = device.send_command("show run | in hostname").split()[1]
        if "r1" in hostname.lower() or "r2" in hostname.lower() :
            print(f'Connecting to {hostname}:{str(device.is_alive())}')
            device.send_command("terminal length 0")
            cmd_out = device.send_command(cmd)
            print(f'This is the output of {hostname}')
            print(cmd_out)
            device.disconnect()
        elif "fw" in hostname.lower():
            pass

cmd = input("Enter the router show command you want to display? ")
dev_username = input("Enter the username: ")
dev_password = getpass.getpass("Enter the password: ")

R1 = ConnectHandler(ip = "11.11.11.102", username = dev_username, password = dev_password, device_type = "cisco_ios" )
R2 = ConnectHandler(ip = "11.11.11.103", username = dev_username, password = dev_password, device_type = "cisco_ios" )
devices = [R1, R2]

dev_output = device_connect(cmd,devices)

