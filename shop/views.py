from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer

from shop.models import Category, Product, Article


class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

class ProductViewset(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = Product.objects.filter(category_id=category_id)
        return queryset

class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = Article.objects.filter(product_id=product_id)
        return queryset