#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
import wx
import wx.xrc as xrc
 
 
if __name__ == "__main__":
    app = wx.App(False)
 
    res = xrc.XmlResource("gui.xrc")
 
    # ここで InsertHandler を呼ぶのがポイント
    res.InsertHandler(MyFrameXmlHandler())
 
    frame = res.LoadFrame(None, "top")
    frame.Show()
 
    app.MainLoop()