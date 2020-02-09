from giao_dien.GDBaitap7_2 import *
from Xu_ly.Xu_ly_NhomTiVi import *
import wx

app = wx.App()
frame = wx.Frame(None, title = 'Nhom TiVi', size=(700,550))
nhomtivi = panelBaiTap7_2(frame)

xlNhomTivi = NhomTiVi('du_lieu/qlTivi.db')
lstNhomTivi = xlNhomTivi.InNhomTiVi()
nhomtivi.m_lstDanhSach.Append(lstNhomTivi)
xlNhomTivi.deConnect()
# print(lstNhomTivi)

frame.Show()
app.MainLoop()