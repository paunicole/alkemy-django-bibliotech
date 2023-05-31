from django.shortcuts import render, redirect, get_object_or_404
from ..models.member import Member


def member_disable(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.is_active = False
    member.save()
    return redirect("member-list")


def member_enable(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.is_active = True
    member.save()
    return redirect("member-list")
