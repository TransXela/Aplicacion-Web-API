from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from app.models import TxdDenuncia
from app.serializables import TxdDenunciaS
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def lista_objetos(request):
    """
    Lista de todas las Buses, o crear una nueva
    """
    try:
        objToken = Token.objects.get(key=request.query_params.get('tk'))
        usuario = User.objects.get(pk=objToken.user.id)
    except ObjectDoesNotExist:
        content = {'Datos incorrectos': 'El token enviado no coincide para ningun usuario'}
        return Response(content, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        if usuario.has_perm('app.view_txddenuncia'):
            objeto = TxdDenuncia.objects.all()
            serializador = TxdDenunciaS(objeto, many=True)
            return Response(serializador.data)
        else:
            content = {'Permiso denegado': 'El usuario no tiene permisos para ver datos'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)


    elif request.method == 'POST':
        if usuario.has_perm('app.add_txddenuncia'):
            serializador = TxdDenunciaS(data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {'Permiso denegado': 'El usuario no tiene permisos para ingresar datos'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'PUT','DELETE'])
def detalle_objetos(request, pk):
    """
    Actualiza, elimina un objeto segun su id
    """
    try:
        objToken = Token.objects.get(key=request.query_params.get('tk'))
        usuario = User.objects.get(pk=objToken.user.id)
    except ObjectDoesNotExist:
        content = {'Datos incorrectos': 'El token enviado no coincide para ningun usuario'}
        return Response(content, status=status.HTTP_403_FORBIDDEN)

    try:
        objeto = TxdDenuncia.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if usuario.has_perm('app.view_txddenuncia'):
            serializador = TxdDenunciaS(objeto)
            return Response(serializador.data)
        else:
            content = {'Permiso denegado': 'El usuario no tiene permisos para ver datos'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)


    elif request.method == 'PUT':
        if usuario.has_perm('app.change_txddenuncia'):
            serializador = TxdDenunciaS(objeto, data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data)
            return Response(serializador.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {'Permiso denegado': 'El usuario no tiene permisos para editar datos'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)

    elif request.method == 'DELETE':
        if usuario.has_perm('app.delete_txddenuncia'):
            objeto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            content = {'Permiso denegado': 'El usuario no tiene permisos para eliminar datos'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)



@api_view(['GET'])
def buses_Activos(request):
    """
    retorna los busese que estan activos
    """
    try:
        objToken = Token.objects.get(key=request.query_params.get('tk'))
        usuario = User.objects.get(pk=objToken.user.id)
    except ObjectDoesNotExist:
        content = {'Datos incorrectos': 'El token enviado no coincide para ningun usuario'}
        return Response(content, status=status.HTTP_403_FORBIDDEN)


    if request.method == 'GET':
        if usuario.has_perm('app.view_txddenuncia'):
            try:
                objetos = TxdDenuncia.objects.filter(estado=1)
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            serializador = TxdDenunciaS(objetos, many=True)
            return Response(serializador.data)
        else:
            content = {'Permiso denegado': 'El usuario no tiene permisos para ver datos'}
            return Response(content, status=status.HTTP_403_FORBIDDEN)
