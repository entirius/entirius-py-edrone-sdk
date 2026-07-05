# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from __future__ import annotations

import requests
from requests import Response

LIVE_URL = "https://api.edrone.me"


class Request:
    method: str
    resource: str
    headers: dict | None
    params: dict | None
    data: dict | None

    def __init__(self, method: str, resource: str, params=None, headers=None, data: dict | str = None):
        if headers is None:
            headers = {}
        self.method = method
        self.resource = resource
        self.headers = headers
        self.params = params
        self.data = data

    def _build_url(self) -> str:
        if LIVE_URL.endswith("/") and self.resource.startswith("/"):
            return LIVE_URL + self.resource[1:]
        return LIVE_URL + self.resource

    def add_content_type_to_header(self):
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"

    def make_request(self) -> Response:
        self.add_content_type_to_header()
        res = requests.request(method=self.method, url=self._build_url(), headers=self.headers, data=self.data)
        return res
