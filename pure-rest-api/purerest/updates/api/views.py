from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse

# creating, updating, deleting, retrieving

class UpdateModelDetailAPIView(View):
    '''
    Retrieve, Update, Delete
    '''
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type='application/json')


class UpdateModelListAPIView(View):
    '''
    List View
    Create View
    '''
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        return #json

    def put(self, request, *args, **kwargs):
        return #json

    def delete(self, request, *args, **kwargs):
        return #json
