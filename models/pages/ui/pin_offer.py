from selene import browser, have, by, be, command
import time
import allure


class Pin_offer:
    with allure.step('Открытие каталога офферов'):
        def open_offers_page(self):
            browser.open('/offers/default')
            browser.element('//div[text()="Список офферов"]').should(be.visible)

    with allure.step('Проверка скролла на странице'):
        def scroll_page(self):
            element = browser.element('.footer-next__phone')
            element.perform(command.js.scroll_into_view)
            element.should(have.text('+7 (800) 500-8344'))
            time.sleep(10)

    with allure.step('Скролл наверх и проверка закреплённого оффера вверху каталога'):
        def check_pin_offer(self):
            element = browser.element('//img[contains(@src, "10945")]')
            element.perform(command.js.scroll_into_view)
            element.should(be.visible)


pin_offer = Pin_offer()
