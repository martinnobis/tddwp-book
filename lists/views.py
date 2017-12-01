# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_}) # 'list_' is a 'context'.

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id) # 1. get the list from the database
    Item.objects.create(text=request.POST['item_text'], list=list_) # 2. get the text from the POST request and put it in the list
    return redirect(f'/lists/{list_.id}/') # 3. redirect, displaying the list
