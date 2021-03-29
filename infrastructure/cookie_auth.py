import hashlib
from datetime import timedelta

auth_cookie_name = 'usr_ath'

def set_cookie(response, user_id):
    hash_val = __hash_text(str(user_id))
    val = f'{user_id}:{hash_val}'
    response.set_cookie(auth_cookie_name, val, secure=False, httponly=True, samesite='Lax') 

def __hash_text(text):
    hash_val = 'salted_' + text + '_val'
    return hashlib.sha512(hash_val.encode('utf-8')).hexdigest()

def __add_cookie_callback(_, response, name, val):
    response.set_cookie(name, val, max_age=timedelta(days=30), secure=False, httponly=True, samesite='Lax')

def get_user_id_by_cookie(request):
    if auth_cookie_name not in request.cookies:
        return None
    val = request.cookies[auth_cookie_name]
    parts = val.split(':')
    if len(parts) != 2:
        return None
    user_id = parts[0]
    hash_val = parts[1]
    hash_check = __hash_text(user_id)
    if hash_val != hash_check:
        return None

    try:
        return int(user_id)
    except:
        return 0

def logout(response):
    response.delete_cookie(auth_cookie_name)
