from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

import requests
import random
import urllib.request

# Create your views here.
def index(request):
    # return HttpResponse("HW")
    random_cat_id, random_cat_url = get_random_cat()
    context = {'random_cat_id': random_cat_id, 'random_cat_url': random_cat_url}
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
    return random_cat_id, random_cat_url

def download_cat(request, cat_id):
    # TODO: Download code
    base_url = "https://cataas.com/cat/"
    cat_detail_url = base_url+cat_id+"?json=true"
    cat_image_url = base_url + cat_id
    print(cat_detail_url)
    cat_detail_response = requests.get(cat_detail_url)
    if cat_detail_response.status_code != 200:
        print(cat_detail_response)
        print("Cataas Server Error:", cat_detail_response.status_code)
        return
    cat_image_extension = cat_detail_response.json()["mimetype"].split("/")[-1]
    print(cat_image_extension)
    urllib.request.urlretrieve(cat_image_url, "D:/Libraries/Downloads/cat-{cat_id}.{extension}".format(cat_id=cat_id, extension=cat_image_extension))
    return HttpResponse("Downloaded")