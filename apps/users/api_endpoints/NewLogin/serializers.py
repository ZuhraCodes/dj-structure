from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .utils import get_tokens_for_user
from apps.users.models import User, OneTimeCode
from datetime import datetime, timedelta
import random

class NewLoginSerializer(serializers.Serializer):
    phone_number = serializers.RegexField(
        regex=r'^\+998\d{9}$',
        error_messages={
            'invalid': "Phone number must be in the format '+998xxyyyzzyy'."
        }
    )
    
    def create(self, validated_data):
        phone_number = validated_data['phone_number']
        one_time_code = random.randint(100000, 999999)
        print(one_time_code)
        
        expire_time = datetime.now() - timedelta(seconds=60)
        User.objects.get_or_create(phone_number=phone_number, username=phone_number)
        
        if OneTimeCode.objects.filter(phone_number=phone_number, created_at__gte=expire_time).exists():
            raise ValidationError({
                "error": "code_already_sent",
                "message": "We have already sent a code, you can try again after 60s"
            })
        
        OneTimeCode.objects.create(code=one_time_code, phone_number=phone_number)

        
        return {
            "message": "Code sent successfully"
        }
        