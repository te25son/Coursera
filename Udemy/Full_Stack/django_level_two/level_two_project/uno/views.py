from django.shortcuts import render
from uno.models import AccessRecord, Topic, Webpage

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {
        'access_records': webpages_list,
    }

    return render(request, 'uno/index.html', context=date_dict)
