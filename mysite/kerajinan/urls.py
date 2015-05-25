from django.conf.urls import patterns, include, url
# from django.conf.urls.static import static
from . import views
from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^add_product/$', views.add_product, name='add_product'),
	url(r'^add_category/$', views.add_category, name="add_category"),
	url(r'^category/(?P<slug>[-_\w]+)/$', views.view_category, name='view_kerajinan_category'),
	url(r'^product/(?P<slug>[-_\w]+)/$', 'kerajinan.views.product_single', name='product_detail'),
	url(r'^product/$', 'kerajinan.views.product_list', name='product_list'),
	# url(r'^product/(?P<pk>[0-9]+)/edit/$', views.product_edit, name='product_edit'),
	url(r'^cart/(?P<slug>[\w-]+)/$', 'kerajinan.views.add_to_cart', name='add_to_cart'),
	url(r'^cart/$', 'kerajinan.views.view', name='cart'),
	url(r'^cart/(?P<pk>[0-9]+)/remove//$', views.remove_from_cart, name='remove_from_cart'),
	# url(r'^checkout/$', 'kerajinan.views.checkout', name='checkout'),

	#--------Home-----------------
    url(r'^home/$', 'kerajinan.views.home', name='home'),
    url(r'^profile/$', 'kerajinan.views.profile', name='profile'),

    url(r'^about/$', 'django.contrib.flatpages.views.flatpage', kwargs= {'url':'/about/'}, name='homepage_about'),
    url(r'^contact/$', 'django.contrib.flatpages.views.flatpage', kwargs= {'url':'/contact/'}, name='homepage_contact'),
    url(r'^term-condition/$', 'django.contrib.flatpages.views.flatpage', kwargs= {'url':'/term-condition/'}, name='homepage_term-condition'),
)
# ) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()