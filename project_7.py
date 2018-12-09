print("Вам предоставляется возможность забронировать билеты на авиарейс по следующим направлениям:")
print("Москва, Астана, Лондон, Берлин, Мадрид, Вашингтон, Рим \n")

list_of_directions = ["москва", "астана", "лондон", "берлин", "мадрид", "вашингтон", "рим"]

list_of_month = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

moscow = [list_of_month, ["01", "04", "05"], 'FobosAir', 'MOSCOW, RUSSIA']
astana = [list_of_month, ["01", "04", "05"], 'KazAir', 'ASTANA, KAZAKHSTAN']
london = [list_of_month, ["01", "04", "05"], 'Aeroplane', 'LONDON, UK']
berlin = [list_of_month, ["01", "04", "05"], 'Aeroplane', 'BERLIN, GERMANY']
madrid = [list_of_month, ["01", "04", "05"], 'FobosAir', 'MADRID, SPAIN']
washington = [list_of_month, ["01", "04", "05"], 'AmericanAirlines', 'WASHINGTON DC, USA']
roma = [list_of_month, ["01", "04", "05"], 'FobosAir', 'ROMA, ITALY']

direction = input("Введите направление полета: ").lower()
while direction not in list_of_directions:
    direction = input("Вы ввели недоступное направление. Пожалуйста, повторите попытку: ").lower()

if direction == "москва":
    direction = moscow
elif direction == "астана":
    direction = astana
elif direction == "лондон":
    direction = london
elif direction == "берлин":
    direction = berlin
elif direction == "мадрид":
    direction = madrid
elif direction == "вашингтон":
    direction = washington
else:
    direction = roma

month = input("Введите месяц отправения. Например: 01 (январь): ")
while int(month) > 12:
    month = input("Вы неверно ввели месяц. Повторите попытку. Пример: 02, 10 ")

print()
print("Доступны билеты по следующим датам: ")
a = direction[1][0] + "." + month
b = direction[1][1] + "." + month
c = direction[1][2] + "." + month
print("1)", a, " 2)", b, " 3)", c)

choose = input("Выберите подходящую дату и введите ее порядковый номер (1, 2, 3): ")
if choose == "1":
    date = a
elif choose == "2":
    date = b
elif choose == "3":
    date = c

while 0 > int(choose) > 3:
    choose = input("Вы ввели неверное число. Пожалуйста, повторите попытку: ")
    if choose == "1":
        date = a
    elif choose == "2":
        date = b
    elif choose == "3":
        date = c

name = input("Пожалуйста, введите свое ФИО через пробел: ")

# Ticket
print()
print("Распечатайте билет.")
print()
print("-"*100)
print("| Airline: {} {:>70}".format(direction[2], "Boarding Pass/Посадочный талон"))
print("|")
print("| Passenger/Пассажир: {:>10}".format(name))
print("| Flight/Рейс: 0215")
print("| Date/Дата: {}".format(date))
print("| To: ---> {} --- ".format(direction[3]))
print("-"*100)
