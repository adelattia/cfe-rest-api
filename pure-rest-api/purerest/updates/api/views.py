import json

from .mixins import CSRFExemptMixin, HttpResponseMixin
from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from updates.forms import UpdateModelForm

# creating, updating, deleting, retrieving


class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    Retrieve, Update, Delete
    '''
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = {'message': 'Not allowed, please use the /api/updates/ endpoint'}
        return self.render_to_response(json_data, status=403)

    def put(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data, status=403)


class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    List View
    Create View
    '''
    is_json = True

    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)

        json_data = json.dumps({"message": "Unknow data"})
        return self.render_to_response(json_data, status=400)

    def put(self, request, *args, **kwargs):
        return #json

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({'message': 'You cannot delete an entire list.'})
        return self.render_to_response(json_data, status=403)

