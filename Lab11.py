intf = []
intf.append({"int":"interface", "name":"G0/0"})
intf.append({"int":"interface", "name":"G0/1"})
intf.append({"int":"interface", "name":"G0/2"})
intf.append({"des":"description", "name":"Connected via Python"})
intf.append({"cmd":"no", "status":"shut"})

with open("r1.interfaces.cfg", "w") as modify_intf:
    modify_intf.write(intf[0]["int"] + " " + intf[0]["name"] + "\n" + intf[3]["des"] + "\n" + intf[4]["cmd"] + " " +intf[4]["status"] + "\n") 
    modify_intf.write(intf[1]["int"] + " " + intf[1]["name"] + "\n" + intf[3]["des"] + "\n" + intf[4]["cmd"] + " " +intf[4]["status"] + "\n") 
    modify_intf.write(intf[2]["int"] + " " + intf[2]["name"] + "\n" + intf[3]["des"] + "\n" + intf[4]["cmd"] + " " +intf[4]["status"] + "\n") 

r1_temp = open("r1.interfaces.cfg", "r")
R1 = r1_temp.read()
print(R1)

# import os 
# os.chdir("/home/vm-ubuntu/scripts")
# os.system("cat r1.interfaces.cfg")