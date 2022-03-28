import re
'''
A programming language  of the PydisEng
so it would look like
Game (400x400) {
      event start {
            Sprite(200,200,image.png)
      }
      event update {
            Game -sprite --image  
      }
}
'''
source = '''Game (400x400) {
      event start {
            new Sprite(200,200,|image.png|) as m
      }
      event update {
            Game [-sprite --image] 
      }
}'''
class Keyreader:
      def __init__(self,obj):
            self.sl = 0
            self.add = ''
            self.obj = ' '+obj+' '
            self.lex = []
      def pros1(self):
            pipe = 0
            while self.sl < len(self.obj):
                  num = self.obj[self.sl]
                  if num == '{':
                        self.lex+=[['braces1']]
                  if num == '}':
                        self.lex+=[['braces2']]
                  if num == '|':
                        if pipe == 0:
                              pipe = 1
                        else:
                              pipe = 0
                        if pipe == 1:
                              self.lex+=[['pipe1']]
                        else:
                              self.lex+=[['pipe2']]
                  self.intread()
                  self.sl+=1
            print(self.lex)
      def intread(self):
            digits = '1234567890.'
            num = ''
            floatp = 0
            while self.obj[self.sl] in digits:
                  
                  num+=self.obj[self.sl]
                  if self.obj[self.sl] == '.':
                        floatp+=1
                  if floatp == 2:
                        break
                  self.sl+=1
            if len(num) > 0 and not num == '.':
                  if floatp > 0:
                        self.lex+=[('FLOAT',num)]
                  else:
                        self.lex+=[('INT',num)]
      

import window

