from selene import browser, be, have, by
import allure


class Checker:
    with allure.step('Открытие страницы Чекера'):
        @staticmethod
        def open_checker():
            browser.open('/app/phone-checker')

    with allure.step('Проверка отображения заголовка'):
        @staticmethod
        def check_header_elements():
            browser.element('.phone-checker-header__title').should(have.text('Checker'))
            browser.all('.phone-checker-offers__item').should(have.size(20))

    with allure.step('Проверка блока API-интеграция'):
        @staticmethod
        def check_block_api_integration():
            browser.element('#phone-checker-integration-token').should(be.not_.blank)
            browser.element('#popover-check-phones-request').should(be.not_.blank)
            browser.element('#popover-get-report-request').should(be.not_.blank)

    with allure.step('Ввод значений в поля'):
        @staticmethod
        def check_input_fields():
            browser.open('/app/phone-checker')
            browser.element(
                'div.phone-checker-entry__field div.lds-input-placeholder input.lds-input-placeholder__field').type(
                '12345678')
            browser.element('div.vs__selected-options input.vs__search').click()
            browser.element('#vs1__option-1').click()
            browser.element(
                'div.phone-checker-entry__field div.lds-input-placeholder input.lds-input-placeholder__field').click()
            browser.element('div.phone-checker-entry__field textarea.lds-input-placeholder__field').type('123')

    with allure.step('Проверка работы кнопки отправки'):
        @staticmethod
        def check_input_buttons():
            browser.element(by.text('Очистить поле')).click()
            browser.element('div.phone-checker-entry__field textarea.lds-input-placeholder__field').type('123')
            browser.element(by.text('Отправить на проверку')).click()
            browser.element('.phone-checker-history__item').should(be.not_.blank)

    with allure.step('Проверка скачивания'):
        @staticmethod
        def download_file():
            browser.element('.phone-checker-history__download').should(be.visible).click()


phone_checker = Checker()
