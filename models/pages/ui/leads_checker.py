from selene import browser, be, have
import allure
import time


class Checker:
    with allure.step('Открытие страницы Чекера'):
        def open_checker(self):
            browser.open('/app/phone-checker')

    with allure.step('Проверка отображения заголовка'):
        def check_header_elements(self):
            browser.element('.phone-checker-header__title').should(have.text('Checker'))
            browser.all('.phone-checker-offers__item').should(have.size(20))

    with allure.step('Проверка блока API-интеграция'):
        def check_block_api_integration(self):
            browser.element('#phone-checker-integration-token').should(be.not_.blank)
            browser.element('#popover-check-phones-request').should(be.not_.blank)
            browser.element('#popover-get-report-request').should(be.not_.blank)

    with allure.step('Ввод значений в поля'):
        def check_input_fields(self):
            browser.open('/app/phone-checker')
            browser.element( 'div.phone-checker-entry__field div.lds-input-placeholder input.lds-input-placeholder__field').type('12345678')
            browser.element('div.vs__selected-options input.vs__search').click()
            browser.element('#vs1__option-1').click()
            browser.element(
                'div.phone-checker-entry__field div.lds-input-placeholder input.lds-input-placeholder__field').click()
            browser.element('div.phone-checker-entry__field textarea.lds-input-placeholder__field').type('123')

    with allure.step('Проверка работы кнопки отправки'):
        def check_input_buttons(self):
            browser.element('//div[contains(@class, "phone-checker-entry__field_actions")]//button[contains(text(), "Очистить поле")]').click()
            browser.element('//span[text()="Номера телефонов (не более 10 000 номеров)"]/following-sibling::textarea').type(
                '123')
            browser.element(
                '//div[contains(@class, "phone-checker-entry__field_actions")]//button[contains(text(), "Отправить на проверку")]').click()
            browser.element('.phone-checker-history__item').should(be.not_.blank)

    with allure.step('Проверка скачивания'):
        def download_file(self):
            browser.element('.phone-checker-history__download').should(be.visible).click()
            time.sleep(10)


phone_checker = Checker()
