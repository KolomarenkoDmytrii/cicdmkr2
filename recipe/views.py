from django.shortcuts import render
from django import http
from django.contrib import messages
from django.views import View

from .models import Category, Recipe


def main_page(request):
    return render(
        request,
        "main.html",
        context={
            "recipes": Recipe.objects.all(),
        },
    )
