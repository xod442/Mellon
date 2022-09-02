
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
import csv
# List of current customers
HONEYWELL_TOTAL = 0.0
AMERICAN_TOTAL = 0.0
FREEPORTMCMORAN_TOTAL = 0.0
CHARLES_TOTAL = 0.0
REPUBLIC_TOTAL = 0.0
SCOTTSDALE_TOTAL = 0.0
USF_TOTAL = 0.0
with open('/Users/rick/opt/dev-salesout/storage.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0][:2] == 'YR':

            if row[21] == '0.00' or row[21][:1] == '-':
                continue
            short_name = row[3].split(" ")
            short_name = short_name[0]
            # Switch for calulating totals
            if short_name == 'HONEYWELL':
                HONEYWELL_TOTAL = HONEYWELL_TOTAL + float(row[21])
            if short_name == 'AMERICAN':
                AMERICAN_TOTAL = AMERICAN_TOTAL + float(row[21])
            if short_name == 'FREEPORT-MCMORAN':
                FREEPORTMCMORAN_TOTAL = FREEPORTMCMORAN_TOTAL + float(row[21])
            if short_name == 'CHARLES':
                CHARLES_TOTAL = CHARLES_TOTAL + float(row[21])
            if short_name == 'REPUBLIC':
                REPUBLIC_TOTAL = REPUBLIC_TOTAL + float(row[21])
            if short_name == 'SCOTTSDALE':
                SCOTTSDALE_TOTAL = SCOTTSDALE_TOTAL + float(row[21])
            if short_name == 'USF':
                USF_TOTAL = USF_TOTAL + float(row[21])
            info = [row[3], short_name, row[16], row[1], row[21]]

            HONEYWELL_TOTAL = round(HONEYWELL_TOTAL,2)
            AMERICAN_TOTAL = round(AMERICAN_TOTAL,2)
            FREEPORTMCMORAN_TOTAL = round(FREEPORTMCMORAN_TOTAL,2)
            CHARLES_TOTAL = round(CHARLES_TOTAL,2)
            REPUBLIC_TOTAL = round(REPUBLIC_TOTAL,2)
            SCOTTSDALE_TOTAL = round(SCOTTSDALE_TOTAL,2)
            USF_TOTAL = round(USF_TOTAL,2)



    print(f'\tHoneywell:{HONEYWELL_TOTAL} American: {AMERICAN_TOTAL} Freeport {FREEPORTMCMORAN_TOTAL} \
            Charles {CHARLES_TOTAL}  Republic {REPUBLIC_TOTAL} Scottsdale {SCOTTSDALE_TOTAL}  \
            USF {USF_TOTAL}')


    print('EOL')
