from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blog, name="blogs"),
    path('message/', views.message, name='message'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



