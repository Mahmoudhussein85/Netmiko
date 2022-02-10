from netmiko import ConnectHandler

R1 = ConnectHandler(ip = "11.11.11.102", username = "Raya", password = "cisco123", device_type = "cisco_ios" )
R2 = ConnectHandler(ip = "11.11.11.103", username = "Raya", password = "cisco123", device_type = "cisco_ios" )


print(f'Connection to Router1:{str(R1.is_alive())}')
print(f'Connection to Router2:{str(R2.is_alive())}')

config = open("R1.cfg", "r")
config_R1 = config.read()

config = open("R2.cfg", "r")
config_R2 = config.read()

cmd = config_R1
R1.enable()
output_R1 = R1.send_config_set(cmd)
#You can use the command R1.send_config_from_file("R1.cfg") without nee to use open() command 
print("=====================R1 Configuration=====================")
print(output_R1)
output_R1 = R1.send_command("show running")
print("Saving running configuration of R1 in R1_runnig.cfg")
runnig_config = open("R1_runnig.cfg", "w")
runnig_config.write(output_R1)
R2.send_command("wr")
R1.disconnect()

cmd = config_R2
R2.enable()
output_R2 = R2.send_config_set(cmd)
print("=====================R2 Configuration=====================")
print(output_R2)
output_R2 = R2.send_command("show running")
print("Saving running configuration of R2 in R2_runnig.cfg")
runnig_config = open("R2_runnig.cfg", "w")
runnig_config.write(output_R2)
R2.send_command("wr")
R2.disconnect()

print("==========================================================")
Check_Connection_to_R1 = R1.is_alive()
Check_Connection_to_R2 = R2.is_alive()
print(f'Connection to Router1:{str(Check_Connection_to_R1)}')
print(f'Connection to Router1:{str(Check_Connection_to_R2)}')
