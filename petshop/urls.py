from django.urls import path
from petshop import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('petshop/', views.dog_list),
    path('petshop/<int:pk>/', views.dog_detail),
    path('petshop/buy/', views.make_order),
]

# urlpatterns = format_suffix_patterns(urlpatterns)