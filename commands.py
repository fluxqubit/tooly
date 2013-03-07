
SQL is not case sensitive


To retrieve data after executing a SELECT statement, you can either treat the cursor as an iterator, call the cursor’s fetchone() method to retrieve a single matching row, or call fetchall() to get a list of the matching rows.

cur.execute('SELECT SQLITE_VERSION()')

data = cur.fetchone()

print "SQLite version: %s" % data 


>>> for i in cur.execute('select sqlite_version()'): print i
... 
(u'3.6.22',)


At a shell or DOS prompt, enter: "sqlite3 test.db"; Enter SQL commands at the prompt to create and populate the new database.

Customers Table: CompanyName 	ContactName 	Address 	City

 SELECT CompanyName, ContactName FROM customers
 
 SELECT * FROM customers WHERE companyname LIKE 'a%'
 
 The TOP clause is used to specify the number of records to return.
 
 SELECT TOP 2 * FROM Persons
 
 SELECT TOP 50 PERCENT * FROM Persons
 
 The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.
 
 SELECT * FROM Persons WHERE City LIKE 's%'   # produces cities starting with an s
 
 SELECT * FROM Persons WHERE City LIKE '%tav%' # produces cities containing 'tav'
 
 % 	A substitute for zero or more characters
_ 	A substitute for exactly one character

SELECT * FROM Persons WHERE FirstName LIKE '_la' # produces Persons with only three letters, containing 'la'

SELECT * FROM Persons WHERE LastName LIKE '[bsp]%'  # select the persons with a last name that starts with "b" or "s" or "p" from the "Persons" table. 

SELECT * FROM Persons WHERE LastName LIKE '[!bsp]%'# select the persons with a last name that does NOT start with "b" or "s" or "p" from the "Persons" table.

SELECT DISTINCT City FROM Persons # repeated results are ignored

SELECT * FROM Persons WHERE City='Sandnes'


NOTICE THE DIFFERENCE, 

SELECT * FROM Persons WHERE FirstName='Tove'             SELECT * FROM Persons WHERE Year=1965          # Numbers do not take quotes

= 	Equal
<> 	Not equal
> 	Greater than
< 	Less than
>= 	Greater than or equal
<= 	Less than or equal
BETWEEN 	Between an inclusive range
LIKE 	Search for a pattern
IN 	To specify multiple possible values for a column

SELECT * FROM Persons
WHERE FirstName='Tove'
AND LastName='Svendson'

# creating table 

CREATE TABLE orders
(id INT IDENTITY(1,1) PRIMARY KEY, \
customer VARCHAR(50), \
city VARCHAR(50), \
avail VARCHAR(50), \
quantity INT)

cur.execute('Create table orders (customer varchar, quantity int)')

## when populting a table, strings must take double quotes. 

cur.execute('insert into orders (customer, quantity) values("Alex", 17)')
for i in cur.execute('select * from orders where (customer like "a%" or customer like "M%") and (quantity between 10 and 40)' )
(u'Mohamed', 40)
(u'Ali', 15)
(u'Alex', 17)

for i in cur.execute('select * from orders where customer like "a%"'):
        print i
(u'Ali', 15)
(u'Alex', 17)

>>> for i in cur.execute('select distinct customer from orders' ):
...     print i

(u'Alex',)
(u'Ali',)
(u'John',)
(u'Mohamed',)
 this removes repeated customer names
 
 SQL SELECT DISTINCT Syntax

SELECT column_name(s)
FROM table_name
ORDER BY column_name(s) ASC|DESC

>>> for i in cur.execute('select * from orders order by quantity desc'):
...     print i
... 
(u'John', 50)
(u'Mohamed', 40)
(u'John', 25)
(u'Alex', 17)
(u'Ali', 15)

# to extend a table 

cur.execute('insert into orders values ("berni", 21)')

# feeding a value to a specific column 
cur.execute('insert into orders (customer) values ("unknown")')
for i in cur.execute('select * from orders'): print i

(u'Mohamed', 40)
(u'Ali', 15)
(u'John', 25)
(u'Alex', 17)
(u'John', 50)
(u'berni', 21)
(u'peter', 22)
(u'unknown', None)


cur.execute('delete from orders where customer = "unknown"')


>>> for i in cur.execute('select * from orders limit 2'): print i[0], i[1]
... 
Mohamed 40
Ali 15


# There is no top 3 command in sqlite , use instead LIMIT 3

# searching a database:

SELECT * FROM Persons
WHERE LastName LIKE 'S_end_on'

SELECT column_name(s)
FROM table_name
WHERE column_name
BETWEEN value1 AND value2

for i in cur.execute('select customer from orders where quantity between 20 and 30'): print i
(u'John',)
(u'berni',)
(u'peter',)
(u'\xf6li',)

# also there is : Not between

SELECT * FROM Persons
WHERE LastName
NOT BETWEEN 'Hansen' AND 'Pettersen'

you could simply add a new column with the following:

ALTER TABLE {tableName} ADD COLUMN COLNew {type};

you could rename your table:

ALTER TABLE {tableName} RENAME TO TempOldTable

### inserting a new column (COLNew) into an existing table with columns  name,qty,rate

ALTER TABLE {tableName} RENAME TO TempOldTable
CREATE TABLE {tableName} (name TEXT, COLNew {type} DEFAULT {defaultValue}, qty INTEGER, rate REAL)
INSERT INTO {tableName} (name, qty, rate) SELECT name, qty, rate FROM TempOldTable
DROP TABLE TempOldTable


HOW TO SHOW THE STRUCTURE OF ANY COLUMN IN THE DATABASE ?? (HOW MANY COLUMNS, HOW ARE THEY CALLED, ...)



