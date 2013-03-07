import sqlite3 as s3

#creating a DB
conn=s3.connect('pythonsqlite.db')


# creating a cursor (allows you to perform queries on a DB)
c=conn.cursor()

c.execute("create table test (id integer, name text)")

#filling table with data
c.execute("insert into test values (1, 'Mohamed')")
c.execute("insert into test values (?,?)", (4, 'May'))

newid = 5
newname='Yasser'
c.execute("insert into test values (?,?)", (newid, newname))

# selecting all data from table 
myrows = c.execute("select * from test")
for i in myrows: print i[0],i[1]

1 Mohamed
1 Yasser
1 Nagla
2 Yasser
3 Nagla
4 May

conn.commit() # to confirm that everything was included in the database

# selecting data under condition
myrows = c.execute("select * from test where name='Yasser'")
myrows = c.execute("select * from test where name=?", [newname])

# to add a new column to a table

c.execute('alter table test add column email text')

# to update values in a table
c.execute('update test set email="mrhs@hotmail.com"')

#delete rows from table
c.execute('delete from table where id=4')



c.close()

