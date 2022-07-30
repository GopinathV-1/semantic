from django.urls import path, include

urlpatterns = [
    path('', include('semantic_app.urls')),
]
