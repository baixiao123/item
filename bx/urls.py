from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bx.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),



          url(r'^new$', 'bx.views.blog_create'),
          url(r'^list/$', 'bx.views.blog_list'),
          
          url(r'^delete/(\d+)$', 'bx.views.blog_delete'),
          url(r'^update/(\d+)$', 'bx.views.blog_update'),
          url(r'^update_save/(\d+)$', 'bx.views.blog_update_save'),
)
