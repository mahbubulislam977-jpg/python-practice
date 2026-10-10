# polymorphis

class vehicle:
    def __init__(self,Model,Brand,componnet,):
        self.model = Model
        self.brand = Brand
        self.componnet = componnet



class plane(vehicle):
    pass


p1 = plane("Mahbub","Mahbub12","")
print(p1.model,p1.brand,p1.componnet)
