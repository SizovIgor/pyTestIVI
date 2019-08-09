# pyTestIVI 


Добро пожаловать на главную страницу Фреймворка `pyTestIVI`.
Данный Фреймворк был создан для выполнения тестового задания.

Исходное задание:
```text
Написать Фреймворк с автотестами; 
Результат: 
- проект в github/bitbucket с тестовыми сценариями, 
- readme.md, 
- исходниками проекта
```

### Установка
Для установки необходимо скачать себе копию проекта.
Затем выполнить команду `pip install -r requirements.txt` для установки необходимых модулей.

#### Подготовка к запуску тестов
Перед запуском тестов необходмо проставить свой почтовый ящик и пароль в `source.option` для `auth = ('username', 'password')` 

### Запуск всех тестов
Для запуска всех тестов необходимо перейти в папку `source` и выполнить команду `pytest -s -v`, ключи нужны для более комфортного отображения результатов тестов.

### Запуск определенных тестов или категории тестов
Для запуска тестов определенной категории необходимо перейти в папку этой категории и выполнить команду `pytest -s -v`

Для запуска определенного теста необходимо перейти в папку этого теста и выполнить команду `pytest -s -v <имя_теста>`
    
### Структура проекта    
В корне проекта находятся файлы, не имеющие отношения к исходному коду.
- файл [README.md](README.md) содержит в себе (данное) описание проекта 
- Файл [requirements.txt](requirements) содержит в себе набор библиотек, которые нужны для работы фрэймоврка 
- Файл [tests.csv](tests.csv) содержит в себе набор тестовых сценариев
- файл [checks.txt](checks.txt) содержит наброс проверок, которые необходимо обдумать
- Папка [source](source) содержит все настройки, фикстуры и тесты. 
    - файл настроек [option.py](source/option.py) содержит в себе глобавльные переменные такие, как настройки прокси, авторизации, необходимые ссылки и т.д.
    - файл фикстур [conftest.py](source/conftest.py) содержит в себе глобальные фикстуры всего проекта, например такие, как создание объекта сессии `create_session`, или обновление заголовков методов `post_setup`
    - базовый тест на проверку готовности к работе [test_ivi.py](source/test_ivi.py), и категории тестов (`test_right_checks`, `test_permissions` и т.д.)

#### Категории тестов

Все тесты предполагается делить на следующие базовые категории

- Тесты, направленные на проверку работы API-методов `test_right_checks`
- Тесты, направленные на проверку обработки сломанных запросов или данных `test_broken_checks`
- Тесты, направленные на тестирование прав доступа `test_permissions`
- Тесты, направленные на корректность работы методов при выполнении быстрых многочисленных запросов `test_consecutive_requests`  
