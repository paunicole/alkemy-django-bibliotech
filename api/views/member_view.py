from rest_framework import viewsets, permissions
from ..serializers.member_serializer import MemberSerializer
from bibliotech.models import Member


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberSerializer
