#===============================================================================
# HTTP请求
#===============================================================================

import requests

class Http_request:
    @staticmethod
    def get(url, return_json=True):
        print("url-",url)
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text




















































