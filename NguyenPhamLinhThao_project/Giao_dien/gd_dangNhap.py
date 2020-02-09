# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from Xu_ly.Xu_ly_nhan_vien import *
from Giao_dien.gd_trangChu import *

###########################################################################
## Class Dang_Nhap
###########################################################################

class Dang_Nhap ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gbSizer2.Add( self.m_staticText21, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Tên Đăng Nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gbSizer2.Add( self.m_staticText22, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtTenDangNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 250,-1 ), 0 )
		gbSizer2.Add( self.m_txtTenDangNhap, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer2.Add( self.m_staticText23, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Mật Khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gbSizer2.Add( self.m_staticText24, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtMatKhau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gbSizer2.Add( self.m_txtMatKhau, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		self.m_staticText25.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer2.Add( self.m_staticText25, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_btnDangNhap = wx.Button( self, wx.ID_ANY, u"Đăng Nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.m_btnDangNhap, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText26.Wrap( -1 )
		gbSizer2.Add( self.m_staticText26, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer2.Add( gbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.m_btnDangNhap.Bind( wx.EVT_BUTTON, self.m_btnDangNhap_click )
	
	def __del__( self ):
		pass

	
	# Virtual event handlers, overide them in your derived class
	def m_btnDangNhap_click( self, event ):
		tenDangNhap = self.m_txtTenDangNhap.GetValue()
		matKhau = self.m_txtMatKhau.GetValue()

		print(tenDangNhap)

		if tenDangNhap == '' or matKhau == '':
			kq = wx.MessageBox('Vui lòng nhập đủ Tên Đăng Nhập và Mật Khẩu','Thông báo', wx.OK|wx.ICON_WARNING)
		else:
			xlNhanVien = ql_nhan_vien('du_lieu/qlNhanVien.db')
			n = xlNhanVien.dang_nhap(tenDangNhap,matKhau)
			if n >= 1:
    			## Lưu tenDangNhap
				path_file =f'Du_lieu/tenDangNhap'
				noiDung = tenDangNhap
				print(noiDung)
				f=open(path_file,'w',encoding='utf-8')
				f.write(noiDung)
				f.close()
				
				app = wx.App()
				frame = Trang_Chu(None)

				frame.Show()
				app.MainLoop()

				# self.Hide()
				# self.Parent.nb.Show()
				# self.Parent.m_btnDangNhap.Show()
				# self.Parent.Layout()

			else:
				kq = wx.MessageBox('Tài khoản không tồn tại hoặc Sai mật khẩu','Thông báo', wx.OK|wx.ICON_WARNING)
