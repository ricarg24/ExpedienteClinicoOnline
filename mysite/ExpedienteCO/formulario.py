from django import forms
from django.forms import widgets
from django.forms import ModelForm,Textarea,TextInput,MultiValueField
from django.core import validators
from ExpedienteCO.models import Padre
from django.contrib.auth.models import User
import re
import datetime
from django.core.validators import validate_email
#limpiezaPersona(tamDui,fieldNombre1,fieldNombre2,fieldApellido1,fieldApellido2,fieldPais,fieldDivision,fieldSubDivision,fieldSexo)
def limpiezaPersona(dui,nombre1,nombre2,apellido1,apellido2,pais,division,subdivision,sexo):
	#se pueden usar los parametros o guardarlos en otra variable
    tamDui=dui
    fieldNombre1=nombre1
    fieldNombre2 = nombre2
    fieldApellido1=apellido1
    fieldApellido2 = apellido2
    fieldPais=pais
    fieldDivision=division
    fieldSubDivision=subdivision

    fieldSexo=sexo
    conta=0
    vocales = "aeiouAEIOU"

    errores=[] #Arreglo para guardar errores
    errorNombre="El nombre ingresado no es válido"
    errorApellido="El apellido ingresado no es válido"
    errorDUI="Error el DUI ingresado no es válido"

    if len(fieldNombre1)!=0 and len(fieldApellido1)!=0 :
        nombr=fieldNombre1.split()
        apell=fieldApellido1.split()

        if len(nombr)==1 and len(apell)==1:
            errores.append("Datos no validos, deben ser por lo menos un Nombre y dos apellidos o dos Nombres y un Apellido") #se agrega el error
        for letra in fieldNombre1:
            if letra not in vocales:
                conta+=1
        if conta==0 or conta==len(fieldNombre1):
            errores.append(errorNombre)

        if len(fieldNombre1)==1:
            errores.append(errorNombre)
            if len(fieldNombre2) == 1:
                errores.append(errorNombre)
        if len(fieldApellido1)==1:
            errores.append(errorApellido)
            if len(fieldApellido2) == 1:
                errores.append(errorApellido)
        for aux1 in nombr:
            if not aux1.isalpha():
                errores.append(errorNombre)
        for aux1 in apell:
            if not aux1.isalpha():
                errores.append(errorApellido)

        conta=0
        for letra in fieldApellido1:
            if letra not in vocales:
                conta+=1
        if conta==0 or conta==len(fieldApellido1):
            errores.append(errorApellido)


    if len(fieldNombre1)==0 and len(fieldApellido1)==0 :
        errores.append(errorNombre)
        errores.append(errorApellido)

    elif len(fieldNombre1)==0:
        errores.append(errorNombre)
    elif len(fieldApellido1)==0:
        errores.append(errorApellido)


    if len(tamDui) != 10:
        errores.append(errorDUI)
    contador=1

    for digit in tamDui:
        if contador == 9:
            if digit!="-":
                errores.append(errorDUI)
        elif not digit.isdigit():
            errores.append(errorDUI)
        contador+=1

    if Padre.objects.filter(dui=tamDui).exists():
        errores.append("Error DUI corresponde a una persona registrada anteriormente")

    if tamDui.isspace():
        errores.append("El DUI solo contiene espacios en blanco")


    if len(fieldPais)<=2:
        errores.append("el pais introducida no es válida")

    if fieldDivision.isspace():
        errores.append("La division introducida solo contiene espacios en blanco")
    if fieldSubDivision.isspace():
            errores.append("La division introducida solo contiene espacios en blanco")

    if fieldSexo=='3':
        errores.append("Elija un sexo para la persona")


    if len(errores)!=0: #si hay errores muestra un mensaje
        raise forms.ValidationError(errores)


class FormAgregarPadre(forms.Form):
    #aqui se declaran los tipos de input,select,etc que vamos a utilizar
    nombre1=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el nombre del padre'}),max_length=20,strip=False)
    nombre2 = forms.CharField(widget=forms.TextInput(attrs={'size': 30, 'placeholder': 'Digite el segundo nombre del padre'}), max_length=20,strip=False)
    apellido1=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el primer apellido'}),max_length=20,strip=False)
    apellido2= forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el primer apellido'}),max_length=20 ,strip=False)
    pais = forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el pais del padre'}),max_length=15,strip=False)
    division = forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el division del division'}),max_length=15,strip=False)
    subdivision = forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el subdivision del padre'}),max_length=15,strip=False)
    dui = forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el dui del padre'}),max_length=15,strip=False)
    genero= forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Digite el genero del padre'}),max_length=15,strip=False)

    def clean(self):
        cleaned_data=super(FormAgregarPadre,self).clean()
        tamDui=cleaned_data.get("dui").strip() #.strip() elimina los espacios en blanco a la izquierda y derecha de la palabra
        fieldNombre1=cleaned_data.get("nombre1").strip()
        fieldNombre2 = cleaned_data.get("nombre2").strip()
        fieldApellido1=cleaned_data.get("apellido1").strip()
        fieldApellido2 = cleaned_data.get("apellido2").strip()
        fieldPais=cleaned_data.get("pais").strip()
        fieldDivision=cleaned_data.get("division").strip()
        fieldSubDivision=cleaned_data.get("subdivision").strip()
        fieldSexo=cleaned_data.get("sexo")
        limpiezaPersona(tamDui,fieldNombre1,fieldNombre2,fieldApellido1,fieldApellido2,fieldPais,fieldDivision,fieldSubDivision,fieldSexo)