from .models import *
from . import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12



class ShowBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    pagination_class = LargeResultsSetPagination
    search_fields = ['title', 'author__full_name', 'description', 'category__title']



class ShowCategories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer



class ShowAuthors(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer



class ShowDetailBook(APIView):

    def post(self, request):
        
        serializer = serializers.DetailBookSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
            
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        book = Book.objects.filter(slug=slug)
        
        data = []
        for b in book:
            data.append({
                'title': b.title,
                'category': [c.title for c in b.category.all()],
                'category_slug': [c.slug for c in b.category.all()],
                'author': [c.full_name for c in b.author.all()],
                'author_slug': [c.slug for c in b.author.all()],
                'slug': b.slug,
                'content': b.content,
                'about_book': b.about_book,
                'image': b.image.url,
                'price': b.price,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



# class ShowDetailBook(ListAPIView):
#     serializer_class = serializers.BookSerializer
#     def get_queryset(self):
#         slug = self.request.data.get('slug')
#         book = Book.objects.filter(slug=slug)
#         return book



class ShowSingleCategory(APIView):
    
    def post(self, request):

        serializer = serializers.DetailBookSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
        
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

        category = get_object_or_404(Category, slug=slug)

        books = category.books.all()

        data = []
        for book in books:
            data.append({
                'title': book.title,
                'category': [b.title for b in book.category.all()],
                'author': [b.full_name for b in book.author.all()],
                'slug': book.slug,
                'description': book.description,
                'cover': book.cover.url,
                'price': book.price,
            })
        
        category_title = category.title
        
        return Response({'status': 'ok', 'data': data, 'category_title':category_title}, status=status.HTTP_200_OK)
        


# class ShowSingleCategory(ListAPIView):
#     serializer_class = serializers.SingleCategorySerialzer
#     def get_queryset(self):
#         slug = self.request.data.get('slug')
#         category = get_object_or_404(Category, slug=slug)
#         books = category.books.all()
#         return books


class ShowSingleAuthor(APIView):

    def post(self, request):

        serializer = serializers.DetailBookSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
        
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        author = get_object_or_404(Author, slug=slug)

        books = author.books.all()

        data = []
        for book in books:
            data.append({
                'title': book.title,
                'category': [b.title for b in book.category.all()],
                'author': [b.full_name for b in book.author.all()],
                'slug': book.slug,
                'description': book.description,
                'cover': book.cover.url,
                'price': book.price,
            })

        author_data = [{
            'full_name': author.full_name,
            'description': author.description,
            'slug': author.slug,
            'image1': author.image1.url,
            'image2': author.image2.url,
            'image3': author.image3.url,
        }]

        quotes = author.quotes.all()

        quotes_data = []
        for quote in quotes:
            quotes_data.append({
                'description': quote.description,
                'source': quote.source,
                'author': [b.full_name for b in quote.author.all()],
            })
        
        return Response({'status': 'ok', 'data': data, 'author_data': author_data, 'quotes_data': quotes_data}, status=status.HTTP_200_OK)



class ShowProfile(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProfileSerialzer
    def get_queryset(self):
        username = self.request.user.username
        users = User.objects.filter(username=username)
        return users



class GetProfileInformation(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProfileInformationSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)



class ShowShopcard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        username = self.request.user.username

        users = get_object_or_404(User, username=username)

        books = users.shopcard.all()

        data = []
        for book in books:
            data.append({
                'title': book.title,
                'category': [b.title for b in book.category.all()],
                'author': [b.full_name for b in book.author.all()],
                'slug': book.slug,
                'description': book.description,
                'cover': book.cover.url,
                'price': book.price,
            })

        total_price = 0
        for book in data:
            total_price += book.get('price')
        

        Number_of_books_in_the_shopcart = len(data)
        

        return Response({'status': 'ok', 'data': data, 'total_price': total_price, 'Number_of_books_in_the_shopcart': Number_of_books_in_the_shopcart}, status=status.HTTP_200_OK)



class RemoveFromShopcard(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ShopCardSerializer

    def update(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        book = get_object_or_404(Book, slug=request.data.get('slug'))
        user.shopcard.remove(book)
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddToShopcard(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ShopCardSerializer

    def update(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.user.username)
        book = get_object_or_404(Book, slug=request.data.get('slug'))
        user.shopcard.add(book)
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)