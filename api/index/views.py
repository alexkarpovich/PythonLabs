from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    return render(request, 'index/index.html', {})


class ExtendedListView(ListView):
    context_object_name = 'list'
    paginate_by = 10

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        fields = self.model._meta.get_all_field_names()
        sort_by = 'id' if sort_by not in fields else sort_by
        qs = super(ExtendedListView,self).get_queryset().order_by(sort_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ExtendedListView, self).get_context_data(**kwargs)
        sort_by = self.request.GET.get('sort_by')
        fields = self.model._meta.get_all_field_names()
        context['sort_by'] = 'id' if sort_by not in fields else sort_by
        return context
