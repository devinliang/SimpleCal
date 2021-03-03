from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import cal

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Cal(request):
    # if request.POST:
    if request.method == "POST": 
        vva = request.POST['va']
        vvb = request.POST['vb']
        result = int(vva)+int(vvb)
        cal.objects.create(value_a=vva, value_b=vvb, result=result)
        # return HttpResponse(result)
        return render(request,'result.html',context={'data':result})
    else:
        return HttpResponse('Please visit us with POST');


def CalList(request):
    data = cal.objects.all()
    return render(request, 'list.html', context={'data':data})

def DelData(request):
    cal.objects.all().delete()
    return HttpResponse("All Data Deleted")