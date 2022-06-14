from .models import *
from . import serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 12



class ShowBooks(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    pagination_class = LargeResultsSetPagination
    search_fields = ['title', 'author__full_name', 'description', 'category__title']



# class ShowBooks(APIView):

#     def get(self, request):

#         books = Book.objects.all()

#         data = []
#         for book in books:
#             data.append({
#                 'title': book.title,
#                 'category': [b.title for b in book.category.all()],
#                 'author': [b.full_name for b in book.author.all()],
#                 'slug': book.slug,
#                 'description': book.description,
#                 'cover': book.cover.url,
#                 'price': book.price,
#             })

#         return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowCategories(APIView):

    def post(self, request):

        categories = Category.objects.all()

        data = []
        for category in categories:
            data.append({
                'title': category.title,
                'slug': category.slug,
                'cover': category.cover.url,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowAuthors(APIView):

    def post(self, request):

        authors = Author.objects.all()

        data = []
        for author in authors:
            data.append({
                'full_name': author.full_name,
                'slug': author.slug,
                'cover': author.cover.url,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



class ShowDetailBook(APIView):

    def post(self, request):
        
        serializer = serializers.DetailBookSerializer(data=request.data)
        print(serializer)
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



class ShowProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        username = self.request.user.username
        
        users = User.objects.filter(username=username)

        data = []
        for user in users:
            data.append({
                'username': user.username,
                'full_name': user.first_name + ' ' + user.last_name,
                'email': user.email,
                'address': user.address,
                'phone_number': user.phone_number,
            })

        return Response({'status': 'ok', 'data': data}, status=status.HTTP_200_OK)



# class GetProfileInformation(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):

#         serializer = serializers.ProfileInformationSerializer(data=request.data)
#         if serializer.is_valid():
#             first_name  = serializer.data.get('first_name ')
#             last_name  = serializer.data.get('last_name ')
#             address  = serializer.data.get('address ')
#             email  = serializer.data.get('email ')
        
#         else:
#             return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

#         username = self.request.user.username

#         users = User.objects.filter(username=username)

#         for user in users:
#             user.first_name = first_name
#             user.last_name = last_name
#             user.address = address
#             user.email = email
#             print()

#         return Response({'status': 'ok'}, status=status.HTTP_200_OK)



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



class RemoveFromShopcard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.DetailBookSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
        
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        username = self.request.user.username

        user = get_object_or_404(User, username=username)

        book = get_object_or_404(Book, slug=slug)

        user.shopcard.remove(book)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)



class AddToShopcard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = serializers.DetailBookSerializer(data=request.data)
        if serializer.is_valid():
            slug = serializer.data.get('slug')
        
        else:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
        username = self.request.user.username

        user = get_object_or_404(User, username=username)

        book = get_object_or_404(Book, slug=slug)

        user.shopcard.add(book.id)

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
