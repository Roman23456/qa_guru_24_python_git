import os
import time
from selene import browser, have, be

def test_automation_form(browser):
    # Открываем браузер
    browser.open('/automation-practice-form')

    # Удаляем баннеры
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('#footer').remove()")

    # 1. Заполняем имя и фамилию
    browser.element('#firstName').type('Иван')
    browser.element('#lastName').type('Иванович')

    # 2. Вводим email
    browser.element('#userEmail').type('ivan_ivanovich@gmail.com')

    # 3. Выбираем пол
    browser.element('[for="gender-radio-1"]').click()

    # 4. Вводим номер телефона
    browser.element('#userNumber').type('7988995876')

    # 5. Выбираем дату рождения через календарь
    browser.element('#dateOfBirthInput').click()

    # Выбираем год
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select').all('option').element_by(have.text('1994')).click()

    # Выбираем месяц
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select').all('option').element_by(have.text('August')).click()

    # Выбираем день
    browser.element('.react-datepicker__day--012').click()

    # 6. Вводим subject
    browser.element('#subjectsInput').type('Computer Science')
    browser.element('.subjects-auto-complete__menu').element('div').click()

    # 7. Выбираем хобби
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Загружаем файл — используем send_keys() вместо set_value()
    browser.element('#uploadPicture').set_value(os.path.abspath('image/test_1.pdf'))

    # Записываем адрес
    browser.element('#currentAddress').type('г. Рязань, ул. Жмайлова, д. 19')

    # Выбираем State and City
    browser.element('#react-select-3-input').type('Haryana')
    browser.element('[id^="react-select-3-option-"]').click()

    browser.element('#react-select-4-input').type('Panipat')
    browser.element('[id^="react-select-4-option-"]').click()

    # Отправляем форму
    browser.element('#submit').click()

    # Проверка: модальное окно появилось
    modal_content = browser.element('.modal-content')
    modal_content.should(be.visible).should(have.text('Thanks for submitting the form'))

    # Ждём, пока таблица загрузится
    table = browser.element('.table-responsive')
    table.should(be.visible)

    # Проверяем заполненные поля в модальном окне
    table.should(have.text('Иван Иванович'))
    table.should(have.text('ivan_ivanovich@gmail.com'))
    table.should(have.text('Male'))
    table.should(have.text('7988995876'))
    table.should(have.text('12 August,1994'))
    table.should(have.text('Computer Science'))
    table.should(have.text('Music'))
    table.should(have.text('test_1.pdf'))
    table.should(have.text('г. Рязань, ул. Жмайлова, д. 19'))
    table.should(have.text('Haryana Panipat'))

    # Закрываем модалку
    browser.element('#closeLargeModal').click()