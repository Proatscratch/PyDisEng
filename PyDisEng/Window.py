import tkinter
import threading
class UnExistentEventError(Exception):
      pass

class Window:
      def __init__(self,windowSize,fps = 1000):
            '''makes a window
            :windowSize | sets the size of the window
            '''
            self.dim = f'{windowSize[0]}x{windowSize[1]}'
            self.w = windowSize[0]
            self.h = windowSize[1]
            self.windowStatus = 1
            self.fps = fps
            
      def update(self,cl,name='PyDisEng Window',isResizeAble = (False,False)):
            '''updates the window, WARNING: code will have a delay of 1 ms otherwise window won't show ANOTHER WARNING: code won't run if fps > 1000
            :cl | the class that updates
            :isResizeAble | makes the window resizeables default to false
            '''
            #code will have a delay of 1 ms otherwise window won't show
            game = cl()
            
            if (hasattr(game,'__init__') and len(vars(game)) > 0):
                  raise UnExistentEventError('__init__ is not an event')
            self.windowStatus = 1
            print(game)
            self.owindow = tkinter.Tk()
            self.owindow.geometry(self.dim)
            self.canvas = tkinter.Canvas(self.owindow, width=10000, height=10000)
            def r():
                self.owindow.after(int(1000/self.fps),func2)
            def r2():
                  try: game.song()
                  except: pass
            def func2():
                  #print(1000/self.fps)
                  
                  
                  game.update()
                  t1 = threading.Thread(target = r)
                  t2 = threading.Thread(target = r2)
                  t1.start()
                  t2.start()
                  
                  
                  
            def func1():
                  w = 1
                  
                  
                  
                  
                  eval(f'self.owindow.resizable'+str(isResizeAble))
                  
                  self.owindow.title(name)
                  self.canvas.pack()
                  self.owindow.after(1,func2)
                  self.owindow.mainloop()
                  self.windowStatus = 0
            game.start()
            func1()
            
if __name__ == '__main__':
      window = Window((200,200))
      
      class Game:
            def start():
                  print("A")
            def update():
                  print("B")

      window.update(Game)
