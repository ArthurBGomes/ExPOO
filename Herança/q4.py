class Forma:
    def area(self):
        return 0
class Retangulo(Forma):
    def area(self,largura,altura):
        return altura * largura 
f1 = Forma()
print(f1.area(),"CM²")
r1 = Retangulo()
print(r1.area(10,5),"CM²")