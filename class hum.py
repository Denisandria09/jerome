#
class Human:
    def __init__(self,name,occupation):
       self.name=name
       self.occupation=occupation
       
    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots film")
            
    def speaks(self):
        print(self.name,"says nice to meet you")
        
B=Human("Tom Holland","actor")
B.do_work()
B.speaks()