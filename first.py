class raja:
    
    def __init__(self):
        self.salary=20000
        self.package=2
        self.designation='ds'
        print("you good man")
    
    def location(self,locate):
        self.locate=locate
        return self.locate

abhi=raja()

print(abhi.location("nepal"))