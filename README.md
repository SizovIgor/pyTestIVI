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

Из документации, предоставленной для выполнения задания, следует:

- для выполнения запросов, к предоставленным API-методам, необходима аутентификация.
  Для этого используется механизм HTTP Basic Authentication.
  
  Например:
    `curl 'http://rest.test.ivi.ru/characters' -u username:password`

##Команды:
- GET /characters - Запрос характеристик всех персонажей коллекции. 
    -
    Например: 
    `curl 'http://rest.test.ivi.ru/characters' -u username:password`
    
    Результат возвращается в виде json'a со следующей структурой:
    ```json
    {
      "result": [
        {
          "education": "High school (unfinished)", 
          "height": 1.9, 
          "identity": "Publicly known", 
          "name": "Hawkeye", 
          "other_aliases": "None", 
          "universe": "Marvel Universe", 
          "weight": 104
        }, 
        {
          "education": "Unrevealed", 
          "height": 1.82, 
          "identity": "Secret", 
          "name": "Abyss", 
          "other_aliases": "None", 
          "universe": "Marvel Universe", 
          "weight": 73
        },
        {
        ...
        }
      ]
    }
    ```

- GET /character/{name} - Запрос характеристик героя с указанием его имени. 
    -
    Например:
    `curl 'http://rest.test.ivi.ru/character/Abyss' -u username:password`
    
    В качестве ответа от сервера приходит json, с аналогичной структурой для одного персонажа:
    
    ```json
    {
      "result": {
        "education": "Unrevealed", 
        "height": 1.82, 
        "identity": "Secret", 
        "name": "Abyss", 
        "other_aliases": "None", 
        "universe": "Marvel Universe", 
        "weight": 73
      }
    }
    ``` 
    
- POST /character - Запрос для добавления нового персонажа, с указанием его характеристик.
    -
    Например:
    ```text
    curl -X POST -H 'Content-type: application/json' 
          -u username:password
          -d '{"name": "Hawkeye", "universe": "Marvel Universe", 
               "education": "High school (unfinished)", "weight": 104, 
               "height": 1.90, "identity": "Publicly known", 
               "other_aliases": "None"}' 
           'http://rest.test.ivi.ru/character'
    ```
    
    Результатом выполнения запроса является новый персонаж, с указанными характеристиками. 
    
    В качестве ответа от сервера приходит json, с аналогичной структурой, как при выполнении `GET`-запроса к API-методу `/character/{name}`
    
    *Для выполнения данного запроса необходимо соблюсти ограничение на количество персонажей: `не более 500`
    В случае нарушения данного ограничения новый персонаж не будет создан. 
    В ответе от сервера возникнет следующая ошибка:*
    
    ```json
    {
      "error": "Collection can't contain more than 500 items"
    }
    ``` 
    
- PUT /character/{name} - Запрос на изменение характеристик указанного персонажа.
    -
    Например:

    ```text
    curl -X PUT -H 'Content-type: application/json' 
         -u username:password
         -d '{"name": "Hawkeye", "universe": "Marvel Universe", 
              "education": "High School (unfinished)", "weight": 104, 
              "height": 1.90, "identity": "Publicly known", 
              "other_aliases": "None"}' 
              'http://rest.test.ivi.ru/character/Hawkeye'
    ```
    
    Результатом выполнения запроса являются обновленные характеристики указанного персонажа.
    В качестве ответа от сервера приходит json, с аналогичной структурой, как при выполнении `GET`-запроса к API-методу `/character/{name}`

- DELETE /character/{name} - Запрос на удаление указанного персонажа.
    - 

    Например:
    `curl -X DELETE 'http://rest.test.ivi.ru/character/Abyss' -u username:password`

    Результатом выполнения запроса является исключение персонажа из коллекции.
    В качестве ответа от сервера приходит json, со следующей структурой:
    
    ```json
    {
  "result": [
    "5bfd2e3fa259e86dc34f29d9 is deleted"
      ]
    }
    ```
    
    В случае, если по `name` невозможно найти персонажа, то отдается стандартный ответ:
    ```json
    {
      "result": [
        "No such name"
      ]
    }
    ```
    
- POST /reset - Запрос на сброс коллекции в первоначальное состояние. 
    -
    Например:
    `curl -X POST 'http://rest.test.ivi.ru/reset' -u username:password`
    
    Результатом выполнения данного запроса является сброс коллекции до первоначального состояния

### Установка
Для установки необходимо скачать себе копию проекта.
Затем выполнить команду `pip install -r requirements.txt` для установки необходимых модулей.

### Запуск всех тестов
Для запуска всех тестов необходимо перейти в папку `source` и выполнить команду `pytest -s -v`, ключи нужны для более комфортного отображения результатов тестов.

### Запуск определенных тестов или категории тестов
Для запуска тестов определенной категории необходимо перейти в папку этой категории и выполнить команду `pytest -s -v`

Для запуска определенного теста необходимо перейти в папку этого теста и выполнить команду `pytest -s -v <имя_теста>`
    
    
### Структура тестов

Все тесты предполагается делить на следующие базовые категории

- Тесты, направленные на проверку работы API-методов `test_right_checks`
- Тесты, направленные на проверку обработки сломанных запросов или данных `test_broken_checks`
- Тесты, направленные на тестирование прав доступа `test_permissions`
- Тесты, направленные на корректность работы методов при выполнении быстрых многочисленных запросов `test_consecutive_requests`  
