from rest_framework import serializers
from .models import Book, User, Category, Author



class DetailBookSerializer(serializers.Serializer):
    slug = serializers.CharField(allow_null=False, allow_blank=False)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class ProfileInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'address', 'phone_number')
        read_only_fields = ('username',)

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance



class ShopCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('shopcard',)
    
    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['title', 'slug', 'cover']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['full_name', 'slug', 'cover']


class ProfileSerialzer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'address', 'phone_number', 'email']



# class SingleCategorySerialzer(serializers.ModelSerializer):
#     author = serializers.StringRelatedField(many=True)
#     category = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Book
#         fields = ['title', 'category', 'author', 'slug', 'description', 'cover', 'price']

