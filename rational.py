from lcm_hcf import *
class rational:
    def __init__(self,nm=1,dn=1):
        self.__nm =nm
        self.__dn=dn
    def __str__(self):
        fraction=''
        fraction += str(self.__nm)
        fraction += str('/')
        fraction += str(self.__dn)
        return fraction
    def simplify_rational(f):
        s=rational()
        n=f.__nm
        d=f.__dn
        h=math.hcf(n,d)
        s.__nm=n//h
        s.__dn=d//h
        return s