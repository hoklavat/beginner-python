#23- Class Object

class MyRouter(object):
    "This class describes the characteristics of a router."
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    
    def print_router(self, manuf_date):
        print("Name:", self.routername)
        print("Model:", self.model)
        print("Serial No:", self.serialno)
        print("IOS:", self.ios)
        print("Date:", manuf_date)

router1 = MyRouter("R1", "2600", "123456", "12.4")
print(router1)
print(router1.routername)
print(router1.model)
print(router1.serialno)
print(router1.ios)
router1.print_router("20181010")
setattr(router1, "routername", "R2")
print(getattr(router1, "routername"))
print(hasattr(router1, "ios"))
delattr(router1, "ios")
print(hasattr(router1, "ios"))
print(isinstance(router1, MyRouter))

class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno
        
    def print_new_router(self, string):
        print(self.model + string)

newrouter1 = MyNewRouter("newr1", "1800", "11111", "12.2", "10")
print(newrouter1.portsno)
print(newrouter1.model)
newrouter1.print_router("Non1")
newrouter1.print_new_router("Non2")
print(issubclass(MyNewRouter, MyRouter))