from django.conf.urls import url
# from django.contrib import admin
from webhook.views import webhook

urlpatterns = [
    url(r'^webhook/', webhook, name='webhook'),
    # url(r'^admin/', admin.site.urls),
]
