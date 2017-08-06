import requests
import warnings
import hashlib
import time
import json
import hmac
import os
import urllib.parse
import httplib2
from config import *
from erro import *

class Bihang:

    def __init__(self, oauth2_credentials=None, api_key=None, api_secret=None, nonce_multipler=1e6):
        """
        :param oauth2_credentials: JSON representation of Bihang oauth2 credentials
        :param api_key:  Bihang API key
        :param api_key:  Bihang API Secret
        :param nonce_multipler: Multipler used for nonce (API_KEY+Secret)
        """
        self.session = requests.session()
        self.session.headers.update({'content-type': 'application/json'})

        self.auth = None
        if oauth2_credentials:
            self.auth = 'oauth'
            ca_directory = os.path.abspath(__file__).split('/')[0:-1]
            ca_path = '/'.join(ca_directory) + '/ca_certs.txt'

            # Set CA certificates (breaks without them)
            self.http = httplib2.Http(ca_certs=ca_path)

            self.oauth2_credentials = oauth2_credentials
            self.token_expired = False
            try:
                self._check_oauth_expired()
            except ResponseException:
                self.token_expired = True
            self.oauth2_credentials.apply(headers=self.session.headers)

        elif api_key and api_secret:
            self.auth = 'api_key+api_secret'
            self.api_key = api_key
            self.api_secret = api_secret
            self.nonce_multipler = nonce_multipler

    def _apply_authentication(self, url, data=None):
        """
        Apply authentication for our request
        """

        if self.auth == 'oauth':
            self._check_oauth_expired()
            return {}

        if self.auth == 'api_key+api_secret':
            nonce = int(time.time() * self.nonce_multipler)
            message = str(nonce) + '/api/v1/' + url + ('' if data is None else data)
            signature = hmac.new(self.api_secret.encode(encoding="utf-8"), message.encode(encoding="utf-8"), hashlib.sha256).hexdigest()
            self.session.headers.update({
                'KEY': self.api_key,
                'NONCE': nonce,
                'SIGNATURE': signature,
            })
            return {}

        return {}   
                
    def _check_status_code(self, response):
        """
        Check the for bad status codes
        """
        if response.status_code >= 400:
            raise erro.ResponseException('Recieved %s code form bihang' % response.status_code, response)  

    def _check_oauth_expired(self):
        """
        Check if the oauth token has expired
        """
        if self.oauth2_credentials.access_token_expired:
            raise AccessTokenCredentialsError('oAuth2 Token Expired. Call CoinbaseClient.refresh_oauth() '
                                              'to refresh token')                             

    def get(self, url, data=None):
        """
        Sends a GET request to Bihang. This should not be called directly
        """

        all_url = ENDPOINT + '/' + url + ('' if data is None else '?'+ urllib.parse.urlencode(data) )
        response = self.session.get(url=all_url, params=self._apply_authentication(url))
        self._check_status_code(response)
        return response.json()


    def post(self, url, data=None):
        """
        Sends a POST request to Bihang. This should not be called directly
        """
        data = json.dumps(data)
        all_url = ENDPOINT + '/' + url
        response = self.session.post(url=all_url, params=self._apply_authentication(url))
        self._check_status_code(response)
        return response.json()

    def put(self, url, data=None, return_data=False, json_data=True):
        """
        Sends a PUT request to Bihang. This should not be called directly
        """
        all_url = ENDPOINT + '/' + url + ('' if data is None else '?'+ urllib.parse.urlencode(data) )
        response = self.session.put(url=all_url, params=self._apply_authentication(url))
        self._check_status_code(response)
        return response.json()

    def delete(self, url, return_data=False, json_data=True):
        """
        Sends a DELETE request to Bihang. This should not be called directly
        """
        all_url = ENDPOINT + '/' + url + ('' if data is None else '?'+ urllib.parse.urlencode(data) )
        response = self.session.delete(url=all_url, params=self._apply_authentication(url))
        self._check_status_code(response)
        return response.json()
