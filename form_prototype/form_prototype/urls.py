from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'form_prototype.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/', 'form.views.form_post', name="form_post"),
    url(r'^login/', 'form.views.login_post', name="login_post"),
    url(r'^register/', 'form.views.register_post', name="register_post"),
    url(r'^logout/', 'form.views.logout', name="logout"),
    url(r'^info/', 'form.views.display_data', name="display_data"),
)
