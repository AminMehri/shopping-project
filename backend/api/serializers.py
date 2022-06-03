from rest_framework import serializers
from .models import Book, User



class DetailBookSerializer(serializers.Serializer):
    slug = serializers.CharField(allow_null=False, allow_blank=False)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ['title', 'description', 'slug', 'category', 'author', 'cover', 'image', 'price']



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