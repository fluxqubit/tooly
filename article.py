# -*- coding: ISO-8859-1 -*-
import sys
import random                   
import sys
sys.path.append('/home/mrhsegypt/termcolor/termcolor-1.1.0')
from termcolor import colored, cprint
import sqlite3 as lite
import db
import codecs

### FEED AN ARTICLE IN FILE SAMPLE.TXT

#### ALWAYS CREATE AN OBJ THEN APPLY THE CLASS METHOD TO THE OBJECT

class Article:
        """ this handles the contents of an article, that I would like to read"""
        """
        #words=None
        sentences= None
        paragraphs= None
        words_inmyKn_known = None
        words_inmyKn_unknown = None
        words_not_inmyKn =None
        """
        def __init__(self,myarticle):
                self.myarticle = myarticle      # necessary for valid input

        def chop(self):     # myarticle= string of the filename containing the article, like "sample.txt"
                """here turn article into words."""
                myarticle=self.myarticle                

                self.paragraphs=[]
                self.sentences=[]
                self.words=[]
                
                examples = codecs.open(str(myarticle),'r',encoding='utf-8').read()      # READING IN UNICODE
                
                for i in range(len(examples.split("\n"))):              #split an article containing many paragraphs into individual ones.
                        a= examples.split("\n")[i] 
                        self.paragraphs.append(a)
                        #print a             # a is the paragraph number i during its iteration
                        for j in range(len(a.split("."))):              #split a paragraph containing many sentences into individual ones.
                                b=a.split(".")[j]
                                self.sentences.append(b)
                                #print b
                                for k in range(len(b.split())):         #split a sentence containing many words into individual ones.
                                        c=b.split()[k]
                                        #print c
                                        self.words.append(c)
                
                return         
        def get_paragraphs(self):
                for i in self.paragraphs: print i
                return # paragraphs
        def get_sentences(self):
                for i in self.sentences: print i+"."
                return # sentences
        def get_words(self):
                """ to style words output ## pushed till later
                for i in range(len(words)/5 +1):
                        #i=i/5
                        for j in range(5): print words[i*5 +j],
                        print words[i*5 ],words[i*5 +1],words[i*5 +2],words[i*5 +3],words[i*5 +4]
                        #except IndexError:
                        #        pass
                        """
                return self.words


        def sniffit(self):     # myarticle= string of the filename containing the article, like "sample.txt"
                """here a comparision against myknowledge database should be made"""
                words = self.words
                import db
                obj=db.Db()

                self.words_inmyKn_known=[]
                self.words_inmyKn_unknown=[]
                self.words_not_inmyKn=[]
                for i in words:
                        if obj.search("myknowledge2","myknowledge",i, "<> 'morsey'"):
                                #self.words_not_inmyKn.append(i)
                                if obj.search("myknowledge2","myknowledge",i, "= 'True'"):
                                        self.words_inmyKn_known.append(i)
                                else: # elif obj.search("myknowledge2","myknowledge",i, "= 'False'"):
                                        self.words_inmyKn_unknown.append(i)
                        else: #elif not obj.search("myknowledge2","myknowledge",i, "<> 'morsey'"):
                                self.words_not_inmyKn.append(i)
                # now three lists are created.
                """
                article_unknowns=[]
                for word in words:
                        word_known = obj.search("myknowledge2", "myknowledge", word, 'True')   
                        if word_known: 
                                pass
                        else:
                                article_unknowns.append(word)   # append it to list of article_unknowns.
                """                
                #????
                percent = (float(len(self.words_inmyKn_unknown)+len(self.words_not_inmyKn)))/float(len(self.words_inmyKn_known)+len(self.words_inmyKn_unknown)+len(self.words_not_inmyKn))*100.   
                #print percent, len(self.words_inmyKn_unknown), len(self.words_not_inmyKn), len(words)
                percent = round(percent,0)
                print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                print "vocabs known: "
                print self.words_inmyKn_known
                print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                print "vocabs not well studied: "
                print self.words_inmyKn_unknown
                print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                print "new vocabs: "
                print self.words_not_inmyKn
                print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                print str(percent) + " of the article is unknowns."
                print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                #decision = raw_input('Show the unknowns in context? ')
                decision = 'y'  #???? I need to activate this decision. why the previous statement does not work?
                if decision == 'y': #printt the article with colors.
                        for i in words:
                                if i in self.words_inmyKn_known:
                                        print colored(i, 'green'),                                  
                                elif i in self.words_inmyKn_unknown:
                                        print colored(i, 'yellow'),     # dots missing ==> to be fixed
                                elif i in self.words_not_inmyKn: 
                                        print colored(i, 'red'), # printt in red


                if decision == 'n' : 
                        pass
                        """ ??? need a smart solution to this trap!
                        no other answer should be accepted, but how?
                                        else :
                        decision2= raw_input("What do you mean? y or n ??")
                                if decision == 'y': printt the article with colors.
                                if decision == 'n' :                  
                        """
                return # ??? the difference between print and return
                #return 
        def feed_db(self):     # myarticle= string of the filename containing the article, like "sample.txt"
                """here new words from the article are added to myknowledge db."""
                words = self.words
                import db
                obj=db.Db()
                #words_inmyKn=[]

                #words_inmyKn_known = self.words_inmyKn_known    XXXX SWITCH BACK IF NEEDED
                #words_inmyKn_unknown = self.words_inmyKn_unknown
                #words_not_inmyKn = self.words_not_inmyKn



                for i in self.words_not_inmyKn:
                        printed= u'Do you know this word: '+ i + u' ? '
                        printed_str= printed.encode(sys.stdout.encoding)
                        decision = raw_input(printed_str).decode(sys.stdin.encoding)
                        #is i already in myknowledge?
                        
                        if decision == u'y': 
                                obj.insert('myknowledge2', (i, "True")) 
                        elif decision == u'n' : 
                                obj.insert('myknowledge2', (i, "False"))
                        else : 
                                print "what do you mean?"
                return
        
        
        


"""
???? is it possible to import another class here?


 ### #COMPARE AGAINST MYKNOWLEDGE2
"""









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

# ar = article.Article('sample.txt')

# sqlite3.OperationalError: database is locked

""" ???
Do you know this word: Während? y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "article.py", line 98, in feed_db
    obj.insert('myknowledge2', (i, "= 'True'")) 
  File "db.py", line 30, in insert
    c.execute("insert into "+ tablename +" values (?,?)", newentry)   # feed (newid, newname)
sqlite3.ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.
"""
