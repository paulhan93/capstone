
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('quote', views.quote),
    path('postit', views.postit),
    path('postit.html', TemplateView.as_view(template_name='RESTexamples/postit.html'), name='posttesthtmlpage')
]



