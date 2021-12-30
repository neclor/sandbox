class Car:
    def __init__(self, brand, colour, mileage):
        self.brand = brand
        self.colour = colour
        self.mileage = mileage
        if mileage == 0:
            print("Автомобиль новый")
        else:
            print("Автомобиль бу")

    def add_mileage(self, mileage):
        if mileage >= 0:
            self.mileage = mileage
        else:
            print("Неверное число")

    def info(self):
        print("Бренд: " + self.brand + " Цвет: " + self.colour + " Пробег: " + str(self.mileage))


print("Введите бренд, цвет, пробег:")
car1 = Car(input(), input(), int(input()))
print("Сколько еще проехали?")
car1.add_mileage(int(input()))
car1.info()






            


