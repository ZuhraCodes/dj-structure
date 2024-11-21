from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .utils import get_tokens_for_user
from apps.users.models import User, OneTimeCode
from datetime import datetime, timedelta

class NewLoginConfirmSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^\+998\d{9}$',
        error_messages={
            'invalid': "Phone number must be in the format '+998xxyyyzzyy'."
        }
    )
    code = serializers.CharField()
    
    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        one_time_code = validated_data['code']
        
        expire_time = datetime.now() - timedelta(seconds=60)
        
        otp = OneTimeCode.objects.filter(phone_number=phone_number).last()
                
        if otp and otp.is_expired():
            raise ValidationError({
                "error": "code_is_expired",
                "message": "Code is expired. Retry again"
            })
            
        if otp and otp.code != one_time_code:
            raise ValidationError({
                "error": "code_is_wrong",
                "message": "Wrong code received."
            })
            
        if not otp:
            raise ValidationError({
                "error": "access_restricted",
                "message": "Access denied. First, request to login"
            })

        user = User.objects.get(username=phone_number, phone_number=phone_number)
        return get_tokens_for_user(user)