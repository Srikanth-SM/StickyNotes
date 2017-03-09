from flask import
import sqlite3
conn = sqlite3.connect('/Users/srikanth.s/StickyNote.db')
print conn
c = conn.cursor()
print c.rowcount
# c.execute("insert in")
rows=(1,"ds","sd",3)
# Create table
# c.execute('''CREATE TABLE NOTES
#              (title text, description text, priority real)''')
# Insert a row of data
c.execute('INSERT INTO NOTES VALUES (?,?,?,?)',rows)
c.execute('SELECT * FROM NOTES')
print c
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
