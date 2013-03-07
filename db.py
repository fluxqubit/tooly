# -*- coding: ISO-8859-1 -*-
import sys
import random 
import sys
sys.path.append('/home/mrhsegypt/termcolor/termcolor-1.1.0')
from termcolor import colored, cprint
import sqlite3 as lite

class Db:
        """ this handles the contents of a database"""
        """
        def __init__(self):
                self.setup()
        def setup(self):        # to feed info used in other methods
                self.points = (-1,-0.5,0,0.5,1)
                self.weights = (1,1,1,1,1)
        """
        def createtable(self, tablename, tablecolumns):      # f is a string containing a tuple of the table column titles, like, "(id integer, name text)"
                conn=lite.connect('pythonsqlite.db')
                c=conn.cursor()
                c.execute("create table "+ tablename + " "+ tablecolumns)
                #c.execute("create table test (?,?)",f)
                conn.commit()
                conn.close()
                #sum = len(f)
                return 
        def insert(self, tablename, newentry):      # newentry is a tuple of the values wanted to insert (a single row entry)
                conn=lite.connect('pythonsqlite.db')
                c=conn.cursor()
                c.execute("insert into "+ tablename +" values (?,?)", newentry)   # feed (newid, newname)
                conn.commit()
                conn.close()
                #sum = len(f)
                return
        def select_all(self, tablename):      # f is a tuple of the values wanted to insert (a single row entry)
                conn=lite.connect('pythonsqlite.db')
                c=conn.cursor()
                output = c.execute("select * from "+ tablename)   # feed (newid, newname)
                rows=[]
                for i in output: rows.append(i)                
                conn.commit()
                conn.close()
                #sum = len(f)
                #print output
                return  rows                    # how to format the output (say I want it to be rows below each other.) ?? 
        def search(self, tablename, columnname, value, state):      # f is a tuple of the values wanted to insert (a single row entry), state =True or False in string
                conn=lite.connect('pythonsqlite.db')
                c=conn.cursor()
                output = c.execute("select * from "+tablename+ " where "+columnname + " = "+ "'"+ value + "'" + " and doiknowit " + state)   # state = "= True" or "= False"
                outty=[]
                for i in output: outty.append(i)                
                conn.commit()
                conn.close()
                if len(outty)==0:
                        return False
                else:
                        return True

                """
                try:
                        outty
                except NameError:
                        print "False"
                else:
                        return True
                #return  outty[0][0] != None                    # is there an elegant way to do this? check that output actually has something?
                """ 


""" XXXXXXXXXXX TO DO NOW XXXXXXXXXXX                                               
        def get_unknown_words_in_article(self, ar):
                
        def sniff_article(self, ar):
                for word in ar.words:
                        
"""

