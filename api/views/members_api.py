from django.http import JsonResponse
from bibliotech.models.member import Member


def member_list(request):
    members = Member.objects.all()
    members_list = []
    for member in members:
        members_list.append(
            {
                "id": member.id,
                "first_name": member.first_name,
                "last_name": member.last_name,
                "birth_date": member.birth_date,
                "is_active": member.is_active,
            }
        )
    return JsonResponse({"members": members_list})


def member_id(request, pk):
    member = Member.objects.get(id=pk)
    member_detail = {
        "id": member.id,
        "first_name": member.first_name,
        "last_name": member.last_name,
        "birth_date": member.birth_date,
        "is_active": member.is_active,
    }
    return JsonResponse({"member": member_detail})
