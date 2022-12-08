from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.core import serializers
from hall_of_shame.models import Corruptor
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
@login_required(login_url='/login/')
def show_hall_of_shame(request):
    data = Corruptor.objects.all()
    if request.user.userprofile.is_admin:
        return render(request, 'hall_of_shame.html', {'data':data})
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
def add_corruptor_flutter(request):
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

        return JsonResponse({"status":"oke"})
    
    return JsonResponse({"status":"gagal"})

@csrf_exempt
def delete_corruptor(request, id):
    if request.method == "DELETE":
        corruptor = Corruptor.objects.filter(pk=id).first()
        corruptor.delete()
        return JsonResponse({"status":"oke"})

    return JsonResponse({"status":"gagal"})

def show_detail(request, id):
    data = Corruptor.objects.filter(pk=id)
    return render(request, 'detail_corruptor.html', {'data':data})