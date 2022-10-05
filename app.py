
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
import os
from bson.json_util import dumps
from bson.json_util import loads
import uuid
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
from werkzeug.utils import secure_filename
from utility.loader import dbloader
from utility.bulkloader import bulkloader

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
        "vm_prod_vlan_number": request.form['vm_prod_vlan_number'],
        "vm_prod_vlan_ip_1": request.form['vm_prod_vlan_ip_1'],
        "vm_prod_vlan_mask_1": request.form['vm_prod_vlan_mask_1'],
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
        "vm_prod_vlan_number": request.form['vm_prod_vlan_number'],
        "vm_prod_vlan_ip_2": request.form['vm_prod_vlan_ip_2'],
        "vm_prod_vlan_mask_2": request.form['vm_prod_vlan_mask_2'],
        "mlag_vip_ip": request.form['mlag_vip_ip'],
        "mlag_vip_mask": request.form['mlag_vip_mask'],
        "mgmt0_switch_2_ip": request.form['mgmt0_switch_2_ip'],
        "mgmt0_switch_2_mask": request.form['mgmt0_switch_2_mask'],
        "gateway": request.form['gateway'],
        "iscsi_a_vlan_number": 4001,
        "iscsi_b_vlan_number": 4002
    }

    config_name = request.form['config_name']
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



    message = 'Configuration files have been generated'
    # Return message
    return render_template('message.html', message=message)
