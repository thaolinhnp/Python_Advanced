import wx
app = wx.App()
frame = wx.Frame(None, title="Ví dụ StatixText", size=(300,100))
panel = wx.Panel(frame, -1)
wx.StaticText(panel, -1, 'Trung Tâm Tin Học KHTN', size=(150,30), pos=(50,10))
frame.Show(True)
app.MainLoop()