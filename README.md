### managetask

Проект содержит консольные скрипты для django:  **поиск людей по образованию** и **получение курсов валют с двух сайтов**.
 
**Requirements:** Python 2.7, Django 1.9.4, SQLite.

**Запуск проекта:**  
 1. Клонируем репозиторий, и переходим в него.
 2. Создаем окружение с python 2.7 `mkvirtualenv --python=/usr/bin/python managetask`
 3. Устанавливаем зависимости: `pip install -r requirements.txt`

----------

**Поиск людей по образованию**  
БД  SQLite уже наполнена начальными данными.  
Консольная команда поиска: `python manage.py showpeople java`

**Получение курсов валют с двух сайтов**  
Для получения курса валют используем консольную команду:  `python manage.py showexchangerates`
