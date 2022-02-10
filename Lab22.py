from netmiko import ConnectHandler
import getpass
import readline
import sys
import argparse
import csv


#Function to send command to the device
def device_connect(cmd,devices,hostnames):

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

#To enable input paramters to the script
parser = argparse.ArgumentParser(description='Connenction to Routers R1,R2')
parser.add_argument('-u','--username', type=str, help='This is username ')
parser.add_argument('-c','--command', type=str, help='This is command you want to execute ')
args = parser.parse_args()

dev_username = args.username
cmd  = args.command

dev_password = getpass.getpass("Enter the password: ")
print(f'The command you entered: {cmd}')
print("---------------------------------------------------------")

#Reading  routers ips from csv file and connect to them
ips=[]
routers = []
hostnames = []
counter = 0
with open('new2.csv', newline='') as csvfile:
    content = csv.reader(csvfile, delimiter=',')
    for row in content:
        ips.append(row)
        hostnames.append(row[0].lower())
        dev = ConnectHandler(ip = row[1], username = dev_username, password = dev_password, device_type = "cisco_ios" )
        routers.append(dev)
        counter += 1

    
print(f'You have {counter} devices')
dev_output = device_connect(cmd,routers,hostnames)