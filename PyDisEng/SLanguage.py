p = """Window{Window[(400,400)]}

start:display.Sprite{a[200,200,"ball.png"]}
start:keys.init{n[window]}
update:a{draw[window]}
update:a{addpos[self.a,2,2]}
package:window{update['func']}
"""

a = p.split('\n')
py = 'import PyDisEng\n'
py+=f'''def x(self,a,b,):
      self.x=a
      self.y=b
def y(self,a=0,b=0):

      self.x+=a
      self.y+=b
'''
f = 0
f1 = 0
for t in a:
      event = ''
      command = ''
      param1 = ''
      param2 = ''
      ov = 0
      ov1 = 0
      ov2 = 0
      ov3 = 0
      for o in t:
            if ov == 0 and (t != a[0]):
                  event+=o if ':' not in event else ''
            
      
            elif ov1 == 0:
                  command+=o if '{' not in command else ''
            elif ov2 == 0:
                  param1+=o if '[' not in param1 else ''
            elif ov3 == 0:
                  param2+=o if ']' not in param2 else ''
            if ':' in event:
                  ov = 1
                  event = event[:-1]
            if '{' in command:
                  ov1 = 1
                  command = command[:-1]
            if '[' in param1:
                  ov2 = 1
                  param1 = param1[:-1]
            if (']' in param2 or '}' in param2):
                  ov2 = 1
                  param2 = param2[:-1]
      #print('"'+command+'"')
      print(event,command)

      if command != '':
            
            
                  
                  
            if event == 'start':
                  if f == 0:
                        f=1
                        py+=f'      def {event}(self):\n'
                  py+=f'            self.{param1} = PyDisEng.{command}({param2})\n'
                  
                  
                  py+=f'            if type(self.{param1}) in [PyDisEng.display.Rect,PyDisEng.display.Sprite]:self.{param1}.pos = x\n'
                  py+=f'            if type(self.{param1}) in [PyDisEng.display.Rect,PyDisEng.display.Sprite]:self.{param1}.addpos = y\n'
                  py+=f'            #print(self.{param1}.__dict__)\n'
                  
            elif event == 'update':
                  if f1 == 0:
                        f1=1
                        py+=f'      def {event}(self):\n'
                  py+=f'            self.{command}.{param1}({param2},)\n'
            else:
                  if command == 'window':
                        py+=f'{command}.update(App,{param2})'
                  elif command == 'Window':
                        py+=f'window=PyDisEng.{command}.{param1}({param2})\n'
                        py+=f'class App:\n'

del a
del f
del f1
print(py)
exec(py)
