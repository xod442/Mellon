#
import json
import uuid
import datetime
import csv
from jinja2 import Environment, FileSystemLoader

def dbloader(filename):

    f = open(filename,'r')
    lines = f.readlines()

    for line in lines:
        row = line.split(',')
        if row[0] == '\ufeffone':
            pass
        if row[0] =='two':
            pass
        if row[0] != '\ufeffone' and row[0] != 'two':
            if row[0] == 'ntp':
                ntp_address = row[2]
            if row[0] == 'config':
                config_name = row[2]
            if row[0] ==  'gate':
                gateway = row[2]
            if row[0] ==  'ilo_vlan':
                ilo_vlan_number = row[2]
            if row[0] ==  'ilo_ip':
                ilo_vlan_ip_1 = row[2]
            if row[0] ==  'ilo_mask':
                ilo_vlan_mask_1 = row[2]
            if row[0] ==  'mgt_vlan':
                management_vlan_number = row[2]
            if row[0] ==  'mgt_ip':
                management_vlan_ip_1 = row[2]
            if row[0] ==  'mgt_mask':
                management_vlan_mask_1 = row[2]
            if row[0] ==  'vm_prod':
                vm_prod_vlan_number = row[2]
            if row[0] ==  'prod_ip':
                vm_prod_vlan_ip_1 = row[2]
            if row[0] ==  'prod_mask':
                vm_prod_vlan_mask_1 = row[2]
            if row[0] ==  'vip':
                mlag_vip_ip = row[2]
            if row[0] ==  'v_mask':
                mlag_vip_mask = row[2]
            if row[0] ==  'man_ip':
                mgmt0_switch_1_ip = row[2]
            if row[0] ==  'man_mask':
                mgmt0_switch_1_mask = row[2]

            # Now process switch two

            if row[0] == 'ntp2':
                ntp_address = row[2]
            if row[0] == 'config2':
                config_name = row[2]
            if row[0] ==  'gate2':
                gateway = row[2]
            if row[0] ==  'ilo_vlan2':
                ilo_vlan_number = row[2]
            if row[0] ==  'ilo_ip2':
                ilo_vlan_ip_2 = row[2]
            if row[0] ==  'ilo_mask2':
                ilo_vlan_mask_2 = row[2]
            if row[0] ==  'mgt_vlan2':
                management_vlan_number = row[2]
            if row[0] ==  'mgt_ip2':
                management_vlan_ip_2 = row[2]
            if row[0] ==  'mgt_mask2':
                management_vlan_mask_2 = row[2]
            if row[0] ==  'vm_prod2':
                vm_prod_vlan_number = row[2]
            if row[0] ==  'prod_ip2':
                vm_prod_vlan_ip_2 = row[2]
            if row[0] ==  'prod_mask2':
                vm_prod_vlan_mask_2 = row[2]
            if row[0] ==  'vip2':
                mlag_vip_ip = row[2]
            if row[0] ==  'v_mask2':
                mlag_vip_mask = row[2]
            if row[0] ==  'man_ip2':
                mgmt0_switch_2_ip = row[2]
            if row[0] ==  'man_mask2':
                mgmt0_switch_2_mask = row[2]

    entryone = {
        "ntp_address": ntp_address,
        "config_name": config_name,
        "ilo_vlan_number": ilo_vlan_number,
        "ilo_vlan_ip_1": ilo_vlan_ip_1,
        "ilo_vlan_mask_1": ilo_vlan_mask_1,
        "management_vlan_number": management_vlan_number,
        "management_vlan_ip_1": management_vlan_ip_1,
        "management_vlan_mask_1": management_vlan_mask_1,
        "vm_prod_vlan_number": vm_prod_vlan_number,
        "vm_prod_vlan_ip_1": vm_prod_vlan_ip_1,
        "vm_prod_vlan_mask_1": vm_prod_vlan_mask_1,
        "mlag_vip_ip": mlag_vip_ip,
        "mlag_vip_mask": mlag_vip_mask,
        "mgmt0_switch_1_ip": mgmt0_switch_1_ip,
        "mgmt0_switch_1_mask": mgmt0_switch_1_mask,
        "gateway": gateway,
        "iscsi_a_vlan_number": 4001,
        "iscsi_b_vlan_number": 4002
    }


    entrytwo = {
        "ntp_address": ntp_address,
        "config_name": config_name,
        "ilo_vlan_number": ilo_vlan_number,
        "ilo_vlan_ip_2": ilo_vlan_ip_2,
        "ilo_vlan_mask_2": ilo_vlan_mask_2,
        "management_vlan_number": management_vlan_number,
        "management_vlan_ip_2": management_vlan_ip_2,
        "management_vlan_mask_2": management_vlan_mask_2,
        "vm_prod_vlan_number": vm_prod_vlan_number,
        "vm_prod_vlan_ip_2": vm_prod_vlan_ip_2,
        "vm_prod_vlan_mask_2": vm_prod_vlan_mask_2,
        "mlag_vip_ip": mlag_vip_ip,
        "mlag_vip_mask": mlag_vip_mask,
        "mgmt0_switch_2_ip": mgmt0_switch_2_ip,
        "mgmt0_switch_2_mask": mgmt0_switch_2_mask,
        "gateway": gateway,
        "iscsi_a_vlan_number": 4001,
        "iscsi_b_vlan_number": 4002
    }

    config_one = config_name + '_switch_one.conf'
    config_two = config_name + '_switch_two.conf'

    env = Environment(loader=FileSystemLoader('templates'))
    template_1 = env.get_template('gold_one.conf')
    template_2 = env.get_template('gold_two.conf')


    output_from_parsed_template = template_1.render(entryone=entryone)
    # to save the results
    with open(config_one, "w") as fh:
        fh.write(output_from_parsed_template)
    fh.close()

    output_from_parsed_template = template_2.render(entrytwo=entrytwo)
    # to save the results
    with open(config_two, "w") as fh:
        fh.write(output_from_parsed_template)
    fh.close()

    return ()
