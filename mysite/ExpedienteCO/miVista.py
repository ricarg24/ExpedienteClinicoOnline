from django.shortcuts import render, redirect

from ExpedienteCO.models import Padre,Paciente
from django.contrib.auth.models import User #importa tabla de users de Django
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404
from django.template import Context,RequestContext
from django.db import IntegrityError

from ExpedienteCO.formulario import FormAgregarPadre #se importa el archivo que contiene el formulario


def AgregarPadre(request):
    #verifica si el usuario es administrador y si esta logueado
    if not request.user.is_authenticated():
        return render(request,'error1.html')
    if request.user.is_staff==0:
        return render(request,'error.html')
    #verifica si hace un post
    if request.method=='POST':
        #se declara el formulario
        formulario1 = FormAgregarPadre(request.POST, prefix="pru1")
        #valida si el formulario es correcto, si es True entra al bloque de codigo
        if formulario1.is_valid():
            duiP=formulario1.cleaned_data['dui']
            nombre1=formulario1.cleaned_data['nombre1'].title()
            nombre2 = formulario1.cleaned_data['nombre2'].title()
            apellido1=formulario1.cleaned_data['apellido1'].title()
            apellido2 = formulario1.cleaned_data['apellido2'].title()
            sexo=formulario1.cleaned_data['sexo']
            division=formulario1.cleaned_data['division']
            subdivision=formulario1.cleaned_data['subdivision']



            #.title() capitaliza las palabras
            if len(division)==0:
                division=" "
            if len(subdivision)==0:
                subdivision=" "
            try:
                #guardar persona en base de datos
                #se delcara una variable y se crea un objeto, en parentesis van los campos de la tabla
                #variable=Modelo.objects.create(campos de tabla)
                person=Padre.objects.create(nombre1=nombre1,nombre2=nombre2,apellido1=apellido1,apellido2=apellido2,dui=duiP,division=division,subdivision=subdivision,
                                            sexo=sexo)
                #el objeto se guarda con .save
                person.save

            except Exception as e:
                #si hay un problema realiza un rollback
                #handle_exception()
                p=False
            #redirige al registro de doctor usando una url que envia los parametros a la siguiente función
            return redirect('miTemplate',nombre1=nombre1,nombre2=nombre2,apellido1=apellido1,apellido2=apellido2,dui=duiP,division=division,subdivision=subdivision,sexo=sexo)
    else:
         formulario1=FormAgregarPadre(prefix="pru1")
         return render(request,'miTemplate.html',{'form1':formulario1})