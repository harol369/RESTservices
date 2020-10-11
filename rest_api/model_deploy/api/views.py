#Import necessary libraries
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework import request
from django.shortcuts import render
import numpy as np
from .models import Autores, Libros
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_diabetictype(request):
    try:
        age = request.data.get('age', None)
        bs_fast = request.data.get('bs_fast', None)
        bs_pp = request.data.get('bs_pp', None)
        plasma_r = request.data.get('plasma_r', None)
        plasma_f = request.data.get('plasma_f', None)
        hbA1c = request.data.get('hbA1c', None)
        fields = [age, bs_fast, bs_pp, plasma_r, plasma_f, hbA1c]
        if not None in fields:
            #Datapreprocessing Convert the values to float
            age = float(age)
            bs_fast = float(bs_fast)
            bs_pp = float(bs_pp)
            plasma_r = float(plasma_r)
            plasma_f = float(plasma_f)
            hbA1c = float(hbA1c)
            result = [age,bs_fast,bs_pp,plasma_r,plasma_f,hbA1c]
            #Passing data to model & loading the model from disks
            model_path = './model.pkl'
            classifier = pickle.load(open(model_path, 'rb'))
            prediction = classifier.predict([result])[0]
            conf_score = np.max(classifier.predict_proba([result]))*100
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'prediction' : prediction,
                'confidence_score' : conf_score
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)

#SERVICIO DE AUTORES

@api_view(["GET"])
def MostrarAutor(request):
    return_data={}
    try:
        id_a = request.data.get("id_autor")
        autores = Autores.objects.all()
        # id_a = autores[0].id_autor
        # nombre = autores[0].nombres
        # apellidos = autores[0].apellidos
        # return_data = {
        #     "id_autor" : id_a,
        #     "nombres": nombre,
        #     "apellidos" : apellidos,
        #     "message" : "Bien papito",
        # }
        #LISTAR
        for autor in autores:
            aut = {'id': autor.id_autor, 'nombres':autor.nombres, 'apellidos': autor.apellidos}
            clave = 'autor ' + str(autor.id_autor)
            return_data[clave] = aut

        
    except Exception as e:
        return_data = {
            'error' : '2',
            "message": str(e)
        } 
    return Response(return_data) 

@api_view(["POST"])
def BuscarAutor(request):
    try:
        id = int(request.data.get("id_autor"))
        autores = Autores.objects.all()

        return_data = {'id_autor':autores[id - 1].id_autor, 'sadsa': autores[id - 1].nombres, 'apellidos': autores[id - 1].apellidos}

    except Exception as e:
        return_data = {
            'error' : '2',
            "message": str(e)
        } 
    return Response(return_data) 
