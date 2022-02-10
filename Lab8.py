info1 = {"hostname":"R1", "mgmt-ip": "10.1.1.1", "username":"rohit", "password":"cisco"}

#info2 = {"hostname":"R2", "mgmt-ip": "10.1.1.2", "username":"rohit", "password":"cisco"}

info2 = {}
info2["hostname"] = "R2"
info2["mgmt-ip"] = "10.1.1.2"
info2["username"] = "rohit"
info2["password"] = "cisco"

info = []
info.append(info1)
info.append(info2)

print(info)


