import matplotlib.font_manager as mfm
import matplotlib.pyplot as plt

font_path = "./stkaiti.ttf"
prop = mfm.FontProperties(fname=font_path)
plt.text(0.5, 0.5, s=u'测试', fontproperties=prop)
plt.show()