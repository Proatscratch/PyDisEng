class Pobject:
      def __init__(self,Kin,Sprite):
            '''
            Makes a pysical object
            :Kin | Kinetic Energy used for moving stuff
            :Sprite | Sprite for operating on 
            ::Mech | Sum of Kinetic Energy and Positional energy
            ::Pos | Positinal energy from Sprite pos (y is reversed so a higher pos is higher pos energy)
            '''
            self.Sprite = Sprite
            self.Pos = (Sprite.x,Sprite.y)
            self.Kin = Kin
      def loop(self,isKin=True):
            '''Loops through the pyshical object
            :isKin | defaults to True if False must be directly moved
            '''
            self.mech = self.Pos[0]+self.Kin[0],self.Kin[1]+self.Pos[1]
            self.Pos = (Sprite.x,Sprite.y)
            self.Pos = list(self.Pos)
            self.Pos[0] +=self.Kin[0]
            self.Pos[1] +=self.Kin[1]
            self.Pos = tuple(self.Pos)
            check_distances = () #checks the closes distances (only if object is Kinetic)
            if isKin:
                  pass
