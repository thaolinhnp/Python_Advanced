import wx
app = wx.App()
frame = wx.Frame(None, title = 'Vi du RadioButton', size=(300,150))
panel = wx.Panel(frame, -1)

wx.RadioButton(panel, -1, 'Nam', (35,40), (150,20))
wx.RadioButton(panel, -1, 'Nữ', (35,60), (150,20))
wx.RadioButton(panel, -1, 'Khác', (35,80), (150,20))

frame.Show(True)
app.MainLoop()