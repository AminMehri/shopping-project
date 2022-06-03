from django.contrib import admin
from .models import Book, Author, Category, Quote, User



class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_shopcard',)


    def get_shopcard(self, obj):
        return " ,".join([p.title for p in obj.shopcard.all()])
    get_shopcard.short_description = "shopcard"


admin.site.register(User, UserAdmin)



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_category', 'get_author', 'price')
    prepopulated_fields = {"slug": ("title",)}


    def get_category(self, obj):
        return " ,".join([p.title for p in obj.category.all()])
    get_category.short_description = "categories"


    def get_author(self, obj):
        return " ,".join([p.full_name for p in obj.author.all()])
    get_author.short_description = "authors"

admin.site.register(Book, BookAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'slug')
    prepopulated_fields = {"slug": ("full_name",)}

admin.site.register(Author, AuthorAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)



class QuoteAdmin(admin.ModelAdmin):
    list_display = ('source', 'get_author')


    def get_author(self, obj):
        return " ,".join([p.full_name for p in obj.author.all()])
    get_author.short_description = "authors"

admin.site.register(Quote, QuoteAdmin)

