import wmi
import time
c = wmi.WMI()  #返回一个 WMI实例

netConfig = c.Win32_NetworkAdapterConfiguration(IPEnabled=True) #获得网卡已开的网络配置对象
for objConfig in netConfig:
    if objConfig.SettingID == '{44798F26-40DD-4616-BC7C-D826A0AD86D3}':
        print("修改前配置信息：")
        print("MAC地址："+objConfig.MACAddress)
        print("IP地址："+str(objConfig.IPAddress)) #ip地址
        print("子网掩码："+str(objConfig.IPSubnet) )  #子网掩码
        print("网关："+str(objConfig.DefaultIPGateway)) # 网关
        print("DNS地址："+str(objConfig.DNSServerSearchOrder))  #DNS地址
        print("Caption："+str(objConfig.Caption))
        print("SettingID："+str(objConfig.SettingID))
        print('#######################################################################')

arrIPAddress = ['10.32.147.226']
arrSubnetMask = ['255.255.255.128']
arrDefaultGateways = ['10.32.147.129']
arrGatewayCostMetrics = [1]
arrDNSServers = ['10.32.166.158']
returnValue_ip = objConfig.EnableStatic(IPAddress=arrIPAddress,SubnetMask=arrSubnetMask) #修改ip和子网掩码
returnValue_gateway = objConfig.SetGateways(DefaultIPGateway= arrDefaultGateways,GatewayCostMetric= arrGatewayCostMetrics)
returnValue_dns = objConfig.SetDNSServerSearchOrder(DNSServerSearchOrder= arrDNSServers)

if returnValue_ip[0]==0:
    print("ip和子网掩码设置成功")
elif returnValue_ip[0]==1:
    print("ip和子网掩码设置成功，需要重启生效")
else:
    print("ip和子网掩码设置失败")

if returnValue_gateway[0]==0:
    print("网关设置成功")
elif returnValue_gateway[0]==1:
    print("网关设置成功，需要重启生效")
else:
    print("网关设置失败")

if returnValue_dns[0]==0:
    print("DNS设置成功")
elif returnValue_dns[0]==1:
    print("DNS设置成功，需要重启生效")
else:
    print("DNS设置失败")

print('#######################################################################')
print("修改后配置信息：")
print("IP地址："+str(arrIPAddress)) #ip地址
print("子网掩码："+str(arrSubnetMask ))  #子网掩码
print("网关："+str(arrDefaultGateways)) # 网关
print("DNS地址："+str(arrDNSServers)) #DNS地址

time.sleep(20)
