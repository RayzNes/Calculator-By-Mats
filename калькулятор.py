import math
import random

print("""
  _    _      _ _       
 | |  | |    | | |      
 | |__| | ___| | | ___  
 |  __  |/ _ \ | |/ _ \ 
 | |  | |  __/ | | (_) |
 |_|  |_|\___|_|_|\___/ 
                        
                        
""")
def main():
    while True:
        multiline_string = """Что бы умножать, делить числа и т.д введите 1;
        Что бы работать с сантиметрами, метрами и т.д введите 2;
        Что бы работать с кг и граммами и т.д введите 3;
        Что бы проверить делиться ли число без остатка введите 4;
        Что бы перевести рубли в доллары и т.д введите 5;
        Что бы преобразовать фаренгейты в цельсии и наоборот введите 6;
        Что бы перейти в режим нахождения скорости, плотности, расстояния и т.д введите 7;
        Что бы конвертировать биты в байты и т.д введите 8;
        Что бы вывести число пи с точностью до 16 чисел введите 9;
        Что бы вывести таблицу умножения для числа введите 10;
        Что бы найти среднее арифметичское введите 11;
        Что бы сортировать числа введите 12;
        Что бы найти квадратный корень числа введите 13;
        Что бы найти синус, косинус или тангенс введите 14;
        Что бы вывести число e с точностью до 16 чисел введите 15;
        Что бы найти арксинус, арккосинус и арктангенс введите 16;
        Что бы показывать сколькими способами можно выбрать объектов из набора введите 17;
        Что бы вычислить факториал введите 18;
        Что бы перейти в режим рандомайзера введите 19;
        для информации введите инфо."""
        print(multiline_string)
        otvet = input().lower()
        if otvet in['инфо']:
            info()
        if otvet in ["1"]:
            base()
        elif otvet in["2"]:
            centimeters()
        elif otvet in["3"]:
            kilograms()
        elif otvet in["4"]:
            remains()
        elif otvet in["5"]:
            dollar()
        elif otvet in["6"]:
            farengeit()
        elif otvet in["7"]:
            physics()
        elif otvet in["8"]:
            bit()
        elif otvet == "9":
           print(f"Число пи = {math.pi}")
        elif otvet == "10":
            table()
        elif otvet == "11":
            numbers_str = input("Введите числа через пробел: ")
            try:
                numbers = [int(x) for x in numbers_str.split()]
                result = arithmetic_mean(numbers)
                if result is not None:
                    print(f"Среднее арифметическое: {result}")
                else:
                    print("Пустой ввод")
            except ValueError:
                print("Вы ввели некорректные числа!")
        elif otvet == "12":
            sorter()
        elif otvet == "13":
            root()
        elif otvet == "14":
            cosine()
        elif otvet == "15":
            print(f"Число е = {math.e}")
        elif otvet == "16":
            arcsinus()
        elif otvet == "17":
            set()
        elif otvet == "18":
            factorial()
        elif otvet == "19":
            randomai()
        elif otvet in["Бакунята"]:
            print("збозйпа со огтйфоцйю бозхолго!")
        else:
            pass
def info():
    print("""  _____        __      
 |_   _|      / _|     
   | |  _ __ | |_ ___  
   | | | '_ \|  _/ _ \ 
  _| |_| | | | || (_) |
 |_____|_| |_|_| \___/ 
                       
                       """)
    print("Calculator by Mats")
    print('Версия: 1.3.9  от 05.12.24')
    print("Версия Python: 3.13.0")
    print("Последнее обновления курса: 02.12.24")
def base():
    while True:
        kaz1_str = input("Введите первое число: ")
        kaz2_str = input("Введите второе число: ")
        oper = input("Введите операцию (+, -, *, /, для возведения в степень **, для подсчета остатка %, для целоисчеленного деления //): ")
        if kaz1_str == "":
            print('Вы не ввели первое число!')
            continue
        if kaz2_str == "":
            print('Вы не ввели второе число!')
            continue
        if oper == "":
            print('Вы не выбрали знак!')
            continue
        try:
            kaz1 = float(kaz1_str)
            kaz2 = float(kaz2_str)
            if oper in ["+"]:
                result = kaz1 + kaz2
            elif oper in ["-"]:
                result = kaz1 - kaz2
            elif oper in ["*"]:
                result = kaz1 * kaz2
            elif oper in ["**"]:
                result = kaz1 ** kaz2
            elif oper in ["//"]:
                result = kaz1 // kaz2
            elif oper in ["%"]:
                result = kaz1 % kaz2
            elif oper in ["/"]:
                if kaz2 == 0:
                    print("Деление на ноль невозможно!")
            else:
                result = kaz1 / kaz2
            if oper in ["+", "-", "*", "/", "**", "//", "%"]:
                print("Ответ:", result)
        except ValueError:(
            print("Некорректный ввод чисел."))
def centimeters():
    while True:
        print(
            'Что бы перевести метры в км введите 1, что бы перевести км в метры введите 2, что бы перевести метры в см введите 3, что бы перевести сантиметры в метры введите 4')
        s = input()
        if s in ["1"]:
            try:
                kazak = int(input("Введите количество метров:"))
                print(kazak / 1000, "км")
            except ValueError:
                print("Неверный ввод!")
        elif s in ["2"]:
            try:
                kazak2 = int(input("Введите количество километров:"))
                print(kazak2 * 1000, "м")
            except ValueError:
                print("Неверный ввод!")
        elif s in ["3"]:
            try:
                kazak3 = int(input("Введите количество метров:"))
                print(kazak3 * 100, "см")
            except ValueError:
                print("Неверный ввод!")
        elif s in ["4"]:
            try:
                kazak4 = int(input("Введите количество сантиметров:"))
                print(kazak4 / 100, "м")
            except ValueError:
                print("Неверный ввод!")
        else:
            print("Вы не выбрали режим")
def kilograms():
    while True:
        print("Что бы перевести кг в граммы введите 1, что бы перевести граммы в кг введите 2.")
        s = input()
        if s in ['1']:
            try:
                uzbek = int(input("Введите количество килограмм:"))
                print(uzbek * 1000, "грамм")
            except ValueError:
                print("Неверный ввод!")
        elif s in ["2"]:
            try:
                uzbek2 = int(input("Введите количество грамм:"))
                print(uzbek2 / 1000, "кг")
            except ValueError:
                print("Неверный ввод!")
        else:
            print("Вы не выбрали режим")
def remains():
    taru = int(input("Введите число:"))
    gg = int(input("Введите число на которое нужно разделить:"))
    if taru % gg == 0:
        print(taru, "делиться без остатка")
    else:
        print(taru, 'делиться с остатком')
def dollar():
    dollar = 104.24
    print("Что-бы перевести рубли в доллары введите 1, что бы перевести доллары в рубли введите 2.")
    s = input()
    if s == "1":
        while True:
            try:
                rub = int(input("Введите количество рублей:"))
                print(rub / dollar, "долларов.")
            except ValueError:
                print("Неверный ввод!")
    elif s == "2":
        while True:
            try:
                dol2 = int(input("Введите количество долларов:"))
                print(dol2 * dollar, "рублей.")
            except ValueError:
                print("Неверный ввод!")
    else:
        print("Неверно выбран режим!")
def farengeit():
    print("Что-бы перевести цельсии в фаренгейты введите 1, что бы перевести фаренгейты в цельсии введите 2.")
    s = input()
    if s == "1":
        while True:
            try:
                c = int(input("Введите количество цельсий:"))
                f = (c * 9 / 5) + 32
                print(f, "фаренгейтов")
            except ValueError:
                print("Некорректный ввод")
    elif s == "2":
        while True:
            try:
                f = int(input("Введите количество фаренгейтов:"))
                c = (f - 32) * 5 / 9
                print(c, "цельсий")
            except ValueError:
                print("Некорректный ввод")
    else:
        print("Невыбран режим!")
def physics():
    sosi = ""
    while sosi not in ["1", "2", "3"]:
        print("Выберите тип: Найти скорость - 1, найти время - 2, найти расстояние - 3, км/ч в м/с введите 4, что бы найти массу введите 5")
        sosi = input()
        if sosi == "1":
            while True:
                try:
                    rass = int(input("Введите расстояние:"))
                    time = int(input("Введите время:"))
                    scoro = rass / time
                    print(f'ответ: {scoro}')
                except ValueError:
                    print("Некорректный ввод")
        elif sosi == "2":
            while True:
                try:
                    rass = int(input("Введите расстояние:"))
                    scoro = int(input("Введите скорость:"))
                    time = rass / scoro
                    print(f'ответ: {scoro}')
                except ValueError:
                    print("Некорректный ввод")
        elif sosi == "3":
            while True:
                try:
                    scoro = int(input("Введите скорость:"))
                    time = int(input("Введите время:"))
                    rass = scoro * time
                    print(f'ответ: {rass}')
                except ValueError:
                    print("Некорректный ввод")
        elif sosi == "4":
            try:
                km = int(input("Введите км/ч:"))
                ms = km * 1000 / 3600
                print(ms)
            except ValueError:
                print("Неверный ввод")
        elif sosi == "5":
            try:
                v = int(input("Введите объем:"))
                p = int(input("Введите плотность:"))
                print(p * v)
            except ValueError:
                print("Неверный ввод")
        else:
            print("Невыбран режим!")
def bit():
    dick = ""
    while dick not in ["1", "2", "3"]:
        print(
            "Выберите режим: биты в байты 1, байты в килобайты 2, килобайты в мегабайты 3, мегабайты в гигабайты 4, гигабайты в терабайты 5.")
        dick = input()
        if dick == "1":
            while True:
                try:
                    bit = int(input("Введите количество битов:"))
                    byte = bit / 8
                    print(f"Количество байт: {byte}")
                except ValueError:
                    print("Некорректный ввод")
        if dick == "2":
            while True:
                try:
                    byte = int(input("Введите количество байт:"))
                    kilobyte = byte / 1024
                    print(f"Количество КБ: {kilobyte}")
                except ValueError:
                    print("Некорректный ввод")
        if dick == "3":
            while True:
                try:
                    kb = int(input("Введите количество КБ:"))
                    mb = kb / 1024
                    print(f"Количество МБ: {mb}")
                except ValueError:
                    print("Некорректный ввод")
        if dick == "4":
            while True:
                try:
                    mb2 = int(input("Введите количество МБ:"))
                    gb = mb2 / 1024
                    print(f"Количество ГБ: {gb}")
                except ValueError:
                    print("Некорректный ввод")
        if dick == "5":
            while True:
                try:
                    gb2 = int(input("Введите количество ГБ:"))
                    tb = gb2 / 1024
                    print(f"Количество ГБ: {tb}")
                except ValueError:
                    print("Некорректный ввод")

        else:
            print("Невыбран режим!")
def table():
        while True:
            try:
                number = int(input("Введите число:"))
                dist = int(input("Введите диапазон, например 11:"))
                break
            except ValueError:
                print("Неверный ввод!")
        for i in range(1, dist +1):
            print(f"{number} * {i} = {number * i}")
def arithmetic_mean(args):
    if not args:
        return None
    try:
        average = sum(args) / len(args)
        return average
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except TypeError:
        return "Вы ввели не число!"
def sorter():
    try:
        how_many = int(input("Сколько чисел надо сортировать:"))
        numbers = []
        for i in range(how_many):
            number = int(input(f"Введите число {i + 1}: "))
            numbers.append(number)
        numbers.sort()
        print(numbers)
    except ValueError:
        print("Неверный ввод")
def root():
    try:
        x = int(input("Введите число:"))
        print(f"Квадратный корень числа {x} равен {math.sqrt(x)}.")
    except ValueError:
        print("Неверный ввод!")
def cosine():
    sq = []
    while sq not in ["1","2","3"]:
        sq = input("1 что бы найти синус, 2 что бы найти косинус, 3 что бы найти тангенс:")
        if sq == "1":
            try:
                x = int(input("Введите число:"))
                print(f"Синус числа {x} равен {math.sin(x)}.")
            except ValueError:
                print("Неверный ввод")
        elif sq == "2":
            try:
                x = int(input("Введите число:"))
                print(f"Косинус числа {x} равен {math.cos(x)}.")
            except ValueError:
                print("Неверный ввод")
        elif sq == "3":
            try:
                x = int(input("Введите число:"))
                print(f"Тангус числа {x} равен {math.tan(x)}")
            except ValueError:
                print("Неверный ввод")
        else:
            print("Вы не выбрали!")
def arcsinus():
    sw = []
    while sw not in ["1", "2", "3"]:
        sw = input("1 что бы найти арксинус, 2 что бы найти арккосинус, 3 что бы найти арктангенс:")
        if sw == "1":
            try:
                x = int(input("Введите число:"))
                print(f"Арксинус числа {x} равен {math.asin(x)}.")
            except ValueError:
                print("Неверный ввод")
        elif sw == "2":
            try:
                x = int(input("Введите число:"))
                print(f"Арккосинус числа {x} равен {math.acos(x)}.")
            except ValueError:
                print("Неверный ввод")
        elif sw == "3":
            try:
                x = int(input("Введите число:"))
                print(f"Арктангус числа {x} равен {math.atan(x)}")
            except ValueError:
                print("Неверный ввод")
        else:
            print("Вы не выбрали!")
def set():
    try:
        k = int(input("Введите сколько объектов:"))
        fak = int(input("Сколько нужно взять:"))
        print(f"Существует способов: {math.comb(k,fak)}")
    except ValueError:
        print("Неверный ввод")
def factorial():
    try:
        nert = int(input("Введите число:"))
        print(math.factorial(nert))
    except ValueError:
        print("Неверный ввод")
def randomai():
    miny = int(input("Введите минимальный порог:"))
    maxy= int(input("Введите максимальный порог:"))
    hhru = int(input("Сколько чисел надос сгенерировать:"))
    for _ in range(hhru):
        num =  random.randint(miny,maxy)
        print(num)
main()
        
