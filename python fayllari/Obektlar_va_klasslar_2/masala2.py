"""ko'p vorislik"""
class bobo:
    def __init__(self,x):
        self.x=x
class ota(bobo):
    def __init__(self,y):
        self.y=y
class nabira(ota):
    def __init__(self,z):
        self.z=z
bobo=bobo(1)
ota=ota(2)
nabira=nabira(3)
# bobo.x
# ota.x,ota.y
# nabira.x, nabira.y, nabira.z