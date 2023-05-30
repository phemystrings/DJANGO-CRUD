from django.http import HttpResponseRedirect
from django.shortcuts import render
from training.models import DB, FormData


def index(request):  # index view i.e. the Home page
    return render(request, 'index.html', {'Boot': DB['Boot'], 'length': len(DB['Boot'])})


def register(request):  # Create
    if request.method == 'POST':
        FormData().create(request.POST)
        return HttpResponseRedirect('../')
    else:
        return render(request, 'register.html', {'form': FormData()})


def details(request, id):
    for item in DB['Boot']:
        if item['csrfmiddlewaretoken'] == id:
            context = item
    return render(request, 'details.html', context)


def update(request, id):
    for item in DB['Boot']:
        if item['csrfmiddlewaretoken'] == id:
            if request.method == 'POST':
                FormData().update(request.POST, DB['Boot'].index(item))
                return HttpResponseRedirect('../')
            else:
                form = FormData(item)
                return render(request, 'update.html', {'form': form})


def delete(request, id):
    FormData().delete(id)
    return HttpResponseRedirect('../')
