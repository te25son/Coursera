from django.shortcuts import render


def index(request):
    context_dict = {
        'text': 'Hello world!',
        'number': 100,
    }
    return render(request, 'basic_app/index.html', context_dict)


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_url_template.html')
