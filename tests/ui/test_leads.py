import allure
from allure_commons.types import Severity
from models.pages.ui.leads_autorization_page import authentication_form
from models.pages.ui.leads_checker import phone_checker
from models.pages.ui.pin_offer import pin_offer
from models.pages.ui.generation_token import generation_token
from models.pages.ui.offer_add_to_favorite import add_to_favorite

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Авторизация ЛКВ")
@allure.story("Тестирование формы авторизации ЛКВ")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_autorization(setup_browser):
    authentication_form.open()
    authentication_form.logpass_enter()
    authentication_form.check_id()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Чекер")
@allure.story("Тестирование отправки запроса и скачивания отчёта")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_checker():
    authentication_form.open()
    authentication_form.logpass_enter()
    phone_checker.open_checker()
    phone_checker.check_header_elements()
    phone_checker.check_block_api_integration()
    phone_checker.check_input_fields()
    phone_checker.check_input_buttons()
    phone_checker.download_file()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Каталог офферов")
@allure.story("Тестирование закреплённого оффера")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_pin_offer():
    authentication_form.open()
    authentication_form.logpass_enter()
    pin_offer.open_offers_page()
    pin_offer.scroll_page()
    pin_offer.check_pin_offer()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Информация об аккаунте")
@allure.story("Тестирование генерации api-токена")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_generation_token():
    authentication_form.open()
    authentication_form.logpass_enter()
    generation_token.open_account_page()
    generation_token.press_key()
    generation_token.check_message()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Каталог офферов")
@allure.story("Тестирование добавления оффера в избранное")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_add_to_favorite_offer():
    authentication_form.open()
    authentication_form.logpass_enter()
    add_to_favorite.open_page()
    add_to_favorite.check_offer()
    add_to_favorite.add_to_favorite()
    add_to_favorite.check_favorites()
