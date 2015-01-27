from django.views.generic import ListView


class BaseListView(ListView):
    paginate_by = 10
    model = None
    sort_fields = None

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by')
        fields = self.model._meta.get_all_field_names()
        sort_by = 'id' if sort_by not in fields else sort_by
        qs = super(BaseListView,self).get_queryset().order_by(sort_by)
        return qs

    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        sort_by = self.request.GET.get('sort_by')
        fields = self.model._meta.get_all_field_names()
        context['sort_by'] = 'id' if sort_by not in fields else sort_by
        if set(self.sort_fields).issubset(set(fields)):
            context['fields'] = list(self.sort_fields)
        else:
            context['fields'] = list(fields)

        for i in range(len(context['fields'])):
            context['fields'][i] = {
                'name': context['fields'][i],
                'value': context['fields'][i].capitalize().replace('_', ' ')
            }

        return context
