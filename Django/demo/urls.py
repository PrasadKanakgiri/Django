from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name="demo"),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]
