import time
import threading
#key = ''
key = {'a':False,'b':False,'c':False,
       'd':False,'e':False,'f':False,
       'g':False,'h':False,'i':False,
       'j':False,'k':False,'l':False,
       'm':False,'n':False,'o':False,
       'p':False,'q':False,'r':False,
       's':False,'t':False,'u':False,
       'v':False,'w':False,'x':False,
       'y':False,'z':False,'Up':False,
       'Down':False,'Right':False,'Left':False}

def down(e):
      global key
      if e.char != '':
            key[e.char] = True
      else:
            key[e.keysym] = True
           
            

def up(e):
      global key
      if e.char != '':
            key[e.char] = False
      else:
            key[e.keysym] = False
def set_lk(e):
      global arrowkeys
      arrowkeys['LEFT'] = True
def set_rk(e):
      arrowkeys['RIGHT'] = True
def set_uk(e):
      arrowkeys['UP'] = True
def set_dk(e):
      arrowkeys['DOWN'] = True
      
def set_lk2(e):
      global arrowkeys
      arrowkeys['LEFT'] = False
def set_rk2(e):
      arrowkeys['RIGHT'] = False
def set_uk2(e):
      arrowkeys['UP'] = False
def set_dk2(e):
      arrowkeys['DOWN'] = False
def set_key(keyobj):
      global keypressed
      key = keyobj
      keypressed = False
def init(window):
      '''Initalizes a key
      :window | key to use
      '''
      window.owindow.bind('<KeyPress>', down)
      window.owindow.bind('<KeyRelease>', up)

      

   
      
