from audioop import error

import wx,random
lst=['会赢的','别太赶了','别想了','不要抱期望','这是必然的，不要抗拒','不要浪费精力','不用担心','大胆一点','放轻松，慢慢来','好运将会降临','会付出代价','肯定的','结果可能让人惊讶','会特别顺利','会后悔的','会很不顺利','全力以赴','认清现实吧','奇迹即将降临','要主动','不会后悔的','需要冒险','三思而后行','尚待时日','省点力气吧','时机未到','答案就在你身边','会感到庆幸','不然呢？','持之以恒']
class Myframe(wx.Frame):
    def __init__(self,name):
        wx.Frame.__init__(self, None, -1, name, size=(400, 400))
        self.panel = wx.Panel(self)
        self.box = wx.BoxSizer(wx.VERTICAL)
        self.fgz = wx.FlexGridSizer(wx.HSCROLL)
        botton1 = wx.Button(self.panel, pos=(0, 300), size=(400, 100), label='开始游戏')
        self.fgz.Add(botton1, 0, wx.ALIGN_CENTER_VERTICAL)
        self.show_text = wx.TextCtrl(self.panel, size=(400, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.box.Add(self.show_text, 0, wx.ALIGN_CENTER)
        self.box.Add(self.fgz, 0, wx.ALIGN_CENTER)
        self.panel.SetSizer(self.box)
        self.Bind(wx.EVT_BUTTON,self.start,botton1)
        self.showdata='游戏规则'
        self.show_text.AppendText(self.showdata)


    def start(self,event):
        self.dig=dialog(None,'答案之书')
        self.dig.ShowModal()
        self.dig.Destroy()
class App(wx.App):
    def __init__(self):
        super(App,self).__init__()
        self.frame=Myframe('答案之书')
        self.frame.Show()
class dialog(wx.Dialog):
    def __init__(self,parent,title):
        super(dialog,self).__init__(parent,style=wx.DEFAULT_DIALOG_STYLE,size=(600,600))
        self.app=wx.App()
        self.panel2=wx.Panel(self)
        self.box2=wx.BoxSizer(wx.VERTICAL)
        self.fgz2=wx.FlexGridSizer(wx.HSCROLL)
        self.botton2=wx.Button(self.panel2,pos=(0,400),size=(600,200),label='获取答案')
        self.show_text2=wx.TextCtrl(self.panel2,size=(600,200),pos=(0,200),style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.show_text3=wx.TextCtrl(self.panel2,size=(600,200),pos=(0,0),style=wx.TE_MULTILINE)
        self.fgz2.Add(self.botton2,0,wx.ALIGN_CENTER_VERTICAL)
        self.box2.Add(self.show_text2,0,wx.ALIGN_CENTER)
        self.box2.Add(self.show_text3, 0, wx.ALIGN_CENTER)
        self.box2.Add(self.fgz2,0,wx.ALIGN_CENTER)
        self.panel2.SetSizer(self.box2)
        self.Bind(wx.EVT_BUTTON,self.play,self.botton2)
        self.showdata='请输入您的问题'
        self.show_text3.AppendText(self.showdata)
        self.judge()

    def play(self,event):
        num=random.choice(lst)
        self.show_text2.AppendText(num)
    def judge(self):
        num2='请先输入您的问题'
        if self.show_text3==self.showdata:
            self.show_text2.AppendText(num2)



if __name__ == '__main__':
    name='开始界面'
    app=wx.App()
    frame=Myframe(name)
    frame.Show()
    app.MainLoop()
