import allure
from allure_commons.types import Severity
from pages.leads_autorization_page import authentication_form
from pages.leads_checker_page import phone_checker
from pages.models.generation_token import generation_token
from pages.offers_page import offer_page


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Авторизация ЛКВ")
@allure.story("Тестирование формы авторизации ЛКВ")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_authorization(setup_browser):
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
@allure.story("Тестирование скролла на странице и добавления оффера в избранное")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_offer_page():
    authentication_form.open()
    authentication_form.logpass_enter()
    offer_page.open_page()
    offer_page.scroll_page()
    offer_page.check_pin_offer()
    offer_page.check_offer()
    offer_page.add_to_favorite()
    offer_page.check_favorites()
