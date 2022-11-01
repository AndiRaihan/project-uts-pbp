from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from hall_of_shame.models import Corruptor
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def show_hall_of_shame(request):
    data = Corruptor.objects.all()
    return render(request, 'hall_of_shame.html', {'data':data})

def show_hall_of_shame_user(request):
    data = Corruptor.objects.all()
    return render(request, 'hall_of_shame_user.html', {'data':data})

def get_hall_of_shame(request):
    data = Corruptor.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_corruptor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        arrested_date = request.POST.get('arrested_date')
        corruption_type = request.POST.get('corruption_type')
        description = request.POST.get('description')

        new_corruptor = Corruptor(
            name=name,
            arrested_date=arrested_date,
            corruption_type=corruption_type,
            description=description
        )
        new_corruptor.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def delete_corruptor(request, id):
    if request.method == "DELETE":
        corruptor = Corruptor.objects.filter(pk=id).first()
        corruptor.delete()
        return HttpResponse(b"DELETED", status=201)

    return HttpResponseNotFound()

def show_detail(request, id):
    data = Corruptor.objects.filter(pk=id)
    return render(request, 'detail_corruptor.html', {'data':data})