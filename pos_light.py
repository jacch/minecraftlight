#!/usr/bin/python
from mcpi.minecraft import Minecraft
import time,os
mc = Minecraft.create('192.168.1.113',4717)

class mic:
    x=0
    y=0
    z=0
    u=1
    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        print self.u

    def playerpostion(self):
        x,y,z=mc.entity.getPos(self.u)
        self.x=x
        self.y=y
        self.z=z
        print x,y,z

    def getblockinfo(self,x,y,z):
        p=mc.getBlockWithData(x,y,z)
        return p

    def getblockinfo1(self):
        print self.x
        p=mc.getBlockWithData(self.x,self.y-1,self.z)
        print p



        
m=mic()
#m.playerid('jacch')

while True:
    block=m.getblockinfo(-0.64,-22,-87.8)
    print block
    if block.id==29 and block.data==10:
        os.system('/home/pi/kiki-minecraft/kiki-minecraft/lighton.py')
    else:
        os.system('/home/pi/kiki-minecraft/kiki-minecraft/lightoff.py')
        print "off"

    time.sleep(3)

