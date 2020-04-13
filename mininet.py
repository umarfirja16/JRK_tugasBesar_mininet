from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import CPULimitedHost

def main():
	# call Miniet function
	net = Mininet(link = TCLink, host=CPULimitedHost)
	
	# add hosts
	h1 = net.addHost('h1',ip = '192.168.1.2/24', mac = '00:00:00:00:01:01') #mac addres is free
	h2 = net.addHost('h2',ip = '192.168.2.2/24', mac = '00:00:00:00:02:02')
	
	# add router
	r1 = net.addHost('r1')
	
	# add links
	net.addLink(r1,h1,bw = 'jumlahbandwidth', max_queue_size = 100) # 1GB = 1000
	net.addLink(r1,h2,bw = 'jumlahbandwidth', max_queue_size = 100)
	net.build()
	
	# build interface
	r1.cmd("ifconfig r1-eth0 0") #set 0 to remove IP Address
	r1.cmd("ifconfig r1-eth1 0")

`	# config mac address & ipconfig for Router
	# assign mac address
	r1.cmd("ifconfig r1-eth0 hw ether 00:00:00:01:01:01")
	r1.cmd("ifconfig r1-eth1 hw ether 00:00:00:01:02:02")
	
	#assign IP Address
	r1.cmd("ip addr add 192.168.1.1/24 brd + dev r1-eth0")
	r1.cmd("ip addr add 192.168.2.1/24 brd + dev r1-eth1")
	r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

	#connecting Device to Router
	#assign default route
	h1.cmd("ip route add default via 192.168.1.1")
	h2.cmd("ip route add default via 192.168.2.1")

	# add congestion control
	h1.cmd("sysctl -w net.ipv4.tcp_congestion_control='namaalgoritma")
	h2.cmd("sysctl -w net.ipv4.tcp_congestion_control='namaalgoritma")

	# run Mininet
	print("== Mininet Berjalan ==")
	CLI(net)
	print("== Mininet Berhenti ==")
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	main()
