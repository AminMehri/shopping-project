from django.urls import path, include
from . import views


urlpatterns = [
    path('ShowBooks/', views.ShowBooks.as_view(), name='show_book'),
    path('ShowCategories/', views.ShowCategories.as_view(), name='show_categories'),
    path('ShowAuthors/', views.ShowAuthors.as_view(), name='show_authors'),
    path('ShowDetailBook/', views.ShowDetailBook.as_view(), name='show_detail_book'),
    path('ShowSingleCategory/', views.ShowSingleCategory.as_view(), name='show_single_category'),
    path('ShowSingleAuthor/', views.ShowSingleAuthor.as_view(), name='show_single_author'),
    path('ShowProfile/', views.ShowProfile.as_view(), name='show_profile'),
    path('ShowShopcard/', views.ShowShopcard.as_view(), name='show_shopcard'),
    path('RemoveFromShopcard/', views.RemoveFromShopcard.as_view(), name='remove_from_shopcard'),
    path('AddToShopcard/', views.AddToShopcard.as_view(), name='add_to_shopcard'),
    path('GetProfileInformation/', views.GetProfileInformation.as_view(), name='get_profile_information'),

]
