from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.test import TestCase

from item.models import Item
# Create your tests here.
@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user)

    return render(request, 'dashboard/index.html', {
        'items':items
    })