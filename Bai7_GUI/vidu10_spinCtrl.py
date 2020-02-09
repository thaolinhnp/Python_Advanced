import wx
def onXem(self):
    dlg = wx.MessageDialog(None, 'Slide 1: value = '+
    str(slider1.GetValue()),'A Message Box',wx.OK)
    dlg.ShowModal()

app = wx.App()
frame = wx.Frame(None, title = 'Vi du SpinCtrl', size=(340,320))
panel = wx.Panel(frame, -1)

sc = wx.SpinCtrl(panel, -1, '', (30,20), (80,-1))
sc.SetRange(1,100)
sc.SetValue(5)

frame.Show(True)
app.MainLoop()