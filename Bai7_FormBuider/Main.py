# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from giao_dien.GDBaitap7_1 import *
from Xu_ly.Xu_ly_Congty import *

from giao_dien.GDBaitap7_2 import *
from Xu_ly.Xu_ly_NhomTiVi import *

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.MDIParentFrame ):
	
	def __init__( self, parent ):
		wx.MDIParentFrame.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItemTTCTy = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thong Tin Cong Ty", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemTTCTy )
		
		self.m_menuItemNhomTV = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Nhom Tivi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemNhomTV )
		
		self.m_menuItemThemNV = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Them Nhan Vien", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemThemNV )
		
		self.m_menuItemTKNV = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thong Ke Nhan Vien", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemTKNV )
		
		self.m_menu1.AppendSeparator()
		
		self.m_menuItemThoat = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Thoat", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItemThoat )
		
		self.m_menubar1.Append( self.m_menu1, u"Cong Ty" ) 
		
		self.m_menu2 = wx.Menu()
		self.m_menuItemThemTV = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Them Tivi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.AppendItem( self.m_menuItemThemTV )
		
		self.m_menubar1.Append( self.m_menu2, u"Ti Vi" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuItemTTCTy_click, id = self.m_menuItemTTCTy.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemNhomTV_click, id = self.m_menuItemNhomTV.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemThemNV_click, id = self.m_menuItemThemNV.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemTKNV_click, id = self.m_menuItemTKNV.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemThoat_click, id = self.m_menuItemThoat.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemThemTV_click, id = self.m_menuItemThemTV.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_menuItemTTCTy_click( self, event ):

		# dsChildren = self.GetChildren()
		# for item in dsChildren:
		# 	if item.GetTitle() == u'Thong tin cong ty':
		# 		item.Activate()
		# 		return
		# xlCongty = CongTy('du_lieu/qlVatTu.db')
		# ttCty = xlCongty.ThongTinCongTy()
		# xlCongty.deConnect()

		frame = wx.MDIChildFrame(self, title = 'Thong tin cong ty', size=(700,550))
		ttct = panelBT7_1(frame)
		ttct.m_txtTen.SetValue(ttCty['tenCongTy'])
		ttct.m_txtMaSo.SetValue(ttCty['maSo'])
		ttct.m_txtDiaChi.SetValue(ttCty['diaChi'])
		ttct.m_txtDienThoai.SetValue(ttCty['dienThoai'])
		ttct.m_txtEmail.SetValue(ttCty['email'])
		frame.CenterOnParent(wx.BOTH)
		frame.Show()
		
	
	def m_menuItemNhomTV_click( self, event ):
		dsChildren = self.GetChildren()
		for item in dsChildren:
			if item.GetTitle() == u'Nhom TiVi':
				item.Activate()
				return
		frame = wx.MDIChildFrame(self, title = 'Nhom TiVi', size=(700,550))
		nhomtivi = panelBaiTap7_2(frame)

		xlNhomTivi = NhomTiVi('du_lieu/qlTivi.db')
		dsNhom = xlNhomTivi.InNhomTiVi()
		nhomtivi.m_lstDanhSach.Append(dsNhom)
		xlNhomTivi.deConnect()
		
		frame.CenterOnParent(wx.BOTH)
		frame.Show()
	
	def m_menuItemThemNV_click( self, event ):
		event.Skip()
	
	def m_menuItemTKNV_click( self, event ):
		event.Skip()
	
	def m_menuItemThoat_click( self, event ):
		event.Skip()
	
	def m_menuItemThemTV_click( self, event ):
		event.Skip()
	

if __name__ == "__main__":
	
	app = wx.App()
	frame = frameMain(None)
	frame.Show()
	app.MainLoop()