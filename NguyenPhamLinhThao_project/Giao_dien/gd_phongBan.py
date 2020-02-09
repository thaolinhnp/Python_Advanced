# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

from Xu_ly.Xu_ly_nhan_vien import *
from Xu_ly.Xu_ly_phong_ban import *

###########################################################################
## Class Phong_ban
###########################################################################

class Phong_ban ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1000,600 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText27 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Phòng Ban", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gbSizer4.Add( self.m_staticText27, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		m_choicePhongBanChoices = ['RISK','COLLECTION','FINANCE','MARKETING','IT']
		self.m_choicePhongBan = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), m_choicePhongBanChoices, 0 )
		self.m_choicePhongBan.SetSelection( 0 )
		gbSizer4.Add( self.m_choicePhongBan, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_btnTimKiem = wx.Button( self.m_panel1, wx.ID_ANY, u"Tìm Kiếm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.m_btnTimKiem, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( gbSizer4 )
		self.m_panel1.Layout()
		gbSizer4.Fit( self.m_panel1 )
		bSizer4.Add( self.m_panel1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText28 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Tổng Số Nhân Viên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gbSizer5.Add( self.m_staticText28, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtTongSoNV = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_txtTongSoNV.Enable( False )
		
		gbSizer5.Add( self.m_txtTongSoNV, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Tên Quản Lý", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		gbSizer5.Add( self.m_staticText29, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtTenQuanLy = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_txtTenQuanLy.Enable( False )
		
		gbSizer5.Add( self.m_txtTenQuanLy, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Vị Trí", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gbSizer5.Add( self.m_staticText30, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtViTri = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.m_txtViTri.Enable( False )
		
		gbSizer5.Add( self.m_txtViTri, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Danh Sách Nhân Viên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gbSizer5.Add( self.m_staticText31, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_gridDSNhanVien = wx.grid.Grid( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_gridDSNhanVien.CreateGrid( 5, 5 )
		self.m_gridDSNhanVien.EnableEditing( True )
		self.m_gridDSNhanVien.EnableGridLines( True )
		self.m_gridDSNhanVien.EnableDragGridSize( False )
		self.m_gridDSNhanVien.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridDSNhanVien.SetColSize( 0, 120 )
		self.m_gridDSNhanVien.SetColSize( 1, 120 )
		self.m_gridDSNhanVien.SetColSize( 2, 120 )
		self.m_gridDSNhanVien.SetColSize( 3, 120 )
		self.m_gridDSNhanVien.SetColSize( 4, 120 )
		self.m_gridDSNhanVien.EnableDragColMove( False )
		self.m_gridDSNhanVien.EnableDragColSize( True )
		self.m_gridDSNhanVien.SetColLabelSize( 30 )
		self.m_gridDSNhanVien.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridDSNhanVien.EnableDragRowSize( True )
		self.m_gridDSNhanVien.SetRowLabelSize( 80 )
		self.m_gridDSNhanVien.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridDSNhanVien.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gbSizer5.Add( self.m_gridDSNhanVien, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( gbSizer5 )
		self.m_panel2.Layout()
		gbSizer5.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		self.m_btnTimKiem.Bind( wx.EVT_BUTTON, self.m_btnTimKiem_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_btnTimKiem_click( self, event ):
		phongBan = self.m_choicePhongBan.GetStringSelection()

		xlNhanvien = ql_nhan_vien('Du_lieu\qlNhanVien.db')
		lstNhanVien = xlNhanvien.ds_nv_theo_phong(phongBan)

		xlPhongban = ql_phong_ban('Du_lieu\qlNhanVien.db')
		phong = xlPhongban.tim_phong_ban(phongBan)

		tongNV = str(len(lstNhanVien))
		self.m_txtTongSoNV.SetValue(tongNV)

		tenQuanLy = phong.get('tenQuanLy')
		self.m_txtTenQuanLy.SetValue(tenQuanLy)

		viTri = phong.get('viTri')
		self.m_txtViTri.SetValue(viTri)

		for c in range(0,5):
			lst = []
			for item in lstNhanVien[0]:
				lst.append(item)
			columnname = lst[c]
			self.m_gridDSNhanVien.SetColLabelValue(c,columnname)

		for c in range(0,5):
			for r in range(0,5):
				self.m_gridDSNhanVien.SetCellValue(r,c, '')

		for r in range(0,len(lstNhanVien)):
			for c in range(0,5):
				lst = []
				for item in lstNhanVien[r].values():
					lst.append(item)
				ttNhanvien = lst[c]
				self.m_gridDSNhanVien.SetCellValue(r,c, ttNhanvien)
				self.m_gridDSNhanVien.SetReadOnly(r,c)