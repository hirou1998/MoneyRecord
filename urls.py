from django.urls import path

from . import views

app_name = "moneyrecord"

urlpatterns = [
    path("moneyrecord_list/", views.show_list, name="moneyrecord_list"),
    path("moneyrecord_create/", views.ListCreateView.as_view(), name="moneyrecord_create"),
    path("moneyrecord_update/<int:pk>/", views.ListUpdateView.as_view(), name="moneyrecord_update"),
path("moneyrecord_delete/<int:pk>/", views.ListDeleteView.as_view(), name="moneyrecord_delete"),
]
