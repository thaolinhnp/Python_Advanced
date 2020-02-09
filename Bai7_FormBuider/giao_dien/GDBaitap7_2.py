# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Xu_ly.Xu_ly_NhomTiVi import *

###########################################################################
## Class panelBaiTap7_2
###########################################################################

class panelBaiTap7_2 ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhom tivi" ), wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Ma So", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_txtMaSo = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		bSizer2.Add( self.m_txtMaSo, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Ten", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_txtTen = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer2.Add( self.m_txtTen, 0, wx.ALL, 5 )


		sbSizer1.Add( bSizer2, 0, 0, 5 )

		self.m_btnThem = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Them", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_btnThem, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( sbSizer1, 0, 0, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh sach nhom" ), wx.VERTICAL )

		m_lstDanhSachChoices = []
		self.m_lstDanhSach = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstDanhSachChoices, 0 )
		sbSizer2.Add( self.m_lstDanhSach, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnThem.Bind( wx.EVT_BUTTON, self.m_btnThem_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_btnThem_click( self, event ):
		xlNhomTivi = NhomTiVi('du_lieu/qlTivi.db')
		MaSo = self.m_txtMaSo.GetValue()
		Ten = self.m_txtTen.GetValue()
		n = xlNhomTivi.ThemNhom(MaSo,Ten)
		if n == 1:
			self.m_lstDanhSach.Append(Ten)
		else:
			wx.MessageBox('Thêm KHôNG thành công','Thông báo', wx.OK|wx.ICON_INFORMATION)


