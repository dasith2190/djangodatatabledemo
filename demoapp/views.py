from django.shortcuts import render
from .models import *
from datatableview.views import DatatableView
# Create your views here.


class MyView(DatatableView):
    model = Blog
    datatable_options = {
        'columns': [
            'name',
            'tagline',
            ],
        'search_fields': [
            'name',
        ],
    }

