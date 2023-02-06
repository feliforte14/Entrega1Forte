from django.urls import path

from products.views import create_product,list_products,ProductUpdateView,ProductDeleteView,CategoryListView,CategoryCreateView,CategoryDeleteView,CategoryUpdateView

urlpatterns = [
    path('create_product/',create_product),
    path('list_products/',list_products),
    path('update_product/<int:pk>',ProductUpdateView.as_view()),
    path('delete_product/<int:pk>',ProductDeleteView.as_view()),
    path('list_categories/',CategoryListView.as_view()),
    path('create_category/',CategoryCreateView.as_view()),
    path('delete_category/<int:pk>',CategoryDeleteView.as_view()),
    path('update_category/<int:pk>',CategoryUpdateView.as_view()),

]