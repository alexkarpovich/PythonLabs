from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Tag, TagType, TagCategory
from .forms import TagForm, TagCategoryForm, TagTypeForm
from api.base.views import BaseListView


class TagViewList(BaseListView):
    model = Tag
    fields = ['name']
    context_object_name = 'list'
    success_url = reverse_lazy('tag:tag-list')
    sort_fields = ['id', 'name']


class TagViewUpdate(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'tag/tag_form_edit.html'
    success_url = reverse_lazy('tag:tag-list')


class TagViewDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('tag:tag-list')


class TagViewCreate(FormView):
    template_name = 'tag/tag_form_add.html'
    form_class = TagForm
    success_url = reverse_lazy('tag:tag-list')

    def form_valid(self, form):
        form.save()
        return super(TagViewCreate, self).form_valid(form)


class TagCategoryViewList(BaseListView):
    model = TagCategory
    fields = ['name']
    context_object_name = 'list'
    success_url = reverse_lazy('tag:tag-list')
    sort_fields = [u'id', u'name', 'tag_type']


class TagCategoryViewUpdate(UpdateView):
    model = TagCategory
    form_class = TagCategoryForm
    template_name = 'tag/tagcategory_form_edit.html'
    success_url = reverse_lazy('tag:category-list')


class TagCategoryViewDelete(DeleteView):
    model = TagCategory
    success_url = reverse_lazy('tag:category-list')


class TagCategoryViewCreate(FormView):
    template_name = 'tag/tagcategory_form_add.html'
    form_class = TagCategoryForm
    success_url = reverse_lazy('tag:category-list')

    def form_valid(self, form):
        form.save()
        return super(TagCategoryViewCreate, self).form_valid(form)


class TagTypeViewList(BaseListView):
    model = TagType
    fields = ['name']
    context_object_name = 'list'
    success_url = reverse_lazy('tag:type-list')
    sort_fields = ['id', 'name']


class TagTypeViewUpdate(UpdateView):
    model = TagType
    form_class = TagTypeForm
    template_name = 'tag/tagtype_form_edit.html'
    success_url = reverse_lazy('tag:type-list')


class TagTypeViewDelete(DeleteView):
    model = TagType
    success_url = reverse_lazy('tag:type-list')


class TagTypeViewCreate(FormView):
    template_name = 'tag/tagtype_form_add.html'
    form_class = TagTypeForm
    success_url = reverse_lazy('tag:type-list')

    def form_valid(self, form):
        form.save()
        return super(TagTypeViewCreate, self).form_valid(form)
