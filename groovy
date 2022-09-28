##
## Active saved database "initial"
## Generated at 2001/01/01 05:35:59 +0000
## Hostname: hon-poc-1
## Product release: 3.9.2110
##

##
## Running-config temporary prefix mode setting
##
no cli default prefix-modes enable

##
## L3 configuration
##
   vrf definition mgmt

##
## Network interface configuration
##
no interface mgmt0 dhcp
   interface mgmt0 ip address 10.132.0.222 /24
no interface mgmt1 dhcp
   interface mgmt1 dhcp hostname
   interface mgmt1 display
   interface mgmt1 duplex auto
   interface mgmt1 mtu 1500
no interface mgmt1 shutdown
   interface mgmt1 speed auto
no interface mgmt1 zeroconf

##
## Network interface IPv6 configuration
##
no interface mgmt0 ipv6 dhcp client enable
no interface mgmt1 ipv6 address autoconfig
   interface mgmt1 ipv6 address autoconfig default
no interface mgmt1 ipv6 address autoconfig privacy
no interface mgmt1 ipv6 dhcp client enable
   interface mgmt1 ipv6 enable

##
## Other IP configuration
##
   interface mgmt1 ip arp timeout 60
   hostname hon-poc-1
   ip domain-list hon-poc
   ip name-server vrf mgmt 4.2.2.2
   ip route vrf mgmt 0.0.0.0/0 10.132.0.1

##
## Local user account configuration
##
   username admin password 7 $6$oGs1RRNF$ROcvkuooKQb9X2TvMxZPe7k0XzKIN3aOUCVT6WaFUCNIZI.0C7wIqqjtg2agu/DboNYTkjAfjY6dkMLLAvfgV0
   username monitor password 7 $6$lnlmXa03$c3ZbOfxJln9fEF4OgmxZzVr8xM46bT.94taAyEVORUVXeU1p9X7lifBhrhyL/YW93rV0Jb62I4yELpIpGy4pL/

##
## Local user account configuration
##
   username admin password 7 $6$oGs1RRNF$ROcvkuooKQb9X2TvMxZPe7k0XzKIN3aOUCVT6WaFUCNIZI.0C7wIqqjtg2agu/DboNYTkjAfjY6dkMLLAvfgV0
   username monitor password 7 $6$lnlmXa03$c3ZbOfxJln9fEF4OgmxZzVr8xM46bT.94taAyEVORUVXeU1p9X7lifBhrhyL/YW93rV0Jb62I4yELpIpGy4pL/

##
## AAA remote server configuration
##
# ldap bind-password ********
   ldap vrf mgmt enable
   radius-server vrf mgmt enable
# radius-server key ********
   tacacs-server vrf mgmt enable
# tacacs-server key ********

##
## Password restriction configuration
##
no password hardening enable

##
## SNMP configuration
##
   snmp-server vrf mgmt enable

##
## Network management configuration
##
# web proxy auth basic password ********
   ntp vrf mgmt enable
   web vrf mgmt enable
