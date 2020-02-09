import wx

app = wx.App()
frame = wx.Frame(None, title='Vi Du 1', size=(500,400))
panel = wx.Panel(frame)
label = wx.StaticText(panel,label='Hello World',pos=(100,50))
frame.Show(True)
app.MainLoop()