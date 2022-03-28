from . import Window
import PIL
import PIL.ImageTk
from PIL import Image
import sys

def rth(rgb):
    return '#'+'%02x%02x%02x' % rgb
class Rect:
      def __init__(self,x,y,w,h):
            '''
            makes a new rectangle
		:x | x position
            :y | y position
            :w | width
            :h | height
            '''
            self.x,self.y,self.w,self.h = x,y,w,h
      def __repr__(self):
            '''
            for debugging positions
            '''
            return f"Rect({self.x},{self.y},{self.w},{self.h})"
      def draw(self,window,color = (0,0,0,)):
            '''
            Draws a rectangle
            :window | displays a rectangle on this
            :color | sets the color of the rectangle
            '''
            window.canvas.create_rectangle(self.x,self.y,self.x+self.w,self.y+self.h,fill = rth(color))    
      def collide(self, secr):
            '''
            Checks collisions with another rectangle
            :secr | checks collision with this
            '''
            return self.x < secr.x+secr.w and secr.x < self.x+self.w and self.y < secr.y+secr.h and secr.y < self.y+self.h

def fill(window,color = (0,0,0,)):
      '''
            Draws a rectangle
            :window | fills the display
            :color | sets the color of the rectangle
      '''
      a = Rect(0,0,10000,10000)
      a.draw(window,color)

class Sprite():
      def __init__(self,x,y,i):
            '''
            Makes an new sprite
            :x | x position
            :y | y position
            :i | image
            '''
            self.i = Image.open(i)
            #self.w = w
            self.img = PIL.ImageTk.PhotoImage(PIL.Image.open(i))
            self.w,self.h = self.i.size
            self.x,self.y = x,y
      def set_image(self,i):
            '''
            Used if you want to change the image
            :i | the image to change to
            '''
            self.i = Image.open(i)
            self.img = PIL.ImageTk.PhotoImage(PIL.Image.open(i))
            self.w,self.h = self.i.size
      def draw(self,window):
            '''
            draws the sprite
            :window | window to draw the sprite
            '''
            x,y = self.x,self.y
            window.canvas.create_image(x, y, anchor='nw', image=self.img)
      def get_image(self):
            '''
            gets the image
            '''
            return self.i
      def collide(self,o,):
            '''
            does pixel perfect collisions by reading the images converting them to rectangles and checks collisions between them WARNING: might be laggy
            :o | object to check collisions with
            '''
            im = self.i # Can be many different formats.
            pix = im.load()
            w,h = im.size
            mw = 0
            mh = 0
            rectangle1 = []
            self.rect = Rect(self.x,self.y,w,h)
            self.rect2 = Rect(o.x,o.y,o.w,o.h)
            if not self.rect.collide(self.rect2):
                return False
            for t in range(w*h):
                  if mw > w:
                        mw = 0
                        mh+=1
                  if mh > h:
                        mh = 0
                  try:
                        if not pix[mw,mh+1] == (0,0,0,0):
                              pix[mw,mh+1] = (255,0,0)  # Set the RGBA Value of the image (tuple)
                              rectangle1.append(Rect(mw+self.x,mh+self.x,1,1))
                  except IndexError:pass
                  try:
                        if not pix[mw,mh+1][3] == 0:
                              pix[mw,mh-1] = (255,0,0)  # Set the RGBA Value of the image (tuple)
                              rectangle1.append(Rect(mw+self.x,mh+self.y,1,1))
                  except IndexError:pass
                  mw+=1

                  
            im = o.i # Can be many different formats.
            pix = im.load()
            w,h = im.size
            mw = 0
            mh = 0
            rectangle2 = []
            for t in range(w*h):
                  if mw > w:
                        mw = 0
                        mh+=1
                  if mh > h:
                        mh = 0
                  try:
                        if not pix[mw,mh+1] == (0,0,0,0):
                              pix[mw,mh+1] = (255,0,0)  # Set the RGBA Value of the image (tuple)
                              rectangle2.append(Rect(mw+o.x,mh+o.x,1,1))
                  except IndexError:pass
                  try:
                        if not pix[mw,mh+1][3] == 0:
                              pix[mw,mh-1] = (255,0,0)  # Set the RGBA Value of the image (tuple)
                              rectangle2.append(Rect(mw+o.x,mh+o.y,1,1))
                  except IndexError:pass
                  mw+=1
            for op in rectangle1:
                  for opp in rectangle2:
                        if op.collide(opp):
                              return True
            return False
      def scale(self,w,h):
            '''
            scales the image
            :w | width to scale image to
            :h | height to scale image to
            '''
            i = self.i
            self.i = i.resize((w, h))
            self.img = PIL.ImageTk.PhotoImage(self.i)
            self.w,self.h = self.i.size
      def rotate(self,degrees):
            '''
            rotates the image
            :degrees | rotates the image to this WARNING: if rotating look weirds make the value closer to multiples of 45
            '''
            #[2,4,8,16,32,64,128,256,512,1024,2048] sorry just playing easy 2048
            i = self.i
            self.i = i.rotate(degrees)
            self.img = PIL.ImageTk.PhotoImage(self.i)
            self.w,self.h = self.i.size
      def __repr__(self):
            '''
            for debugging positions
            '''
            return f"Image({self.x},{self.y},{self.i})"
            
