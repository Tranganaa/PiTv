import wx

ID_FILE_NEW = wx.NewId()
ID_FILE_OPEN = wx.NewId();
ID_FILE_SAVE = wx.NewId(); 
ID_EDIT_CUT = wx.NewId()
ID_EDIT_COPY = wx.NewId()
ID_EDIT_PASTE= wx.NewId()
ID_HELP_ABOUT = wx.NewId()

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,200))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        editmenu= wx.Menu()
        helpmenu= wx.Menu()

        #File Menu contents
        filemenu.Append(ID_FILE_NEW, "&New","Create a blank document")
        filemenu.Append(ID_FILE_OPEN, "&Open","Open an existing document")
        filemenu.Append(ID_FILE_SAVE, "&Save","Save the current document")
        filemenu.AppendSeparator()
        #self.Bind(wx.EVT_MENU, self.FileExit,filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program"))
        self.Bind(wx.EVT_MENU, self.FileNew,ID_FILE_NEW)
        EVT_MENU(self, ID_FILE_OPEN,self.FileOpen)
        EVT_MENU(self, ID_FILE_SAVE,self.FileSave)
		        
        #Edit Menu contents
        editmenu.Append(ID_EDIT_CUT,"Cut")
        editmenu.Append(ID_EDIT_COPY,"Copy")
        editmenu.Append(ID_EDIT_PASTE,"Paste")
        EVT_MENU(self, ID_EDIT_CUT,self.EditCut)
        EVT_MENU(self, ID_EDIT_COPY,self.EditCopy)
        EVT_MENU(self, ID_EDIT_PASTE,self.EditPaste)
        
        #Help Menu contents
        helpmenu.Append(ID_HELP_ABOUT,"A&bout")
        EVT_MENU(self, ID_HELP_ABOUT,self.HelpAbout)
        
        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(editmenu,"&Edit") # Adding the "editmenu" to the Menubar
        menuBar.Append(helpmenu,"Help")
        
        self.SetMenuBar(menuBar)
        #self.SetMenuBar(menuBarEdit)  # Adding the MenuBar to the Frame content.
        self.Show(True)

        
        #Functions for the Menu items 
	def FileNew(self):
		self.Msg(self,"Under Construction","")
	def FileOpen(self):
		self.Msg(self,"Under Construction","")
	def FileSave(self):	
		self.Msg(self,"Under Construction","")
	def FileExit(self,event=None):			
		self.Msg(self,"Under Construction","")
	def EditCut(self):
		self.Msg(self,"Under Construction","")
	def EditCopy(self):
		self.Msg(self,"Under Construction","")
	def EditPaste(self):
		self.Msg(self,"Under Construction","")
	def HelpAbout(self):
		self.Msg(self,"Under Construction","")
	def Msg(self,message,caption):
		dlg =wx.MessageDialog(self,message,caption,wxOK_DEFAULT)
			       
       
app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()
