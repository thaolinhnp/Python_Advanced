# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from Giao_dien.gd_phongBan import *
from Giao_dien.gd_nhanVien import *
from Giao_dien.gd_lienHe import *

###########################################################################
## Class Trang_Chu
###########################################################################

class Trang_Chu ( wx.MDIParentFrame ):
	
	def __init__( self, parent ):
		wx.MDIParentFrame.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1200,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menuThongTin = wx.Menu()
		self.m_menuItemPhongBan = wx.MenuItem( self.m_menuThongTin, wx.ID_ANY, u"Phòng Ban", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuThongTin.AppendItem( self.m_menuItemPhongBan )
		
		self.m_menuItemNhanVien = wx.MenuItem( self.m_menuThongTin, wx.ID_ANY, u"Nhân Viên", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuThongTin.AppendItem( self.m_menuItemNhanVien )
		
		self.m_menubar2.Append( self.m_menuThongTin, u"Thông tin" ) 
		
		self.m_menuQLNhanVien = wx.Menu()
		self.m_menuItemNghiPhep = wx.MenuItem( self.m_menuQLNhanVien, wx.ID_ANY, u"Đơn nghỉ phép", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuQLNhanVien.AppendItem( self.m_menuItemNghiPhep )
		
		self.m_menuItemChamCong = wx.MenuItem( self.m_menuQLNhanVien, wx.ID_ANY, u"Chấm công", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuQLNhanVien.AppendItem( self.m_menuItemChamCong )
		
		self.m_menubar2.Append( self.m_menuQLNhanVien, u"Quản Lý Nhân Viên" ) 
		
		self.m_menuLienHe = wx.Menu()
		self.m_menuItemLienHe = wx.MenuItem( self.m_menuLienHe, wx.ID_ANY, u"Liên hệ nhân sự", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuLienHe.AppendItem( self.m_menuItemLienHe )
		
		self.m_menubar2.Append( self.m_menuLienHe, u"Liên Hệ" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_menuItemPhongBan_click, id = self.m_menuItemPhongBan.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemNhanVien_click, id = self.m_menuItemNhanVien.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemNghiPhep_click, id = self.m_menuItemNghiPhep.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemChamCong_click, id = self.m_menuItemChamCong.GetId() )
		self.Bind( wx.EVT_MENU, self.m_menuItemLienHe_click, id = self.m_menuItemLienHe.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_menuItemPhongBan_click( self, event ):
		dsChildren = self.GetChildren()
		for item in dsChildren:
			if item.GetTitle() == u'Tra Cứu Phòng Ban':
				item.Activate()
				return

		frame = wx.MDIChildFrame(self, title = u'Tra Cứu Phòng Ban', size=(1200,600))
		PhongBan = Phong_ban(frame)
		frame.CenterOnParent(wx.BOTH)
		frame.Show()
		frame.Maximize(True)
	
	def m_menuItemNhanVien_click( self, event ):
		dsChildren = self.GetChildren()
		for item in dsChildren:
			if item.GetTitle() == u'Tra Cứu Thông Tin Nhân Viên':
				item.Activate()
				return

		frame = wx.MDIChildFrame(self, title = u'Tra Cứu Thông Tin Nhân Viên', size=(600,500))
		NhanVien = Nhan_Vien(frame)
		frame.CenterOnParent(wx.BOTH)
		frame.Show()
		frame.Maximize(True)
	
	def m_menuItemNghiPhep_click( self, event ):
		kq = wx.MessageBox('Chức năng đang được xây dựng\n \
							Vui lòng Liên Hệ để biết thêm thông tin','Thông báo', wx.OK|wx.ICON_INFORMATION)
	
	def m_menuItemChamCong_click( self, event ):
		kq = wx.MessageBox('Chức năng đang được xây dựng\n \
							Vui lòng Liên Hệ để biết thêm thông tin','Thông báo', wx.OK|wx.ICON_INFORMATION)
	
	def m_menuItemLienHe_click( self, event ):
		dsChildren = self.GetChildren()
		for item in dsChildren:
			if item.GetTitle() == u'Liên Hệ':
				item.Activate()
				return

		frame = wx.MDIChildFrame(self, title = u'Liên Hệ', size=(1000,600))
		LienHe = Lien_He(frame)
		frame.CenterOnParent(wx.BOTH)
		frame.Show()
		frame.Maximize(True)

