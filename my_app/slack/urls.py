
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

from .views import * # To get the sendmessage.html to show

urlpatterns = [
    path('sendmessage', views.sendmessage),
    path('sendmessage.html', TemplateView.as_view(template_name='slack/sendmessage.html'), name='slacksendmessage')
    # path('test/sendmessage', TestSendMessageView.as_view(), name="sendmessage")
]



