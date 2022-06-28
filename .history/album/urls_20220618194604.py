from django.urls import path

urlpatterns = [
    path('<int:id>/<int:page>.html',album)
]
