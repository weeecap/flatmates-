from django.shortcuts import render

def index(request):
    context = {
        'title': 'Tets Title ',
        'user': "Test User",
        }
    return render(request, 'index.html', context)
