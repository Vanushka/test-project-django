from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.registration, name='registration'),
    url(r'^signup$', views.signup),
    url(r'^signin$', views.signin),
    url(r'^login$', views.login, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
