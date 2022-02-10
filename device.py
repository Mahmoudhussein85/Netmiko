def device_type(OS):
    dev1 = {"hostname":"R1", "OS":"IOS-XE", "mgmt-ip":"10.1.1.1"}
    dev2 = {"hostname":"R2", "OS":"IOS-XR", "mgmt-ip":"10.1.1.2"}
    dev3 = {"hostname":"R3", "OS":"IOS-XE", "mgmt-ip":"10.1.1.3"}
    dev4 = {"hostname":"R4", "OS":"IOS-XR", "mgmt-ip":"10.1.1.4"}
    dev5 = {"hostname":"R5", "OS":"NEXUS", "mgmt-ip":"10.1.1.5"}
    device_list = [dev1, dev2, dev3, dev4, dev5]
    count = 0
    for device in device_list:
        if device["OS"] == OS:
            print(f'The maagement IP of {device["hostname"]} running {device["OS"]} is {device["mgmt-ip"]}')    
        else:
            count = count + 1
            pass
    if count == len(device_list):
        print(f'OS: {OS} not found')
