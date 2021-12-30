from django.core import validators
from rest_framework.serializers import *
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(ModelSerializer):

    first_name = CharField(max_length=255, required=True)
    last_name = CharField(max_length=255, required=True)
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = CharField(
        max_length=255,
        required=True,
        write_only=True,
        validators=[validate_password]
    )
    password2 = CharField(
        max_length=255,
        required=True,
        write_only=True,
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                "Les deux mots de passe ne sont pas identiques")
        return attrs

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
