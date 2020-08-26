# -*- coding: utf-8 -*-
import random
import hashlib

from random import choice

# Функция генерации номеров
def random_phone_num_generator():

    # Для примера использован список кодов Билайн 
    kod_Beeline = ['900','903','905','906','909','961','962','963','964','965','966','967','968','969','980','983','926','930']
    
    first = str(random.choice(kod_Beeline))
    second = str(random.randint(100, 999)).zfill(3)
    last_1 = str(random.randint(1, 98)).zfill(2)
    last_2 = str(random.randint(1, 98)).zfill(2)
    fin = str('{}{}{}{}'.format(first,second, last_1, last_2))
    
    # Возвращаем отформатированное под мобильный номер значение
    return '"' + fin + '",'

def add(m):
		return '\n\t]\n}'

# Запрашиваем у пользователя сколько ему генерировать номеров
countStartFrom = notepad.prompt("Enter value of quantity phone numbers (only numbers, max - 10000):", 'Python Script GeneratePhoneNumber_10simbol', '1')

# Проверка введенного значения, должны быть только цифры, больше 0 но меньше 10000
while countStartFrom.isdigit() == False or int(countStartFrom) == 0 or int(countStartFrom) > 10000:
        countStartFrom = notepad.prompt("Enter value of quantity phone numbers (only integer numbers, max - 10000):", 'Python Script GeneratePhoneNumber', '1')
        # editor.addText("Just new file ))")
        
        
else:
    # Создаем новый документ
    notepad.new()
    
    # Форматируем что документ будет Json
    notepad.menuCommand(MENUCOMMAND.LANG_JSON)

    # Открывающая скобка Json`а
    editor.addText("{\n\t\"phones\": [\n")
    i = 0
    while i < int(countStartFrom) :
        editor.addText("\t\t")
        editor.addText(random_phone_num_generator()+"\n")
        i += 1
    editor.addText("\t]\n}")
    
editor.rereplace(",\n\t]\n}", add)
    

# Заготовка под перегенерацию
# while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
    # last = (str(random.randint(1, 9998)).zfill(4))
