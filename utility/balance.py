
'''
 ________  ________  ___       _______   ________  ________  ___  ___  _________
|\   ____\|\   __  \|\  \     |\  ___ \ |\   ____\|\   __  \|\  \|\  \|\___   ___\
\ \  \___|\ \  \|\  \ \  \    \ \   __/|\ \  \___|\ \  \|\  \ \  \\\  \|___ \  \_|
 \ \_____  \ \   __  \ \  \    \ \  \_|/_\ \_____  \ \  \\\  \ \  \\\  \   \ \  \
  \|____|\  \ \  \ \  \ \  \____\ \  \_|\ \|____|\  \ \  \\\  \ \  \\\  \   \ \  \
    ____\_\  \ \__\ \__\ \_______\ \_______\____\_\  \ \_______\ \_______\   \ \__\
   |\_________\|__|\|__|\|_______|\|_______|\_________\|_______|\|_______|    \|__|
   \|_________|                            \|_________|

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
from bson.json_util import dumps
from bson.json_util import loads

def get_balance(db):

    balance_customers=[]
    totals = []

    entry = db.balance.find({})
    line = loads(dumps(entry))
    for item in line:

        short_name = item['short_name']

        if short_name == "HONEYWELL":
            if short_name in balance_customers:
                BAL_HW_TOT = BAL_HW_TOT + item['credit']
                BAL_HW_TOT = round(BAL_HW_TOT,2)
            else:
                BAL_HW_TOT = item['credit']
                balance_customers.append(short_name)
        if short_name == "AMERICAN":
            if short_name in balance_customers:
                BAL_AM_TOT = BAL_AM_TOT + item['credit']
                BAL_AM_TOT = round(BAL_AM_TOT,2)
            else:
                BAL_AM_TOT = item['credit']
                balance_customers.append(short_name)
        if short_name == "USF":
            if short_name in balance_customers:
                BAL_USF_TOT = BAL_USF_TOT + item['credit']
                BAL_USF_TOT = round(BAL_USF_TOT,2)
            else:
                BAL_USF_TOT = item['credit']
                balance_customers.append(short_name)
        if short_name == "FREEPORT-MCMORAN":
            if short_name in balance_customers:
                BAL_MAC_TOT = BAL_MAC_TOT + item['credit']
                BAL_MAC_TOT = round(BAL_MAC_TOT,2)
            else:
                BAL_MAC_TOT = item['credit']
                balance_customers.append(short_name)
        if short_name == "REPUBLIC":
            if short_name in balance_customers:
                BAL_REP_TOT = BAL_REP_TOT + item['credit']
                BAL_REP_TOT = round(BAL_REP_TOT,2)
            else:
                BAL_REP_TOT = item['credit']
                balance_customers.append(short_name)
        if short_name == "SCOTTSDALE":
            if short_name in balance_customers:
                BAL_SC_TOT = BAL_SC_TOT + item['credit']
                BAL_SC_TOT = round(BAL_SC_TOT,2)
            else:
                BAL_SC_TOT = item['credit']
                balance_customers.append(short_name)
        if short_name == "CHARLES":
            if short_name in balance_customers:
                BAL_CH_TOT = BAL_CH_TOT + item['credit']
                BAL_CH_TOT = round(BAL_CH_TOT,2)
            else:
                BAL_CH_TOT = item['credit']
                balance_customers.append(short_name)
    balance = {}
    if 'AMERICAN' in balance_customers:
        balance['BAL_AM_TOT'] = BAL_AM_TOT
    else:
        balance['BAL_AM_TOT'] = float(0)
    if 'HONEYWELL' in balance_customers:
        balance['BAL_HW_TOT'] = BAL_HW_TOT
    else:
        balance['BAL_HW_TOT'] = float(0)
    if 'SCOTTSDALE' in balance_customers:
        balance['BAL_SC_TOT'] = BAL_SC_TOT
    else:
        balance['BAL_SC_TOT'] = float(0)
    if 'FREEPORT-MCMORAN' in balance_customers:
        balance['BAL_MAC_TOT'] = BAL_MAC_TOT
    else:
        balance['BAL_MAC_TOT'] = float(0)
    if 'REPUBLIC' in balance_customers:
        balance['BAL_REP_TOT'] = BAL_REP_TOT
    else:
        balance['BAL_REP_TOT'] = float(0)
    if 'USF' in balance_customers:
        balance['BAL_USF_TOT'] = BAL_USF_TOT
    else:
        balance['BAL_USF_TOT'] = float(0)
    if 'CHARLES' in balance_customers:
        balance['BAL_CH_TOT'] = BAL_CH_TOT
    else:
        balance['BAL_CH_TOT'] = float(0)
    return balance
