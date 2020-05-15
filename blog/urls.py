"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import listaPostView, PostDetailView2, modificaPostView, eliminaPostView

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista-post', listaPostView.as_view(), name='lista_post'),
    path('leggi-post/<int:pk>', PostDetailView2, name='leggi_post'),
    path('modifica-post/<int:pk>', modificaPostView, name='modifica_post'),
    path('elimina-post/<int:pk>', eliminaPostView, name='elimina_post'),
    path('crea-post', views.creaPostView, name='crea_post'),
]