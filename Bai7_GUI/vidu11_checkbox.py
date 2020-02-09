import wx
app = wx.App()
frame = wx.Frame(None, title = 'Vi du CheckBox', size=(300,150))
panel = wx.Panel(frame, -1)

wx.CheckBox(panel, -1, 'Một', (35,40), (150,20))
wx.CheckBox(panel, -1, 'Hai', (35,60), (150,20))
wx.CheckBox(panel, -1, 'Ba', (35,80), (150,20))

frame.Show(True)
app.MainLoop()