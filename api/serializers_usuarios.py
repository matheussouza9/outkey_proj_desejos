from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'email', 'password',  'is_active', 'is_superuser')
        extra_kwargs = {
            'url': {'view_name': 'api_retrieve_update_destroy_usuario', 'lookup_field': 'pk'},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, user, validated_data):
        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        user.set_password(validated_data.get('password', user.password))
        user.is_active = validated_data.get('is_active', user.is_active)
        user.is_superuser = validated_data.get('is_superuser', user.is_superuser)
        user.save()
        return user

class RestrictedUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = ('is_active', 'is_superuser')

    def update(self, user, validated_data):
        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.email = validated_data.get('email', user.email)
        user.set_password(validated_data.get('password', user.password))
        user.save()
        return user
