from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import TxdDuenio
from app.serializables import TxdDuenioS, DueniosChoferBuses,DueniosChoferes,DueniosHorarios,DueniosBuses


@api_view(['GET', 'POST'])
def lista_objetos(request):
    """
    Lista de todos los Duenios, o crea uno nuevo.
    """
    if request.method == 'GET':
        objeto = TxdDuenio.objects.all()
        serializador = TxdDuenioS(objeto, many=True)
        return Response(serializador.data)

    elif request.method == 'POST':
        serializador = TxdDuenioS(data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def principal_duenio_choferes(request,pk, var):
    """
    Lista los buses y choferes
    """
    try:
        objeto = TxdDuenio.objects.get(pk=pk)
    except objeto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if var==0:
            serializador = DueniosChoferBuses(objeto)
            return Response(serializador.data)
        elif var==1:
            serializador = DueniosChoferes(objeto)
            return Response(serializador.data)
        elif var==2:
            serializador = DueniosHorarios(objeto)
            return Response(serializador.data)
        elif var==3:
            serializador = DueniosBuses(objeto)
            return Response(serializador.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def detalle_objetos(request, pk):
    """
    Actuliza, elimina un objeto segun su id
    """
    try:
        objeto = TxdDuenio.objects.get(pk=pk)
    except objeto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializador = TxdDuenioS(objeto)
        return Response(serializador.data)

    elif request.method == 'PUT':
        serializador = TxdDuenioS(objeto, data=request.data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data)
        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
