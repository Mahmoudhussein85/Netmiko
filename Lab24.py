traceroute = '''
Type escape sequence to abort 
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 mesc 0 mesc
  2 16.0.0.5  0 msec 5 mesc 4 mesc
  3 10.0.12.1 4 msec 1 mesc 4 mesc
  4 19.0.12.1 4 msec *  1 mesc
'''
import textfsm

with open("traceroute.template") as temp:
    fsm = textfsm.TextFSM(temp)
    result = fsm.ParseText(traceroute)

print(fsm.header)
print(result)