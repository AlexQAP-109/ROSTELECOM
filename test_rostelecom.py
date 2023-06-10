from auth_rostelecom import *




def test_keys_1():
    """Проверка полей "мобильный телефон", "палоль" на функцмональность(в html
    должны отображаться введеные валидные данные пользователя"""
    phone = pole_mobil_phone()
    print(f'В поле ввода Моб. телефон отображается-- {phone[0]}')
    assert phone[0] == MyAuth.valid_phone
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{phone[1]}')
    assert phone[1] == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    """Чекбокс изначально вкл. потому в методе "pole_mobil_phone" мы используем нажатие два раза
    и сравниваем с позицией тега при в вкл. чек боксе"""
    assert len(phone[2]) > 0

def test_keys_2():
    """Проверка кнопки "Войти" на функциональность с заполнеными полями
    аторизации зарегестрированного пользователя"""
    mob_phone, pasw , chec_box, url1, url2 = button_voyti()
    print(f'В поле ввода Моб. телефон отображается-- {mob_phone}')
    assert mob_phone == MyAuth.valid_phone
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    """Чекбокс изначально вкл. потому в методе "pole_mobil_phone" мы используем нажатие два раза
    и сравниваем с позицией тега при в вкл. чек боксе"""
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2

def test_keys_3():
    """Проверка полей "почта", "палоль" на функцмональность(в html
    должны отображаться введеные валидные данные пользователя"""
    mail, pasw, chec_box = pole_email()
    print(f'В поле ввода email отображается-- {mail}')
    assert mail == MyAuth.valid_email
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0

def test_keys_4():
    """Проверка кнопки "Войти" на функциональность с заполнеными полями
    авторизации зарегестрированного пользователя"""
    mail, pasw , chec_box, url1, url2 = button_voyti_mail()
    print(f'В поле ввода почта  отображается-- {mail}')
    assert mail == MyAuth.valid_email
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2

def test_keys_5():
    """Проверка вкладок : "Телефон, Почта, Логин, Лицевой счет" -на функциональность"""
    text1, text2, text3, text4 = vkladki_forma()
    print(f'Пустое поле вкладки Почта имеет текст -- {text1} , это значит что открыта форма на вкладке почта')
    assert len(text1) > 0
    print(f'Пустое поле вкладки Логин имеет текст -- {text2} , это значит что открыта форма на вкладке логин')
    assert len(text2) > 0
    print(f'Пустое поле вкладки лицевой счет имеет текст -- {text3} , это значит что открыта форма на вкладке лицевой счет')
    assert len(text3) > 0
    print(f'Пустое поле вкладки Мобильный телефон имеет текст -- {text4} , это значит что открыта форма на вкладке моб. тел.')
    assert len(text4) > 0

def test_keys_6():
    """Проверка функциональности поля "Пароль" в форме регистрации в скрытом и открытом режиме."""
    type1, simvol, summa, type2 = password_hide()
    print(f'В скрытом пароле длинна соответствует длине введеного пароля-- {summa}')
    assert summa == 7
    print(f'В скрытом режиме тип соответствует--{type1}')
    assert type1 == 'type="password"/>]'
    print(f'В открытом режиме тип соответствует--{type2}')
    assert type2 == 'type="text"/>]'
    print(f'Значение пароля в  открытом режиме соответствует {simvol} == 1234567')
    assert simvol == '1234567'


def test_keys_7():
    """Проверка функциональности ссылки "Пользовательское соглашение" в форме авторизации."""
    Url1, Url2 = linc_terms_of_use()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_8():
    """Проверка функциональности ссылки "Забыл пароль"  в форме авторизации."""
    Url1, Url2 = linc_forgot_password()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_9():
    """Проверка на функциональность иконки "Вконтакте" в форме авторизации."""
    Url1, Url2 = linc_vk()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_10():
    """Проверка на функциональность иконки "Однокласники" в форме авторизации."""
    Url1, Url2 = linc_odnoklasniki()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_11():
    """Проверка на функциональность иконки "Мой мир" в форме авторизации."""
    Url1, Url2 = linc_mail_ru()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_12():
    """Проверка на функциональность иконки "Яндекс" в форме авторизации."""
    Url1, Url2 = linc_yandex()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_13():
    """Проверка на функциональность ссылки "Зарегистрироваться" в форме авторизации."""
    Url1, Url2 = linc_yandex()
    print(f'Сравниваем URL: Url1 != Url2 --ссылка рабочая')
    assert Url1 != Url2


def test_keys_14():
    """Проверка авторизации зарегистрированого
    пользователя( вход в личный аккаунт пользователя по номеру телефона)"""
    phone, pasw, chec_box, url1, url2, url3, text, url4 = auth_phone()
    print(f'В поле ввода почта  отображается-- {phone}')
    assert phone == MyAuth.valid_phone
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2
    print(f'проверяем URL для перехода в личный кабинет ({url3} == https://lk.rt.ru/')
    assert url3 == 'https://lk.rt.ru/'
    print(f'Текст на странице "Личный кабинет" == {text}')
    assert text == 'Личный кабинет'
    print(f'Возвращенный URL  {url4} == "https://start.rt.ru/?tab=main"')
    assert url4 == 'https://start.rt.ru/?tab=main'


def test_keys_15():
    """Проверка авторизации зарегистрированого пользователя( вход в личный кабинет пользователя по email)"""
    mail, pasw, chec_box, url1, url2, url3, text, url4 = auth_maill()
    print(f'В поле ввода почта  отображается-- {mail}')
    assert mail == MyAuth.valid_email
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2
    print(f'проверяем URL для перехода в личный кабинет ({url3} == https://lk.rt.ru/')
    assert url3 == 'https://lk.rt.ru/'
    print(f'Текст на странице "Личный кабинет" == {text}')
    assert text == 'Личный кабинет'
    print(f'Возвращенный URL  {url4} == "https://start.rt.ru/?tab=main"')
    assert url4 == 'https://start.rt.ru/?tab=main'


def test_keys_16():
    """Проверка авторизации зарегистрированого пользователя( вход в личный кабинет пользователя по login)"""
    login, pasw, chec_box, url1, url2, url3, text, url4 = auth_login()
    print(f'В поле ввода "логин"  отображается-- {login}')
    assert login == MyAuth.valid_login
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2
    print(f'проверяем URL для перехода в личный кабинет ({url3} == https://lk.rt.ru/')
    assert url3 == 'https://lk.rt.ru/'
    print(f'Текст на странице "Личный кабинет" == {text}')
    assert text == 'Личный кабинет'
    print(f'Возвращенный URL  {url4} == "https://start.rt.ru/?tab=main"')
    assert url4 == 'https://start.rt.ru/?tab=main'


def test_user_story_1():
    """Тесты на проверку user story №1 «Ростелеком Информационные Технологии»"""

    url, url1, url2, url3, url4, text_auth, text_office, text_vse_dok, phone, pasw, chec_box = user_story_1()
    print(f'На открывшейся странице Авторизации  URL --{url} '
          f'Присутствует форма авторизации c текстом == {text_auth}')
    assert text_auth == 'Авторизация'
    print(f'В поле ввода телефон  отображается-- {phone}')
    assert phone == MyAuth.valid_phone
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2
    print(f'проверяем URL для перехода в личный кабинет ({url3} == https://lk.rt.ru/')
    assert url3 == 'https://lk.rt.ru/'
    print(f'Текст на странице "Личный кабинет" == {text_office}')
    assert text_office == 'Личный кабинет'
    print(f'Возвращенный URL  {url4} == "https://start.rt.ru/?tab=main"')
    assert url4 == 'https://start.rt.ru/?tab=main'
    print(f'На страцице URL {url4} есть ссылка с текстом {text_vse_dok}')
    assert text_vse_dok == 'Посмотреть все документы по моим лицевым счетам'


def test_user_story_2():
    """Тесты на проверку user story №2 «Ростелеком Информационные Технологии»"""

    url, url1, url2, url3, url4, url5, text_auth, text_office, text_for_my, phone, pasw, chec_box = user_story_2()
    print(f'На открывшейся странице Авторизации  URL --{url} '
          f'Присутствует форма авторизации c текстом == {text_auth}')
    assert text_auth == 'Авторизация'
    print(f'В поле ввода телефон  отображается-- {phone}')
    assert phone == MyAuth.valid_phone
    print(f'В поле ввода пароль отображается введеный пароль пользователя--{pasw}')
    assert pasw == MyAuth.valid_password
    print(f'Чек бокс вкл "Запомнить меня" -- {True}')
    assert len(chec_box) > 0
    print("_____URL  != URL____2")
    assert url1 != url2
    print(f'проверяем URL для перехода в личный кабинет ({url3} == https://lk.rt.ru/')
    assert url3 == 'https://lk.rt.ru/'
    print(f'Текст на странице "Личный кабинет" == {text_office}')
    assert text_office == 'Личный кабинет'
    print(f'Возвращенный URL  {url4} == "https://start.rt.ru/?tab=main"')
    assert url4 == 'https://start.rt.ru/?tab=main'
    print(f'На страцице URL {url4} есть ссылка с текстом {text_for_my}')
    assert text_for_my == 'Для меня'
    print(f'При нажатии на ссылку {text_for_my} страница открылась с URL {url5}')
    assert url5 == 'https://msk.rt.ru/'


def test_keys_17():
    """Проверка загрузки страницы авторизации
    на время( в независимости от скорости время загрузки не должно превышать 15 сек)"""

    datetime1, datetime2, url, text_auth, time1, time2, time3 = time_auth()

    print(f'Начало загрузки страницы time--{time1}--{datetime1}')
    print(f'Страница открыта УРЛ - {url}')
    print(f'На странице присутствует форма {text_auth} == Авторизация')
    assert text_auth == 'Авторизация'
    assert url == 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type'
    print(f'Проверяем два показателя время {time2} > {time1}')
    assert time2 > time1
    print(f'Разница между {time2} и {time1} <= 15.000000')
    assert time3 <= 15.000000


def test_keys_18():
    """На странице авторизации присутствует Тел. Службы поддержки 8 800 100 0 800"""

    phone = phone_support()
    print(f'Тел {phone} == 8 800 100 0 800')
    assert phone == '8 800 100 0 800'
