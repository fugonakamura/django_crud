from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import TestModel
from django.urls import reverse_lazy

# Create your views here.
class TestList(generic.ListView):
    template_name="list.html"
    model=TestModel

class TestDetail(generic.DetailView):
    template_name="detail.html"
    model=TestModel

class TestCreate(generic.CreateView):
    template_name="create.html"
    model=TestModel #作成したモデル
    fields=("title","memo") #作成したモデルのフィールド
    success_url=reverse_lazy("list")

class TestUpdate(generic.UpdateView):
    template_name="update.html"
    model=TestModel #作成したモデル
    fields=("title","memo") #作成したモデルのフィールド
    success_url=reverse_lazy("list")

class TestDelete(generic.DeleteView):
    template_name="delete.html"
    model=TestModel #作成したモデル
    success_url=reverse_lazy("list")