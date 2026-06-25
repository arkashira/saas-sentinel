import json
from saas_sentinel import SaaSSentinel

def test_init():
    """Test initializing the SDK"""
    sdk = SaaSSentinel()
    sdk.init()
    assert sdk.context is not None

def test_setContext():
    """Test setting the context"""
    sdk = SaaSSentinel()
    sdk.init()
    data = {"key": "value"}
    sdk.setContext(data)
    assert sdk.getContext() == data

def test_getContext():
    """Test getting the context"""
    sdk = SaaSSentinel()
    sdk.init()
    data = {"key": "value"}
    sdk.setContext(data)
    assert sdk.getContext() == data

def test_getContext_not_initialized():
    """Test getting the context when not initialized"""
    sdk = SaaSSentinel()
    try:
        sdk.getContext()
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Context not initialized"

def test_to_json():
    """Test converting the context to JSON"""
    sdk = SaaSSentinel()
    sdk.init()
    data = {"key": "value"}
    sdk.setContext(data)
    json_data = sdk.to_json()
    assert json.loads(json_data) == data
