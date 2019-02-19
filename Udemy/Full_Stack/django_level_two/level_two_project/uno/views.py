from django.shortcuts import render

def index(request):
    index_dict = {
        'index_content': 'This is from the app "uno".'
    }
    return render(request, 'uno/index.html', context=index_dict)
