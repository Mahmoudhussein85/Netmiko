import os 
os.chdir("/home/vm-ubuntu/scripts")

from netmiko import ConnectHandler

r1 = ConnectHandler(ip = "11.11.11.102", username = "Raya", password = "cisco123", device_type = "cisco_ios" )
r2 = ConnectHandler(ip = "11.11.11.103", username = "Raya", password = "cisco123", device_type = "cisco_ios" )

devices = [r1, r2]
n = 1
    
for dev in devices:
    print(f'Connecting to Router{n}:{str(dev.is_alive())}')
    dev.establish_connection()
    dev.enable()
    print("Saving the Config")
    dev.send_command("wr")
    print("Backing up Configs")
    dev.send_command("terminal length 0")
    dev_config = dev.send_command("show run")
    with open("R" + str(n) + "_running_new.cfg","w") as temp:
        temp.write(dev_config)

    dev.disconnect()
    n += 1
