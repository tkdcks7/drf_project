from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        pass


class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass
    
    def put(self, request, article_id):
        pass

    def delete(self, request, article_id):
        pass


class ArticleView(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        pass


class CommentDetailView(APIView):
    def get(self, request, comment_id):
        pass
    
    def put(self, request, comment_id):
        pass

    def delete(self, request, comment_id):
        pass


class LikeView(APIView):
    def post(self, request):
        pass