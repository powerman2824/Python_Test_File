from ipaddress import IPv4Network



print("## Hello I am FOO                      ###")
print("## Welcome to My Magic IPv4 Calculator ###")
# X gets input from the user
x = input("Please enter your IPv4 Address with / Subnet Mask notation ex:192.168.1.1/24-->")  
x_ip = IPv4Network(x, strict=False)


# X number of statements related to IPv4 addr
x_show_num_addresses = "## This is the IPv4 address ammount of Hosts Addresses"
x_show_network_address = "## This is the IPv4 address Network Address"
x_show_broadcast_address = "## This is the IPv4 address Broadcast Address"


# X if statement to classify IPv4 addr
x_if_class_a = "## This is a Class A Network"
x_if_class_b = "## This is a Class B Network"
x_if_class_c = "## This is a Class C Network"
x_if_class_d = "## This is a Class D Network"
x_if_class_e = "## This is a Class E Network"
x_if_invaild = "## 127 is an Invaild IPv4 Address"
x_if_multicast = "## This is a Multicast address. See RFC 3171"
x_if_private = "## This is a Private address. See iana-ipv4-special-registry"
x_if_global = "## This is a Global address. See iana-ipv4-special-registry"
x_if_unspecified = "## This is a Unspecified address. RFC 5735"
x_if_reserved = "## This is a Reserved address, otherwise IETF reserved."
x_if_loopback = "## This is a Loopback address. See RFC 3330"
x_if_link_local = "## This is a Link Local address. See RFC 3927"
x_if_site_local = "## This is a Site Local addrss. See RFC 3879"

# This is where we will make new funtion to add to the main funtion

def foo_info(x_ip):
    print(x_show_num_addresses) ; print(str(x_ip.num_addresses))
    print(x_show_network_address) ; print(x_ip.network_address)
    print(x_show_broadcast_address) ; print(x_ip.broadcast_address)

def foo_class(x_ip):
    if x_ip.is_multicast == True:
        print(x_if_private)
    elif x_ip.is_private == True:
        print(x_if_private)
    elif x_ip.is_global == True:
        print(x_if_global)
    elif x_ip.is_unspecified == True:
        print(x_if_unspecified)
    elif x_ip.is_reserved == True:
        print(x_if_reserved)
    elif x_ip.is_loopback == True:
        print(x_if_loopback)
    elif x_ip.is_link_local == True:
        print(x_if_link_local)
    elif x_ip.is_site_local == True:
        print(x_if_site_local)
    else:
        print("## Somthing went wrong?")

# The main fuintion we can write the funtion into here

def foo_ip(x_ip):
    if float(x_ip.compressed[0:3]) >= 240:
        print(x_if_class_e) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif float(x_ip.compressed[0:3]) >= 224:
        print(x_if_class_d) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif float(x_ip.compressed[0:3]) >= 192:
        print(x_if_class_c) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif float(x_ip.compressed[0:3]) >= 128:
        print(x_if_class_b) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif float(x_ip.compressed[0:3]) == 127:
        print(x_if_invaild)
    elif float(x_ip.compressed[0:3]) >= 1:
        print(x_if_class_a) ;
        foo_class(x_ip)
        foo_info(x_ip)
    else:
        print("## Please re-enter your IPv4 address.")
    
foo_ip(x_ip)
