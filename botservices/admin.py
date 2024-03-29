from django.contrib import admin
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from .models import ChatLog, ChatIntents
# Register your models here

class ChatLogViewSet(SnippetViewSet):
    model = ChatLog
    menu_label = "Chat Log"
    icon = "pick"
    menu_order = 200
    list_display = (
        "user_chat",
        "bot_response",
        "prob",
        "date_time",
    )
    search_field =(
        "user_chat",
    )
  
class ChatIntentsViewSet(SnippetViewSet):
    model = ChatIntents
    menu_label = "Chat Intents"
    icon = "pick"
    menu_order = 200
    list_display = (
        "tag",
    )
    search_field =(
        "tag",
    )

class ChatViewSetGroup(SnippetViewSetGroup):
    menu_icon = "pick"
    menu_label = "Chat Bot"
    menu_name = "Chat Bot"
    items = (
        ChatLogViewSet, ChatIntentsViewSet
    )

  
register_snippet(ChatViewSetGroup)
admin.site.register(ChatLog)
