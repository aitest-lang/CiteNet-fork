from django.urls import path

from . import views

urlpatterns = [
    path("", views.search, name="search"),
    path("save-search",views.save_search,name="save-search")
]