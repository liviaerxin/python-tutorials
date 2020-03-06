#!/usr/bin/env python3

import wx
from observable import Observable

class Model:
    def __init__(self):
        self.myMoney = Observable(0)

    def addMoney(self, value):
        self.myMoney.set(self.myMoney.get() + value)

    def removeMoney(self, value):
        self.myMoney.set(self.myMoney.get() - value)


class View(wx.Frame):
    def __init__(self, parent, model):
        wx.Frame.__init__(self, parent, title="Main View")
        sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.StaticText(self, label="My Money")
        ctrl = wx.TextCtrl(self)
        sizer.Add(text, 0, wx.EXPAND | wx.ALL)
        sizer.Add(ctrl, 0, wx.EXPAND | wx.ALL)
        ctrl.SetEditable(False)
        self.SetSizer(sizer)
        self.moneyCtrl = ctrl

        self.model = model
        self.model.myMoney.addCallback(self.SetMoney)
        self.SetMoney(self.model.myMoney.get())

    def SetMoney(self, money):
        self.moneyCtrl.SetValue(str(money))


class ChangerWidget(wx.Frame):
    def __init__(self, parent, model):
        wx.Frame.__init__(self, parent, title="Main View")
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.add = wx.Button(self, label="Add Money")
        self.remove = wx.Button(self, label="Remove Money")
        sizer.Add(self.add, 0, wx.EXPAND | wx.ALL)
        sizer.Add(self.remove, 0, wx.EXPAND | wx.ALL)
        self.SetSizer(sizer)

        self.model = model
        self.add.Bind(wx.EVT_BUTTON, self.AddMoney)
        self.remove.Bind(wx.EVT_BUTTON, self.RemoveMoney)

    def AddMoney(self, evt):
        self.model.addMoney(10)

    def RemoveMoney(self, evt):
        self.model.removeMoney(10)

class Controller:
    def __init__(self, app):
        self.model = Model()
        self.view1 = View(None, self.model)
        self.view2 = ChangerWidget(self.view1, self.model)

        self.view1.Show()
        self.view2.Show()

app = wx.App(False)
controller = Controller(app)
app.MainLoop()