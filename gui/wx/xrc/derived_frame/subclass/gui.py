# -*- coding: UTF-8 -*-
 
import wx
import wx.xrc as xrc
 
 
class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
 
        # window create イベント登録
        self.Bind(wx.EVT_WINDOW_CREATE, self.on_create)
 
    def on_create(self, event):
        # window create 後でないとリソースへのアクセスはできない
        self.button = xrc.XRCCTRL(self, "button")
        self.button.Bind(wx.EVT_BUTTON, self.on_click)
 
    def on_click(self, event):
        print("clicked")