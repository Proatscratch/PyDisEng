from . import *

window = Window.Window((300,300),30)
class App:
      def start(self):
            self.a = display.Sprite(150,150,'Ball.png')
            self.b = display.Sprite(165,165,'Ball.png')
            self.a.scale(100,100)
            mouse.init(window)
            keys.init(window)
      def update(self):
            
            display.fill(window,(255,255,255))
            self.a.rotate(90)
            keys.key = ''
            print(keys.keypressed)
                  
            self.a.draw(window)
            #self.b.draw(window)
            #aa = self.a.collide(self.b)
            
            
window.update(App)
