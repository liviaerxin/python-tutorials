from os import path
import PIL
from PIL import Image
import matplotlib.image as mpimg

import wxmplot.interactive as wi

thisdir, _ = path.split(__file__)

#imgdata =  Image.open(path.join(thisdir, '1.jpg'))
imgdata =  mpimg.imread(path.join(thisdir, '1.jpg'))

wi.imshow(imgdata, contrast_level=0.1, colormap='coolwarm')