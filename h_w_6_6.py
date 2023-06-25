from datetime import time


def test_dark_theme_by_time():

    current_time = time(hour=23)
    no_dark_theme_1 = time(hour=6)
    no_dark_theme_2 = time(hour=22)

    if current_time > no_dark_theme_1 and current_time > no_dark_theme_2:
        is_dark_theme = True
    else:
        is_dark_theme = False
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():

    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    is_dark_theme = None

    if dark_theme_enabled_by_user is None:
        if current_time > 6 and current_time < 22:
            is_dark_theme = False
    else:
        is_dark_theme = True
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    suitable_users = None

    for i in users:
        if i["name"] == "Olga":
            suitable_users = i

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = None
    suitable_users = []

    for i in users:
        if i["age"] < 20:
            suitable_users.append(i)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]



def function_everyone(func, *args):
        new_func_name = func.__name__.replace("_", " ").title()
        new_args_result = ", ".join([*args])
        result = f"{new_func_name} [{new_args_result}]"

        print(result)
        return result

def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = function_everyone(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"
    print(actual_result)


def go_to_companyname_homepage(page_url):
    actual_result = function_everyone(go_to_companyname_homepage,page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = function_everyone(find_registration_button_on_login_page,page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
