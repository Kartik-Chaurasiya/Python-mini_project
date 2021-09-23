from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Meetslot

# Create your views here.
def home(request,context={'booked' : False}):
    return render(request, 'meet_home.html', context)

def manager(request, new_context={}):
    if request.method == 'POST':
        slot_date = request.POST['slot_date']
        slot_time = request.POST['slot_time']
        ins = Meetslot(slot_time = slot_time, slot_date = slot_date)
        ins.save()
        context = {'success' : True}
    alltasks = Meetslot.objects.all().order_by('-slot_date')
    context = {'tasks' : alltasks}
    context.update(new_context)
    return render(request, 'manager.html', context)

def employee(request, context={}):
    if request.method == 'POST':
        slot_date = request.POST['slot_date']
        alltasks = Meetslot.objects.filter(slot_date__iexact=slot_date, slot_booked__iexact='Not Booked')
        context = {'tasks' : alltasks}
        context.update(context)
    return render(request, 'employee.html', context)

def update_task(request, id):
    if request.method == 'POST':
        task = Meetslot.objects.get(id=id)
        task.slot_booked_by = request.POST['slot_name']
        task.slot_booked = 'Booked'
        task.save()
        context = {'booked' : False}
        return home(request, context)