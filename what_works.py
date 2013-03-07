import db
import article
ar = article.Article('sample.txt')
ar.chop()       # ??? do I have to chop it first? can't that be done automatically as soon as I apply any of the next ones?
        
ar.get_words()
ar.get_sentences()
ar.get_paragraphs()
ar.sniffit()
ar.feed_db()   # !!!  except for special german letters. 



db = DataBase('file.db')
db.setup()
db.connect() # make connection and cursor
db.feed_article(ar)
db.sniff_article(ar)
...
db.close()


ar,db

interactor = Interactor(db)
interactor.ask_for_unknown_words(ar)
# perhaps clean the words here.
interactor.submit_unknown_words()
        
