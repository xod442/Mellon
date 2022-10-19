'''
                _ _
                | | |
  _ __ ___   ___| | | ___  _ __
 | '_ ` _ \ / _ \ | |/ _ \| '_ \
 | | | | | |  __/ | | (_) | | | |
 |_| |_| |_|\___|_|_|\___/|_| |_|

Mellanox 2010 Switch configuration

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick@rickkauffman.com"

'''
from flask import Flask, request, render_template, abort, redirect, url_for
import json
import uuid
import datetime
import csv
from jinja2 import Environment, FileSystemLoader

def commands(entryone, entrytwo):

    commands_one = [
    'potocol mlag',
    'lldp',
    'lacp',
    'vlan ' + str(entryone['ilo_vlan_number']),
    'vlan ' + str(entryone['management_vlan_number']),
    'vlan ' + str(entryone['iscsi_a_vlan_number']),
    'vlan ' + str(entryone['iscsi_b_vlan_number']),
    'vlan 4094',
    'dcb priority-flow-control enable force',
    'interface port-channel 200',
    'interface ethernet 1/21-1/22 channel-group 200 mode active',
    'interface vlan 4094 mtu 9216',
    'interface vlan 4094 ip address 10.100.100.1/30 primary',
    'interface port-channel 200 ipl 1',
    'interface vlan 4094 ipl 1 peer-address 10.100.100.2',
    'interface port-channel 200 dcb priority-flow-control mode on force',
    'mlag system-mac 00:00:5E:00:01:5D',
    'mlag-vip MLAG-DHCI ip ' + str(entryone['mlag_vip_ip']) + '/' + str(entryone['mlag_vip_mask']) + ' force',
    'no mlag shutdown',
    'interface mlag-port-channel 100',
    'interface ethernet 1/16 mlag-channel-group 100 mode active',
    'interface mlag-port-channel 100 mtu 9216 force',
    'interface mlag-port-channel 100 switchport mode trunk',
    'interface mlag-port-channel 100 switchport trunk allowed-vlan none',
    'interface mlag-port-channel 100 switchport trunk allowed-vlan add ' + str(entryone['ilo_vlan_number']),
    'interface mlag-port-channel 100 switchport trunk allowed-vlan add ' + str(entryone['management_vlan_number']),
    'interface mlag-port-channel 100 no shutdown',
    'interface ethernet 1/1-1/15 speed auto force',
    'interface ethernet 1/1 description dHCI-Server-1-ILO',
    'interface ethernet 1/2 description dHCI-Nimble-CB-VM-MGMT',
    'interface ethernet 1/3 description dHCI-Nimble-CA-ISCSI-A',
    'interface ethernet 1/4 description dHCI—UPD-OOBM-MGMT',
    'interface ethernet 1/5 description dHCI-Nimble-CA-VM-MGMT',
    'interface ethernet 1/6 description dHCI-Nimble-CB-ISCSI-A',
    'interface ethernet 1/7 description shutdown',
    'interface ethernet 1/8 description dHCI-Server-2-VM-MGMT',
    'interface ethernet 1/9 description dHCI-Server-1-ISCSI-A',
    'interface ethernet 1/10 description shutdown',
    'interface ethernet 1/11 description shutdown',
    'interface ethernet 1/12 description dHCI-Server-2-ISCSI-A',
    'interface ethernet 1/13 description shutdown',
    'interface ethernet 1/14 description dHCI-Server-1-VM-MGMT',
    'interface ethernet 1/15 description shutdown',
    'interface ethernet 1/16 description UPLINK mlag-port-channel 100',
    'interface ethernet 1/17 description shutdown',
    'interface ethernet 1/18 description shutdown',
    'interface ethernet 1/19 description shutdown',
    'interface ethernet 1/20 description shutdown',
    'interface ethernet 1/21 description NUMBER 1 LINK TO SWITCH 2',
    'interface ethernet 1/22 description NUMBER 2 LINK TO SWITCH 2',
    'interface ethernet 1/1 switchport access vlan ' + str(entryone['ilo_vlan_number']),
    'interface ethernet 1/2 switchport access vlan ' + str(entryone['management_vlan_number']),
    'interface ethernet 1/3 switchport access vlan ' + str(entryone['iscsi_a_vlan_number']),
    'interface ethernet 1/4 switchport access vlan ' + str(entryone['ilo_vlan_number']),
    'interface ethernet 1/5 switchport access vlan ' + str(entryone['management_vlan_number']),
    'interface ethernet 1/6 switchport access vlan ' + str(entryone['iscsi_a_vlan_number']),
    'interface ethernet 1/7 shutdown',
    'interface ethernet 1/8 switchport access vlan ' + str(entryone['management_vlan_number']),
    'interface ethernet 1/9 switchport access vlan ' + str(entryone['iscsi_a_vlan_number']),
    'interface ethernet 1/10 shutdown',
    'interface ethernet 1/11 switchport access vlan ' + str(entryone['management_vlan_number']),
    'interface ethernet 1/12 switchport access vlan ' + str(entryone['iscsi_a_vlan_number']),
    'interface ethernet 1/13 shutdown',
    'interface ethernet 1/14 switchport access vlan ' + str(entryone['management_vlan_number']),
    'interface ethernet 1/15 switchport access vlan ' + str(entryone['iscsi_a_vlan_number']),
    'interface ethernet 1/17 shutdown',
    'interface ethernet 1/18 shutdown',
    'spanning-tree mode rpvst',
    'spanning-tree port type edge default',
    'interface ethernet 1/1-1/18 spanning-tree port type edge',
    'interface mlag-port-channel 100 spanning-tree port type normal',
    'interface mlag-port-channel 200 spanning-tree port type normal',
    'spanning-tree vlan ' + str(entryone['ilo_vlan_number']) + ' priority 4096',
    'spanning-tree vlan ' + str(entryone['management_vlan_number']) +  ' priority 4096',
    'no interface mgmt0 dhcp',
    'interface mgmt0 ip address ' + str(entryone['mgmt0_switch_1_ip']) + '/'+ str(entryone['mgmt0_switch_1_mask']),
    'interface vlan ' + str(entryone['ilo_vlan_number']) + ' ip address ' + str(entryone['ilo_vlan_ip_1']) + '/' + str(entryone['ilo_vlan_mask_1']) + ' primary',
    'interface vlan ' + str(entryone['management_vlan_number']) + ' ip address ' + str(entryone['management_vlan_ip_1']) + '/' + str(entryone['management_vlan_mask_1']) + ' primary',
    'vrf definition mgmt',
    'ip routing vrf default',
    'interface ethernet 1/1-1/15 lldp tlv-select sys-description',
    'interface ethernet 1/20-1/22 lldp tlv-select sys-description',
    'dcb application-priority tcp iscsi 4',
    'dcb priority-flow-control priority 4 enable',
    'ip igmp snooping',
    'logging monitor events notice',
    'username admin password 0 admin',
    'username monitor password 0 monitor',
    'hostname dHCI-Switch-One',
    'ip route vrf mgmt 0.0.0.0/0 ' + str(entryone['gateway']),
    'snmp-server vrf default enable force',
    'cli default prefix-modes enable'
    ]

    commands_two = [
    'potocol mlag',
    'lldp',
    'lacp',
    'vlan ' + str(entrytwo['ilo_vlan_number']),
    'vlan ' + str(entrytwo['management_vlan_number']),
    'vlan ' + str(entrytwo['iscsi_a_vlan_number']),
    'vlan ' + str(entrytwo['iscsi_b_vlan_number']),
    'vlan 4094',
    'dcb priority-flow-control enable force',
    'interface port-channel 200',
    'interface ethernet 1/21-1/22 channel-group 200 mode active',
    'interface vlan 4094 mtu 9216',
    'interface vlan 4094 ip address 10.100.100.2/30 primary',
    'interface port-channel 200 ipl 1',
    'interface vlan 4094 ipl 1 peer-address 10.100.100.1',
    'interface port-channel 200 dcb priority-flow-control mode on force',
    'mlag system-mac 00:00:5E:00:01:5D',
    'mlag-vip MLAG-DHCI ip ' + str(entrytwo['mlag_vip_ip']) + '/' + str(entrytwo['mlag_vip_mask']) + ' force',
    'no mlag shutdown',
    'interface mlag-port-channel 100',
    'interface ethernet 1/16 mlag-channel-group 100 mode active',
    'interface mlag-port-channel 100 mtu 9216 force',
    'interface mlag-port-channel 100 switchport mode trunk',
    'interface mlag-port-channel 100 switchport trunk allowed-vlan none',
    'interface mlag-port-channel 100 switchport trunk allowed-vlan add ' + str(entrytwo['ilo_vlan_number']),
    'interface mlag-port-channel 100 switchport trunk allowed-vlan add ' + str(entrytwo['management_vlan_number']),
    'interface mlag-port-channel 100 no shutdown',
    'interface ethernet 1/1-1/15 speed auto force',
    'interface ethernet 1/1 description "dHCI-Server-2-ILO"',
    'interface ethernet 1/2 description "dHCI-Nimble-CA-VM-MGMT"',
    'interface ethernet 1/3 description "dHCI-Nimble-CA-ISCSI-B"',
    'interface ethernet 1/4 description "shutdown"',
    'interface ethernet 1/5 description "dHCI-Nimble-CB-VM-MGMT"',
    'interface ethernet 1/6 description "dHCI-Nimble-CB-ISCSI-B"',
    'interface ethernet 1/7 description "shutdown"',
    'interface ethernet 1/8 description "dHCI-Server-2-VM-MGMT"',
    'interface ethernet 1/9 description "dHCI-Server-2-ISCSI-B"',
    'interface ethernet 1/10 description "shutdown"',
    'interface ethernet 1/11 description "shutdown"',
    'interface ethernet 1/12 description "dHCI-Server-2-ISCSI-B"',
    'interface ethernet 1/13 description "shutdown"',
    'interface ethernet 1/14 description "dHCI-Server-w-VM-MGMT"',
    'interface ethernet 1/15 description "shutdown"',
    'interface ethernet 1/16 description "MLAG port channel 100"',
    'interface ethernet 1/17 description "shutdown"',
    'interface ethernet 1/18 description "shutdown"',
    'interface ethernet 1/19 description "shutdown"',
    'interface ethernet 1/20 description "shutdown"',
    'interface ethernet 1/21 description "NUMBER 1 LINK TO SWITCH 1"',
    'interface ethernet 1/22 description "NUMBER 2 LINK TO SWITCH 1"',
    'interface ethernet 1/1 switchport access vlan ' + str(entrytwo['ilo_vlan_number']),
    'interface ethernet 1/2 switchport access vlan ' + str(entrytwo['management_vlan_number']),
    'interface ethernet 1/3 switchport access vlan ' + str(entrytwo['iscsi_a_vlan_number']),
    'interface ethernet 1/4 switchport access vlan ' + str(entrytwo['ilo_vlan_number']),
    'interface ethernet 1/5 switchport access vlan ' + str(entrytwo['management_vlan_number']),
    'interface ethernet 1/6 switchport access vlan ' + str(entrytwo['iscsi_a_vlan_number']),
    'interface ethernet 1/7 shutdown',
    'interface ethernet 1/8 switchport access vlan ' + str(entrytwo['management_vlan_number']),
    'interface ethernet 1/9 switchport access vlan ' + str(entrytwo['iscsi_a_vlan_number']),
    'interface ethernet 1/10 shutdown',
    'interface ethernet 1/11 switchport access vlan ' + str(entrytwo['management_vlan_number']),
    'interface ethernet 1/12 switchport access vlan ' + str(entrytwo['iscsi_a_vlan_number']),
    'interface ethernet 1/13 shutdown',
    'interface ethernet 1/14 switchport access vlan ' + str(entrytwo['management_vlan_number']),
    'interface ethernet 1/15 switchport access vlan ' + str(entrytwo['iscsi_a_vlan_number']),
    'interface ethernet 1/17 shutdown',
    'interface ethernet 1/18 shutdown',
    'spanning-tree mode rpvst',
    'spanning-tree port type edge default',
    'interface ethernet 1/1-1/18 spanning-tree port type edge',
    'interface mlag-port-channel 100 spanning-tree port type normal',
    'interface mlag-port-channel 200 spanning-tree port type normal',
    'spanning-tree vlan ' + str(entrytwo['ilo_vlan_number']) + ' priority 4096',
    'spanning-tree vlan ' + str(entrytwo['management_vlan_number']) +  ' priority 4096',
    'no interface mgmt0 dhcp',
    'interface mgmt0 ip address ' + str(entrytwo['mgmt0_switch_2_ip']) + '/'+ str(entrytwo['mgmt0_switch_2_mask']),
    'interface vlan ' + str(entrytwo['ilo_vlan_number']) + ' ip address ' + str(entrytwo['ilo_vlan_ip_2']) + '/' + str(entrytwo['ilo_vlan_mask_2']) + ' primary',
    'interface vlan ' + str(entrytwo['management_vlan_number']) + ' ip address ' + str(entrytwo['management_vlan_ip_2']) + '/' + str(entrytwo['management_vlan_mask_2']) + ' primary',
    'vrf definition mgmt',
    'ip routing vrf default',
    'interface ethernet 1/1-1/15 lldp tlv-select sys-description',
    'interface ethernet 1/20-1/22 lldp tlv-select sys-description',
    'dcb application-priority tcp iscsi 4',
    'dcb priority-flow-control priority 4 enable',
    'ip igmp snooping',
    'logging monitor events notice',
    'username admin password 0 admin',
    'username monitor password 0 monitor',
    'hostname dHCI-Switch-Two',
    'ip route vrf mgmt 0.0.0.0/0 ' + str(entrytwo['gateway']),
    'snmp-server vrf default enable force',
    'cli default prefix-modes enable'
    ]

    return commands_one, commands_two
