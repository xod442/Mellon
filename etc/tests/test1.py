
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
import csv
import xlrd

f = open('/Users/rick/opt/dev-mell/mellanox_config_super.csv','r')
lines = f.readlines()
print('----------------------------------------------------------------')
for line in lines:
    line.rstrip('\n')
    row = line.split(',')
    if row[0] == 'one':

        entryone = {
            "ntp_address": row[1],
            "config_name": row[2],
            "gateway": row[3],
            "ilo_vlan_number": row[4],
            "ilo_vlan_ip_1": row[5],
            "ilo_vlan_mask_1": row[6],
            "management_vlan_number": row[7],
            "management_vlan_ip_1": row[8],
            "management_vlan_mask_1": row[9],
            "vm_prod_vlan_number": row[10],
            "vm_prod_vlan_ip_1": row[11],
            "vm_prod_vlan_mask_1": row[12],
            "mlag_vip_ip": row[13],
            "mlag_vip_mask": row[14],
            "mgmt0_switch_1_ip": row[15],
            "mgmt0_switch_1_mask": row[16],

            "iscsi_a_vlan_number": 4001,
            "iscsi_b_vlan_number": 4002
        }
        config_name = row[2]

        config_one = config_name + '_switch_one.conf'

        env = Environment(loader=FileSystemLoader('templates'))
        template_1 = env.get_template('gold_one.conf')

        output_from_parsed_template = template_1.render(entryone=entryone)
        # to save the results
        with open(config_one, "w") as fh:
            fh.write(output_from_parsed_template)
        fh.close()

    if row[0] == 'two':
        entrytwo = {
            "ntp_address": row[1],
            "config_name": row[2],
            "gateway": row[3],
            "ilo_vlan_number": row[4],
            "ilo_vlan_ip_2": row[5],
            "ilo_vlan_mask_2": row[6],
            "management_vlan_number": row[7],
            "management_vlan_ip_2": row[8],
            "management_vlan_mask_2": row[9],
            "vm_prod_vlan_number": row[10],
            "vm_prod_vlan_ip_2": row[11],
            "vm_prod_vlan_mask_2": row[12],
            "mlag_vip_ip": row[13],
            "mlag_vip_mask": row[14],
            "mgmt0_switch_2_ip": row[15],
            "mgmt0_switch_2_mask": row[16],

            "iscsi_a_vlan_number": 4001,
            "iscsi_b_vlan_number": 4002
        }
        config_name = row[2]
        config_two = config_name + '_switch_two.conf'

        env = Environment(loader=FileSystemLoader('templates'))
        template_2 = env.get_template('gold_two.conf')

        output_from_parsed_template = template_2.render(entrytwo=entrytwo)
        # to save the results
        with open(config_two, "w") as fh:
            fh.write(output_from_parsed_template)
        fh.close()
