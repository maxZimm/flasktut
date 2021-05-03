import pytest

from models.user import User
from services import user_services

def test_hash_text():
   text = 'abcd1234'
   hashed = user_services.hash_text(text)  
   assert '$rounds=170201' in hashed

def test_hash_verify():
   text = 'abcd1234'
   hashed = user_services.hash_text(text)  
   assert user_services.verify_hash(text, hashed)
