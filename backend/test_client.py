import json
from unittest.mock import patch
import unittest

from client import ZendeskApiClient, API_ROOT

test_ticket = {
    "subject": "Subject",
    "description": "Description",
    "updated_at": "2017-01-01T00:00:00Z"
}

class MockRequests(object):
    """ Helper class to mock the Zendesk REST API for unit testing """
    class MockResponse(object):
        def __init__(self, json):
            self._json = json

        def json(self):
            return self._json

    api_dict = {
        API_ROOT + "/api/v2/tickets.json": MockResponse([test_ticket]),
    }

    def get(self, uri, **kwArgs):
        return self.api_dict[uri]


class TestZendeskApiClient(unittest.TestCase):
    api = ZendeskApiClient()

    @patch("requests.get")
    def test_list_tickets(self, mock_get):
        mock_get.side_effect = MockRequests().get
        tickets = self.api.list_tickets()
        self.assertEqual(tickets, [test_ticket])

if __name__ == "__main__":
    unittest.main()

