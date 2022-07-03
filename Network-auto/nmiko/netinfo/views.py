from django.shortcuts import render
from .forms import CmdForm
from .networks import NetForm
# Create your views here.

# try declaring conn1 and conn2 as global variables

neighbor1 = ''
neighbor2 = ''

route1 = ''
route2 = ''

def enableOspf1(conn1) :
    conn1.send_command('router ospf 1') 

def enableOspf2(conn2) :
    conn2.send_command('router ospf 2')    

def addNetwork(conn1,conn2,address,mask,area):
    config_list = ['router ospf 1','network {} {} area {}'.format(address, mask,area)]
    conn1.send_config_set(config_list)
    config_list2 = ['router ospf 2','network {} {} area {}'.format(address, mask,area)]
    conn2.send_config_set(config_list2)
                        
def showNeighbors(conn):
    neighbor1 = conn.send_command('show ip ospf neighbor')
    return neighbor1

def showIpRoute(conn):
    route1 = conn.send_command('show ip route ospf')
    return route1
def index(request):
        if request.method == "POST":
            # if request.POST['do'] == 'Submit':
                form = CmdForm(request.POST)
                network = NetForm(request.POST)
                if form.is_valid():
                        from netmiko import ConnectHandler
                       
                        username = request.POST.get('username','')
                        password = request.POST.get('password','')
                        ip1=request.POST.get('ip1','')
                        ip2=request.POST.get('ip2','')

                        device1 = {}
                        device2 = {}
                        device1['device_type'] = 'cisco_ios'
                        device1['ip'] = ip1
                        device1['username'] = username
                        device1['password'] = password
                        device2['device_type'] = 'cisco_ios'
                        device2['ip'] = ip2
                        device2['username'] = username
                        device2['password'] = password


                        conn1 = ConnectHandler(**device1)
                        conn1.enable()
                        conn2 = ConnectHandler(**device2)
                        conn2.enable()

                        # output = conn2.send_command('sh ip ospf neighbor')
                        output=''

                        address = request.POST.get('address','')
                        mask=request.POST.get('mask','')
                        area=request.POST.get('area','')


                if request.POST['do'] == 'EnableOspf1':
                    enableOspf1(conn1)
                elif request.POST['do'] == 'EnableOspf2':
                    enableOspf2(conn2)
                elif request.POST['do'] == 'Add network':
                    addNetwork(conn1, conn2,address,mask,area)           # i need to return conn1 and conn2 !!
                elif request.POST['do'] == 'Show neighbors for router 1':
                    output = showNeighbors(conn1)
                elif request.POST['do'] == 'Show neighbors for router 2':
                    output = showNeighbors(conn2)    
                elif request.POST['do'] == 'Show ip routes for router 1':
                    output = showIpRoute(conn1)
                elif request.POST['do'] == 'Show ip routes for router 2':
                    output = showIpRoute(conn2)

                return render(request, 'netinfo/index.html', {
                            'form' : form,
                            'network':network,
                            'neighbor1':neighbor1,
                            'output':output
                            })
        else:
                form = CmdForm()
                network = NetForm()
                return render(request, 'netinfo/index.html', {'form' : form,'network':network})
# def enableOspf1(request):
#     if request.method == 'GET':
#         conn1 = request.GET.get('value')
#         enableOspf1(conn1)
#         result="Ospf enabled"
#         return HttpResponse(result)                
# # def enableOspf2(request):
# #     if request.method == 'POST':
# #         enableOspf2()
# def addNetwork(request):
#     if request.method == 'POST':
#         addNetwork()
# def showNeighbors(request):
#     if request.method == 'POST':
#         showNeighbors()
# def showIpRoute(request):
#     if request.method == 'POST':
#         showIpRoute()
# Create your views here.
