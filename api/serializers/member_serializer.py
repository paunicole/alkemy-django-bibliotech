from rest_framework import serializers
from bibliotech.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "first_name", "last_name", "birth_date", "is_active"]
