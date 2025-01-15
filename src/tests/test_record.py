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
import time
from src.casvisor import Record, BaseClient, _RecordSDK
from src.tests.test_util import (
    TestClientId,
    TestClientSecret,
    TestEndpoint,
    TestOrganization,
    get_random_name,
)


class TestRecord(unittest.TestCase):
    def test_record(self):
        name = get_random_name("record")

        timestamp = int(time.time())
        tm = time.gmtime(timestamp)
        createdTime = time.strftime("%Y-%m-%dT%H:%M:%SZ", tm)

        # Create a new record
        record = Record(
            owner=TestOrganization,
            name=name,
            createdTime=createdTime,
            organization=TestOrganization,
            clientIp="120.85.97.21",
            user="admin",
            method="POST",
            requestUri="/api/test_request_uri",
            action="test_action",
            object="test_object",
            language="en",
            response='{"status":"ok", "msg":"test_response"}',
            isTriggered=True,
        )

        client = BaseClient(TestClientId, TestClientSecret, TestEndpoint)
        sdk = _RecordSDK(client, TestOrganization)

        # Add a new record
        try:
            result = sdk.add_record(record)
        except Exception as e:
            self.fail(f"Failed to add record: {e}")

        # Get all records, check if our added record is inside the list
        try:
            records = sdk.get_records()
        except Exception as e:
            self.fail(f"Failed to get records: {e}")
        names = [item.name for item in records]
        self.assertIn(name, names, "Added record not found in list")

        # Get the record
        try:
            retrieved_record = sdk.get_record(name)
        except Exception as e:
            self.fail(f"Failed to get record: {e}")
        self.assertEqual(
            name, retrieved_record.name, "Retrieved record does not match added record"
        )

        # Update the record
        updated_action = "updated_action"
        retrieved_record.action = updated_action
        try:
            result = sdk.update_record(retrieved_record)
        except Exception as e:
            self.fail(f"Failed to update record: {e}")
        self.assertTrue(result, "Failed to update record")

        # Validate the update
        try:
            updated_record = sdk.get_record(name)

        except Exception as e:
            self.fail(f"Failed to get record: {e}")
        self.assertEqual(
            updated_action,
            updated_record.action,
            "Failed to update record, action mismatch",
        )

        # Delete the record
        try:
            result = sdk.delete_record(record)
        except Exception as e:
            self.fail(f"Failed to delete record: {e}")
        self.assertTrue(result, "Failed to delete record")

        # Validate the deletion
        try:
            records = sdk.get_records()
        except Exception as e:
            self.fail(f"Failed to get records: {e}")
        names = [item.name for item in records]
        self.assertNotIn(name, names, "Failed to delete record, it's still in the list")
