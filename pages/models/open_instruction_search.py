import allure
from selene import browser, be


class Instructions:
    @staticmethod
    def search_field():
        with allure.step('Проверка ввода в строку поиска'):
            browser.open('/help/instruction/view/instrukcija-vebmastera')
            browser.element('div.search-input input[name="query"]').send_keys('Типы трафика').press_enter()

    @staticmethod
    def check_search():
        with allure.step('Проверка результата'):
            browser.element('[href="/help/instruction/view/tipy-trafika"]').should(be.visible)


instructions = Instructions()