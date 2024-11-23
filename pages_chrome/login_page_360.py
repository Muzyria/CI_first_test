import time

from pages_chrome import PageChrome
from .config import LinksBetaSyncWise360


class LoginPageSyncWise360(PageChrome):
    PAGE_URL = LinksBetaSyncWise360.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@aria-label='submit']")

    SPINNER = ("xpath", "//div[@class='loader']")

    def __init__(self) -> None:
        super().__init__()

    def login_button_is_displayed(self) -> bool:
        return self.element_to_be_clickable(self.USERNAME_FIELD).is_displayed()

    def password_field_is_displayed(self) -> bool:
        return self.element_to_be_clickable(self.PASSWORD_FIELD).is_displayed()

    def click_login_button(self) -> None:
        self.element_to_be_clickable(self.BUTTON_LOGIN).click()


