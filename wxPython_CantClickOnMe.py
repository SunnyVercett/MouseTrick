#! /usr/bin/env python
#coding=utf-8
# Can't click on me!

import wx
import random

class FunnyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Click Me!",
                            size=(800,600),style=wx.MAXIMIZE|wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX^wx.MINIMIZE_BOX^wx.CLOSE_BOX)
        self.panel = wx.Panel(parent=self)
        x = random.randint(10,70)
        y = random.randint(10,50)
        pos = (x,y)
        self.button = wx.Button(self.panel,2,'Click Me!',pos,size=(85,45))
        self.button.Bind(wx.EVT_ENTER_WINDOW,self.changepos)
        self.Bind(wx.EVT_BUTTON,self.kill,self.button)
        #self.button.Bind() is also OK, because is a CommandEvent() 
    
    def changepos(self,event):
        x = random.randint(10,700)
        y = random.randint(10,500)
        pos = (x,y)
        self.button.SetPosition(pos)
        colors=['Red','Blue','White','Black','Grey','Green','Pink','Purple','Yellow']
        color=random.choice(colors)
        self.panel.SetBackgroundColour(color)
        self.panel.Refresh()
        
    def kill(self,event):
        self.button.Destroy()
        wx.Exit()
        
class SZApp(wx.App):
    def __init__(self):
        wx.App.__init__(self, True, filename='wxPython Error Info.txt')
        
    def OnInit(self):
        frame = FunnyFrame()
        frame.Show()
        return True
        
        
if __name__=='__main__':
    app= SZApp()
    app.MainLoop()