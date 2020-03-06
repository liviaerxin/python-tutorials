# -*- coding: UTF-8 -*-
 
import wx
import wx.xrc as xrc
 
__res = None
 
 
def get_resources():
    global __res
    if __res is None:
        __init_resources()
 
    return __res
 
 
def __init_resources():
    global __res
    __res = xrc.XmlResource()
    __res.Load("gui.xrc")
 
 
class MyFrame(wx.Frame):
    def pre_create(self):
        """ クラスの初期化時に呼ばれる関数
 
        window の生成前に呼ぶべきカスタムセットアップを記述してください。
        SetWindowStyle() や SetExtraStyle() 等。
        """
        pass
 
    def __init__(self, parent):
        # 引数なしのコンストラクタを呼ぶ
        wx.Frame.__init__(self)
        self.pre_create()
        # ここで self.Create() が呼ばれる
        get_resources().LoadFrame(self, parent, "top")