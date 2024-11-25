import time

import pytest

from pages_chrome.login_page_360 import LoginPageSyncWise360


class TestFirst:
    def test_first(self, request) -> None:
        print()
        print(f"START {request.node.name}")
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        assert LoginPageSyncWise360().login_button_is_displayed()
        time.sleep(3)
        print(f"FINISH {request.node.name}")

    def test_second(self, request) -> None:
        print()
        print(f"START {request.node.name}")
        LoginPageSyncWise360.open(LoginPageSyncWise360.PAGE_URL)
        assert LoginPageSyncWise360().password_field_is_displayed() == False
        time.sleep(3)
        print(f"FINISH {request.node.name}")
