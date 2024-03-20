from django.http import HttpResponse, HttpRequest
from timeit import default_timer
from django.shortcuts import render


def shop_index(request: HttpRequest):
    books = [
    {'title': '1984', 'author': {'name': 'George', 'age': 45}},
    {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
    {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
]
    context = {
        "timer": default_timer(),
        "books": books
    }
    return render(request, "shopapp/shop-index.html", context=context)

