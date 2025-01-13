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

import json
from typing import Dict, List, Optional, Tuple
from .base import BaseClient
from . import util


class Record:
    def __init__(
        self,
        id: int,
        owner: str,
        name: str,
        created_time: str,
        organization: str,
        client_ip: str,
        user: str,
        method: str,
        request_uri: str,
        action: str,
        language: str,
        object: str,
        response: str,
        provider: str,
        block: str,
        is_triggered: bool,
    ):
        self.id = id
        self.owner = owner
        self.name = name
        self.created_time = created_time
        self.organization = organization
        self.client_ip = client_ip
        self.user = user
        self.method = method
        self.request_uri = request_uri
        self.action = action
        self.language = language
        self.object = object
        self.response = response
        self.provider = provider
        self.block = block
        self.is_triggered = is_triggered

    def to_dict(self) -> Dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict) -> "Record":
        return cls(**data)


class _RecordSDK:
    def __init__(self, base_client: BaseClient, organization_name: str):
        self.base_client = base_client
        self.organization_name = organization_name

    def get_records(self) -> List[Record]:
        query_map = {"owner": self.organization_name}
        url = util.get_url(self.base_client.endpoint, "get-records", query_map)
        bytes = self.base_client.do_get_bytes(url)
        return [Record.from_dict(record) for record in json.loads(bytes)]

    def get_record(self, name: str) -> Record:
        query_map = {"id": f"{self.organization_name}/{name}"}
        url = util.get_url(self.base_client.endpoint, "get-record", query_map)
        bytes = self.base_client.do_get_bytes(url)
        return Record.from_dict(json.loads(bytes))

    def get_pagination_records(
        self, p: int, page_size: int, query_map: Dict[str, str]
    ) -> Tuple[List[Record], int]:
        query_map["owner"] = self.organization_name
        query_map["p"] = str(p)
        query_map["page_size"] = str(page_size)
        url = util.get_url(self.base_client.endpoint, "get-records", query_map)
        response = self.base_client.do_get_response(url)
        return [Record.from_dict(record) for record in response.data], response.data2

    def update_record(self, record: Record) -> bool:
        _, affected = self.modify_record("update-record", record, None)
        return affected

    def add_record(self, record: Record) -> bool:
        if not record.owner:
            record.owner = self.organization_name
        if not record.organization:
            record.organization = self.organization_name
        _, affected = self.modify_record("add-record", record, None)
        return affected

    def delete_record(self, record: Record) -> bool:
        _, affected = self.modify_record("delete-record", record, None)
        return affected

    def modify_record(
        self, action: str, record: Record, columns: Optional[List[str]]
    ) -> Tuple[Dict, bool]:
        query_map = {"id": f"{record.owner}/{record.name}"}
        if columns:
            query_map["columns"] = ",".join(columns)
        if not record.owner:
            record.owner = "admin"
        post_bytes = json.dumps(record.to_dict()).encode("utf-8")
        resp = self.base_client.do_post(action, query_map, post_bytes, False, False)
        return resp, resp["data"] == "Affected"
