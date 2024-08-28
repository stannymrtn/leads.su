import allure
from selene import browser, be, have, command


class OffersPage:
    with allure.step('Открытие каталога офферов'):
        @staticmethod
        def open_page():
            browser.open('/offers/default')
            browser.element('//div[contains(text(), "Список офферов")]').should(be.visible)

    with allure.step('Проверка скролла на странице'):
        @staticmethod
        def scroll_page():
            element = browser.element('.footer-next__phone')
            element.perform(command.js.scroll_into_view)
            element.should(have.text('+7 (800) 500-8344'))

    with allure.step('Скролл наверх и проверка закреплённого оффера вверху каталога'):
        @staticmethod
        def check_pin_offer():
            element = browser.element('//img[contains(@src, "10945")]')
            element.perform(command.js.scroll_into_view)
            element.should(be.visible)

    with allure.step('Поиск оффера 1051'):
        @staticmethod
        def check_offer():
            element = browser.element('//img[contains(@src, "1051")]')
            element.perform(command.js.scroll_into_view)
            element.should(be.visible)

    with allure.step('Добавить оффер в избранное'):
        @staticmethod
        def add_to_favorite():
            browser.element('[href="/offers/1051/default/favorite"]').click()

    with allure.step('Проверка добавления оффера в избранное'):
        @staticmethod
        def check_favorites():
            browser.open('/offers/default/favoriteOffers')
            browser.element('//img[contains(@src, "1051")]').should(be.visible)
            browser.element('[href="/offers/1051/default/favorite"]').click()
            browser.element('//a[span[text()="В избранное"]]').should(be.visible)


offer_page = OffersPage()
