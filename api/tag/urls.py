from django.conf.urls import patterns, url

from .views import TagViewList, TagViewCreate, TagViewUpdate, TagViewDelete, \
    TagCategoryViewList, TagCategoryViewCreate, TagCategoryViewUpdate, TagCategoryViewDelete, \
    TagTypeViewList, TagTypeViewCreate, TagTypeViewUpdate, TagTypeViewDelete

urlpatterns = patterns('',
    url(r'^$', TagViewList.as_view(), name="tag-list"),
    url(r'^add/$', TagViewCreate.as_view(), name="tag-add"),
    url(r'^edit/(?P<pk>\d+)/$', TagViewUpdate.as_view(), name="tag-edit"),
    url(r'^delete/(?P<pk>\d+)$', TagViewDelete.as_view(), name="tag-delete"),
    url(r'^categories$', TagCategoryViewList.as_view(), name="category-list"),
    url(r'^category/add/$', TagCategoryViewCreate.as_view(), name="category-add"),
    url(r'^category/edit/(?P<pk>\d+)/$', TagCategoryViewUpdate.as_view(), name="category-edit"),
    url(r'^category/delete/(?P<pk>\d+)$', TagCategoryViewDelete.as_view(), name="category-delete"),
    url(r'^types$', TagTypeViewList.as_view(), name="type-list"),
    url(r'^type/add/$', TagTypeViewCreate.as_view(), name="type-add"),
    url(r'^type/edit/(?P<pk>\d+)/$', TagTypeViewUpdate.as_view(), name="type-edit"),
    url(r'^type/delete/(?P<pk>\d+)$', TagTypeViewDelete.as_view(), name="type-delete"),

)
