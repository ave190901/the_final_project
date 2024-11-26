import copy
import random

class CowsAndBulls:
    def __init__(self):
        self.n = 0
        self.user_num, self.num = '', ''
        self.cows, self.bulls = 0, 0
        self.history = [f'Ваше число | Быки | Коровы']

    def generate_num(self, n):
        self.n = n
        for i in range (self.n):
            self.num += str(random.randint(0,self.n))
        return self.num

    def get_num(self):
        return self.num

    def set_user_num(self, new_user_num):
        # self.user_num = f"{new_user_num:0{self.n}}"
        self.user_num = new_user_num

    def count_cows(self):
        self.cows = 0
        numbers = copy.copy(set(self.num)) # Копирует и преобразует загаданное число во множество.
        print(numbers)
        numbers = list(numbers)
        for i in range(len(numbers)): # Цикл считает количество цифр из загаданного числа в введенном пользователем.
            for j in range(len(self.user_num)):
                if numbers[i] == self.user_num[j]:
                    self.cows += 1
                    # numbers = numbers.replace(numbers[i], ' ', 1)
        #if self.cows == 0:
        #    return self.cows
        #elif self.cows >= self.count_bulls():
        return self.cows - self.count_bulls()

    def count_bulls(self):
        self.bulls = 0
        for i in range(len(self.user_num)):
            if self.num[i] == self.user_num[i]:
                self.bulls += 1
        return self.bulls

    def write_history(self, number, cows, bulls):
        self.history += [f'{number} | {bulls} | {cows}']
        return self.history

    def rewrite_history(self):
        self.history = [f'Ваше число | Быки | Коровы']



def get_rules(value):
    value = value.lower()
    match value:
        case 'нет':
            return(
                f'Правила игры: \n'
                f'Компьютер загадывает число. В классической версии число \n'
                f'4-ехзначное, в данной версии Вы можете выбрать длину \n'
                f'числа, которое будет загадано. \n'
                f'Цель игры: отгадать число. При каждой попытке вводится\n'
                f'число равное по количеству знаков загаданному выводится\n'
                f'количество "коров" - сколько цифр угадано без совпадения \n'
                f'с их позициями в тайном числе и быков - сколько "цифр" \n'
                f'угадано вплоть до позиции в тайном числе.\n'
                f'Игра завершается, когда число угадано.'
                f'Пример.\n'
                f'Задумано тайное число «3219».\n'
                f'Попытка: «2310».\n'
                f'Результат: две «коровы» (две цифры: «2» и «3» — угаданы на\n'
                f'неверных позициях) и один «бык» (одна цифра «1» угадана\n'
                f'вплоть до позиции).\n'
            )
        case 'да':
            return 'Тогда начнем.'
        case _:
            return (f'Введено неверное значение. '
                    f'Тогда будем считать, что правила Вам известны. :)')

def get_restart(value):
    value = value.lower()
    match value:
        case 'нет':
            return exit()
        case 'да':
            return 'Тогда начнем.'
        case _:
            return (f'Введено неверное значение... '
                    f'Тогда играем дальше :)')


if __name__ == '__main__':

    print(f'Начало игры.\n ')

    print(get_rules(input(str('Вам известны правила?\n (Да/Нет) '))))

    while True:
        try:
            while True:
                n = int(input('Введите количество цифр в числе (от 4 до 9 знаков) '))
                if n in range(4, 10):
                    number = CowsAndBulls()
                    break
                else:
                    print ('Введено значение вне диапозона. '
                           'Повторите ввод.')
        except ValueError:
            print(f'Введено некорректное число. '
                  f'Проверьте, что число введено цифрами.')
            continue

        x = 0 # счетчик попыток
        while True:
            user_num = str(input('Введите число: '))
            try:
                num_num = int(copy.copy(user_num))
                print(type(num_num))
            except ValueError:
                print(f'Введено некорректное число. '
                      f'Проверьте, что число введено цифрами.')
                continue

            if len(str(user_num)) == n:
                number.set_user_num(user_num)
                x += 1
                cows = number.count_cows()
                bulls = number.count_bulls()
                if bulls == number.n:
                    number.write_history(user_num, cows, bulls)
                    for el in number.history:
                        print(el)
                    print('Победа!')
                    print(f'Загадонное число {number.get_num()}.')
                    print(f'Вы угадали за {x} попыток.')
                    number.rewrite_history()
                    print(get_restart(str(input('Начать сначала? '))))
                    break

                else:
                    number.write_history(user_num, cows, bulls)
                    for el in number.history:
                        print(el)
            else:
                print(f'Введено некорректное число. '
                      f'Проверьте, что количество цифр в вашем числе совпадает\n'
                      f'с выбранным вами для тайного числа.\n'
                      f'Повторите попытку.')
