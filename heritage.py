class Animal:
    def __init__(self,name,espece):
        self.nom = name
        self.espece= espece

class Chat(Animal):
    def __init__(self,name):
        Animal.__init__(self,name,"Chat")
        self.cri="miaule"

#main
monChat = Chat("Link")


input()