import json
import time

import requests

class APICall:
    '''
        ===========================================================================
        API HELPER
        ===========================================================================
    '''

    # api get user by id ( refer https://reqres.in/)
    # depend system is built so api has number of different paramenter
    def call_API_load(self, url):
        payload = ""
        headers = {}
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
            result = response.json()
            result['status'] = response.status_code
            return result
        except Exception as e:
            print(e)

    def call_API_Add(self, url, headers, payload):
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            result = response.json()
            result['status'] = response.status_code
            return result
        except Exception as e:
            print(e)

    def call_API_Upadte(self, url, headers, payload):
        try:
            response = requests.request("UPDATE", url, headers=headers, data=payload)
            return response.json()
        except Exception as e:
            print(e)

    def call_API_Delete(self, url, headers, payload):
        try:
            response = requests.request("DELETE", url, headers=headers, data=payload)
            return response.json()
        except Exception as e:
            print(e)
