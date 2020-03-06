import numpy as np

import wx
import wx.lib.mixins.inspection as WIT
import wxmplot
import PIL
from PIL import Image
import numpy as np
import matplotlib.cm as cmap
import matplotlib.image as mpimg
from numpy import exp, random, arange, outer, array

def gauss2d(x, y, x0, y0, sx, sy):
    return outer( exp( -(((y-y0)/float(sy))**2)/2), exp( -(((x-x0)/float(sx))**2)/2) )


# alternatively you could use
#class App(wx.App):
class App(WIT.InspectableApp):
    def OnInit(self):
        """Create the main window and insert the custom frame."""
        self.Init()
        frame = wx.Frame(None, size=(500,400))
        
        im_panel = wxmplot.ImagePanel(frame)
        
        ny, nx = 350, 400
        x = arange(nx)
        y = arange(ny)
        ox =  x / 100.0
        oy = -1 + y / 200.0
        red  = 0.02 * random.random(size=nx*ny).reshape(ny, nx)
        red =  red + (6.0*gauss2d(x, y, 90,   76,  5,  6) +
                    3.0*gauss2d(x, y, 165, 190,  70,  33) +
                    2.0*gauss2d(x, y, 180, 100,  12,  6))
        green  = 0.3 * random.random(size=nx*ny).reshape(ny, nx)
        green = green  + (5.0*gauss2d(x, y, 173,  98,  4,  9) +
                        3.2*gauss2d(x, y, 270, 230, 78, 63))

        blue = 0.1 * random.random(size=nx*ny).reshape(ny, nx)
        blue = blue + (2.9*gauss2d(x, y, 240, 265,  78,  23) +
                    3.5*gauss2d(x, y, 185,  95,  22, 11) +
                    7.0*gauss2d(x, y, 220,  310,  40,  133))

        dat = array([red, green, blue]).swapaxes(2, 0)
        print(dat.dtype, dat.shape, dat)

        dat1 = np.array(Image.open('1.jpg'))/255.
        print(dat1.dtype, dat1.shape, dat1)

        dat2 = mpimg.imread('1.jpg')/255.
        print(dat2.dtype, dat2.shape, dat2)

        im_panel.display(dat1)
        frame.Show(True)

        return True

app = App(0)
app.MainLoop()