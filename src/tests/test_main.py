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


class TestCasvisorSDK(unittest.TestCase):
    def test_casvisor_sdk_initialization(self):
        # Arrange
        endpoint = "https://example.com"
        client_id = "client123"
        client_secret = "secret456"
        organization_name = "org789"
        application_name = "app012"

        # Act
        sdk = CasvisorSDK(
            endpoint=endpoint,
            client_id=client_id,
            client_secret=client_secret,
            organization_name=organization_name,
            application_name=application_name,
        )

        # Assert
        self.assertEqual(sdk.endpoint, endpoint)
        self.assertEqual(sdk.client_id, client_id)
        self.assertEqual(sdk.client_secret, client_secret)
        self.assertEqual(sdk.organization_name, organization_name)
        self.assertEqual(sdk.application_name, application_name)
        self.assertIsInstance(sdk.base_client, BaseClient)
