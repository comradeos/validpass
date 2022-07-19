import os, re # подключение модулей для работы с операционной системой и регулярными выражениями
os.chdir(os.path.dirname(__file__)) # установка текущего каталога в качестве рабочего

def is_valid(line: str)->bool:
    try:
        split_line = re.findall(r'(^([a-zA-Z{1}]) ([0-9])-([0-9]): )(.*)', line) # разделить строку на группы
        
        char = split_line[0][1] # искомый символ
        min = int(split_line[0][2]) # минимальное количество повторений
        max = int(split_line[0][3])  # максимальное количество повторений
        pass_value = split_line[0][4] # значение пароля
    except:
        return False

    char_counter = int(list(pass_value).count(char)) # подсчет количества искомых символов

    if min <= char_counter <= max: # проверка условия и возврат значений 
        return True
    else:
        return False

def valid_pass_counter(file_name:str)->int:
    counter = 0 # счетчик
    try:
        with open(file_name, 'r') as file: # чтение файла
            lines = file.readlines() # получение списка из строк
    except FileNotFoundError: # обработка ошибки "файл не найден"
        print(f'Ошибка: Не удалось найти файл "{file_name}"!')
        return 0
        
    for line in lines: # 
        if is_valid(line):
            counter+=1
    return counter


if __name__ == '__main__':
    file_name = input('Введите имя файла, содержащего пароли: ')
    print(f'Количество валидных паролей: {valid_pass_counter(file_name)}')