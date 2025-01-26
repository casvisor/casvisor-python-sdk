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

import requests_mock

from src.casvisor import BaseClient, Response
from src.tests.test_util import TestClientId, TestClientSecret, TestEndpoint


class TestBaseClient(unittest.TestCase):
    def test_base_client_do_get_response_success(self):
        # Arrange
        baseClient = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
        mockResponse = {"status": "ok", "msg": "Success", "data": [], "data2": []}
        url = f"{TestEndpoint}/api/action"

        # Mock HTTP GET response
        with requests_mock.Mocker() as m:
            m.get(url, json=mockResponse)
            # Act
            response = baseClient.do_get_response(url)

        # Assert
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status, "ok")
        self.assertEqual(response.msg, "Success")
        self.assertEqual(response.data, [])
        self.assertEqual(response.data2, [])

    def test_base_client_do_get_response_error(self):
        # Arrange
        baseClient = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
        mockResponse = {"status": "error", "msg": "Something went wrong"}
        url = f"{TestEndpoint}/api/action"

        # Mock HTTP GET response
        with requests_mock.Mocker() as m:
            m.get(url, json=mockResponse)
            # Act & Assert
            with self.assertRaises(Exception) as context:
                baseClient.do_get_response(url)
            self.assertTrue("Something went wrong" in str(context.exception))

    def test_do_get_bytes(self):
        # Arrange
        baseClient = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
        mockResponse = {
            "status": "ok",
            "msg": "Success",
            "data": {"key": "value"},
            "data2": [],
        }
        url = f"{TestEndpoint}/api/action"

        # Mock HTTP GET response
        with requests_mock.Mocker() as m:
            m.get(url, json=mockResponse)
            # Act
            result = baseClient.do_get_bytes(url)

        # Assert
        self.assertIsInstance(result, bytes)
        self.assertEqual(result.decode("utf-8"), '{"key": "value"}')

    def test_do_post(self):
        # Arrange
        baseClient = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
        mockResponse = {
            "status": "ok",
            "msg": "Success",
            "data": "Affected",
            "data2": [],
        }

        # Act
        with requests_mock.Mocker() as m:
            m.post(f"{TestEndpoint}/api/action", json=mockResponse)
            response = baseClient.do_post(
                "action", {"param": "value"}, b'{"test": "data"}', False, False
            )

        # Assert
        self.assertEqual(response.status, "ok")
        self.assertEqual(response.msg, "Success")
        self.assertEqual(response.data, "Affected")

    def test_prepare_body_form(self):
        # Arrange
        baseClient = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
        postBytes = b'{"field": "value"}'

        # Act
        content_type, body = baseClient.prepare_body(postBytes, True, False)

        # Assert
        self.assertTrue(content_type.startswith("multipart/form-data"))
        self.assertIsInstance(body, bytes)
