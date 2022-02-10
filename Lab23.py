from importlib_metadata import version
from netmiko import ConnectHandler
import getpass
import readline
import sys
import argparse
import csv
import re


#Function to send command to the device
def device_connect(cmd,devices):

    for device in devices:
        device.enable()
        hostname = get_hostname(device)
        version = get_version(device)
        #if "r1" in hostname.lower() or "r2" in hostname.lower() 
        if "fw" in hostname.lower(): 
            pass
        else:
            print("------------------------------------------------")
            print(f'Connecting to {hostname}:{str(device.is_alive())}')
            device.send_command("terminal length 0")
            cmd_out = device.send_command(cmd)
            print(f'Info of Configured Interfaces')
            get_ip (device)
            print("------------------------------------------------")
            print(f'Output of {cmd}:')
            print(cmd_out)
            
        print("##############################################")
        device.disconnect()
       

#Function to get the hostname
def get_hostname(device):
    device.enable()
    hostname = device.send_command("show run | in hostname").split()[1]
    return hostname

#Function to get the version
def get_version(device):
    device.enable()
    hostname = get_hostname(device)
    output = device.send_command("show version")
    if "fw" in hostname.lower():
        pass
    else:
        pattern = re.compile(r"Software Version (\S+)") 
    version_match = pattern.search(output)
    return version_match

#Fucntion to get the configured interfaces 
def get_ip(device):
    device.enable()
    hostname = get_hostname(device)
    output = device.send_command("show run")
    if "fw" in hostname.lower(): 
        pass
    else:
        #pattern = re.compile(r"interface (\w+\d.\d)\r?\n?\s?ip address ([\d\.]+) ([\d\.]+)")
        pattern = re.compile(r"interface (:?\w+\d.\d|Loopback\d\d)\r?\n?\s?ip address ([\d\.]+) ([\d\.]+)")
        match = pattern.findall(output)
        for matches in match:
            #print("\tInterface: "+ matches[0] + "\n" + "\tIP Address: " + matches[1] + "\n" + "\tMask: " + matches[2])
	        print("Interface: "+ matches[0] + "\n" + "\tIP Address: " + matches[1] + "\n" + "\tMask: " + matches[2])

        


#To enable input paramters to the script
parser = argparse.ArgumentParser(description='Connenction to Routers R1,R2')
parser.add_argument('-u','--username', type=str, help='This is username ')
parser.add_argument('-c','--command', type=str, help='This is command you want to execute ')
args = parser.parse_args()


dev_username = args.username
cmd  = args.command
dev_password = getpass.getpass("Enter the password: ")
print(f'The command you entered: {cmd}')
print("------------------------------------------------")

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
dev_output = device_connect(cmd,routers)