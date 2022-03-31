class Pobject:
      def __init__(self,Kin,Sprite):
            '''
            Makes a pysical object
            :Kin | Kinetic Energy used for moving stuff
            :Sprite | Sprite for operating on 
           ::Pos | Positinal energy from Sprite pos (y is reversed so a higher pos is higher pos energy)
            '''
            self.OrigKin = Kin
            self.Sprite = Sprite
            self.Pos = (Sprite.x,Sprite.y)
            self.Kin = Kin
            self.PastKinVal =self.Kin
      def loop(self,window,isKin=True,pysobject=[]):
            '''Loops through the pyshical object
            :isKin | defaults to True if False must be directly moved
            '''
            
            self.Pos = (self.Sprite.x,self.Sprite.y)
            p = self.Pos
            self.Pos = list(self.Pos)
            self.Pos[0] +=self.Kin[0]
            self.Pos[1] +=self.Kin[1]
            
            try:self.Kin[1]-=1*self.Kin[1]/abs(self.Kin[1])
            except:pass

            try:self.Kin[0]-=1*self.Kin[0]/abs(self.Kin[0])
            except:pass
            self.Pos = tuple(self.Pos)
            self.Sprite.x,self.Sprite.y = self.Pos
            #check_distances = () #checks the closes distances (only if object is Kinetic)
            for thing in pysobject:
                  if self.Sprite.collide(thing):
                        Sprite.x,Sprite.y = p
            self.Sprite.draw(window)
            
