
import data
import sender_stand_request
def get_kit_body (name):
    boddy = data.kit_body.copy()
    boddy["name"]= name

    return boddy
def get_new_token ():
    reply_user = data.user_body
    response = sender_stand_request.post_new_user(reply_user)
    return response.json()["authToken"]

def possitive_assert (kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400 (kid_body):
    response = sender_stand_request.post_new_client_kit(kid_body,get_new_token())
    assert response.status_code == 400

#Número de caracteres permitidos en el nombre de usuario: 1
def test_one_new_kit_single_letter_name_response_ok ():
    reply_kit_body = get_kit_body(data.single_char)
    possitive_assert(reply_kit_body)

#Número de caracteres permitidos en el nombre de usuario: 511
def test_two_new_kit_511_letter_name_response_ok ():
    reply_kit_body = get_kit_body(data.test2_name)
    possitive_assert(reply_kit_body)

#Número de caracteres permitidos en el nombre de usuario: 0
def test_three_empy_char_name_response_bad():
    reply_kit_body = get_kit_body(data.empy_char)
    negative_assert_400(reply_kit_body)

#Número de caracteres mayor que los permitidos en el nombre de usuario: 512
def test_four_new_kit_512_letter_name_response_bad ():
    reply_kit_body = get_kit_body(data.allowed_char_second)
    negative_assert_400(reply_kit_body)

#Caracteres especiales permitidos en el nombre de usuario
def test_five_simbol_letter_name_response_ok():
    reply_kit_body = get_kit_body(data.simbol_char)
    possitive_assert(reply_kit_body)

#Caracteres permitidos en el nombre de usuario con espacios.
def test_six_spaces_letter_name_response_ok():
    reply_kit_body = get_kit_body(data.allowed_spaces)
    possitive_assert(reply_kit_body)

#Caracteres permitidos en el nombre de usuario: Números como string
def test_seven_number_letter_name_response_ok():
    reply_kit_body = get_kit_body(data.numer_allowed)
    possitive_assert(reply_kit_body)

#El parámetro no se pasa en la solicitud
def test_eith_without_name_response_bad():
    reply_kit_body = data.kit_body.copy()
    reply_kit_body.pop("name")
    negative_assert_400(reply_kit_body)

#Caracteres permitidos en el nombre de usuario: Números
def test_nine_numeric_name_response_bad():
    reply_kit_body = get_kit_body(data.numeric_par)
    negative_assert_400(reply_kit_body)
