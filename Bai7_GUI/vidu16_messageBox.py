import wx
def OnXem(event):
    kq = wx.MessageBox('Bạn có chắc chắn muốn xóa không','Thông báo', wx.YES_NO|wx.ICON_INFORMATION)
    if wx.YES == kq:
        stTraLoi.SetLabel('Bạn chọn YES')
    else:
        stTraLoi.SetLabel('Bạn chọn NO')

app = wx.App()
frame = wx.Frame(None, title = 'Vi du MessageBox', size=(300,150))
panel = wx.Panel(frame, -1)
btnChon = wx.Button(panel, -1, 'Click vào để xem Message', pos=(10,10))
frame.Bind(wx.EVT_BUTTON, OnXem, btnChon)
stTraLoi = wx.StaticText(panel,-1, pos=(10,50))
frame.Show(True)
app.MainLoop()