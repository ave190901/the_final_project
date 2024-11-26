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