import allure
from selene import browser, be, command

class Add_to_favorite:

    with allure.step('Открытие каталога офферов'):
        def open_page(self):
            browser.open('/offers/default')
            browser.element('//div[contains(text(), "Список офферов")]').should(be.visible)

    with allure.step('Поиск оффера 1051'):
        def check_offer(self):
            element = browser.element('//img[contains(@src, "1051")]')
            element.perform(command.js.scroll_into_view)
            element.should(be.visible)

    with allure.step('Добавить оффер в избранное'):
        def add_to_favorite(self):
            browser.element('[href="/offers/1051/default/favorite"]').click()

    with allure.step('Проверка добавления оффера в избранное'):
        def check_favorites(self):
            browser.open('/offers/default/favoriteOffers')
            browser.element('//img[contains(@src, "1051")]').should(be.visible)
            browser.element('[href="/offers/1051/default/favorite"]').click()
            browser.element('//a[span[text()="В избранное"]]').should(be.visible)


add_to_favorite = Add_to_favorite()
