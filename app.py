
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
from pymongo import MongoClient
import datetime
import requests
import os
import json
import uuid
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
from werkzeug.utils import secure_filename
from utility.command_list import commands

from jinja2 import Environment, FileSystemLoader
#
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_TEMPLATE = os.path.join(APP_ROOT, 'templates')

config = {
    "username": "admin",
    "password": "siesta3",
    "server": "mongo",
}

connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = MongoClient(connector)
db = client["sales"]
s = requests.Session()

auth_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

auth_params = {
    'script': 'rh',
    'template': 'json-request',
    'action': 'json-login',
}


'''
#-------------------------------------------------------------------------------
Home
#-------------------------------------------------------------------------------
'''

@app.route("/main", methods=('GET', 'POST'))
@app.route("/", methods=('GET', 'POST'))
def home():

    return render_template('mellon.html')

@app.route("/menu", methods=('GET', 'POST'))
def menu():

    return render_template('home.html')



'''
#-------------------------------------------------------------------------------
Load and Database Section
#-------------------------------------------------------------------------------
'''


@app.route("/network", methods=('GET', 'POST'))
def network():
    pass
    return render_template('network.html')

@app.route("/vlans", methods=('GET', 'POST'))
def vlans():
    pass
    return render_template('vlans.html')

@app.route("/help", methods=('GET', 'POST'))
def help():
    pass
    entry = 'HELP!'
    return render_template('help.html', entry=entry)

@app.route("/load", methods=('GET', 'POST'))
def load():
    if request.method == 'POST':
        image = request.files['file']
        filename = secure_filename(image.filename)
        arrays = dbloader(filename)
        message = 'Configuration files are generated'
        return render_template('message.html', message=message)
    # Return for HTTP GET
    return render_template('load.html')

@app.route("/loadbulk", methods=('GET', 'POST'))
def loadbulk():
    if request.method == 'POST':
        image = request.files['file']
        filename = secure_filename(image.filename)
        bulk = bulkloader(filename)
        message = 'Configuration files are generated'
        return render_template('message.html', message=message)
    # Return for HTTP GET
    return render_template('loadbulk.html')

@app.route("/generate", methods=('GET', 'POST'))
def generate():

    entryone = {
        "ntp_address": request.form['ntp_address'],
        "config_name": request.form['config_name'],
        "ilo_vlan_number": request.form['ilo_vlan_number'],
        "ilo_vlan_ip_1": request.form['ilo_vlan_ip_1'],
        "ilo_vlan_mask_1": request.form['ilo_vlan_mask_1'],
        "management_vlan_number": request.form['management_vlan_number'],
        "management_vlan_ip_1": request.form['management_vlan_ip_1'],
        "management_vlan_mask_1": request.form['management_vlan_mask_1'],
        "mlag_vip_ip": request.form['mlag_vip_ip'],
        "mlag_vip_mask": request.form['mlag_vip_mask'],
        "mgmt0_switch_1_ip": request.form['mgmt0_switch_1_ip'],
        "mgmt0_switch_1_mask": request.form['mgmt0_switch_1_mask'],
        "gateway": request.form['gateway'],
        "iscsi_a_vlan_number": 4001,
        "iscsi_b_vlan_number": 4002
    }

    entrytwo = {
        "ntp_address": request.form['ntp_address'],
        "config_name": request.form['config_name'],
        "ilo_vlan_number": request.form['ilo_vlan_number'],
        "ilo_vlan_ip_2": request.form['ilo_vlan_ip_2'],
        "ilo_vlan_mask_2": request.form['ilo_vlan_mask_2'],
        "management_vlan_number": request.form['management_vlan_number'],
        "management_vlan_ip_2": request.form['management_vlan_ip_2'],
        "management_vlan_mask_2": request.form['management_vlan_mask_2'],
        "mlag_vip_ip": request.form['mlag_vip_ip'],
        "mlag_vip_mask": request.form['mlag_vip_mask'],
        "mgmt0_switch_2_ip": request.form['mgmt0_switch_2_ip'],
        "mgmt0_switch_2_mask": request.form['mgmt0_switch_2_mask'],
        "gateway": request.form['gateway'],
        "iscsi_a_vlan_number": 4001,
        "iscsi_b_vlan_number": 4002
    }
    # Start the machine
    commands_one, commands_two = commands(entryone, entrytwo)

    # Create url for switch one
    url = 'http://'+entryone['mgmt0_switch_1_ip']+'/admin/launch'
    # create data
    data = {"username": "admin","password": "admin"}
    data= json.dumps(data)

    # Get authentication session_key
    response = s.post(url, params=auth_params, auth_headers=headers, data=data)
    client_dict = s.cookies.get_dict()
    session_key = client_dict['session']
    key = 'session=' + session_key

    # Set headers and params for authenticating with a session key
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cookie': key
    }

    params = {
        'script': 'json',
    }

    # Init log list
    log1 = []

    # to save the results
    for line in commands_one:
        data = {"execution_type":"async"}
        data = {"cmd": line}
        data= json.dumps(data)
        response = s.post(url,params=params,headers=headers,data=data)
        log1.append('--------------------------------------------------')
        log1.append(response.text)
    data = {"execution_type":"async"}
    data = {"cmd": "show run"}
    data= json.dumps(data)
    response = s.post(url,params=params,headers=headers,data=data)
    # Get running config file switch one
    one_run = response.text['data']

    # Init log list
    log2 = []

    # to save the results
    for line in commands_two:
        # Prep command to write async to the switch
        data = {"execution_type":"async"}
        data = {"cmd": line}
        data= json.dumps(data)
        # Send request
        response = s.post(url,params=params,headers=headers,data=data)
        log2.append('--------------------------------------------------')
        log2.append(response.text)
    # Prep command to write async to the switch
    data = {"execution_type":"async"}
    data = {"cmd": "show run"}
    data= json.dumps(data)
    response = s.post(url,params=params,headers=headers,data=data)
    # Get running config file switch two
    two_run = response.text['data']

    # Return message
    return render_template('results.html',commands_one=commands_one,commands_two=commands_two,log1=log1,log2=log2,one=one_run,two=two_run)
