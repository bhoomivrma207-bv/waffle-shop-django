
from django.urls import path
from . import views
from .views import waffle_stores_view

urlpatterns = [
    path('',views.all_waffle, name = 'All_Waffle'),
    path('<int:waffle_id>/',views.waffle_detail, name = 'waffle_detail'),

    path('waffle_stores/',views.waffle_stores_view, name = 'waffle_stores'),
]
   