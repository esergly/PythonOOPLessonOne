class Goods:
    def __init__(self, name, length, width, height, price):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.price = price

    def __str__(self):
        return "Goods [name = {}, size = {}, price = {}]".format(self.name, self.length, self.width, self.height,
                                                                 self.price)


class Bayer:
    def __init__(self, name, surname, age, phone, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.sex = sex

    def __str__(self):
        return "Bayer [name = {}, surname = {}, age = {}, phone = {}, sex = {}]".format(self.name, self.surname,
                                                                                        self.age, self.phone, self.sex)


class Order:
    # *order позволяет указывать переменное количество входных параметров"
    def __init__(self, *order):
        self.order = order

    def __str__(self):
        return "Order = {}".format(self.order)

    def result(*mylist):
        # Убираем служебные символы для удобства итерации по элементам"
        sum = 0
        test_list = ''
        temp = ''
        test_list = (test_list + str(mylist[0])).split(',')
        temp = (temp + test_list[0]).split("(")
        test_list[0] = temp[1]
        temp.clear()
        temp = temp + test_list[-1].split(")")
        test_list[-1] = temp[0]
        # Считаем сумму элементов не являющихся описанием.
        for i in range(len(test_list)):
            if i % 2 == 0 and i > 1: # i > "количества элементов описания покупателя"(например, не только имя, но и фамилия, номер телефона и т.д.)
                sum = sum + float(test_list[i])
        return print('Bayer ' + test_list[0] + ' ordered for ' + str(sum) + ' money units.')


bayerOne = Bayer('Ivan', 'Kravets', 30, 1234567, 'male')
bayerTwo = Bayer('Sveta', 'Kostakis', 22, 5556677, 'female')
bayerThree = Bayer('Katya', 'Taran', 27, 7658765, 'female')
box = Goods('Box for pizza', 70, 45, 10, 10)
envelope = Goods('Envelope for mail', 15, 10, 0.1, 7)
stamp = Goods('Stamp', 5, 3, 0.1, 0.5)
order_one = Order(bayerOne.name, stamp.name, stamp.price, box.name, box.price)
order_two = Order(bayerTwo.name, stamp.name, stamp.price, envelope.name, envelope.price, box.name, box.price)

print(order_one)
print(order_two)
print()
print(bayerOne)
print(bayerTwo)
print(bayerThree)
print()
print(box)
print(envelope)
print(stamp)
print()
Order.result(order_one)
Order.result(order_two)
