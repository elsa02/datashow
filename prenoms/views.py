from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import jwt


def index(request):
    
    METABASE_SITE_URL = "http://51.83.76.196:3001"
    METABASE_SECRET_KEY = "aea884fe2edf2ab799e765bb687c22634f611c95048b289245b15373716a0516"
    
    payload = {
        "resource": {"dashboard": 1},
        "params": {
    
        }
    }
    
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token.decode("utf8") + "#bordered=true&titled=true"

    return render(request, 'prenoms/index.html',{'iframeUrl': iframeUrl})
