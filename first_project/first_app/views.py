from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    acces_records_list = AccessRecord.objects.order_by('date')
    webpages_list = Webpage.objects.order_by('topic')
    date_dict = {'acces_records':acces_records_list, 'webpages':webpages_list}
    return render(request,'first_app/index.html', context=date_dict)
