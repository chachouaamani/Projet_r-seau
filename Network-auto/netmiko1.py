from netmiko import ConnectHandler
device = {}
device['device_type'] = 'cisco_ios'
device['ip'] = '192.168.43.120'
device['username'] = 'admin'
device['password'] = 'cisco'

conn = ConnectHandler(**device)

output = conn.send_command("show version | i uptime")
print(output)