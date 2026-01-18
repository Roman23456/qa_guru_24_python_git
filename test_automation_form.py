import os
import pytest
from selene import have


def test_automation_form(browser):
    # Открываем браузер
    browser.open('/automation-practice-form')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

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
    browser.element('.react-datepicker__year-select') \
        .all('option') \
        .element_by(have.text('1994')) \
        .click()

    # Выбираем месяц
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select') \
        .all('option') \
        .element_by(have.text('August')) \
        .click()

    # Выбираем день
    browser.element('.react-datepicker__day--012').click()

    # 6. Вводим subject
    browser.element('#subjectsInput').type('Computer Science')
    browser.element('.subjects-auto-complete__menu').element('div').click()

    # 7. Выбираем хобби
    browser.element('[for="hobbies-checkbox-3"]').click()

    # Загружаем файл
    browser.element('#uploadPicture').set_value(os.path.abspath('image/test 3.pdf'))  # Путь к файлу

    # Записываем адрес
    browser.element('#currentAddress').type('г. Рязань, ул. Жмайлова, д. 19')

    # Выбираем State and City
    browser.element('#react-select-3-input').type('Haryana')
    browser.element('[id^="react-select-3-option-"]').click()

    browser.element('#react-select-4-input').type('Panipat')
    browser.element('[id^="react-select-4-option-"]').click()

    browser.element('#submit').click()

    # Проверка модалки с подтверждением
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))

    # Проверяем заполненные поля в модальном окне
    browser.element('.table-responsive').should(have.text('Иван Иванович'))
    browser.element('.table-responsive').should(have.text('ivan_ivanovich@gmail.com'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('7988995876'))
    browser.element('.table-responsive').should(have.text('12 August,1994'))
    browser.element('.table-responsive').should(have.text('Computer Science'))
    browser.element('.table-responsive').should(have.text('Music'))
    browser.element('.table-responsive').should(have.text('test 3.pdf'))
    browser.element('.table-responsive').should(have.text('г. Рязань, ул. Жмайлова, д. 19'))
    browser.element('.table-responsive').should(have.text('Haryana Panipat'))

    # Закрываем модалку
    browser.element('#closeLargeModal').click()


