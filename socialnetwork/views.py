from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    user = request.user
    welcome = 'welcome'

    context = {
        'user': user,
        'welcome': welcome,
    }

    return render(request, 'main/home.html', context)
    # return HttpResponse('Hello world')
