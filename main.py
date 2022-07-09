import os
import argparse
import sqlite3


#pihole_location = r'/etc/pihole'
regexListnew = open("regex.list").read().splitlines()

blacklistnew = open("blacklist.list").read().splitlines()

pihole_location =r'g:\\'
gravity_db_location = os.path.join(pihole_location, 'gravity.db')
print('[i] Connecting to Gravity.')
sqliteConnection = sqlite3.connect(gravity_db_location)
cursor = sqliteConnection.cursor()
print('[i] Successfully Connected to Gravity.')
RegexList_before = cursor.execute(" SELECT domain FROM domainlist WHERE type = 3")

gravScriptBeforeTUP = RegexList_before.fetchall()
rows = [r[0] for r in gravScriptBeforeTUP]

unique= list(set(regexListnew + rows))


cursor.execute("delete from domainlist WHERE type = 3")
sqliteConnection.commit()  
sqliteConnection
for i in unique:
    print (i)
    cursor.execute('''INSERT INTO domainlist (type,domain,enabled, comment)
                       VALUES (?,?,?,?);'''
                    ,(3,i,1,"auto-add-python"))

sqliteConnection.commit()  


backlist_before = cursor.execute(" SELECT address FROM adlist")

rows = [r[0] for r in backlist_before]
unique= list(set(blacklistnew + rows))

cursor.execute("delete from adlist")

sqliteConnection.commit()  
for i in unique:
    print (i)
    cursor.execute('''INSERT INTO adlist (address,enabled, comment)
                       VALUES (?,?,?);'''
                    ,(i,1,"auto-add-python"))

sqliteConnection.commit()  