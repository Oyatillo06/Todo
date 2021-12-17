from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def take(request):
    if request.method=='POST':
        Todo.objects.create(
            title=request.POST.get('title'),
            vaqt= request.POST['vaqt'],
            joy=request.POST['joy'],
            description=request.POST['description'],
            status=request.POST['status'],
        )

        return redirect("take")
    Tas=Todo.objects.all()
    return render(request, "todo.html",{'T':Tas})





def take_ochir(request,son):
    t =Todo.objects.get(id=son)
    t.delete()
    return redirect("take")


