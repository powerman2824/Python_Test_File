# This calls in the ipaddess-IPv4/IPv6 manipulation library python module
# Source code: Lib/ipaddress.py
from ipaddress import IPv4Network


# Hello messages form Mr.Foo This is Foo = :{
print("-> Hello & Welcome to Foo's :{ IPv4 'IP Address' Info Helper")
print("-> This is not a Full IPv4/IPv6 Calculator YET!! :{ ")
print("-> Foo's IPv4 Info Helper shows basic info about the entered IPv4 address")
print("-> Please enter the IPv4 Address you would like to know more info about")
print("-> Enter the IPv4 Address in / Subnet Mask Notation")
print("   ___________________________________________")
print("  *___________________________________________*")
print("")

# X gets input from the user
x = input("-> Please see eample:192.168.1.1/24\n-> Enter the address below\n-> ")
x_ip = IPv4Network(x, strict=False)


# X number of statements related to IPv4 addr
x_show_num_addresses = "-> This is how many Host Addresses your IPv4 Address has"
x_show_network_address = "-> This is your IPv4 Address - Network address"
x_show_broadcast_address = "-> This is your IPv4 Address - Broadcast Address"


# X if statement to classify IPv4 addr
x_if_class_a = "-> This is a Class A Network"
x_if_class_b = "-> This is a Class B Network"
x_if_class_c = "-> This is a Class C Network"
x_if_class_d = "-> This is a Class D Network"
x_if_class_e = "-> This is a Class E Network"
x_if_invaild = "-> 127 is an Invaild IPv4 Address"
x_if_multicast = "-> This is a Multicast address.\n-> See RFC 3171 www.rfc-editor.org/info/rfc3171"
x_if_private = "-> This is a Private address.\n-> See the Iana IPv4 Special Registry\n-> www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml\n-> See RFC 1918 for more info www.rfc-editor.org/info/rfc1918"
x_if_global = "-> This is a Global address.\n-> See the Iana Ipv4 Special Registry\n-> www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml "
x_if_unspecified = "-> This is a Unspecified address.\n-> See RFC 5735 www.rfc-editor.org/info/rfc5735"
x_if_reserved = "-> This is a Reserved address, otherwise IETF reserved."
x_if_loopback = "-> This is a Loopback address.\n-> See RFC 3330 www.rfc-editor.org/info/rfc3330"
x_if_link_local = "-> This is a Link Local address.\n-> See RFC 3927 www.rfc-editor.org/info/rfc3927"
x_if_site_local = "-> This is a Site Local addrss.\n-> See RFC 3879 www.rfc-editor.org/info/rfc3879"


# This is where we will make new funtion to add to the main funtion

def foo_info(x_ip):
    print(x_show_num_addresses) ; print("-> " + str(x_ip.num_addresses))
    print(x_show_network_address) ; print("-> " + str(x_ip.network_address))
    print(x_show_broadcast_address) ; print("-> " + str(x_ip.broadcast_address))

def foo_class(x_ip):
    if x_ip.is_multicast == True:
        print(x_if_multicast)
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
        print("-> Somthing went wrong?")


# The main fuintion we can write the funtion into here
def foo_ip(x_ip):
    if x_ip >= IPv4Network('240.0.0.1',strict=False):
        print(x_if_class_e) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif x_ip >= IPv4Network('224.0.0.1',strict=False):
        print(x_if_class_d) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif x_ip >= IPv4Network('192.0.0.1',strict=False):
        print(x_if_class_c) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif x_ip >= IPv4Network('128.0.0.1',strict=False):
        print(x_if_class_b) ;
        foo_class(x_ip)
        foo_info(x_ip)
    elif float(x_ip.compressed[0:3]) == 127:
        print(x_if_invaild)
    elif x_ip >= IPv4Network('1.0.0.1',strict=False):
        print(x_if_class_a) ;
        foo_class(x_ip)
        foo_info(x_ip)
    else:
        print("-> Please re-enter your IPv4 address.")

# This calls in or funtion    
foo_ip(x_ip)
