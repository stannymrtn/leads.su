from selene import browser, by, be, command
import allure


class MetricYandex:
    @staticmethod
    def open_metric_page():
        with allure.step('Открытие страницы'):
            browser.open('app/metric-transfer')
            browser.element('div.connection-list__header-container').should(be.visible)

    @staticmethod
    def open_creation_modal_page():
        with allure.step('Открытие формы создания нового подключения'):
            browser.element('#hgcj4').click()
            browser.element('.title').should(be.visible)

    @staticmethod
    def insert_type_fields():
        with allure.step('Заполнение полей формы'):
            browser.element('#n8n36').type('test')
            for option in ['#vs5__option-1', '#vs5__option-2', '#vs5__option-3']:
                browser.element('#vs5__combobox').click()
                browser.element(option).click()
            browser.element('button.vs__deselect').click()
            browser.element('#r0v5h').type('12345678')
            browser.element('#vlgba').type('123test')
            browser.element('#vs6__combobox').click()
            browser.element('#vs6__option-0').click()
            browser.element('#vs6__combobox').click()
            browser.element('#vs6__option-1').click()
            browser.element('#lmex3').type('123Test123')

    @staticmethod
    def check_filtres_for_request():
        with allure.step('Установка фильтров'):
            browser.element('#yylhf').click().perform(command.js.scroll_into_view)
            for option in ['#vs7__option-0', '#vs7__option-1']:
                browser.element('#yylhf').click()
                browser.element(option).click()
            browser.element('//div[@id="21wu0"]').click().click()
            browser.element('#vs8__option-0').click()
            browser.element('//div[@id="21wu0"]').click()
            browser.element('#vs8__option-1').click()
            browser.element('//div[@id="21wu0"]').click()
            browser.element('#vs8__option-2').click()

    @staticmethod
    def check_aff_sub():
        with allure.step('Установка параметров'):
            browser.element(by.text('Добавить параметр aff_sub')).click().click()
            browser.element('#vs9__combobox').click()
            browser.element('#vs9__option-0').click()
            browser.element('#p5qhp').type('123')
            browser.element('#n9v6k').click()

    @staticmethod
    def check_save():
        with allure.step('Сохранение подключения'):
            browser.element('#y6sr4').click()
            browser.element('div.connection-list__header-container').should(be.visible)


yandex_metric = MetricYandex()
