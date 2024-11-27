import copy
import random


class CowsAndBulls:
    """Игра Быки и Коровы."""
    def __init__(self):
        """Устанавливает атрибуты CowsAndBulls."""
        self.n: int = 0
        self.user_num, self.num = '', ''
        self.cows, self.bulls = 0, 0
        self.history: list = [f'Ваше число | Быки | Коровы']

    def generate_num(self, n) -> str:
        """Генерирует рандомное n-значное число."""
        self.n = n
        for i in range (self.n):
            self.num += str(random.randint(0,self.n))
        return self.num

    def get_num(self) -> str:
        """Выводит загаданное число."""
        return self.num

    def set_user_num(self, new_user_num: str):
        """Устанавливает новое значение числа пользователя"""
        self.user_num = new_user_num

    def count_cows(self) -> int:
        """Счетчик коров"""
        self.cows = 0
        numbers: set = copy.copy(set(self.num))
        # Представляет множество с цифрами загаданного числа, без повторов.
        # Копия загаданного числа.
        numbers: list = list(numbers)
        for i in range(len(numbers)):
            # Цикл считает количество цифр из загаданного числа
            # в введенном пользователем.
            for j in range(len(self.user_num)):
                if numbers[i] == self.user_num[j]:
                    self.cows += 1
        return self.cows - self.count_bulls()

    def count_bulls(self) -> int:
        """Счетчик быков"""
        self.bulls = 0
        for i in range(len(self.user_num)):
            if self.num[i] == self.user_num[i]:
                self.bulls += 1
        return self.bulls

    def write_history(self, cows, bulls) -> list:
        """Запись истории попыток.

        Args:
            cows: Количество коров.
            bulls: Количество быков.

        Returns:
            Лист записей попыток.

        """
        self.history += [f'{self.user_num} | {bulls} | {cows}']
        return self.history

    def rewrite_history(self):
        """Очистка истории"""
        self.history = [f'Ваше число | Быки | Коровы']


def get_rules(value) -> str:
    """Выводит правила игры.

    Args:
        value: Ответ пользователя на вопрос о выводе правил.

    Returns:
        Выводит правила при положительном ответе, при другом ответе пропускает
        вывод правил и начинает игру

    """
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
    """В зависимости от ответа пользователя перезапускает игру после того,
    как отгаданно число.

    Args:
        value: Ответ пользователя.

    """
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
                n: int = int(input(
                    'Введите количество цифр в числе (от 4 до 9 знаков) ')
                )
                if n in range(4, 10):
                    number: CowsAndBulls = CowsAndBulls()
                    print(number.generate_num(n))  # Убрать принт!!!
                    break
                else:
                    print ('Введено значение вне диапозона. '
                           'Повторите ввод.')
        except ValueError:
            print(f'Введено некорректное число. '
                  f'Проверьте, что число введено цифрами.')
            continue

        x = 0 # Переменная счетчика попыток
        while True:
            user_num: str = str(input('Введите число: '))
            try:
                num_num: int = int(copy.copy(user_num))
            except ValueError:
                print(f'Введено некорректное число. '
                      f'Проверьте, что число введено цифрами.')
                continue

            if len(user_num) == n:
                number.set_user_num(user_num)
                x += 1
                cows: int = number.count_cows()
                bulls: int = number.count_bulls()
                if bulls == number.n:
                    number.write_history(cows, bulls)
                    for el in number.history:
                        print(el)
                    print('Победа!')
                    print(f'Загадонное число {number.get_num()}.')
                    print(f'Вы угадали за {x} попыток.')
                    number.rewrite_history()
                    print(get_restart(str(input('Начать сначала? '))))
                    break

                else:
                    number.write_history(cows, bulls)
                    for el in number.history:
                        print(el)

            else:
                print(f'Введено некорректное число. '
                      f'Проверьте, что количество цифр в вашем '
                      f'числе совпадает с выбранным вами для тайного числа.\n'
                      f'Повторите попытку.')
