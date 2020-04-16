import logging.config
from collections import deque
import json
import os
import time

import boxsdk


log = logging.getLogger(__name__)


BOX_AUTH_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    "box-auth.json"
)


class RateLimiter:
    def __init__(
        self,
        rate_limit=10,
        rate_period=1,
    ):

        self._rate_limit = rate_limit
        self._rate_period = rate_period
        self._request_start_times_deque = deque()

    def __enter__(self):
        self.limit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def limit(self):
        while True:
            now = time.time()

            while self._request_start_times_deque:
                if now - self._request_start_times_deque[0] > self._rate_period:
                    self._request_start_times_deque.popleft()
                else:
                    break

            if len(self._request_start_times_deque) < self._rate_limit:
                break

            time.sleep(0.001)

        self._request_start_times_deque.append(time.time())


def main():
    # Load the Box Platform app's JWT keys into memory as a dicitons
    with open(BOX_AUTH_FILE_PATH) as fh:
        box_auth_dict = json.load(fh)

    # Get Box access tokens with the JWT keys from Box's authentication service
    auth = boxsdk.JWTAuth.from_settings_dictionary(
        box_auth_dict
    )
    auth.authenticate_instance()

    # Set up a Box HTTP client
    box_client = boxsdk.Client(auth)

    # Set up a rate limiter
    rate_limiter = RateLimiter()

    while True:

        # Call the rate limiter as content manager
        with rate_limiter:

            # Call Box
            folder = box_client.folder("0")

        # Call the rate limiter method directly
        # rate_limiter.limit()
        # folder = box_client.folder("0")
        # print(folder)


if __name__ == '__main__':
    main()
