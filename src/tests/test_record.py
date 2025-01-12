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
from src.casvisor import Record, BaseClient, _RecordSDK
import requests_mock


class TestRecord(unittest.TestCase):
    def test_record_to_dict(self):
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
            is_triggered=True,
        )

        # Act
        record_dict = record.to_dict()

        # Assert
        self.assertEqual(record_dict["id"], 1)
        self.assertEqual(record_dict["owner"], "org123")
        self.assertEqual(record_dict["name"], "record_name")
        # Additional assertions as needed

    def test_record_from_dict(self):
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
            "is_triggered": True,
        }

        # Act
        record = Record.from_dict(record_data)

        # Assert
        self.assertEqual(record.id, 1)
        self.assertEqual(record.owner, "org123")
        self.assertEqual(record.name, "record_name")
        # Additional assertions as needed

    def test_record_sdk_get_records(self):
        # Arrange
        client_id = "client123"
        client_secret = "secret456"
        endpoint = "https://example.com"
        organization_name = "org123"
        base_client = BaseClient(client_id, client_secret, endpoint)
        sdk = _RecordSDK(base_client, organization_name)

        # 这个测试需要补充更多断言
        self.assertIsInstance(sdk, _RecordSDK)

    def test_get_records(self):
        # Arrange
        client_id = "client123"
        client_secret = "secret456"
        endpoint = "https://example.com"
        organization_name = "org123"
        base_client = BaseClient(client_id, client_secret, endpoint)
        sdk = _RecordSDK(base_client, organization_name)

        mock_response = {
            "status": "ok",
            "msg": "Success",
            "data": [
                {
                    "id": 1,
                    "owner": "org123",
                    "name": "record1",
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
                    "is_triggered": True,
                }
            ],
            "data2": [],  # 添加缺失的 data2 字段
        }

        # Mock HTTP GET response
        with requests_mock.Mocker() as m:
            m.get(f"{endpoint}/api/get-records", json=mock_response)
            # Act
            records = sdk.get_records()

        # Assert
        self.assertEqual(len(records), 1)
        self.assertIsInstance(records[0], Record)
        self.assertEqual(records[0].id, 1)
        self.assertEqual(records[0].name, "record1")

    def test_get_pagination_records(self):
        # Arrange
        client_id = "client123"
        client_secret = "secret456"
        endpoint = "https://example.com"
        organization_name = "org123"
        base_client = BaseClient(client_id, client_secret, endpoint)
        sdk = _RecordSDK(base_client, organization_name)

        mock_response = {
            "status": "ok",
            "msg": "Success",
            "data": [
                {
                    "id": 1,
                    "owner": "org123",
                    "name": "record1",
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
                    "is_triggered": True,
                }
            ],
            "data2": 10,  # total count
        }

        # Mock HTTP GET response
        with requests_mock.Mocker() as m:
            m.get(f"{endpoint}/api/get-records", json=mock_response)
            # Act
            records, total = sdk.get_pagination_records(1, 10, {})

        # Assert
        self.assertEqual(len(records), 1)
        self.assertEqual(total, 10)
        self.assertIsInstance(records[0], Record)
