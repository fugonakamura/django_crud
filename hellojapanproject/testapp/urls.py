from django.urls import path
from .views import TestList,TestDetail,TestCreate,TestUpdate,TestDelete

urlpatterns=[
    path("list/",TestList.as_view(),name="list"),
    path("detail/<int:pk>/",TestDetail.as_view(),name="detail"),
    path("create/",TestCreate.as_view(),name="create"),
    path("update/<int:pk>",TestUpdate.as_view(),name="update"),
    path("delete/<int:pk>",TestDelete.as_view(),name="delete"),
]