
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
from utility.balance import get_balance
from utility.ezandaas import get_ezandaas
from utility.storage import get_storage

def get_buckets(db):
    data = []
    comp=['AMERICAN','HONEYWELL','SCHWAB','FREEPORT','REPUBLIC','USF','HONOR']
    balance = get_balance(db)
    ezandaas = get_ezandaas(db)
    storage = get_storage(db)

    for item in comp:
        if item == 'AMERICAN':
            atotal = [ezandaas['EZ_AM_TOT'],storage['STOR_AM_TOT'],balance['BAL_AM_TOT']]
            atotal = sum(atotal)
            atotal = round(atotal,2)
            line = ['AMEX',ezandaas['EZ_AM_TOT'],storage['STOR_AM_TOT'],balance['BAL_AM_TOT'],atotal]
        if item == 'HONEYWELL':
            htotal = [ezandaas['EZ_HW_TOT'],storage['STOR_HW_TOT'],balance['BAL_HW_TOT']]
            htotal = sum(htotal)
            htotal = round(htotal,2)
            line = ['HONEYWELL',ezandaas['EZ_HW_TOT'],storage['STOR_HW_TOT'],balance['BAL_HW_TOT'],htotal]
        if item == 'SCHWAB':
            stotal = [ezandaas['EZ_CH_TOT'],storage['STOR_CH_TOT'],balance['BAL_CH_TOT']]
            stotal = sum(stotal)
            stotal = round(stotal,2)
            line = ['SCHWAB',ezandaas['EZ_CH_TOT'],storage['STOR_CH_TOT'],balance['BAL_CH_TOT'],stotal]
        if item == 'FREEPORT':
            ftotal = [ezandaas['EZ_MAC_TOT'],storage['STOR_MAC_TOT'],balance['BAL_MAC_TOT']]
            ftotal = sum(ftotal)
            ftotal = round(ftotal,2)
            line = ['FREEPORT',ezandaas['EZ_MAC_TOT'],storage['STOR_MAC_TOT'],balance['BAL_MAC_TOT'],ftotal]
        if item == 'REPUBLIC':
            rtotal = [ezandaas['EZ_REP_TOT'],storage['STOR_REP_TOT'],balance['BAL_REP_TOT']]
            rtotal = sum(rtotal)
            rtotal = round(rtotal,2)
            line = ['REPUBLIC',ezandaas['EZ_REP_TOT'],storage['STOR_REP_TOT'],balance['BAL_REP_TOT'],rtotal]
        if item == 'USF':
            utotal = [ezandaas['EZ_USF_TOT'],storage['STOR_USF_TOT'],balance['BAL_USF_TOT']]
            utotal = sum(utotal)
            utotal = round(utotal,2)
            line = ['USF',ezandaas['EZ_USF_TOT'],storage['STOR_USF_TOT'],balance['BAL_USF_TOT'],utotal]
        if item == 'HONOR':
            ototal = [ezandaas['EZ_SC_TOT'],storage['STOR_SC_TOT'],balance['BAL_SC_TOT']]
            ototal = sum(ototal)
            ototal = round(ototal,2)
            line = ['HONOR',ezandaas['EZ_SC_TOT'],storage['STOR_SC_TOT'],balance['BAL_SC_TOT'],ototal]

        data.append(line)
    ez_total = [ezandaas['EZ_SC_TOT'],ezandaas['EZ_HW_TOT'],ezandaas['EZ_AM_TOT'],ezandaas['EZ_REP_TOT'],
                 ezandaas['EZ_USF_TOT'],ezandaas['EZ_MAC_TOT'],ezandaas['EZ_CH_TOT']]
    st_total = [storage['STOR_SC_TOT'],storage['STOR_HW_TOT'],storage['STOR_AM_TOT'],storage['STOR_REP_TOT'],
                 storage['STOR_USF_TOT'],storage['STOR_MAC_TOT'],storage['STOR_CH_TOT']]
    bl_total = [balance['BAL_SC_TOT'],balance['BAL_HW_TOT'],balance['BAL_AM_TOT'],balance['BAL_REP_TOT'],
                 balance['BAL_USF_TOT'],balance['BAL_MAC_TOT'],balance['BAL_CH_TOT']]
    ez_total = sum(ez_total)
    ez_total = round(ez_total,2)
    st_total = sum(st_total)
    st_total = round(st_total,2)
    bl_total = sum(bl_total)
    bl_total = round(bl_total,2)
    grand = [atotal,htotal,stotal,ftotal,rtotal,utotal,ototal]
    grand = sum(grand)
    grand = round(grand,2)



    line = ['TOTALS', ez_total,st_total,bl_total,grand]
    data.append(line)
    return data, grand, ez_total, st_total, bl_total
