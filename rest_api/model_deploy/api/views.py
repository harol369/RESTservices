#Import necessary libraries
import pickle
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
import numpy as np
from .models import Autores,Clientes,Categorias,PedidoCliente,LibroPorAutor,Libros
import json
from .Serializers import CategoriaSerializer

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

@api_view(['GET'])
def mostrarAutores(request):
    id = request.data.get("id_autor")
    #autor = Autores.objects.get(id_autor = id)
    autores = Autores.objects.all()
    # id_a =autores[0].id_autor
    # nombre=autores[0].nombres
    # apellidos=autores[0].apellidos

    return_data = {}

    for autor in autores:
        aut ={'id': autor.id_autor, 'apellidos': autor.apellidos, 'nombres': autor.nombres}
        clave = 'autor' + str(autor.id_autor)
        return_data[clave] = aut

        # 'id' : id_a,
        # 'nombres' : nombre,
        # 'apellidos' : apellidos,
    
    return Response(return_data)

@api_view(['GET'])
def mostrarCategorias(request):
    id = request.data.get("id_autor")
    #autor = Autores.objects.get(id_autor = id)
    categorias = Categorias.objects.all()
    # id_a =autores[0].id_autor
    # nombre=autores[0].nombres
    # apellidos=autores[0].apellidos

    return_data = {}

    for categoria in categorias:
        cat ={'id': categoria.id_categoria, 'nombre': categoria.categoria}
        clave = 'categoria' + str(categoria.id_categoria)
        return_data[clave] =  cat

        # 'id' : id_a,
        # 'nombres' : nombre,
        # 'apellidos' : apellidos,
    
    return Response(return_data)

@api_view(['POST'])
def mostrarAut(request):
    id = int(request.data.get("id_autor"))
    autores = Autores.objects.all()

    return_data = {'id': autores[id - 1].id_autor, 'nombres': autores[id - 1].nombres,'apellidos': autores[id - 1].apellidos}

    return Response(return_data)


# SERVICIOS DE CATEGORÍAS
# Eliminar Pedido Cliente método GET
@api_view(['GET'])
def eliminaPedidoCliente(request):
    pedido = int(request.data.get('id_pedido'))
    isbn = int(request.data.get('isbn'))
    
    try:
        id_p = PedidoCliente.objects.get(id_pedido = pedido)
        id_l = PedidoCliente.objects.get(isbn = isbn)

        PedidoCliente.delete(id_p)
        PedidoCliente.delete(id_l)

        elimina = {'id pedido': pedido,
                    'id libro': isbn,
                'eliminado': '200 Ok',
                'error': 0
        }
    except Exception as e:
        error = str(e)
        elimina = {'id pedido': pedido,
                    'id libro': isbn,
                   'eliminado': False,
                   'error': error}
        
    return Response(elimina)




# Insertar Categorías método GET
@api_view(['POST'])
def insertarAutores(request):
    nom = request.data.get('nombres')
    ape = request.data.get('apellidos')
    
    try:
        autores= Autores()
        autores.nombres = nom
        autores.apellidos=ape
        autores.save()
        insertar = {'nombres': nom,
                    'apellidos':ape,
                    'insertado': '200 Ok',
                    'error': 0}
    except Exception as e:
        error = 'No se ha podido insertar el registro.  ' + str(e)
        insertar = {'categoria': None,
                    'insertado': False,
                    'error': error}
    
    return Response(insertar)


# Insertar Categorias método POST
@api_view(['POST'])
def insertarCategoriaPOST(request):
    cat = request.data.get('categoria')
    
    try:
        categoria = Categorias()
        categoria.categoria = cat
        categoria.save()
        insertar = {'categoria': cat,
                    'insertado': '200 Ok',
                    'error': 0}
    except Exception as e:
        error = 'No se ha podido insertar el registro.  ' + str(e)
        insertar = {'categoria': cat,
                    'insertado': False,
                    'error': error}
    
    return Response(insertar)


# Actualizar Categorias método GET
@api_view(['GET'])
def actualizarCategoria(request):
    a = request.data.get('id_categoria')
    task = Categorias.objects.get(id_categoria=a)
    serializer = CategoriaSerializer(task, data=request.data)

    if serializer.is_valid():
       serializer.save()
    return Response(serializer.data)
    
    # try:
    #     categoria = Categorias()
    #     categoria.categoria = cat
    #     categoria.save()
    #     insertar = {'categoria': json_categoria.categoria,
    #                 'insertado': '200 Ok',
    #                 'error': 0}
    # except Exception as e:
    #     error = 'No se ha podido insertar el registro.  ' + str(e)
    #     actualizar = {'categoria': cat,
    #                 'insertado': False,
    #                 'error': error}
    
    return Response(actualizar)
