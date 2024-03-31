from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'users': '/users',
        'posts': '/posts',
        'comments': '/comments',
        'likes': '/likes',
        'followers': '/followers',
    })
