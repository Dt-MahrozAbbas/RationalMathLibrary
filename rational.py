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
    def rec(f):
        r=rational()
        r.__nm=f.__dn
        r.__dn=f.__nm 
        return r
    staticmethod(simplify_rational)
    def add(f1,f2):
        r=rational()
        d1=f1.__dn
        d2=f2.__dn
        n1=f1.__nm
        n2=f2.__nm
        lm=math.lcm(d1,d2)
        lm_div_d1=lm//d1
        lm_div_d2=lm//d2
        r_nm=(lm_div_d1*n1)+(lm_div_d2*n2)
        if r_nm==0:
            return 0
        r.__nm=r_nm
        r.__dn=lm
        return r.simplify_rational()#it way to call a function without static method , invoke the function we write the any argument at the first
    staticmethod(add)
    def diff(f1,f2):
        r=rational()
        d1=f1.__dn
        d2=f2.__dn
        n1=f1.__nm
        n2=f2.__nm
        lm=math.lcm(d1,d2)
        lm_div_d1=lm//d1
        lm_div_d2=lm//d2
        r_nm=(lm_div_d1*n1)-(lm_div_d2*n2)
        if r_nm==0:
            return 0
        r.__nm=r_nm
        r.__dn=lm
        return r.simplify_rational()
    staticmethod(diff)
    def multiply(f1,f2):
        m=rational()
        m.__nm=f1.__nm*f2.__nm
        m.__dn=f1.__dn*f2.__dn
        return m.simplify_rational()
    def divide(f1,f2):
        rc=f2.rec()
        d=rational()
        d.__nm=f1.__nm*rc.__nm
        d.__dn=f1.__dn*rc.__dn
        return d.simplify_rational()
r=rational(15,30)    
r2=rational(4,36)
print(r)
print(r2)
d=rational.divide(r,r2)
# m=rational.multiply(r,r2)
# dif=rational.diff(r,r2)
# add=rational.add(r,r2)
print(d)    
# print(m)    
# print(dif)    
# print(add)    
