from cms.models import Desejo
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

class DesejoSerializer(HyperlinkedModelSerializer):
    dono = HyperlinkedRelatedField(view_name="api_retrieve_update_destroy_usuario", queryset=User.objects.all(), required=True)

    class Meta:
        model = Desejo
        fields = ('url', 'pk', 'descricao', 'dono')
        extra_kwargs = {
            'url': {'view_name': 'api_retrieve_update_destroy_desejo', 'lookup_field': 'pk'},
        }

    def create(self, validated_data):
        desejo = Desejo(**validated_data)
        desejo.save()
        return desejo

    def update(self, desejo, validated_data):
        desejo.descricao = validated_data.get('descricao', desejo.descricao)
        desejo.dono = validated_data.get('dono', desejo.dono)
        desejo.save()
        return desejo

class RestrictedDesejoSerializer(DesejoSerializer):
    dono = HyperlinkedRelatedField(view_name="api_retrieve_update_destroy_usuario", read_only=True)

    class Meta(DesejoSerializer.Meta):
        read_only_fields = ('dono',)

    def update(self, desejo, validated_data):
        desejo.descricao = validated_data.get('descricao', desejo.descricao)
        desejo.save()
        return desejo