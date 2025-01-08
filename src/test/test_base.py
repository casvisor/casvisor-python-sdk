
import requests_mock
import pytest

from casvisor import BaseClient,Response


def test_base_client_do_get_response_success():
    # Arrange
    client_id = "client123"
    client_secret = "secret456"
    endpoint = "https://example.com"
    base_client = BaseClient(client_id, client_secret, endpoint)
    mock_response = {
        "status": "ok",
        "msg": "Success",
        "data": [],
        "data2": []
    }
    url = f"{endpoint}/api/action"

    # Mock HTTP GET response
    with requests_mock.Mocker() as m:
        m.get(url, json=mock_response)
        # Act
        response = base_client.do_get_response(url)

    # Assert
    assert isinstance(response, Response)
    assert response.status == "ok"
    assert response.msg == "Success"
    assert response.data == []
    assert response.data2 == []

def test_base_client_do_get_response_error():
    # Arrange
    client_id = "client123"
    client_secret = "secret456"
    endpoint = "https://example.com"
    base_client = BaseClient(client_id, client_secret, endpoint)
    mock_response = {
        "status": "error",
        "msg": "Something went wrong"
    }
    url = f"{endpoint}/api/action"

    # Mock HTTP GET response
    with requests_mock.Mocker() as m:
        m.get(url, json=mock_response)
        # Act & Assert
        with pytest.raises(Exception, match="Something went wrong"):
            base_client.do_get_response(url)