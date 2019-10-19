from django.urls import path
from .views import registerListView, registerDetailView

urlpatterns =[
    path('',registerListView.as_view()),
    path('<pk>',registerDetailView.as_view())
]