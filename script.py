#!/usr/bin/env python3
import sqlite3
import re
import os

# stop chrome
try:
    os.system("taskkill /im chrome.exe /f")
except:
    print("Chrome is already closed.")


# windows user
user = input("What is your windows user? ")

# function
def deleteHistory():
    count = 0
    result = True
    id = 0
    while result:
        result = False
        ids = []
        for row in c.execute("""SELECT id, url FROM urls WHERE url LIKE '%{}%'""".format(prompt)):
            print (row)
            id = row[0]
            ids.append((id,))
            count += 1
        c.executemany('DELETE FROM urls WHERE id=?', ids)
        conn.commit()

    conn.close()
    return count

# connect to the database
conn = sqlite3.connect('c:/Users/{}/AppData/Local/Google/Chrome/User Data/Default/History'.format(user))
c = conn.cursor()

# history count
print("history length", c.execute('SELECT count(1) FROM urls').fetchone()[0])

# user input
prompt = input("What do you want to remove? ")
confirmation = input("Are you sure you want to remove {} (y/n)".format(prompt))


if (confirmation == "y"):
    elements = deleteHistory()
    print("{} elements have been removed".format(elements))
else:
    print("No records have been removed.")
