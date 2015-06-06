"""
Interface with the Github API
"""
import requests
import json
from .utils import filter_by_claimed

class API(object):
    def __init__(self, token=None, useragent="GHI Assist"):
        self.token = token
        self.useragent = useragent

    def _call(self, api_url, content=None, method="PUT"):
        """
        Convenience method which calls the Github API with default arguments.

        Args:
            api_url: URL of API endpoint.
            content (optional): dictionary of content.
            method (optional): HTTP method. Defaults to "PUT".
        Returns:
            The response object.
        """
        headers = {
            'User-Agent': self.useragent,
            'Authorization': "token %s" % self.token,
        }
        return requests.request(method, api_url, headers=headers, data=json.dumps(content))

    def assign_issue(self, issue_url=None, assignee=None):
        """
        Assigns an issue to the given user.

        Args:
            issue_url: API endpoint for this issue. Taken from previous API response.
            assignee: String with the user's login username.
        """
        self._call(issue_url, content={"assignee": assignee}, method="PATCH")

    def label_claimed(self, issue_url=None, labels=None):
        """
        Replace the list of labels if we've changed the issue's claimed status
        """
        new_labels, replace = filter_by_claimed(labels, claimed=True)
        if replace:
            self._call("%s/labels" % issue_url, content=new_labels)

    def issue(self, issue_url=None):
        """
        Get issue data.

        Args:
            issue_url: url for the issue we're getting data for.
        Returns:
            The issue data as a dictionary.
        """
        response = self._call(issue_url, method="GET")
        return response.json()
