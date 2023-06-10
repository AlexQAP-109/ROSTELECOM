from selenium import webdriver
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium.webdriver.common.by import By

import time
from datetime import datetime
import pytest
"""МЕТОДЫ ДЛЯ ТЕСТ КЕЙС"""
"""Валидные личные данные пользователя"""
class MyAuth():
    load_dotenv()

    valid_email = os.getenv("valid_email")
    valid_password = os.getenv("valid_password")
    valid_phone = os.getenv("valid_phone")
    valid_login = os.getenv("valid_login")



"""Т-К №1..МЕТОД НА ПРОВЕРКУ ПОЛЯ МОБИЛЬНЫЙ ТЕЛЕФОН, ПАРОЛЬ, ЧЕК БОКС С ЗАРЕГЕСТРИРОВАННЫМ ПОЛЬЗОВАТЕЛЕМ"""

def pole_mobil_phone():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """ Ввод в поле моб. телефон валидные данные пользователя"""
    pole_phone = browser.find_element(By.XPATH, '//*[@id="username"]')
    pole_phone.send_keys(MyAuth.valid_phone)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        nach_span = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_phone:
                nach_span.append(i.text)
            else:
                musor.append(i.text)
    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)

    return nach_span[0], pasw[0], chec_box

""" Т-К №2  МЕТОД НА ПРОВЕРКУ КНОПКИ "ВОЙТИ" С ЗАРЕГЕСТРИРОВАННЫМ ПОЛЬЗОВАТЕЛЕМ ПО ТЕЛЕФОНУ"""

def button_voyti():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """ Ввод в поле моб. телефон валидные данные пользователя"""
    pole_phone = browser.find_element(By.XPATH, '//*[@id="username"]')
    pole_phone.send_keys(MyAuth.valid_phone)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        mob_phone = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_phone:
                mob_phone.append(i.text)
            else:
                musor.append(i.text)
    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза проверяем функциональность"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    url2 = browser.current_url

    return mob_phone[0], pasw[0], chec_box, url1, url2

"""Т-К №3..МЕТОД НА ПРОВЕРКУ ПОЛЯ ПОЧТА, ПАРОЛЬ, ЧЕК БОКС С ЗАРЕГЕСТРИРОВАННЫМ ПОЛЬЗОВАТЕЛЕМ"""

def pole_email():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Меняем форму заполнения с телефон на почту"""
    vkladka_email = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]')
    vkladka_email.click()

    """ Ввод в поле email валидные данные пользователя"""
    pole_mail = browser.find_element(By.XPATH, '//*[@id="username"]')
    pole_mail.send_keys(MyAuth.valid_email)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        mail = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_email:
                mail.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим пароль для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)

    return mail[0], pasw[0], chec_box

""" Т-К №4  МЕТОД НА ПРОВЕРКУ КНОПКИ "ВОЙТИ" С ЗАРЕГЕСТРИРОВАННЫМ ПОЛЬЗОВАТЕЛЕМ ПО ПОЧТЕ"""

def button_voyti_mail():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Меняем форму заполнения с телефон на почту"""
    vkladka_email = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]')
    vkladka_email.click()

    """ Ввод в поле email валидные данные пользователя"""
    pole_mail = browser.find_element(By.XPATH, '//*[@id="username"]')
    pole_mail.send_keys(MyAuth.valid_email)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        mail = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_email:
                mail.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    url2 = browser.current_url

    return mail[0], pasw[0], chec_box, url1, url2

"""Т-К №5 ПРОВЕРКА ВКЛАДОК НА ФУНКЦИОНАЛЬНОСТЬ МОБ. ТЕЛ, ПОЧТА, ЛОГИН, ЛИЦЕВОЙ СЧЕТ"""

def vkladki_forma():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Меняем форму заполнения с телефон на почту"""
    vkladka_email = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]')
    vkladka_email.click()
    """Возвращаем текст пустого поля почты"""

    vkladka_email_text1 = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    text1 = vkladka_email_text1.text

    """Меняем форму заполнения с почты на логин"""
    vkladka_login = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]')
    vkladka_login.click()
    """Возвращаем текст пустого поля логин"""
    vkladka_login_text2 = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    text2 = vkladka_login_text2.text

    """Меняем форму заполнения с логин на лицевой счет"""
    vkladka_check = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-ls"]')
    vkladka_check.click()

    """возвращаем текст пустого поля со счетом"""
    vkladka_check_text3 = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    text3 = vkladka_check_text3.text

    """Меняем форму заполнения с  лицевой счет телефон"""
    vkladka_phone = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-phone"]')
    vkladka_phone.click()
    """Возвращаем текст пустого поля телефон"""
    vkladka_phone_text4 = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    text4 = vkladka_phone_text4.text

    return text1, text2, text3, text4


"""Т-К №6 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ПОЛЯ "Пароль" в форме регистрации в скрытом и открытом режиме"""
def password_hide():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys('1234567')

    """Количество символов"""
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        simvol = []
        for i in teg_span:
            if i.text == '1234567':
                simvol.append(i.text)

        summa = len(simvol[0])

    """Записываем файл с html, открываем и парсим """
    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('input')
        types = []
        for i in teg_span:
            if i == teg_span[3]:
                types.append(i)

        types2 = str(types).split(' ')

    """Нажимем на глазик"""
    pole_pass2 = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/div[2]')
    pole_pass2.click()

    """Записываем и открываем фаил для парсинга"""
    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('input')
        types3 = []
        for i in teg_span:
            if i == teg_span[3]:
                types3.append(i)

    types3 = str(types3).split(' ')
    """Выводит два типа с глазиком и без глазика(type="password и 'type="text) длину пароля и сам пароль"""
    return types2[7], simvol[0], summa, types3[7]


"""T-К №7 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ССЫЛКИ "Пользовательское соглашение" в форме авторизации."""

def linc_terms_of_use():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    link_soglachenie = browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    """Возвращаем текущий урл."""
    Url1 = browser.current_url
    link_soglachenie.click()
    """Возвращаем текущий урл"""
    Url2 = browser.current_url
    return Url1, Url2


"""Т-К №8 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ССЫЛКИ "Забыл пароль"  в форме авторизации"""

def linc_forgot_password():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    linc_pass = browser.find_element(By.XPATH, '//*[@id="forgot_password"]')
    Url1 = browser.current_url
    linc_pass.click()
    Url2 = browser.current_url
    return Url1, Url2


"""Т-К №9 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ИКОНКИ "Вконтакте" в форме авторизации."""
def linc_vk():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    vk = browser.find_element(By.XPATH, '//*[@id="oidc_vk"]')
    Url1 = browser.current_url
    vk.click()
    Url2 = browser.current_url
    return Url1, Url2


"""Т-К №10 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ИКОНКИ "Однокласники" в форме авторизации."""
def linc_odnoklasniki():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    ok = browser.find_element(By.XPATH, '//*[@id="oidc_ok"]')
    Url1 = browser.current_url
    ok.click()
    Url2 = browser.current_url
    return Url1, Url2


"""Т-К №11 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ИКОНКИ "Мой мир" в форме авторизации."""
def linc_mail_ru():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    mall = browser.find_element(By.XPATH, '//*[@id="oidc_mail"]')
    Url1 = browser.current_url
    mall.click()
    Url2 = browser.current_url
    return Url1, Url2


"""Т-К №12 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ИКОНКИ "Яндекс" в форме авторизации."""
def linc_yandex():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    ya = browser.find_element(By.XPATH, '//*[@id="oidc_ya"]')
    Url1 = browser.current_url
    ya.click()
    Url2 = browser.current_url
    return Url1, Url2

"""Т-К №13 ПРОВЕРКА ФУНКЦИОНАЛЬНОСТИ ССЫЛКИ "Зарегистрироваться" в форме авторизации."""
def linc_register():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    register = browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    Url1 = browser.current_url
    register.click()
    Url2 = browser.current_url
    return Url1, Url2


"""Т-К №14 ПРОВЕРКА АВТОРИЗАЦИИ зарегистрированого
 пользователя( вход в личный аккаунт пользователя по номеру телефона)"""

def auth_phone():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """ Ввод в поле Мой телефон валидные данные пользователя"""
    my_phone = browser.find_element(By.XPATH, '//*[@id="username"]')
    my_phone.send_keys(MyAuth.valid_phone)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        phone = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_phone:
                phone.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    """Записываем урл"""
    url2 = browser.current_url
    """Вход в личный кабинет"""
    my_office = browser.find_element(By.XPATH, '//*[@id="lk-btn"]')
    my_office.click()
    url3 = browser.current_url

    text_my_office = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[3]')
    text = text_my_office.text
    url4 = browser.current_url
    """Возвращаем: номер телефона, пароль, вкл чекбокс, изначальный УРЛ, УРЛ после нажатия на кнопку,
    УРЛ - переход, Текст Личный кабинет, УРЛ - личного кабинета"""
    return phone[0], pasw[0], chec_box, url1, url2, url3, text, url4



"""Т-К №15 ПРОВЕРКА АВТОРИЗАЦИИ зарегистрированого пользователя( вход в личный кабинет пользователя по email)"""

def auth_maill():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Меняем форму заполнения с телефон на почту"""
    vkladka_email = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-mail"]')
    vkladka_email.click()

    """ Ввод в поле email валидные данные пользователя"""
    pole_mail = browser.find_element(By.XPATH, '//*[@id="username"]')
    pole_mail.send_keys(MyAuth.valid_email)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        mail = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_email:
                mail.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    """Записываем урл"""
    url2 = browser.current_url
    """Вход в личный кабинет"""
    my_office = browser.find_element(By.XPATH, '//*[@id="lk-btn"]')
    my_office.click()
    url3 = browser.current_url

    text_my_office = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[3]')
    text = text_my_office.text
    url4 = browser.current_url
    """Возвращаем: номер телефона, пароль, вкл чекбокс, изначальный УРЛ, УРЛ после нажатия на кнопку,
    УРЛ - переход, Текст Личный кабинет, УРЛ - личного кабинета"""
    return mail[0], pasw[0], chec_box, url1, url2, url3, text, url4


"""Т-К №16 ПРОВЕРКА АВТОРИЗАЦИИ ЗАРЕГИСТРИРОВАНОГО пользователя( вход в личный кабинет пользователя по login)"""

def auth_login():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Меняем форму заполнения с почты на логин"""
    vkladka_login = browser.find_element(By.XPATH, '//*[@id="t-btn-tab-login"]')
    vkladka_login.click()

    """ Ввод в поле логин  валидные данные пользователя"""
    pole_login = browser.find_element(By.XPATH, '//*[@id="username"]')
    pole_login.send_keys(MyAuth.valid_login)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        login = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_login:
                login.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    """Записываем урл"""
    url2 = browser.current_url
    """Вход в личный кабинет"""
    my_office = browser.find_element(By.XPATH, '//*[@id="lk-btn"]')
    my_office.click()
    url3 = browser.current_url

    text_my_office = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[3]')
    text = text_my_office.text
    url4 = browser.current_url
    """Возвращаем: номер телефона, пароль, вкл чекбокс, изначальный УРЛ, УРЛ после нажатия на кнопку,
    УРЛ - переход, Текст Личный кабинет, УРЛ - личного кабинета"""
    return login[0], pasw[0], chec_box, url1, url2, url3, text, url4


"""МЕТОДЫ на автоматизацию user story №1 «Ростелеком Информационные Технологии»"""

def user_story_1():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Возврат текущего урл"""
    url = browser.current_url

    """Обращаемся к форме авторизации и выводим текст формы"""
    forma_autch = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    text_auth = forma_autch.text

    """В форме авторизации отображается телефон пользователя"""
    """ Ввод в поле Мой телефон валидные данные пользователя"""
    my_phone = browser.find_element(By.XPATH, '//*[@id="username"]')
    my_phone.send_keys(MyAuth.valid_phone)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        phone = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_phone:
                phone.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    """Записываем урл"""
    url2 = browser.current_url
    """Вход в личный кабинет"""
    my_office = browser.find_element(By.XPATH, '//*[@id="lk-btn"]')
    my_office.click()
    url3 = browser.current_url

    text_my_office = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[3]')
    text_office = text_my_office.text
    url4 = browser.current_url

    """Обращаемся к полю (Посмотреть все документы по моим лицевым счетам)"""
    vse_doc_po_chetam = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/p')
    text_vse_dok = vse_doc_po_chetam.text

    """Возвращаем: номер телефона, пароль, вкл чекбокс, изначальный УРЛ, УРЛ после нажатия на кнопку,
    УРЛ - переход, Текст Личный кабинет, УРЛ - личного кабинета, текст все доки """
    return url, url1, url2, url3, url4, text_auth, text_office, text_vse_dok, phone[0], pasw[0], chec_box



"""МЕТОДЫ на автоматизацию user story №2 «Ростелеком Информационные Технологии»"""

def user_story_2():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Возврат текущего урл"""
    url = browser.current_url

    """Обращаемся к форме авторизации и выводим текст формы"""
    forma_autch = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    text_auth = forma_autch.text

    """В форме авторизации отображается телефон пользователя"""
    """ Ввод в поле Мой телефон валидные данные пользователя"""
    my_phone = browser.find_element(By.XPATH, '//*[@id="username"]')
    my_phone.send_keys(MyAuth.valid_phone)
    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        span = soup.find_all('span')
        phone = []
        musor = []
        for i in span:
            if i.text == MyAuth.valid_phone:
                phone.append(i.text)
            else:
                musor.append(i.text)

    """ Ввод в поле пароль валидные данные пользователя"""
    pole_pass = browser.find_element(By.XPATH, '//*[@id="password"]')
    pole_pass.send_keys(MyAuth.valid_password)

    """Записываем файл с html, открываем и парсим номер телефона для сравнения в тесте"""

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('span')
        pasw = []
        for i in teg_span:
            if i.text == MyAuth.valid_password:
                pasw.append(i.text)

    """Так как чек бокс по умолчанию нажат, кликаем два раза"""
    chek_box = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/span[1]')
    chek_box.click()
    chek_box.click()

    with open('index_selenium_html', 'w', encoding='utf8') as file:
        file.write(browser.page_source)
    with open('index_selenium_html', encoding='utf8') as file:
        teg = file.read()
        soup = BeautifulSoup(teg, 'lxml')
        teg_span = soup.find_all('svg')
        chec_box = []
        for i in teg_span:
            if i == teg_span[3]:
                chec_box.append(i)
    """Записываем УРЛ"""
    url1 = browser.current_url
    """Нажимаем на кнопку Войти"""
    button = browser.find_element(By.XPATH, '//*[@id="kc-login"]')
    button.click()
    """Записываем урл"""
    url2 = browser.current_url
    """Вход в личный кабинет"""
    my_office = browser.find_element(By.XPATH, '//*[@id="lk-btn"]')
    my_office.click()
    url3 = browser.current_url

    text_my_office = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[3]')
    text_office = text_my_office.text
    url4 = browser.current_url

    """Обращаемся к ссылке (для меня) и выводим текст"""
    """Нажимаем на ссылку для меня и осуществляем переход"""
    """Возвращаем урл"""
    for_my = browser.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/p')
    text_for_my = for_my.text
    for_my.click()
    url5 = browser.current_url


    """Возвращаем: номер телефона, пароль, вкл чекбокс, изначальный УРЛ, УРЛ после нажатия на кнопку,
    УРЛ - переход, Текст Личный кабинет, УРЛ - личного кабинета, текст все доки """
    return url, url1, url2, url3, url4, url5, text_auth, text_office, text_for_my, phone[0], pasw[0], chec_box


"""Т-К №17 Метод на Проверку загрузки страницы авторизации на время"""
def time_auth():
    time1 = time.time()
    datetime1 = datetime.now().time()
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Возврат текущего урл"""
    url = browser.current_url

    """Обращаемся к форме авторизации и выводим текст формы"""
    forma_autch = browser.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    text_auth = forma_autch.text

    datetime2 = datetime.now().time()
    time2 = time.time()
    time3 = time2 - time1

    return datetime1, datetime2, url, text_auth, time1, time2, time3

"""Т-К №18 МЕТОД НА ПРОВЕРКУ страницы Авторизации присутствует Тел. Службы поддержки 8 800 100 0 800"""
def phone_support():
    browser = webdriver.Chrome()
    browser.set_window_size(1200, 800)
    browser.implicitly_wait(10)
    browser.get("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=1e59f178-633e-4a0f-aaf6-7aac572afb42&theme&auth_type")

    """Обращаемся в подвал и выводим телефон поддержки"""
    phone_suport = browser.find_element(By.XPATH, '//*[@id="app-footer"]/div[2]/a')
    phone = phone_suport.text

    return phone