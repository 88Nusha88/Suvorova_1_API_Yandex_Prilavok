import sender_stand_request
import data

#Создание пользователя+вытаскивание токена
def create_new_user():
   user_body = data.user_body.copy()
   response = sender_stand_request.post_new_user(user_body)
   assert response.status_code == 201
   assert response.json()["authToken"] != ""
   return response.json()["authToken"]

#Получение заголовка для набора
def get_header_kit(auth_token):
    current_header = data.kit_headers.copy()
    current_header["Authorization"] = "Bearer " + auth_token
    return current_header

#Получение тела запроса
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Набор пользователя
def create_new_kit(auth_token,kit_body):
    kit_headers = get_header_kit(auth_token)
    return sender_stand_request.post_new_user_kit(kit_headers, kit_body)

# Позитивные проверки
def positive_assert(name):
    auth_token = create_new_user()
    kit_body = get_kit_body(name)
    response = create_new_kit(auth_token, kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name

# Негативные проверки
def negative_assert_code_400(name):
    kit_body = get_kit_body(name)
    auth_token = create_new_user()
    response = create_new_kit(auth_token, kit_body)
    assert response.status_code == 400
    assert response.json()["name"] == name
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Test 1
def test_1_symbol_in_name_get_success_response():
    positive_assert("a")

# Test 2
def test_511_symbols_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Test 3
def test_0_symbols_in_name_get_negative_response():
    negative_assert_code_400("")

# Test 4
def test_512_symbols_in_name_get_negative_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Test 5
def test_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Test 6
def test_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Test 7
def test_has_special_symbol_in_name_get_success_response():
    positive_assert("№%@,")

# Test 8
def test_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")

# Test 9
def test_has_number_in_name_get_success_response():
    positive_assert("123")

def negative_assert_no_kit_name(name):
    kit_body = get_kit_body(name)
    auth_token = create_new_user()
    response = create_new_kit(auth_token, kit_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Test 10
def test_create_user_no_kit_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_kit_name(kit_body)

# Test 11
def test_create_user_number_type_kit_name_get_error_response():
    kit_body = get_kit_body(123)
    auth_token = create_new_user()
    response = create_new_kit(auth_token, kit_body)
    assert response.status_code == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"





