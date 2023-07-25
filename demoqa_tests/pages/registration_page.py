from selene import browser, have

from demoqa_tests.data.users import User
from tests.conftest import path


class RegistrationPage:

    def __init__(self):
        self.fist_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('#genterWrapper .custom-control')
        self.mobile_number = browser.element('#userNumber')
        self.subject = browser.element('#subjectsInput')
        self.hobbies = browser.all('label[for^= hobbies]')
        self.select_picture = browser.element('#uploadPicture')

    def open(self):
        browser.open('/automation-practice-form')
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    def fill_registration(self, user: User):
        self.fist_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.exact_text(user.gender)).click()
        self.mobile_number.type(user.mobile_number)
        self.fill_date_of_birth(user.date_of_birth)
        self.subject.type(user.subjects).press_enter()
        self.hobbies.element_by(have.text(user.hobbies)).click()
        self.select_picture.send_keys(path(user.picture))
        self.fill_current_address(user.current_address)
        self.select_state(user.state)
        self.select_city(user.city)
        self.submit()
        return self

    def fill_date_of_birth(self, date):
        year = date.year
        month = date.month - 1
        day = date.strftime('%d')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month').click()
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('#state div').element_by(have.exact_text(value)).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('#city div').element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_have_registered(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.mobile_number}',
            '{0} {1},{2}'.format(user.date_of_birth.strftime("%d"),
                                 user.date_of_birth.strftime("%B"),
                                 user.date_of_birth.year),
            f'{user.subjects}',
            f'{user.hobbies}',
            f'{user.picture}',
            f'{user.current_address}',
            f'{user.state} {user.city}'
        ))

    def close_modal(self):
        browser.element('#closeLargeModal').should(have.exact_text('Close')).click()
