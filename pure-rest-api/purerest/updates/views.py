import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import View

from purerest.mixins import JsonResponseMixin
from .models import Update


def json_example_view(request):
    data = {
        "count": 1001,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1002,
            "content": "Some new content"
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
        # return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1003,
            "content": "Some new content"
        }
        return self.render_to_json_response(data)


class SerializeDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        data = Update.objects.all().serialize()
        return HttpResponse(data, content_type='application/json')
