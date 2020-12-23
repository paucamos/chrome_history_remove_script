#!/usr/bin/env python3
import sqlite3
import re
import os
import psutil

# stop chrome
def get_pid(name):
    notepads = (item.pid for item in psutil.process_iter() if item.name() == name)
    return list(notepads)

# check if any chrome process is open 
if len(get_pid("chrome.exe")) > 0:
    # close them
    os.system("taskkill /im chrome.exe 2> nul")

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
conn = sqlite3.connect('c:/Users/Pablo/AppData/Local/Google/Chrome/User Data/Default/History')
c = conn.cursor()

# history count
print("history length", c.execute('SELECT count(1) FROM urls').fetchone()[0])

# user input
prompt = input("What do you want to remove? ")
confirmation = input("Are you sure you want to remove {} (y/n)".format(prompt))


if (confirmation == "y"):
    elements = deleteHistory()
    print("{} elements have been removed".format(elements))
elif (confirmation == "n"):
    print("No records have been removed.")
else:
    print("Script closed.")
