import wx
app = wx.App()
frame = wx.Frame(None, title = 'Vi du Image', size=(300,400))
panel = wx.Panel(frame, -1)
hinh = wx.Image('close.png',wx.BITMAP_TYPE_ANY).ConvertToBitmap()
stStaticBitmap = wx.StaticBitmap(panel,-1,hinh)

frame.Show(True)
app.MainLoop()