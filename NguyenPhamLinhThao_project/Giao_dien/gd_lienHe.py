# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from Xu_ly.Xu_ly_lien_he import *

###########################################################################
## Class Lien_He
###########################################################################
class Lien_He ( wx.Panel ):
    	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		gbSizer15 = wx.GridBagSizer( 0, 0 )
		gbSizer15.SetFlexibleDirection( wx.BOTH )
		gbSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		gbSizer15.Add( self.m_staticText131, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText132 = wx.StaticText( self, wx.ID_ANY, u"Tiêu Đề", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )
		gbSizer15.Add( self.m_staticText132, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtTieuDe = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		gbSizer15.Add( self.m_txtTieuDe, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText134 = wx.StaticText( self, wx.ID_ANY, u"Nội Dung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )
		gbSizer15.Add( self.m_staticText134, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText134 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )
		gbSizer15.Add( self.m_staticText134, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtNoiDung = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.m_txtNoiDung, wx.GBPosition( 3, 1 ), wx.GBSpan( 5, 4 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText135 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText135.Wrap( -1 )
		gbSizer15.Add( self.m_staticText135, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText136 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText136.Wrap( -1 )
		gbSizer15.Add( self.m_staticText136, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText137 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText137.Wrap( -1 )
		gbSizer15.Add( self.m_staticText137, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText138 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 35,-1 ), 0 )
		self.m_staticText138.Wrap( -1 )
		gbSizer15.Add( self.m_staticText138, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_btnGui = wx.Button( self, wx.ID_ANY, u"Gửi", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer15.Add( self.m_btnGui, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( gbSizer15 )
		self.Layout()
		
		# Connect Events
		self.m_btnGui.Bind( wx.EVT_BUTTON, self.m_btnGui_click )
	
	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def m_btnGui_click( self, event ):
		tieuDe = self.m_txtTieuDe.GetValue()
		noiDung = self.m_txtNoiDung.GetValue()

		xlLienHe = Lien_he('du_lieu/qlNhanVien.db')
		n = xlLienHe.them_lien_he(tieuDe,noiDung)
		if n > 0:
			kq = wx.MessageBox('Gửi Liên Hệ thành công','Thông báo', wx.OK|wx.ICON_INFORMATION)
		else:
			kq = wx.MessageBox('Gửi Liên Hệ không thành công','Thông báo', wx.OK|wx.ICON_INFORMATION)
		xlLienHe.DeConnect()
	

