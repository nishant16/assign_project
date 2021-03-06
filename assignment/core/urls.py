from django.conf.urls import url

from .views import CategoryListAPIView, SubcategoryListAPIView, ProductListAPIView, ProductCreateAPIView

urlpatterns = [
    url(r'^category/$', CategoryListAPIView.as_view(), name='category'),
    url(r'^subcategory/(?P<category_name>\w+)/$', SubcategoryListAPIView.as_view(), name='subcategory'),
    url(r'^product/$', ProductListAPIView.as_view(), name='product'),
    url(r'^product/create/$', ProductCreateAPIView.as_view(), name='create'),

]