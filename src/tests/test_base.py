# Copyright 2025 The casbin Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import requests_mock
from src.casvisor import BaseClient, Response

class TestBaseClient(unittest.TestCase):
    def test_base_client_do_get_response_success(self):
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
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, "ok")
        self.assertEqual(response.msg, "Success")
        self.assertEqual(response.data, [])
        self.assertEqual(response.data2, [])

    def test_base_client_do_get_response_error(self):
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
            with self.assertRaises(Exception) as context:
                base_client.do_get_response(url)
            self.assertTrue("Something went wrong" in str(context.exception))

    def test_do_get_bytes(self):
        # Arrange
        client_id = "client123"
        client_secret = "secret456"
        endpoint = "https://example.com"
        base_client = BaseClient(client_id, client_secret, endpoint)
        mock_response = {
            "status": "ok",
            "msg": "Success",
            "data": {"key": "value"},
            "data2": []
        }
        url = f"{endpoint}/api/action"

        # Mock HTTP GET response
        with requests_mock.Mocker() as m:
            m.get(url, json=mock_response)
            # Act
            result = base_client.do_get_bytes(url)

        # Assert
        self.assertIsInstance(result, bytes)
        self.assertEqual(result.decode('utf-8'), '{"key": "value"}')

    def test_do_post(self):
        # Arrange
        client_id = "client123"
        client_secret = "secret456"
        endpoint = "https://example.com"
        base_client = BaseClient(client_id, client_secret, endpoint)
        mock_response = {
            "status": "ok",
            "msg": "Success",
            "data": "Affected",
            "data2": []
        }
        
        # Act
        with requests_mock.Mocker() as m:
            m.post(f"{endpoint}/api/action", json=mock_response)
            response = base_client.do_post(
                "action",
                {"param": "value"},
                b'{"test": "data"}',
                False,
                False
            )

        # Assert
        self.assertEqual(response.status, "ok")
        self.assertEqual(response.msg, "Success")
        self.assertEqual(response.data, "Affected")

    def test_prepare_body_form(self):
        # Arrange
        client = BaseClient("id", "secret", "endpoint")
        post_bytes = b'{"field": "value"}'
        
        # Act
        content_type, body = client.prepare_body(post_bytes, True, False)
        
        # Assert
        self.assertTrue(content_type.startswith('multipart/form-data'))
        self.assertIsInstance(body, bytes)