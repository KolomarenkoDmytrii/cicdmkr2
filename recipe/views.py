from django.shortcuts import render
from django import http
from django.contrib import messages
from django.views import View

import random
from .models import Category, Recipe


def main(request):
    return render(
        request,
        "main.html",
        context={
            "recipes": random.choices(Recipe.objects.all(), k=10),
        },
    )

def category_detail(request, id):
    return render(
        request,
        "category_detail.html",
        context={
            "category": Category.objects.get(pk=id),
        },
    )
