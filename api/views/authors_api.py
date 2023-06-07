from django.http import JsonResponse
from bibliotech.models.author import Author


def author_list(request):
    authors = Author.objects.all()
    authors_list = []
    for author in authors:
        authors_list.append(
            {
                "id": author.id,
                "first_name": author.first_name,
                "last_name": author.last_name,
                "nationality": author.nationality.name,
                "is_active": author.is_active,
            }
        )
    return JsonResponse({"authors": authors_list})


def author_id(request, pk):
    author = Author.objects.get(id=pk)
    author_detail = {
        "id": author.id,
        "first_name": author.first_name,
        "last_name": author.last_name,
        "nationality": author.nationality.name,
        "is_active": author.is_active,
    }
    return JsonResponse({"author": author_detail})
