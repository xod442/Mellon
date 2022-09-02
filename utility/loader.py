#
import json
import uuid
import datetime
import csv

def dbloader(db,filename):
    coll,junk = filename.split('.')

    # Clean the db's
    if filename == 'ezandaas.csv':
        db.ezandaas.drop()
    if filename == 'balance.csv':
        db.balance.drop()
    if filename == 'storage.csv':
        db.storage.drop()

    f = open(filename,'r')
    lines = f.readlines()

    for line in lines:
        row = line.split(',')
        # Make sure the line starts with YR
        if row[0][:2] == 'YR':
            # Find the credit and strip the carrige return
            credit= float(row[21].strip())
            # Get the shortname and generate a uuid
            short_name = row[3].split(" ")
            short_name = short_name[0]
            my_uuid = uuid.uuid4()
            my_uuid = str(my_uuid)

            # Build entry and write to the collection
            if coll == 'ezandaas':
                entry = {
                    "full_name": row[3],
                    "short_name": short_name,
                    "uuid": my_uuid,
                    "credit": credit,
                    "type": row[1],
                    "product": row[14],
                    "transaction": row[6]
                }
                res = db.ezandaas.insert_one(entry)
            if coll == 'storage':
                entry = {
                    "full_name": row[3],
                    "short_name": short_name,
                    "uuid": my_uuid,
                    "credit": credit,
                    "type": row[1],
                    "product": row[14],
                    "transaction": row[6]
                }
                res = db.storage.insert_one(entry)

            if coll == 'balance':
                entry = {
                    "full_name": row[3],
                    "short_name":short_name,
                    "uuid": my_uuid,
                    "credit": credit,
                    "type": row[1],
                    "product": row[14],
                    "transaction": row[6]
                    }
                res = db.balance.insert_one(entry)
    return
