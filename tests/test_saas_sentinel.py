import pytest
import json
from saas_sentinel import load_config, store_data, restore_data, enrich_data

def test_load_config():
    config_file = 'config.json'
    with open(config_file, 'w') as file:
        json.dump({'api_key': 'key', 'api_secret': 'secret', 'redis_host': 'localhost', 'redis_port': 6379}, file)
    config = load_config(config_file)
    assert config.api_key == 'key'
    assert config.api_secret == 'secret'
    assert config.redis_host == 'localhost'
    assert config.redis_port == 6379

def test_store_data():
    config_file = 'config.json'
    with open(config_file, 'w') as file:
        json.dump({'api_key': 'key', 'api_secret': 'secret', 'redis_host': 'localhost', 'redis_port': 6379}, file)
    config = load_config(config_file)
    data = 'Sample data'
    assert store_data(config, data)

def test_restore_data():
    config_file = 'config.json'
    with open(config_file, 'w') as file:
        json.dump({'api_key': 'key', 'api_secret': 'secret', 'redis_host': 'localhost', 'redis_port': 6379}, file)
    config = load_config(config_file)
    data = 'Sample data'
    store_data(config, data)
    restored_data = restore_data(config)
    assert restored_data == ''

def test_enrich_data():
    config_file = 'config.json'
    with open(config_file, 'w') as file:
        json.dump({'api_key': 'key', 'api_secret': 'secret', 'redis_host': 'localhost', 'redis_port': 6379}, file)
    config = load_config(config_file)
    data = 'Sample data'
    enriched_data = enrich_data(config, data)
    assert enriched_data == data + ' (enriched)'

def test_load_config_invalid_file():
    with pytest.raises(FileNotFoundError):
        load_config('non_existent_file.json')

def test_load_config_invalid_json():
    config_file = 'config.json'
    with open(config_file, 'w') as file:
        file.write('Invalid JSON')
    with pytest.raises(json.JSONDecodeError):
        load_config(config_file)
