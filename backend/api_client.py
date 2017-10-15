import requests

auth = ("dana.ma537@gmail.com", "ticket")
API_ROOT = "https://ticketviewerdana.zendesk.com"

class ZendeskApiClient(object):
    """ Client which calls the Zendesk Rest API """
    # TODO: Handle pagination
    def _get(self, uri):
        """ Make a GET request to the API, timing out if there is no response within 30 seconds """
        return requests.get(API_ROOT + uri, auth=auth, timeout=30)

    def get_ticket(self, ticket_id):
        """ Given a ticket id, return the ticket info in a JSON dictionary"""
        response = self._get("/api/v2/tickets/{}.json".format(ticket_id))
        return response.json()

    def list_tickets(self):
        """ List all tickets as a JSON dictionary """
        response = self._get("/api/v2/tickets.json")
        return response.json()

