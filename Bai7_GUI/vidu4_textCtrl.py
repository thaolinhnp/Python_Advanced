import wx
app = wx.App()
frame = wx.Frame(None, title="Ví dụ TextCtrl", size=(300,100))
panel = wx.Panel(frame, -1)
wx.TextCtrl(panel, -1, 'Nhập họ tên', size=(175,30), pos=(50,10))
frame.Show(True)
app.MainLoop()