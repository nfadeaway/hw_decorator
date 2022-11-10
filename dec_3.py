import os
import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        with open('dec_3.log', 'a+', encoding='utf-8') as log_file:
            line = f'Функция {old_function.__name__} с аргументами {args} {kwargs} вызвана {datetime.datetime.now()}'
            result = old_function(*args, **kwargs)
            log_file.write(line + '\n')
            log_file.write(f'Результат выполнения функции: {str(result)}' + '\n')
        return result

    return new_function


def main():

    @logger
    def cook_book():
        cook_book_dict = {}
        with open('recipes.txt', encoding='utf-8') as recipes_file:
            recipes_file_lines = recipes_file.readlines()
            i = 0
            while i < len(recipes_file_lines):
                cook_book_dict[recipes_file_lines[i].rstrip()] = []
                for j in range(i + 2, i + 2 + int(recipes_file_lines[i + 1])):
                    ingredient = [x for x in recipes_file_lines[j].split(' | ')]
                    cook_book_dict[recipes_file_lines[i].rstrip()].append({'ingredient_name': ingredient[0],
                                                                           'quantity': int(ingredient[1]),
                                                                           'measure': ingredient[2].rstrip()})
                i += 3 + int(recipes_file_lines[i + 1])
        return cook_book_dict

    result = logger(cook_book())


if __name__ == '__main__':
    main()
