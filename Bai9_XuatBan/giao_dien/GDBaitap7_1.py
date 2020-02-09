# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Xu_ly.Xu_ly_Congty import *

###########################################################################
## Class panelBT7_1
###########################################################################

class panelBT7_1 ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.TAB_TRAVERSAL )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/it.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Ten", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_txtTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 550,-1 ), 0 )
		gbSizer1.Add( self.m_txtTen, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Ma so", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_txtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtMaSo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Dia chi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_txtDiaChi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtDiaChi, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Dien thoai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_txtDienThoai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtDienThoai, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_txtEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtEmail, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )

		self.m_btnCapNhat = wx.Button( self, wx.ID_ANY, u"Cap nhat", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_btnCapNhat, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnCapNhat.Bind( wx.EVT_BUTTON, self.m_btnCapNhat_click )

	def __del__( self ):
		pass	




	# Virtual event handlers, overide them in your derived class
	def m_btnCapNhat_click( self, event ):
		tenCongTy = self.m_txtTen.GetValue()
		maSo = self.m_txtMaSo.GetValue()
		dienThoai = self.m_txtDienThoai.GetValue()
		diaChi = self.m_txtDiaChi.GetValue()
		email = self.m_txtEmail.GetValue()

		xlCongTy = CongTy('du_lieu/qlVatTu.db')
		n = xlCongTy.CapNhatCongty(tenCongTy, maSo, dienThoai, diaChi, email)
		if n == 1:
			kq = wx.MessageBox('Cập nhật thành công','Thông báo', wx.OK|wx.ICON_INFORMATION)
			frame.Destroy()
			# def onClose(self):
			# 	frame.Destroy()
			# app = wx.App()
			# frame = wx.Frame(None, title = 'Close', size=(300,100))
			# panel = wx.Panel(frame, -1)
			# button = wx.Button(panel, -1, 'Close', pos=(50,20))
			# frame.Bind(wx.EVT_BUTTON, onClose, button)
			# button.SetDefault()
			# frame.Show(True)
			# app.MainLoop()
		else:
			kq = wx.MessageBox('Cập nhật KHôNG thành công','Thông báo', wx.OK|wx.ICON_INFORMATION)