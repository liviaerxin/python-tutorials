#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
 
import wx
 
from gui import MyFrame
 
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()