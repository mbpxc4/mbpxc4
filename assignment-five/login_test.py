import pytest

"""
    This program will check if the login has the correct information
    given certain inputs of username and password.  The first test will
    pass because the username and the password are the correct
    information. The second test will fail due to the username of
    'wronguser' and the password of 'wrongpassword' not being the
    correct information.
"""

def right_User():
    username = "mpilgrim"
    return username

def wrong_User():
    username = "wronguser"
    return username

def right_password():
    password = "testtest"
    return password

def wrong_password():
    password = "wrongpassword"
    return password

def test_correct_login():
    username = right_User()
    password = right_password()
    assert username == "mpilgrim" and password == "testtest"
    
def test_wrong_login():
    username = wrong_User()
    password = wrong_password()
    assert username == "mpilgrim" and password == "testtest"