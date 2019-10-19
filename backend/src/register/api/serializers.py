from rest_framework import serializers
from register.models import register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ('title','content')