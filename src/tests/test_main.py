# Copyright 2025 The casbin Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from src.casvisor import BaseClient, CasvisorSDK
from src.tests.test_util import (
    TestApplication,
    TestClientId,
    TestClientSecret,
    TestEndpoint,
    TestOrganization,
)


class TestCasvisorSDK(unittest.TestCase):
    def test_casvisor_sdk_initialization(self):
        # Arrange
        endpoint = TestEndpoint
        client_id = TestClientId
        client_secret = TestClientSecret
        organization_name = TestOrganization
        application_name = TestApplication

        # Act
        sdk = CasvisorSDK(
            endpoint=endpoint,
            clientId=client_id,
            clientSecret=client_secret,
            organizationName=organization_name,
            applicationName=application_name,
        )

        # Assert
        self.assertEqual(sdk.endpoint, endpoint)
        self.assertEqual(sdk.clientId, client_id)
        self.assertEqual(sdk.clientSecret, client_secret)
        self.assertEqual(sdk.organizationName, organization_name)
        self.assertEqual(sdk.applicationName, application_name)
        self.assertIsInstance(sdk.baseClient, BaseClient)

    def test_casvisor_sdk_inheritance(self):
        sdk = CasvisorSDK(
            endpoint=TestEndpoint,
            clientId=TestClientId,
            clientSecret=TestClientSecret,
            organizationName=TestOrganization,
            applicationName=TestApplication,
        )

        self.assertTrue(hasattr(sdk, "get_records"))
        self.assertTrue(hasattr(sdk, "get_record"))
        self.assertTrue(hasattr(sdk, "add_record"))
        self.assertTrue(hasattr(sdk, "update_record"))
        self.assertTrue(hasattr(sdk, "delete_record"))

    def test_casvisor_sdk_base_client_initialization(self):
        sdk = CasvisorSDK(
            endpoint=TestEndpoint,
            clientId=TestClientId,
            clientSecret=TestClientSecret,
            organizationName=TestOrganization,
            applicationName=TestApplication,
        )

        self.assertIsInstance(sdk.baseClient, BaseClient)
        self.assertEqual(sdk.baseClient.endpoint, TestEndpoint)
        self.assertEqual(sdk.baseClient.clientId, TestClientId)
        self.assertEqual(sdk.baseClient.clientSecret, TestClientSecret)
