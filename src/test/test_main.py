from unittest.mock import MagicMock
from casvisor import BaseClient, CasvisorSDK


def test_casvisor_sdk_initialization():
    # Arrange
    endpoint = "https://example.com"
    client_id = "client123"
    client_secret = "secret456"
    organization_name = "org789"
    application_name = "app012"

    # Mock BaseClient
    base_client_mock = MagicMock(spec=BaseClient)

    # Act
    sdk = CasvisorSDK(
        endpoint=endpoint,
        client_id=client_id,
        client_secret=client_secret,
        organization_name=organization_name,
        application_name=application_name
    )

    # Assert
    assert sdk.endpoint == endpoint
    assert sdk.client_id == client_id
    assert sdk.client_secret == client_secret
    assert sdk.organization_name == organization_name
    assert sdk.application_name == application_name
    assert isinstance(sdk.base_client, BaseClient)

