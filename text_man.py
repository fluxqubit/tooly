#***
### FEED AN ARTICLE IN FILE SAMPLE.TXT


sent_file = "sample.txt"
examples = open(str(sent_file)).read()

article_in_words=[]
for i in range(len(examples.split("\n"))):              #split an article containing many paragraphs into individual ones.
        a= examples.split("\n")[i] 
        #print a             # a is the paragraph number i during its iteration
        for j in range(len(a.split("."))):              #split a paragraph containing many sentences into individual ones.
                b=a.split(".")[j]
                #print b
                for k in range(len(b.split())):         #split a sentence containing many words into individual ones.
                        c=b.split()[k]
                        #print c
                        article_in_words.append(c)

 ### #COMPARE AGAINST MYKNOWLEDGE2

obj=db.Db()

words_knowns=[]
words_unknowns=[]
for i in article_in_words:
        if obj.search("table2","name",i):
                words_knowns.append(i)
        else:
                words_unknowns.append(i)

for i in words_unknowns:
        decision = raw_input('Do you know this word: '+ i + '? ')
        if decision == 'y': 
                obj.insert('myknowledge2', (i, "True"))
        if decision == 'n' : 
                obj.insert('myknowledge2', (i, "False"))
        else : 
                print "what do you mean?"








"""
        
                

print " ".join(article_in_words)                This binds the words back to the whole article. however, with not points! To be fixed!! 
## 






#for i in examples.split("/n"): print i  #splitting text into paragraphs

#for i in x.split("."): print i          #splitting paragraphs into sentences.
                                        # also produces some lines. "\n" 

ss=a.strip()                            # loop over your strings to remove any spaces or newlines.

#sentence.split()                        # splitting sentences into words.












n="table2"
titles="(id integer, name text)"        #BOOLEAN
obj1 = Db()
obj1.createtable(n, titles)
obj1.search("table2", "name", "ashraf")

entry1=(3,"Hassan")
obj2=Db()
obj2.insert(n, entry1)

obj2.insert(entry1)



c.execute("insert into test values (?,?)", (newid, newname))
c.execute("insert into test values (1, 'Mohamed')")
c.execute("create table test (id integer, name text)")
myrows = c.execute("select * from test")
DELETE FROM Persons WHERE LastName='Tjessem' AND FirstName='Jakob'      # delete from table where condition

output = c.execute("select * from "+ tablename)   # feed (newid, newname)


	
"""
"""
try:
        asdf
except NameError:
        asdf=20
else:
        print "sure, it was defined."
"""
"""
isPresent = cur.execute( "SELECT target FROM stringList WHERE target='specificString';" ).fetchall()
return isPresent == None

random.choice(xrange(100000)

if value in list : print "True"
"""
