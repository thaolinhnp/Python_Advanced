import wx
def onChoice(self):
    x = lst.GetStringSelection()
    print(x)

app = wx.App()
frame = wx.Frame(None, title = 'Vi du Choice', size=(300,150))
panel = wx.Panel(frame, -1)

sampleList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
wx.StaticText(panel, -1, 'Select one:', (15,20))
lst = wx.Choice(panel, -1, (85,18), choices=sampleList)
frame.Bind(wx.EVT_CHOICE, onChoice, lst)

# print(lst.GetStringSelection())

frame.Show(True)
app.MainLoop()