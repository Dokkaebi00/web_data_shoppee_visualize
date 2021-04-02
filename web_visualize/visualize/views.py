from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util

# Create your views here.

def index(request):
    list_label = util.list_label_group()
    return render(request, 'visualize/index.html', {
        "list_label": list_label
    })

def view_images(request, label_group):
    label_group = int(label_group)
    list_image_paths, list_titles = util.information_retrieval(label_group)
    return render(request, 'visualize/views.html', {
        "list_image_paths": list_image_paths,
        "list_titles": list_titles
    })

def search(request):
    label = request.POST.get('label').strip()
    label = int(label)
    labels_founded = util.search_by_label(str(label))
    return render(request, "visualize/search.html", {
        "labels_founded": labels_founded
    })