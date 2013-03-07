class Trap:
        """ this is some class"""
        def __init__(self):
                self.setup()
        def setup(self):        # to feed info used in other methods
                self.points = (-1,-0.5,0,0.5,1)
                self.weights = (1,1,1,1,1)
        def eval(self, f):
                sum = 0.
                for i in range(len(self.points)):
                        sum += self.weights[i]*f(self.points[i])
                return sum

obj1 = Trap()
obj1.eval(lambda x:x**2)







class MyBase:
        def __init__(self, i, j):       # seems like __init__ has the initial values that you would feed into the class while creating an object. __init__ == A constructor
                                        # this can come later within the class. order should not be a problem.
                self.i = i;self.j=j     # i, j are instance attributes. we can access them as obj1.i, obj.j
        def write(self):
                print 'MyBase: i=', self.i, 'j=', self.j

obj1=MyBase(2,3)
obj1.write()


In a class, every method must have self at the first argument. BUT, it should not be written explicitely when the method is called.


SUBCLASSING,

class MySub(MyBase):
        def __init__(self,i,j,k):
                MyBase.__init__(self,i,j)
                self.k=k
        def write(self):
                print 'MySub: i=', self.i, 'j=', self.j, 'k=', self.k

-----------------------------

how return could add more stuff to the output

>>> def printme(s):
...     print s
...     return x
... 
>>> y=100
>>> printme(y)
100
10



import sqlite3 as lite

class DB:
        """ this is a database"""
        def __init__(self):
                self.setup()
        
        def setup(self):        # to feed info used in other methods
                self.points = (-1,-0.5,0,0.5,1)
                self.weights = (1,1,1,1,1)
        def eval(self, f):
                sum = 0.
                for i in range(len(self.points)):
                        sum += self.weights[i]*f(self.points[i])
                return sum

obj1 = Trap()
obj1.eval(lambda x:x**2)


conn=s3.connect('pythonsqlite.db')
c=conn.cursor()

c.execute("create table test (id integer, name text)")



conn.commit()
conn.close()

------------------------------------
how to change string to unicode :
y='Ivan Krsti\x49\x6e'
type(y)
<type 'str'>

yy=y.decode('utf8')
type(yy)
<type 'unicode'>
----


s.decode(encoding)

    <type 'str'> to <type 'unicode'>

u.encode(encoding)

    <type 'unicode'> to <type 'str'>

---

one advantage of switching to unicode, is that each new letter is presented by a single letter in the presentation. So word[:-1] removes exactly single letter from the word.  ==> unique number (code point) for each character of every language

To save text to file, you have to encode it !!!

x=open('sink.txt','r')
x.readlines()[-1].decode('utf8')

Here is what should be done
text = f.read()
type(text.decode('utf-8'))

The defult encoding for Python 2 is ASCII

----------------------

a little code to convert every string to unicode 

def ConvToUnicode(obj,encoding='utf-8'):
        if isinstance(obj,basestring):
                if not isinstance(obj, unicode):
                        obj = unicode(obj, encoding)
        return obj

-------------------

XXXX   when writing to Disk, 
f.write(ivan_uni.encode('utf-8'))
f.close

XXXX Example:

>>> f=open('sink.txt','r')
>>> f.read()    This reads in ASCII encoding
'Ivan Krsti\xc4\x87\nIvan Krsti\xc4\x87\nAB\n\nwir k\xc3\xb6nnen aus \xc3\x84gypten\n\xd8\xa7\xd9\x84\xd9\x84\xd9\x87 \xd8\xa7\xd9\x83\xd8\xa8\xd8\xb1 \xd9\x81\xd9\x88\xd9\x82 \xd9\x83\xd9\x8a\xd8\xaf \xd8\xa7\xd9\x84\xd9\x85\xd8\xb9\xd8\xaa\xd8\xaf\xd9\x8a\n'
>>> f=open('sink.txt','r')
ON THE OTHERHAND:
>>> import codecs
>>> f=codecs.open('sink.txt','r',encoding='utf-8')
>>> f.read()    This reads&converts DIRECTLY to unicode
u'Ivan Krsti\u0107\nIvan Krsti\u0107\nAB\n\nwir k\xf6nnen aus \xc4gypten\n\u0627\u0644\u0644\u0647 \u0627\u0643\u0628\u0631 \u0641\u0648\u0642 \u0643\u064a\u062f \u0627\u0644\u0645\u0639\u062a\u062f\u064a\n'

AND TO WRITE UNICODED TEXT DIRECTLY TO FILE, DO :
import codecs
f=codecs.open('sink.txt','w',encoding='utf-8')
f.write(text_in_unicode)


