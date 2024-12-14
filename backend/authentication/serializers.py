from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
	confirm_password = serializers.CharField(write_only=True, required=True)
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'confirm_password']
		extra_kwargs = {
			'password': {'write_only': True},
		}
	
	def validate(self, data):
		# Check if passwords match
		if data['password'] != data['confirm_password']:
			raise serializers.ValidationError({"password": "Passwords do not match."})
		return data
	
	def create(self, validated_data):
		validated_data.pop('confirm_password')  # Remove confirm_password from data
		user = User.objects.create_user(
			username=validated_data['username'],
			email=validated_data['email'],
			password=validated_data['password']
		)
		return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom serializer to add user information to the token response."""
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom response data (like user info)
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data