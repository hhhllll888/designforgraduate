
import wx
import wx.xrc

m_PickImg1 = 1000

###########################################################################
## Class Main_ui
###########################################################################


class Main_ui ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"图片分类系统", pos = wx.DefaultPosition, size = wx.Size( 640,575 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		Img_label = wx.FlexGridSizer( 0, 2, 8, 8 )
		Img_label.SetFlexibleDirection( wx.VERTICAL )
		Img_label.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"选择图片" ), wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.file_picker = wx.FilePickerCtrl( sbSizer4.GetStaticBox(), m_PickImg1, wx.EmptyString, u"选择你的文件", u"*.jpg;*.png", wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST, wx.DefaultValidator, u"浏览文件" )
		self.file_picker.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		fgSizer3.Add( self.file_picker, 0, wx.ALL, 5 )

		self.predict_but = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"识别图片", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.predict_but.Enable( False )

		fgSizer3.Add( self.predict_but, 0, wx.ALL, 5 )


		sbSizer4.Add( fgSizer3, 0, 0, 5 )

		self.image_show = wx.StaticBitmap( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.image_show.SetMinSize( wx.Size( 300,200 ) )

		sbSizer4.Add( self.image_show, 0, 0, 5 )


		Img_label.Add( sbSizer4, 0, 0, 1 )

		show_result = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"图像识别结果" ), wx.VERTICAL )

		self.result_Text = wx.StaticText( show_result.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.result_Text.Wrap( -1 )

		show_result.Add( self.result_Text, 0, wx.ALL, 5 )


		Img_label.Add( show_result, 1, wx.TOP|wx.LEFT|wx.EXPAND, 5 )


		bSizer4.Add( Img_label, 1, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )

		Log_show = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"日志" ), wx.VERTICAL )

		self.log_text = wx.TextCtrl( Log_show.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE|wx.TE_READONLY )
		Log_show.Add( self.log_text, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( Log_show, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()
		self.MenuBar = wx.MenuBar( 0 )
		self.help_but = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.help_but, wx.ID_ANY, u"帮助", wx.EmptyString, wx.ITEM_NORMAL )
		self.help_but.Append( self.m_menuItem1 )

		self.MenuBar.Append( self.help_but, u"帮助" )

		self.SetMenuBar( self.MenuBar )


		self.Centre( wx.HORIZONTAL )

		# Connect Events
		self.file_picker.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_file_pick )
		self.predict_but.Bind( wx.EVT_BUTTON, self.on_predict_but )
		self.Bind( wx.EVT_MENU, self.show_help, id = self.m_menuItem1.GetId() )
class help_windows ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"帮助", pos = wx.DefaultPosition, size = wx.Size( 250,311 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"这个是一个专科的毕业设计作业，只要在界面中选择文件的地方选择使用你的文件，然后点识别图片即可\n组长：高星\n组员：陆子健，孙广凡，刘俊豪，孙海洋", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer3.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.out )