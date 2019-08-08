# -*- coding: utf-8 -*-

"""
Файл настроек содержит в себе глобавльные переменные такие,
как настройки прокси, авторизации, необходимые ссылки и т.д.
"""

proxies = {
}
auth = ('username', 'password')

base_url = 'http://rest.test.ivi.ru{}'
characters = '/characters'
character = '/character'
characters_by_name = '/characters/{}'
character_by_name = '/character/{}'
reset = "/reset"
session = None

