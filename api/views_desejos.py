from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from api.permissions import IsSuperuserOrBasicForDesejo
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cms.models import Desejo
from django.shortcuts import get_object_or_404
from api.serializers_desejos import DesejoSerializer, RestrictedDesejoSerializer


class DesejoListCreateApiView(APIView):
    permission_classes = (IsAuthenticated, IsSuperuserOrBasicForDesejo,)

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            desejos = Desejo.objects.all()
            serializer = DesejoSerializer(desejos, many=True, context={'request': request})
        else:
            desejos = Desejo.objects.filter(dono=request.user)
            serializer = RestrictedDesejoSerializer(desejos, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = DesejoSerializer(data=request.data, context={'request': request})
        else:
            serializer = RestrictedDesejoSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            if request.user.is_superuser:
                serializer.save()
            else:
                serializer.save(dono=request.user)

            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.error_messages)


class DesejoRetrieveUpdateDestroyApiView(APIView):
    permission_classes = (IsAuthenticated, IsSuperuserOrBasicForDesejo,)

    def get(self, request, pk, *args, **kwargs):
        desejo = get_object_or_404(Desejo, pk=pk)
        self.check_object_permissions(request, desejo)

        if request.user.is_superuser:
            serializer = DesejoSerializer(desejo, context={'request': request})
        else:
            serializer = RestrictedDesejoSerializer(desejo, context={'request': request})

        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        desejo = get_object_or_404(Desejo, pk=pk)
        self.check_object_permissions(request, desejo)

        if request.user.is_superuser:
            serializer = DesejoSerializer(desejo, data=request.data, context={'request': request})
        else:
            serializer = RestrictedDesejoSerializer(desejo, data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            if request.user.is_superuser:
                serializer.save()
            else:
                serializer.save(dono=request.user)

            return Response(serializer.data)

        return Response(serializer.error_messages)

    def delete(self, request, pk, *args, **kwargs):
        desejo = get_object_or_404(Desejo, pk=pk)
        self.check_object_permissions(request, desejo)
        desejo.delete()

        return Response({}, status=HTTP_204_NO_CONTENT)
