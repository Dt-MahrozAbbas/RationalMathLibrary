class math:
    def hcf(n1,n2):
        if n1>=n2:
            divisior=n2
            dividend=n1
        else:   
            divisior=n1
            dividend=n2
        reminder=dividend%divisior
        while  reminder!=0  :
            dividend=divisior
            divisior=reminder
            reminder=dividend%divisior
        return divisior
    staticmethod(hcf)   

 
    def lcm(n1,n2): 
        hf=math.hcf(n1,n2)
        lcm=(n1*n2)//hf
        return lcm
    staticmethod(lcm)