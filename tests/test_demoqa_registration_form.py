import allure

from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage
import datetime
from allure_commons.types import Severity

Darya = User(
    first_name='Darya',
    last_name='Andronova',
    email='test@mail.ru',
    gender='Male',
    mobile_number='9111111111',
    date_of_birth=datetime.date(year=1996, month=7, day=10),
    subjects='Arts',
    hobbies='Reading',
    picture='picture.jpg',
    current_address='Testovaya Street',
    state='Uttar Pradesh',
    city='Agra'
)


@allure.tag("WEB")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "darya.andro")
@allure.feature("Регистрационная форма студента")
@allure.story("Регистрация студента проходит успешно после заполнения формы")
@allure.link("https://github.com/DaryaAndro", name="Darya Andronova")
def test_registration(setup_browser):
    registration_page = RegistrationPage()

    with allure.step("Открыть страницу для регистрации"):
        registration_page.open()

    with allure.step("Заполнить форму регистрации"):
        registration_page.fill_registration(Darya)

    with allure.step("Проверить, что регистрация прошла успешно"):
        registration_page.should_have_registered(Darya)

    with allure.step("Проверить закрытие окна с данными пользователя по кнопке"):
        registration_page.close_modal()
