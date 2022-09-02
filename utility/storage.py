
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

def get_storage(db):

    storage_customers=[]
    totals = []

    entry = db.storage.find({})
    line = loads(dumps(entry))
    for item in line:

        short_name = item['short_name']

        if short_name == "HONEYWELL":
            if short_name in storage_customers:
                STOR_HW_TOT = STOR_HW_TOT + item['credit']
                STOR_HW_TOT = round(STOR_HW_TOT,2)
            else:
                STOR_HW_TOT = item['credit']
                storage_customers.append(short_name)
        if short_name == "AMERICAN":
            if short_name in storage_customers:
                STOR_AM_TOT = STOR_AM_TOT + item['credit']
                STOR_AM_TOT = round(STOR_AM_TOT,2)
            else:
                STOR_AM_TOT = item['credit']
                storage_customers.append(short_name)
        if short_name == "USF":
            if short_name in storage_customers:
                STOR_USF_TOT = STOR_USF_TOT + item['credit']
                STOR_USF_TOT = round(STOR_USF_TOT,2)
            else:
                STOR_USF_TOT = item['credit']
                storage_customers.append(short_name)
        if short_name == "FREEPORT-MCMORAN":
            if short_name in storage_customers:
                STOR_MAC_TOT = STOR_MAC_TOT + item['credit']
                STOR_MAC_TOT = round(STOR_MAC_TOT,2)
            else:
                STOR_MAC_TOT = item['credit']
                storage_customers.append(short_name)
        if short_name == "REPUBLIC":
            if short_name in storage_customers:
                STOR_REP_TOT = STOR_REP_TOT + item['credit']
                STOR_REP_TOT = round(STOR_REP_TOT,2)
            else:
                STOR_REP_TOT = item['credit']
                storage_customers.append(short_name)
        if short_name == "SCOTTSDALE":
            if short_name in storage_customers:
                STOR_SC_TOT = STOR_SC_TOT + item['credit']
                STOR_SC_TOT = round(STOR_SC_TOT,2)
            else:
                STOR_SC_TOT = item['credit']
                storage_customers.append(short_name)
        if short_name == "CHARLES":
            if short_name in storage_customers:
                STOR_CH_TOT = STOR_CH_TOT + item['credit']
                STOR_CH_TOT = round(STOR_CH_TOT,2)
            else:
                STOR_CH_TOT = item['credit']
                storage_customers.append(short_name)
    storage = {}
    if 'AMERICAN' in storage_customers:
        storage['STOR_AM_TOT'] = STOR_AM_TOT
    else:
        storage['STOR_AM_TOT'] = float(0)
    if 'HONEYWELL' in storage_customers:
        storage['STOR_HW_TOT'] = STOR_HW_TOT
    else:
        storage['STOR_HW_TOT'] = float(0)
    if 'SCOTTSDALE' in storage_customers:
        storage['STOR_SC_TOT'] = STOR_SC_TOT
    else:
        storage['STOR_SC_TOT'] = float(0)
    if 'FREEPORT-MCMORAN' in storage_customers:
        storage['STOR_MAC_TOT'] = STOR_MAC_TOT
    else:
        storage['STOR_MAC_TOT'] = float(0)
    if 'REPUBLIC' in storage_customers:
        storage['STOR_REP_TOT'] = STOR_REP_TOT
    else:
        storage['STOR_REP_TOT'] = float(0)
    if 'USF' in storage_customers:
        storage['STOR_USF_TOT'] = STOR_USF_TOT
    else:
        storage['STOR_USF_TOT'] = float(0)
    if 'CHARLES' in storage_customers:
        storage['STOR_CH_TOT'] = STOR_CH_TOT
    else:
        storage['STOR_CH_TOT'] = float(0)
    return storage
