from . import Window
x = 0
y = 0
Down = [False,False,False]
def get_pos(binder):
      global x
      global y
      x = binder.x
      y = binder.y
def set_down(binder,m=0):
      global Down
      Down[m] = True
def set_up(binde,m=0):
      global Down
      Down[m] = False
def set_down1(binder,m=1):
      global Down
      Down[m] = True
def set_up1(binde,m=1):
      global Down
      Down[m] = False
def set_down2(binder,m=2):
      global Down
      Down[m] = True
def set_up2(binde,m=2):
      global Down
      Down[m] = False
def init(win):
      '''Initalizes the mouse
      :win | window to use
      '''
      win.owindow.bind('<Motion>',get_pos)
      win.canvas.bind("<Button-1>", set_down)
      win.canvas.bind('<ButtonRelease-1>', set_up)
      win.canvas.bind("<Button-2>", set_down1)
      win.canvas.bind('<ButtonRelease-2>', set_up1)
      win.canvas.bind("<Button-3>", set_down2)
      win.canvas.bind('<ButtonRelease-3>', set_up2)
