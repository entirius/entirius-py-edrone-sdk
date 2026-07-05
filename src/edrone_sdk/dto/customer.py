# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from dataclasses import dataclass

from edrone_sdk.dto import DTO


@dataclass
class SubscribeEdrone(DTO):
    email: str
    customer_tags: str  # string, | separated
    subscriber_status: int
    action_type: str = "subscribe"
    sender_type: str = "server"
    opt_in_email: bool = True
