import azure.functions as func

class ApiRequest:

    def __init__(self):
        pass

    def getApiRequest(self,req):
        req_body = req.get_json()
        operationdetails = req_body.get('query')
        return operationdetails