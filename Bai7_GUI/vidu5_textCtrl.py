import wx
app = wx.App()
frame = wx.Frame(None, title='Vi du TextCtrl', size=(300,150))
panel = wx.Panel(frame, -1)
str = 'Thông tin công ty'
text = wx.StaticText(panel, -1, str, (20,20))
font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
text.SetFont(font)
wx.StaticText(panel, -1, 'Công ty trách nhiệm hữu hạn',(20,50))
frame.Show(True)
app.MainLoop()