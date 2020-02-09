# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from Giao_dien.gd_taoTaiKhoan import *

from Giao_dien.gd_dangNhap import *

###########################################################################
## Class Welcome
###########################################################################

class Welcome ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap5 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/Welcome.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_bitmap5, 0, wx.ALL, 5 )
        
        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,20 ), 0 )
        self.m_staticText28.Wrap( -1 )
        bSizer4.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_btnNVMoi = wx.Button( self, wx.ID_ANY, u"Nhân Viên Mới", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
        self.m_btnNVMoi.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
        
        bSizer4.Add( self.m_btnNVMoi, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_btnNVHienTai = wx.Button( self, wx.ID_ANY, u"Nhân Viên Hiện Tại", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
        self.m_btnNVHienTai.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
        
        bSizer4.Add( self.m_btnNVHienTai, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer4 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_btnNVMoi.Bind( wx.EVT_BUTTON, self.m_btnNVMoi_click )
        self.m_btnNVHienTai.Bind( wx.EVT_BUTTON, self.m_btnNVHienTai_click )

        # panel_Dang_Nhap = Dang_Nhap(self)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_btnNVMoi_click( self, event ):

        frame = wx.Frame(self, title = u'Tạo Tài Khoản', size=(500,450))
        taoTK = Tao_tai_khoan(frame)
        frame.Show()

    def m_btnNVHienTai_click( self, event ):
        frame = wx.Frame(None, title = 'Đăng Nhập', size=(500,200))
        dangNhap = Dang_Nhap(frame)
        frame.Show()


if __name__ == "__main__":

    app = wx.App()
    frame = Welcome(None)

    frame.Show()
    app.MainLoop()
