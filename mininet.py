from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import CPULimitedHost

def A():
	#Pemanggilan Fungsi Miniet
	net = Mininet(link=TCLink, host=CPULimitedHost)

	#Membuat Adonan Dasar
	# Add hosts
	h1 = net.addHost( 'h1',ip='192.168.1.2/24', mac='00:00:00:00:01:01' ) #mac addres bisa bebas
	h2 = net.addHost( 'h2',ip='192.168.2.2/24', mac='00:00:00:00:02:02' ) #mac addres bisa bebas
	# Add router
	r1 = net.addHost('r1')
	# Add links
	net.addLink(r1,h1,bw='jumlahbw',max_queue_size=100) #bw diatur sesuai bandwidth soal, misal 1gb maka tulis 1000
	net.addLink(r1,h2,bw='jumlahbw',max_queue_size=100)
	net.build()
	#Build Interface
	r1.cmd("ifconfig r1-eth0 0") #diset 0 maka remove IP Address
	r1.cmd("ifconfig r1-eth1 0") #diset 0 maka remove IP Address

`	#Pada Bagian ini, akan diatur mac address dan ipconfig untuk Router
	#Assign Mac Address
	r1.cmd("ifconfig r1-eth0 hw ether 00:00:00:01:01:01")
	r1.cmd("ifconfig r1-eth1 hw ether 00:00:00:01:02:02")
	#Assign IP Address
	r1.cmd("ip addr add 192.168.1.1/24 brd + dev r1-eth0")
	r1.cmd("ip addr add 192.168.2.1/24 brd + dev r1-eth1")
	r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

	#Menghubungkan Device dengan Router
	#Assign Default Route
	h1.cmd("ip route add default via 192.168.1.1")
	h2.cmd("ip route add default via 192.168.2.1")

	#Menambahkan Congestion Control
	h1.cmd("sysctl -w net.ipv4.tcp_congestion_control='namaalgoritma")
	h2.cmd("sysctl -w net.ipv4.tcp_congestion_control='namaalgoritma")

	#Menjalankan Mininet
	print("== Mininet Berjalan ==")
	CLI(net)
	print("== Mininet Berhenti ==")
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	A()
