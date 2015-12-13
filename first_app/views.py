from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect

from models import FirstModel

def basic(request):
    objects = FirstModel.objects.all()
    return render_to_response('basic.html', {'objects': objects, 'count': len(objects)})


def clear_db(request):
    if "mysuperpass" == request.GET.get("password", "wrongpass"):
        FirstModel.objects.all().delete()
        return redirect('../')
    else:
        from django.http import HttpResponse
        return HttpResponse("Wrong password! <a href='/'>back<a/>")


def add_to_db(request):
    m = FirstModel()
    m.name = "Some Name"
    m.save()
    return redirect('../')

