
import pytest
from unittest.mock import MagicMock

from casvisor import Record, BaseClient, _RecordSDK


def test_record_to_dict():
    # Arrange
    record = Record(
        id=1,
        owner="org123",
        name="record_name",
        created_time="2023-10-01T12:00:00Z",
        organization="org123",
        client_ip="192.168.1.1",
        user="user1",
        method="GET",
        request_uri="/api/endpoint",
        action="view",
        language="en",
        object="object1",
        response="200 OK",
        provider="provider1",
        block="block1",
        is_triggered=True
    )

    # Act
    record_dict = record.to_dict()

    # Assert
    assert record_dict['id'] == 1
    assert record_dict['owner'] == "org123"
    assert record_dict['name'] == "record_name"
    # Additional assertions as needed

def test_record_from_dict():
    # Arrange
    record_data = {
        "id": 1,
        "owner": "org123",
        "name": "record_name",
        "created_time": "2023-10-01T12:00:00Z",
        "organization": "org123",
        "client_ip": "192.168.1.1",
        "user": "user1",
        "method": "GET",
        "request_uri": "/api/endpoint",
        "action": "view",
        "language": "en",
        "object": "object1",
        "response": "200 OK",
        "provider": "provider1",
        "block": "block1",
        "is_triggered": True
    }

    # Act
    record = Record.from_dict(record_data)

    # Assert
    assert record.id == 1
    assert record.owner == "org123"
    assert record.name == "record_name"
    # Additional assertions as needed

def test_record_sdk_get_records():
    # Arrange
    client_id = "client123"
    client_secret = "secret456"
    endpoint = "https://example.com"
    organization_name = "org123"
    base_client = BaseClient(client_id, client_secret, endpoint)
    sdk = _RecordSDK(base_client, organization_name)

    mock_response = {
        "status": "ok",
        "msg": "Succes"
    }