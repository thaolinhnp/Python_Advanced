import wx
class ManHinhChinh(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, title='Vi Du 2', size=(500,400))
        panel = wx.Panel(self,-1)
        wx.StaticText(panel,label='Hello World',pos=(10,20))

if __name__ == "__main__":
    app = wx.App()
    frame = ManHinhChinh()
    frame.Show(True)
    app.MainLoop()