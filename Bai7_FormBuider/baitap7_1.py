from giao_dien.GDBaitap7_1 import *
from Xu_ly.Xu_ly_Congty import *
import wx

xlCongty = CongTy('du_lieu/qlVatTu.db')
ttCty = xlCongty.ThongTinCongTy()
xlCongty.deConnect()
print(ttCty)

app = wx.App()
frame = wx.Frame(None, title = 'Thong tin cong ty', size=(700,550))
ttct = panelBT7_1(frame)
ttct.m_txtTen.SetValue(ttCty['tenCongTy'])
ttct.m_txtMaSo.SetValue(ttCty['maSo'])
ttct.m_txtDiaChi.SetValue(ttCty['diaChi'])
ttct.m_txtDienThoai.SetValue(ttCty['dienThoai'])
ttct.m_txtEmail.SetValue(ttCty['email'])
frame.Show()
app.MainLoop()