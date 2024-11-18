from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

import requests
import random

# Create your views here.
def index(request):
    # return HttpResponse("HW")
    context = {'random_cat_url': get_random_cat()}
    return render(request, "catrousel_app/index.html", context=context)

# https://cataas.com/doc.html
def get_random_cat():
    count_url = "https://cataas.com/api/count"
    count_response = requests.get(count_url)
    if count_response.status_code != 200:
        print(count_url)
        print("Cataas Server Error:", count_response.status_code)
        return
    count = int(count_response.json()["count"])

    random_count = random.randrange(count)
    random_cat_id_url = "https://cataas.com/api/cats?limit=1&skip=" + str(random_count)
    random_cat_id_response = requests.get(random_cat_id_url)
    if random_cat_id_response.status_code != 200:
        print(random_cat_id_url)
        print("Cataas Server Error:", random_cat_id_response.status_code)
        return
    random_cat_id = random_cat_id_response.json()[0]["_id"]

    random_cat_url = "https://cataas.com/cat/" + random_cat_id + "?position=center"
    return random_cat_url
