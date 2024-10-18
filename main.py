with open('text.txt', 'r', encoding='utf-8') as readfile, open('output.txt', 'w', encoding='utf-8') as writefile: # Открываем файл 'text.txt' для чтения и 'output.txt' для записи, оба с кодировкой utf-8.
    for line in readfile: # Перебираем каждую строку в файле 'text.txt'.
        line_for_writefile = "" # Создаем пустую строку для хранения модифицированной версии текущей строки.
        for letter in line: # Перебираем каждый символ в строке.
            if letter == 'о': # Если символ 'о'.
                line_for_writefile += 'a' # Заменяем символ 'о' на 'a'.
            else: # Если символ не 'о'.
                line_for_writefile += letter # Добавляем его в исходном виде.
        writefile.write(line_for_writefile) # Записываем модифицированную строку в файл 'output.txt'.