class Hero:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        
    def sleep(self,hours):
        print(f'{self.name}は{hours}時間寝た')
        self.hp+=hours

print('はじまり')
h=Hero('松田',100)
h.sleep(3)
print(f'{h.name}のhpは現在{h.hp}です')
