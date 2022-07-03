
import telnetlib
import getpass
import sys
 
 
HOST = input("Enter Device IP:")
user = input("Enter your telent username:")
password = getpass.getpass()
 
tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user+"\n")
if password:
    tn.read_until("Password: ")
    tn.write(password+"\n")

tn.write("enable\n")
tn.write("cicsco\n")
tn.write("conf t\n")
tn.write("int loop 0\1\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

