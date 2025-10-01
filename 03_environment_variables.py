# // Вы можете создать переменную окружения MY_NAME с помощью
# $ export MY_NAME="Wade Wilson"

# // Затем её можно использовать в других программах, например
# $ echo "Hello $MY_NAME"

# Hello Wade Wilson

import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
# Второй аргумент os.getenv() - это возвращаемое по умолчанию
#  значение.

# Если значение не указано, то по умолчанию оно равно None.
#  В данном случае мы указываем «World» в качестве значения
#  по умолчанию.

# // Здесь мы еще не устанавливаем переменную окружения
# $ python environment_variables.py

# // Поскольку мы не задали переменную окружения, мы получим значение по умолчанию

# Hello World from Python

# // Но если мы сначала создадим переменную окружения
# $ export MY_NAME="Wade Wilson"

# // А затем снова запустим программу
# $ python environment_variables.py

# // Теперь она прочитает переменную окружения

# Hello Wade Wilson from Python


# // Создайте переменную окружения MY_NAME в строке для этого вызова программы
# $ MY_NAME="Wade Wilson" python main.py

# // Теперь она может прочитать переменную окружения

# Hello Wade Wilson from Python

# // После этого переменная окружения больше не существует
# $ python main.py

# Hello World from Python

# Переменная окружения PATH

# Существует специальная переменная окружения PATH,
#  которая используется операционными системами
#  (Linux, macOS, Windows) для поиска программ для запуска.

# Значение переменной PATH - это длинная строка,
#  состоящая из каталогов, разделенных двоеточием : в Linux
#  и macOS, и точкой с запятой ; в Windows.

# Например, переменная окружения PATH может выглядеть следующим
#  образом: Linux, macOS, Windows

# /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
