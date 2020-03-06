# -*- coding: UTF-8 -*-
 
import wx
import wx.xrc as xrc
 
 
class MyFrameXmlHandler(xrc.XmlResourceHandler):
    def CanHandle(self, node):
        # DoCreateResource を呼ぶ条件を指定
        # 今回の場合、wxFrame だけで大丈夫だが、現実的には名前のチェックも入れたほうが良い
        return self.IsOfClass(node, "wxFrame") and node.GetAttribute("name") == "top"
 
    def DoCreateResource(self):
        frame = MyFrame(None)
        # XML から子クラスを生成してぶらさげる
        self.CreateChildren(frame)
        return frame
 
 
class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
 
        # window create されてからリソースアクセスするためにイベント登録
        self.Bind(wx.EVT_WINDOW_CREATE, self._on_create)
 
    def _on_create(self, event):
        self.button = xrc.XRCCTRL(self, "button")
        self.button.Bind(wx.EVT_BUTTON, self._on_click)
 
    def _on_click(self, event):
        print("clicked")