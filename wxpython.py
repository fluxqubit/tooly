

http://zetcode.com/wxpython/
SQLite database browser



BUILDING SIMPLE WINDOW



#!/usr/bin/python

# simple.py

import wx

app = wx.App()

frame = wx.Frame(None, -1, 'simple.py')
frame.Show()

app.MainLoop()



---------------------------

WINDOW WITHOUT MINIMIZE BUTTON 

#!/usr/bin/python

# nominimizebox.py

import wx

app = wx.App()
window = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER 
	| wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
window.Show(True)

app.MainLoop()


----------------------------

WINDOW WITH 250X200 PIXEL SIZE

#!/usr/bin/python
# -*- coding: utf-8 -*-

# size.py

import wx

class Example(wx.Frame):
  
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(250, 200))
        self.Centre()
        self.Show()


if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Size')
    app.MainLoop()
    
---------------------


SHOWS THE COORDINATES OF THE WINDOW INTERACTIVELY

#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        self.InitUI()
    def InitUI(self):
        wx.StaticText(self, label='x:', pos=(10,10))
        wx.StaticText(self, label='y:', pos=(10,30))     
        self.st1 = wx.StaticText(self, label='', pos=(30, 10))
        self.st2 = wx.StaticText(self, label='', pos=(30, 30))
        self.Bind(wx.EVT_MOVE, self.OnMove)
        self.SetSize((250, 180))
        self.SetTitle('Move event')
        self.Centre()
        self.Show(True)  
    def OnMove(self, e):    
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  



--------------------------------------


A WINDOW WITH A FEW BUTTONS.

#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx

class Example(wx.Frame):  
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)   
        self.InitUI()    
    def InitUI(self):
        pnl = wx.Panel(self)
        grid = wx.GridSizer(3, 2)
        grid.AddMany([(wx.Button(pnl, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_DELETE), 0, wx.TOP, 9),
            (wx.Button(pnl, wx.ID_SAVE), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_EXIT)),
            (wx.Button(pnl, wx.ID_STOP), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_NEW))])
        self.Bind(wx.EVT_BUTTON, self.OnQuitApp, id=wx.ID_EXIT)         # THE ONLY ACTIVE BUTTON. SHUTS DOWN THE WINDOW
        #self.Bind(wx.EVT_BUTTON, self.OnQuitApp, id=wx.ID_SAVE)
        pnl.SetSizer(grid)
        self.SetSize((220, 180))
        self.SetTitle("Standard ids")
        self.Centre()
        self.Show(True)
    def OnQuitApp(self, event):
        self.Close()

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()

-----------------------------------------------


#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx

ID_MENU_NEW = wx.NewId()
ID_MENU_OPEN = wx.NewId()
ID_MENU_SAVE = wx.NewId()

class Example(wx.Frame): 
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()       
    def InitUI(self):
        self.CreateMenuBar()
        self.CreateStatusBar()
        
        self.SetSize((250, 180))
        self.SetTitle('Global ids')
        self.Centre()
        self.Show(True)  
    def CreateMenuBar(self):
        mb = wx.MenuBar()
        
        fMenu = wx.Menu()
        fMenu.Append(ID_MENU_NEW, 'New')
        fMenu.Append(ID_MENU_OPEN, 'Open')
        fMenu.Append(ID_MENU_SAVE, 'Save')
        
        mb.Append(fMenu, '&File')
        self.SetMenuBar(mb)
        
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_NEW)
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_OPEN)
        self.Bind(wx.EVT_MENU, self.DisplayMessage, id=ID_MENU_SAVE)        
    def DisplayMessage(self, e):
        sb = self.GetStatusBar()       
        eid = e.GetId()
        if eid == ID_MENU_NEW:
            msg = 'New menu item selected'
        elif eid == ID_MENU_OPEN:
            msg = 'Open menu item selected'
        elif eid == ID_MENU_SAVE:
            msg = 'Save menu item selected'
        sb.SetStatusText(msg)

def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  


---------------------------------------------
CRAP THAT SHOWS FOCUS SCREENS

#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx

class MyWindow(wx.Panel):
    def __init__(self, parent):
        super(MyWindow, self).__init__(parent)
        self.color = '#b3b3b3'
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        #self.Bind(wx.EVT_SET_FOCUS, self.OnQuitApp)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
    #def OnQuitApp(self, event):
    #    self.Close()
    def OnPaint(self, e):
        
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)
    def OnSize(self, e):
        
        self.Refresh()
    def OnSetFocus(self, e):
        
        self.color = '#0099f7'
        self.Refresh()
    def OnKillFocus(self, e):
        
        self.color = '#b3b3b3'
        self.Refresh()

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
        
    def InitUI(self):
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.LEFT, 9),
            (MyWindow(self), 0, wx.EXPAND|wx.TOP|wx.RIGHT, 9), 
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.LEFT, 9), 
            (MyWindow(self), 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 9)])
        self.SetSizer(grid)
        self.SetSize((350, 250))
        self.SetTitle('Focus event')
        self.Centre()
        self.Show(True)  
    def OnMove(self, e):
        
        print e.GetEventObject()
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  



--------------------------------------------



#!/usr/bin/python
# -*- coding: utf-8 -*-


import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
                
    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        pnl.SetFocus()
        self.SetSize((250, 180))
        self.SetTitle('Key event')
        self.Centre()
        self.Show(True)  
    def OnKeyDown(self, e):
        
        key = e.GetKeyCode()
        
        if key == wx.WXK_ESCAPE:
            
            ret  = wx.MessageBox('Are you sure to quit?', 'Question', 
                wx.YES_NO | wx.NO_DEFAULT, self)
                
            if ret == wx.YES:
                self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()  

----------------------------------------------------


#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx


class Example(wx.Frame):
    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw) 
        
        self.InitUI()
        
    def InitUI(self):   
        pnl = wx.Panel(self)
        font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        heading = wx.StaticText(self, label='The Central Europe', pos=(130, 15))
        heading.SetFont(font)
        wx.StaticLine(self, pos=(25, 50), size=(300,1))
        wx.StaticText(self, label='Sentence:', pos=(25, 80))
        wx.StaticText(self, label='I went where noone has ever gone before', pos=(90, 80))   # where the original sentence is shown
        ## parse the original sentence and spit words one by one.
        wx.StaticLine(self, pos=(25, 260), size=(300,1))
        #tsum = wx.StaticText(self, label='164 336 000', pos=(240, 280))
        #sum_font = tsum.GetFont()
        #sum_font.SetWeight(wx.BOLD)
        #tsum.SetFont(sum_font)
        btn = wx.Button(self, label='No idea!', pos=(200, 310))
        btn2 = wx.Button(self, label='Know it!', pos=(300, 310))
        btn3 = wx.Button(self, label='Close', pos=(400, 310))
        btn.Bind(wx.EVT_BUTTON, self.AddToDB)
        btn2.Bind(wx.EVT_BUTTON, self.Skip)
        btn3.Bind(wx.EVT_BUTTON, self.OnClose)        
        self.SetSize((700, 380))
        self.SetTitle('wx.StaticLine')
        self.Centre()
        self.Show(True)      
    def OnClose(self, e):
        self.Close(True) 
    def Change(self, e):
        self.Close(True)   
    def Skip(self, e):
        ???? skip to next word
    def AddToDB(self,e):
        ???? add this word to the database


def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()   

---------------------------------------

CREATES TEXT SPACE (TEXTBOX)


#!/usr/bin/env python
import wx
class MyFrame(wx.Frame):
        """ We simply derive a new class of Frame. """
        def __init__(self, parent, title):
                wx.Frame.__init__(self, parent, title=title, size=(200,100))
                self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
                self.Show(True)
        """
        def Copy(self):
                self.Copy()
        """


app = wx.App(False)
frame = MyFrame(None, 'Small editor')
app.MainLoop()

