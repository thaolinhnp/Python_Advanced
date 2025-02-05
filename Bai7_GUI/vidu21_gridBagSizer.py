import wx
app = wx.App()
frame = wx.Frame(None, title='Ví dụ Grid', size=(300,150))
panel = wx.Panel(frame,-1)
wxGridBagSizer = wx.GridBagSizer(5,5)

stTitle = wx.StaticText(panel,-1,label='THÔNG TIN CÔNG TY')
wxGridBagSizer.Add(stTitle,pos=(0,0),span(1,2),flag=wx.ALIGN_CENTER_HORIZONTAL)

stTenCongTy = wx.StaticText(panel,-1,label='Tên Công Ty')
wxGridBagSizer.Add(stTenCongTy,pos=(1,0),span(1,1))

txtTenCongTy = wx.TextCtrl(panel,-1)
wxGridBagSizer.Add(txtTenCongTy,pos=(1,1),span(1,1),flag=wx.EXPAND|wx.ALL, border =5)

wxGridBagSizer.AddGrowableCol(1)
panel.SetSizerAndFit(wxGridBagSizer)

frame.Center(wx.BOTH)
frame.Show(True)
app.MainLoop()