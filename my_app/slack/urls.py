
from django.urls import include, path
from . import views
from django.views.generic import TemplateView

from .views import * # To get the sendmessage.html to show

urlpatterns = [
    path('sendmessage', views.sendmessage),
    path('sendmessage.html', TemplateView.as_view(template_name='slack/sendmessage.html'), name='slack_send_message_page'),
    path('displaymessages.html', TemplateView.as_view(template_name='slack/displaymessages.html'), name='slack_display_messages_page'),
    path('slack.html', TemplateView.as_view(template_name='slack/slack.html'), name='slack_widget'),
    path('get_formatted_messages/', views.get_formatted_messages, name='get_formatted_messages')
    # path('test/sendmessage', TestSendMessageView.as_view(), name="sendmessage")
]



