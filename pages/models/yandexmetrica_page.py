from selene import browser, by, be, command, have
import allure
import requests
import json
from selenium.common.exceptions import UnexpectedAlertPresentException
import os
import time



class MetricYandex:
    def open_metric_page(self):
        with allure.step('Открытие страницы'):
            browser.open('app/metric-transfer')
            time.sleep(10)

    def open_creation_modal_page(self):
        with allure.step('Открытие формы создания нового подключения'):
            browser.all('.lds-btn').element_by(have.text('Создать новое подключение')).click()
            browser.element('.title').should(be.visible)

    def insert_type_fields(self):
        with allure.step('Заполнение полей формы'):
            browser.all('.lds-input-placeholder').element_by(have.text('Название подключения')).element(
                '[type=text]').click().type('test123')
            browser.element('[type=search]').type('platform')
            browser.all('[role=option]').element(0).click()
            browser.element('[type=search]').type('platform')
            browser.all('[role=option]').element(1).click()
            browser.element('[type=search]').type('platform')
            browser.all('[role=option]').element(2).click()
            browser.all('.vs__selected').element_by(have.text('platform 1079761')).element('[type=button]').click()

            browser.all('.lds-input-placeholder').element_by(have.text('Номер счетчика Яндекс.Метрики')).element('[type=number]').type('12345678')
            browser.all('.lds-input-placeholder').element_by(have.text('Токен разработчика')).element(
                '[type=text]').click().type('test123')

            browser.all('.lds-input-placeholder').element_by(have.text('Идентификатор клиента')).element('[role=combobox]').click()
            browser.all('[role=option]').element(0).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Идентификатор клиента')).element(
                '[role=combobox]').click()
            browser.all('[role=option]').element(1).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Идентификатор цели')).element(
                '[type=text]').type('test1234')

    def check_high_tooltips(self):
        with allure.step('Проверка тултипов верхней части экрана'):
            browser.element('#dfnvl').click()
            browser.element('#bk1lg').click()
            browser.element('#\\32 506c').click()
            browser.element('#rly96').click()
            browser.element('#pusea').click()


    def check_filtres_for_request(self):
        with allure.step('Установка фильтров'):
            browser.all('.lds-input-placeholder').element_by(have.text('Тип события')).element('[role=combobox]').perform(command.js.scroll_into_view)
            browser.all('.lds-input-placeholder').element_by(have.text('Тип события')).element('[role=combobox]').click()
            browser.all('[role=option]').element(0).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Тип события')).element(
                '[role=combobox]').click()
            browser.all('[role=option]').element(1).click()
            browser.all('.vs__selected').element_by(have.text('Изменение выплаты')).element('[type=button]').click()
            browser.all('.lds-input-placeholder').element_by(have.text('Статус конверсии')).element('[role=combobox]').click().click()
            browser.all('[role=option]').element(0).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Статус конверсии')).element(
                '[role=combobox]').click()
            browser.all('[role=option]').element(1).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Статус конверсии')).element(
                '[role=combobox]').click()
            browser.all('[role=option]').element(2).click()
            browser.all('.vs__selected').element_by(have.text('Отклонена')).element('[type=button]').click()


    def check_aff_sub(self):
        with allure.step('Установка параметров'):
            browser.element(by.text('Добавить параметр aff_sub')).click().click()
            browser.element('#a9w8v').click()
            browser.element(by.text('Добавить параметр aff_sub')).should(be.visible).click()
            browser.all('.lds-input-placeholder').element_by(have.text('Название метки')).element('[type=search]').click()
            browser.all('[role=option]').element(0).click()
            browser.element('#n9v6k').click()
            browser.all('.lds-input-placeholder').element_by(have.text('Значение')).element('[type=text]').click().type('123')

    def check_low_tooltips(self):
        with allure.step('Проверка тултипов нижней части экрана'):
            browser.element('#pwwfp').click()
            browser.element('#vyhh0').click()
            browser.element('#brgl4').click()


    def check_saved(self):
        with allure.step('Сохранение подключения'):
            browser.all('.lds-btn').element_by(have.text('Сохранить')).click()
            browser.element('div.connection-list__header-container').should(be.visible)

    def check_buttons(self):
        with allure.step('Проверка работы кнопок рядом с созданным подключением'):
           element = browser.element('#g2b01')
           element.hover()
           element.click()
           browser.element('.leads-notify-content').should(be.visible)
           element.click()
           browser.element('.leads-notify-content').should(be.visible)
           browser.element('#wzy4z').hover().click()
           browser.element(by.text('Передача конверсий')).click()
           browser.element(r'#\39 kj8v').hover().click()
           try:
               alert = browser.driver.switch_to.alert
               print(f"Alert text: {alert.text}")
               alert.accept()
           except UnexpectedAlertPresentException:
               print("Всплывающий alert обработан корректно")
           browser.element('.leads-notify-content').should(be.visible)

    def check_filters(self):
        with allure.step('Проверка работы фильтров'):
            browser.execute_script("window.scrollBy(0, 300);")
            browser.element('.mx-input-wrapper').should(be.visible)
            dates = browser.element(r'#\0032 e1ao')
            dates.click()
            browser.all('.mx-calendar-header-label').element_by(have.text('2024')).click()
            browser.all('.mx-calendar-content').element_by(have.text('2024')).click()
            browser.element(by.text('нояб.')).click()
            browser.element('[title="2024-11-06"]').click()
            browser.element('[title="2024-11-19"]').click()
            browser.element('.statistic-table__item').should(be.visible)
            browser.element(by.text('22ab7617c4a62b46be61')).with_(timeout=5).should(be.visible)
            dates.click()
            browser.element('[title="2024-11-05"]').click()
            browser.element('[title="2024-11-20"]').click()
            browser.element(by.text('22ab7617c4a62b46be61')).with_(timeout=5).should(be.not_.present)
            send_status = browser.element('#x5owa')
            send_status.click()
            browser.all('[role=option]').element(1).click()
            browser.element(by.text('673c0b63daaff24c0b51')).should(be.visible)
            send_status.click()
            browser.all('[role=option]').element(2).click()
            browser.element(by.text('1f78435c3bcf753e071b')).should(be.visible)
            send_status.click()
            browser.all('[role=option]').element(3).click()
            browser.element(by.text('22ab7617c4a62b46be61')).with_(timeout=5).should(be.not_.present)
            send_status.click()
            browser.all('[role=option]').element(0).click()
            load_status = browser.element('#fygic')
            load_status.click()
            browser.all('[role=option]').element(1).click()
            browser.element(by.text('673c0b63daaff24c0b51')).with_(timeout=5).should(be.visible)
            load_status.click()
            browser.all('[role=option]').element(2).click()
            browser.element(by.text('1f78435c3bcf753e071b')).with_(timeout=5).should(be.visible)
            load_status.click()
            browser.all('[role=option]').element(3).click()
            load_status.click()
            browser.all('[role=option]').element(0).click()
            id_connection = browser.element('#my47a')
            id_connection.click().type('279939')
            browser.element(by.text('279939')).with_(timeout=5).should(be.visible)

    def check_download(self):
        with allure.step('Проверка скачивания отчёта'):
            download_button = browser.element('#gy4l4')
            download_button.click()
            url = "http://webmaster.dev-qa.leads/metricTransfer/transferTask/export"
            payload = json.dumps({
                "offset": 0,
                "limit": 5
            })
            headers = {
                'Content-Type': 'application/json',
                'Cookie': 'user=f4b6e08f86d091b54f21bd56f2b662ee'
            }
            response = requests.post(url, headers=headers, data=payload)

            file_path = r"C:\Users\Timur\PycharmProjects\cabinet-test_python\resources\metric.xslx"

        with open(file_path, "wb") as file:
            file.write(response.content)

        if os.path.exists(file_path):
            os.remove(file_path)

yandex_metric = MetricYandex()
