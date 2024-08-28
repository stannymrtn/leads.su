import allure
from selene import browser, be, have, command


class OffersPage:
        @staticmethod
        def open_page():
            with allure.step('Открытие каталога офферов'):
                browser.open('/offers/default')
                browser.element('//div[contains(text(), "Список офферов")]').should(be.visible)

        @staticmethod
        def scroll_page():
            with allure.step('Проверка скролла на странице'):
                element = browser.element('.footer-next__phone')
                element.perform(command.js.scroll_into_view)
                element.should(have.text('+7 (800) 500-8344'))

        @staticmethod
        def check_pin_offer():
            with allure.step('Скролл наверх и проверка закреплённого оффера вверху каталога'):
                element = browser.element('//img[contains(@src, "10945")]')
                element.perform(command.js.scroll_into_view)
                element.should(be.visible)

        @staticmethod
        def check_offer():
            with allure.step('Поиск оффера 1051'):
                element = browser.element('//img[contains(@src, "1051")]')
                element.perform(command.js.scroll_into_view)
                element.should(be.visible)


        @staticmethod
        def add_to_favorite():
            with allure.step('Добавить оффер в избранное'):
                browser.element('[href="/offers/1051/default/favorite"]').click()

        @staticmethod
        def check_favorites():
            with allure.step('Проверка добавления оффера в избранное'):
                browser.open('/offers/default/favoriteOffers')
                browser.element('//img[contains(@src, "1051")]').should(be.visible)
                browser.element('[href="/offers/1051/default/favorite"]').click()
                browser.element('//a[span[text()="В избранное"]]').should(be.visible)


offer_page = OffersPage()
