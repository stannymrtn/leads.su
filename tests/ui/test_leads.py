import allure
from allure_commons.types import Severity
from pages.leads_autorization_page import authentication_form
from pages.leads_checker_page import phone_checker
from pages.models.generation_token import generation_token
from pages.offers_page import offer_page
from pages.models.open_instruction_search import instructions
from pages.models.postback_page import postback
from pages.models.yandexmetrica_page import yandex_metric


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Авторизация ЛКВ")
@allure.story("Тестирование формы авторизации ЛКВ")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_authorization(setup_browser):
    authentication_form.open()
    authentication_form.pass_enter()
    authentication_form.check_id()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Чекер")
@allure.story("Тестирование отправки запроса и скачивания отчёта")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_checker():
    authentication_form.open()
    authentication_form.pass_enter()
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
    authentication_form.pass_enter()
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
    authentication_form.pass_enter()
    offer_page.open_page()
    offer_page.scroll_page()
    offer_page.check_pin_offer()
    offer_page.check_offer()
    offer_page.add_to_favorite()
    offer_page.check_favorites()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Страница с инструкцией для вебмастера")
@allure.story("Тестирование строки поиска на странице инструкции вебмастера")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_instructions_page():
    authentication_form.open()
    authentication_form.pass_enter()
    instructions.search_field()
    instructions.check_search()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Страница с инструкцией для вебмастера")
@allure.story("Тестирование строки поиска на странице инструкции вебмастера")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_postback():
    authentication_form.open()
    authentication_form.pass_enter()
    authentication_form.check_id()
    postback.open_global_postback()
    postback.transition_global_postback()
    postback.create_global_postback()
    postback.save_global_postback()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Timur")
@allure.feature("Страница с инструкцией для вебмастера")
@allure.story("Тестирование строки поиска на странице инструкции вебмастера")
@allure.link("http://webmaster.dev-qa.leads/", name="Testing")
def test_ya_metric():
    authentication_form.open()
    authentication_form.pass_enter()
    yandex_metric.open_metric_page()
    yandex_metric.open_creation_modal_page()
    yandex_metric.insert_type_fields()
    yandex_metric.check_filtres_for_request()
    yandex_metric.check_aff_sub()
    yandex_metric.check_save()
