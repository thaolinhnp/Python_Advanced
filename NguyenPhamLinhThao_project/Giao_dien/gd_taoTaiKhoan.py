# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
import re

from Xu_ly.Xu_ly_nhan_vien import *

###########################################################################
## Class Tao_tai_khoan
###########################################################################

class Tao_tai_khoan ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,390 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Nhập Thông Tin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Họ Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtHoTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		gbSizer1.Add( self.m_txtHoTen, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Ngày Sinh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		# self.m_datePickerNgaySinh = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN)
		# gbSizer1.Add( self.m_datePickerNgaySinh, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.m_txtNgaySinh = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,-1 ), 0 )
		gbSizer1.Add( self.m_txtNgaySinh, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gbSizer1.Add( self.m_staticText6, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtDiaChi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtDiaChi, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText7, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Điện Thoại", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gbSizer1.Add( self.m_staticText8, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtDienThoai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtDienThoai, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		self.m_staticText9.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText9, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Ngày Vào Làm", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gbSizer1.Add( self.m_staticText10, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		# self.m_datePickerNgayVaoLam = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_DROPDOWN )
		# gbSizer1.Add( self.m_datePickerNgayVaoLam, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtNgayVaoLam = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtNgayVaoLam, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText11, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Phòng Ban", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gbSizer1.Add( self.m_staticText12, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		m_lstPhongChoices = ['RISK','COLLECTION','FINANCE','MARKETING','IT']
		self.m_lstPhong = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstPhongChoices, 0 )
		self.m_lstPhong.SetSelection( 0 )
		gbSizer1.Add( self.m_lstPhong, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText13, wx.GBPosition( 6, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Tên Đăng Nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gbSizer1.Add( self.m_staticText19, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtTenDangNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_txtTenDangNhap, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText20, wx.GBPosition( 7, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gbSizer1.Add( self.m_staticText14, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtMatKhau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gbSizer1.Add( self.m_txtMatKhau, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText15, wx.GBPosition( 8, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Nhập Lại MK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gbSizer1.Add( self.m_staticText16, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_txtNhapLaiMK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gbSizer1.Add( self.m_txtNhapLaiMK, wx.GBPosition( 9, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		gbSizer1.Add( self.m_staticText17, wx.GBPosition( 9, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_btnTaoTK = wx.Button( self, wx.ID_ANY, u"Tạo Tài Khoản", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_btnTaoTK.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		gbSizer1.Add( self.m_btnTaoTK, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 3 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_btnTaoTK.Bind( wx.EVT_BUTTON, self.m_btnTaoTK_click )
	
	def __del__( self ):
		pass
		
	# Virtual event handlers, overide them in your derived class
	def m_btnTaoTK_click( self, event ):
		hoTen = self.m_txtHoTen.GetValue()
		# ngaySinh = self.m_datePickerNgaySinh.GetValue()
		ngaySinh = self.m_txtNgaySinh.GetValue()
		diaChi = self.m_txtDiaChi.GetValue()
		dienThoai = self.m_txtDienThoai.GetValue()
		# ngayVaoLam = self.m_datePickerNgayVaoLam.GetValue()
		ngayVaoLam = self.m_txtNgayVaoLam.GetValue()
		phongBan = self.m_lstPhong.GetStringSelection()
		tenDangNhap = self.m_txtTenDangNhap.GetValue()
		matKhau = self.m_txtMatKhau.GetValue()
		nhapLaiMK = self.m_txtNhapLaiMK.GetValue()

		btdk = [hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap,matKhau,nhapLaiMK]
		n = 0
		for item in btdk:
			if item == '':
				n += 1

		matchNgaySinh = re.match(r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', ngaySinh, re.M|re.I)
		if matchNgaySinh:
			checkNgaySinh = True
		else:
			checkNgaySinh = False

		matchNgayVaoLam = re.match(r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', ngayVaoLam, re.M|re.I)
		if matchNgayVaoLam:
			checkNgayVaoLam = True
		else:
			checkNgayVaoLam = False

		matchMatKhau = re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', matKhau, re.M|re.I)
		if matchMatKhau:
			checkMatKhau = True
		else:
			checkMatKhau = False
		
		matchDienThoai = re.match(r'^(0)\d{9}$', dienThoai, re.M|re.I)
		if matchDienThoai:
			checkDienThoai = True
		else:
			checkDienThoai = False

		#### Thiếu thông tin
		if n > 0:
			kq = wx.MessageBox('Vui lòng nhập đủ thông tin','Thông báo', wx.OK|wx.ICON_WARNING)

		#### Sai định dạng ngày
		elif checkNgaySinh == False:
			kq = wx.MessageBox('Vui lòng nhập Ngày Sinh theo format dd/mm/yyyy','Thông báo', wx.OK|wx.ICON_WARNING)
		elif checkNgayVaoLam == False :
			kq = wx.MessageBox('Vui lòng nhập Ngày Vào Làm theo format dd/mm/yyyy','Thông báo', wx.OK|wx.ICON_WARNING)

		#### Sai định dạng điện thoại
		elif checkDienThoai == False:
			kq = wx.MessageBox('Điện thoại phải bắt đầu 0 và đủ 10 số','Thông báo', wx.OK|wx.ICON_WARNING)

		#### Sai định dạng mật khẩu
		elif checkMatKhau == False:
			kq = wx.MessageBox('Mật khẩu tối thiểu 8 ký tự.\n \
								Có ít nhất 1 ký tự viết hoa, 1 số và 1 ký tự đặc biệt (@#$%^&+=)'
								 ,'Thông báo', wx.OK|wx.ICON_WARNING)
		
		#### Sai mật khẩu nhập lại
		elif matKhau != nhapLaiMK:
			kq = wx.MessageBox('Nhập lại mật khẩu chưa đúng','Thông báo', wx.OK|wx.ICON_WARNING)
		
		#### Thông tin đủ và đúng
		elif n == 0 and matKhau == nhapLaiMK:
			xlNhanVien = ql_nhan_vien('du_lieu/qlNhanVien.db')
			DangNhap = xlNhanVien.check_ten_dang_nhap(tenDangNhap)
			if DangNhap != None:
				kq = wx.MessageBox('Tên đăng nhập này đã tồn tại','Thông báo', wx.OK|wx.ICON_WARNING)

			else:
				n = xlNhanVien.them_tai_khoan(hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap,matKhau)
				if n > 0:
					kq = wx.MessageBox('Tạo tài khoản thành công','Thông báo', wx.OK|wx.ICON_INFORMATION)
				else:
					kq = wx.MessageBox('Tạo tài khoản không thành công.\n \
										Vui lòng liên hệ quản trị viên','Thông báo', wx.OK|wx.ICON_INFORMATION)
				xlNhanVien.DeConnect()