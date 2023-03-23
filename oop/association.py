"============================Ассоциация======================================"
#Ассоциация - принцип ООП, в котором два класса друг с другом связаны
# ассоциация делится на 2 принципа
# 1 - агрегация (более слабая связь)
# 2 - композиция (более сильная связь)

class Battery:
    power = 100

    def charge(self):
        if self.power <100:
            self.power = 100
            return self.power

class Iphone:
    def __init__(self,color):
        self.color = color
        self.battery = Battery()
        # в этот момент когда мы создаем обьект от другого класса прям внутри другого - композиция

# iphone = Iphone('gold')
# iphone.battery.power=50
# print(iphone.battery.power)
# print(iphone.battery.charge())
# # del iphone
# print(iphone)

class Nokia:
    def __init__(self,color,battery):
        self.color = color
        self.battery = battery
        # когда ммы принимаем уже созданный вне класса обьект - агрегация

# battery = Battery
# nokia = Nokia('black', battery) #передаем в обьект другой обьект
# print(nokia.battery.power)
# del nokia #удаляет только обьект nokia, обьект батарейки остается
# print(battery.power)