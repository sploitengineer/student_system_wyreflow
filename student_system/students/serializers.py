from rest_framework import serializers
from .models import Students
from django.contrib.auth.hashers import make_password

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'full_name', 'email', 'mobile', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            student = Students.objects.get(email=data['email'])
        except Students.DoesNotExist:
            raise serializers.ValidationError("Invalid email")

        from django.contrib.auth.hashers import check_password
        if not check_password(data['password'], student.password):
            raise serializers.ValidationError("Invalid password")

        data['student'] = student
        return data