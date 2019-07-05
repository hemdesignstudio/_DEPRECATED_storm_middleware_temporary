from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import json

@api_view(['GET'])
def index(request):

    if request.query_params:
        url = request.query_params["url"]
    else:
        api_host = "servicesstage"
        api_path = "21"
        product_no = "PRD0001324"
        url = f"https://{api_host}.enferno.se/api/{api_path}/ProductService.svc/rest/GetProductByPartNo?format=json&partNo={product_no}"

    certificate = ('Hem.com-EU.crt', 'Hem.com-EU-decrypted.key')

    try:
        res = requests.get(url, cert=certificate)
    except:
        return Response("Error, bad url param", status=status.HTTP_400_BAD_REQUEST)

    return Response(json.loads(res.text), status=status.HTTP_200_OK)