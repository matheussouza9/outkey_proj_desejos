from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from api.permissions import IsSuperuserOrBasicForUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from api.serializers import UserSerializer, RestrictedUserSerializer

class UserListCreateApiView(APIView):
    permission_classes = (IsAuthenticated, IsSuperuserOrBasicForUser,)

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            usuarios = User.objects.all()
            # se passar a variavel request para o context, a url para o recurso passa de relativa para absoluta
            serializer = UserSerializer(usuarios, many=True, context={'request': request})
        else:
            usuarios = User.objects.filter(pk=request.user.id)
            serializer = RestrictedUserSerializer(usuarios, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data, context={'request': request})
        # raise_exception=True retorna status 400 se nao for valido
        if serializer.is_valid(raise_exception=True):
            if serializer.save():
                return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.error_messages)

class UserRetriveUpdateDestroyApiView(APIView):
    permission_classes = (IsAuthenticated, IsSuperuserOrBasicForUser,)

    def get(self, request, pk, *args, **kwargs):
        usuario = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, usuario)

        if request.user.is_superuser:
            serializer = UserSerializer(usuario, context={'request': request})
        else:
            serializer = RestrictedUserSerializer(usuario, context={'request': request})

        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        usuario = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, usuario)

        if request.user.is_superuser:
            serializer = UserSerializer(usuario, data=request.data, context={'request': request})
        else:
            serializer = RestrictedUserSerializer(usuario, data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            if serializer.save():
                return Response(serializer.data)

        return Response(serializer.error_messages)

    def delete(self, request, pk, *args, **kwargs):
        usuario = get_object_or_404(User, pk=pk)
        usuario.delete()

        return Response({}, status=HTTP_204_NO_CONTENT)