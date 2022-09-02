
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

def get_ezandaas(db):

    ezandaas_customers=[]
    totals = []

    entry = db.ezandaas.find({})
    line = loads(dumps(entry))
    for item in line:

        short_name = item['short_name']

        if short_name == "HONEYWELL":
            if short_name in ezandaas_customers:
                EZ_HW_TOT = EZ_HW_TOT + item['credit']
                EZ_HW_TOT = round(EZ_HW_TOT,2)
            else:
                EZ_HW_TOT = item['credit']
                ezandaas_customers.append(short_name)
        if short_name == "AMERICAN":
            if short_name in ezandaas_customers:
                EZ_AM_TOT = EZ_AM_TOT + item['credit']
                EZ_AM_TOT = round(EZ_AM_TOT,2)
            else:
                EZ_AM_TOT = item['credit']
                ezandaas_customers.append(short_name)
        if short_name == "USF":
            if short_name in ezandaas_customers:
                EZ_USF_TOT = EZ_USF_TOT + item['credit']
                EZ_USF_TOT = round(EZ_USF_TOT,2)
            else:
                EZ_USF_TOT = item['credit']
                ezandaas_customers.append(short_name)
        if short_name == "FREEPORT-MCMORAN":
            if short_name in ezandaas_customers:
                EZ_MAC_TOT = EZ_MAC_TOT + item['credit']
                EZ_MAC_TOT = round(EZ_MAC_TOT,2)
            else:
                EZ_MAC_TOT = item['credit']
                ezandaas_customers.append(short_name)
        if short_name == "REPUBLIC":
            if short_name in ezandaas_customers:
                EZ_REP_TOT = EZ_REP_TOT + item['credit']
                EZ_REP_TOT = round(EZ_REP_TOT,2)
            else:
                EZ_REP_TOT = item['credit']
                ezandaas_customers.append(short_name)
        if short_name == "SCOTTSDALE":
            if short_name in ezandaas_customers:
                EZ_SC_TOT = EZ_SC_TOT + item['credit']
                EZ_SC_TOT = round(EZ_SC_TOT,2)
            else:
                EZ_SC_TOT = item['credit']
                ezandaas_customers.append(short_name)
        if short_name == "CHARLES":
            if short_name in ezandaas_customers:
                EZ_CH_TOT = EZ_CH_TOT + item['credit']
                EZ_CH_TOT = round(EZ_CH_TOT,2)
            else:
                EZ_CH_TOT = item['credit']
                ezandaas_customers.append(short_name)
    ezandaas = {}
    if 'AMERICAN' in ezandaas_customers:
        ezandaas['EZ_AM_TOT'] = EZ_AM_TOT
    else:
        ezandaas['EZ_AM_TOT'] = float(0)
    if 'HONEYWELL' in ezandaas_customers:
        ezandaas['EZ_HW_TOT'] = EZ_HW_TOT
    else:
        ezandaas['EZ_HW_TOT'] = float(0)
    if 'SCOTTSDALE' in ezandaas_customers:
        ezandaas['EZ_SC_TOT'] = EZ_SC_TOT
    else:
        ezandaas['EZ_SC_TOT'] = float(0)
    if 'FREEPORT-MCMORAN' in ezandaas_customers:
        ezandaas['EZ_MAC_TOT'] = EZ_MAC_TOT
    else:
        ezandaas['EZ_MAC_TOT'] = float(0)
    if 'REPUBLIC' in ezandaas_customers:
        ezandaas['EZ_REP_TOT'] = EZ_REP_TOT
    else:
        ezandaas['EZ_REP_TOT'] = float(0)
    if 'USF' in ezandaas_customers:
        ezandaas['EZ_USF_TOT'] = EZ_USF_TOT
    else:
        ezandaas['EZ_USF_TOT'] = float(0)
    if 'CHARLES' in ezandaas_customers:
        ezandaas['EZ_CH_TOT'] = EZ_CH_TOT
    else:
        ezandaas['EZ_CH_TOT'] = float(0)
    return ezandaas
