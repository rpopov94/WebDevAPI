from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.models import Post
from core.serializers import PostSerializer


class Paginator(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100


class PostViews(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = Paginator
