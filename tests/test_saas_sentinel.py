import pytest
from saas_sentinel import SaaSSENTINEL

def test_query():
    sentinel = SaaSSENTINEL()
    sentinel.add_user_context(123, {'theme': 'dark', 'language': 'en'})
    assert sentinel.query('get user preferences for user 123') == {'theme': 'dark', 'language': 'en'}

def test_query_non_existent_user():
    sentinel = SaaSSENTINEL()
    with pytest.raises(ValueError):
        sentinel.query('get user preferences for user 123')

def test_query_invalid_key():
    sentinel = SaaSSENTINEL()
    sentinel.add_user_context(123, {'theme': 'dark', 'language': 'en'})
    with pytest.raises(ValueError):
        sentinel.query('get user settings for user 123')

def test_fuzzy_query():
    sentinel = SaaSSENTINEL()
    sentinel.add_user_context(123, {'theme': 'dark', 'language': 'en'})
    assert sentinel.fuzzy_query('user preferences') == {'theme': 'dark', 'language': 'en'}

def test_fuzzy_query_no_match():
    sentinel = SaaSSENTINEL()
    sentinel.add_user_context(123, {'theme': 'dark', 'language': 'en'})
    assert sentinel.fuzzy_query('settings') is None
