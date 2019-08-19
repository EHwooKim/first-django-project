import requests

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'services/index.html')


def artii(request):
    return render(request, 'services/artii.html')

def artii_result(request):
    string = request.GET.get('string')
    font = request.GET.get('font')
    response = requests.get(f'http://artii.herokuapp.com/make?text={string}&font={font}')

    context = {
        'string': string,
        'font': font,
        'result': response.text
    }
    return render(request, 'services/artii_result.html', context)

def push(request):
    return render(request, 'services/push.html')
    
def pull(request):
    text = request.GET.get('text')
    context = {
        'text': text
    }
    return render(request, 'services/pull.html', context)