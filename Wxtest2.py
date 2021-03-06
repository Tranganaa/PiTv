#!/usr/bin/env python
import wx

class WindowTest(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(400,200))
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar() # A Statusbar in the bottom of the window

		# Setting up the menu.
		filemenu= wx.Menu()
        
        
		fileNewItem=filemenu.Append(wx.NewId(), "&New","Create a blank document")
		self.Bind(wx.EVT_MENU, self.FileNew,fileNewItem)
        
		#Editmenu
        editmenu= wx.Menu()
        
        
        helpmenu= wx.Menu()
        
        menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File",editmenu,"&Edit",helpmenu,"&Help") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar)
		self.Show(True)

	def FileNew(self,event=None):
		self.Msg(self,"Under Construction","Hello")

	def Msg(self,event,message,caption):
		dlg=wx.MessageDialog(self,message,caption,wx.OK)
		dlg.ShowModal()

        


app = wx.App(False)
frame = WindowTest(None, "Sample editor")
app.MainLoop()
