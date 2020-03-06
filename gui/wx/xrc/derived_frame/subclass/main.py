#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
import wx
import wx.xrc as xrc
 
 
if __name__ == "__main__":
    app = wx.App(False)
 
    # 以下の処理を wx.App を継承したクラスに書いてあるものが多いが、見やすさ重視で
    res = xrc.XmlResource("gui.xrc")
    frame = res.LoadFrame(None, "top")
    frame.Show()
 
    app.MainLoop()