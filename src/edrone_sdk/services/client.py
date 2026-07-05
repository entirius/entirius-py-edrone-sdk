# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import json
import logging
from dataclasses import asdict

from edrone_sdk.dto.auth import Auth as AuthDTO
from edrone_sdk.dto.customer import SubscribeEdrone
from edrone_sdk.exceptions import EdroneError
from edrone_sdk.services.request import Request
from edrone_sdk.validators.response import validate_edrone_request_success, validate_edrone_response

logger_process = logging.getLogger("process")


class EdroneClient:
    url: str
    auth: AuthDTO
    payload: dict

    def __init__(self, app_id: str, version: str = "1.0.0"):
        self.auth = AuthDTO(app_id=app_id, version=version)
        self.payload = {}

    def authorize(self):
        self.payload.update(asdict(self.auth))

    def sub_or_unsub_customer_subscription(self, sub_data: SubscribeEdrone):
        """Creates customer subscription in edrone."""
        self.payload = sub_data.to_dict()
        self.authorize()
        if hasattr(self.payload, "subscriber_status") and self.payload["subscriber_status"] is None:
            self.payload.pop("subscriber_status")
        json_sub_data = json.dumps(self.payload)
        request = Request(method="POST", resource="/trace", data=self.payload)
        response = request.make_request()
        validation, response_body = validate_edrone_response(response)
        if validation:
            success = validate_edrone_request_success(response_body)
            if success:
                return True, response_body
            else:
                logger_process.error(
                    "Edrone API response failed",
                    extra={"details": {"request_data": json_sub_data, "response_body": response_body}},
                )
                raise EdroneError("Edrone response is not correct.")
        else:
            logger_process.error(
                "Edrone API response failed",
                extra={"details": {"request_data": json_sub_data, "response_body": response_body}},
            )
            raise EdroneError(f"The Edrone API responded with an error. Message: {response_body.get('message')}")
