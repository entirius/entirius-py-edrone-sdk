# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import random

import pytest

from edrone_sdk.dto.customer import SubscribeEdrone
from edrone_sdk.dto.response import SubscribeResponse
from edrone_sdk.services.client import EdroneClient

APP_ID = os.environ.get("EDRONE_APP_ID")

pytestmark = pytest.mark.skipif(not APP_ID, reason="edrone credentials not set (EDRONE_APP_ID env var)")


def test_create_order():

    sub_data = SubscribeEdrone(
        email=f"test_{random.randint(1, 1000)}@example.pl",
        subscriber_status=0,
        customer_tags="przykladowy_tag1",
    )
    edrone = EdroneClient(app_id=APP_ID)
    response, is_success = edrone.sub_or_unsub_customer_subscription(sub_data=sub_data)
    assert isinstance(SubscribeResponse(**response), SubscribeResponse)
    assert is_success
