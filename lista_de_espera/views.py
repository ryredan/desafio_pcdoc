from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .forms import PacienteForm
from .models import Paciente
from django.db.models import Case, When, Value, IntegerField

def index(request):
    form = PacienteForm()
    return render(request, 'index.html', {'form': form})

def post_paciente(request):
    if request.is_ajax and request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)

def get_pacientes(request):
    pacientes = Paciente.objects.all().annotate(
        ordem_prio=Case(
            When(prioridade__gt=1, then=Value(2)),
            When(prioridade=1, then=Value(1)),
            default=Value(0),
            output_field=IntegerField(),
        )).order_by('-ordem_prio')
    ser_pacientes = serializers.serialize('json', pacientes)
    return JsonResponse({"pacientes": ser_pacientes}, status=200)

def delete_paciente(request):
    if request.is_ajax and request.method == "POST":
        pac_pk = request.POST['pk']
        Paciente.objects.get(pk=pac_pk).delete()
        return HttpResponse()
