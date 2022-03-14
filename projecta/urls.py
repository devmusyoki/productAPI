from django.urls import path
from django.views.generic import TemplateView

app_name = "projecta"

urlpatterns = [
    path('', TemplateView.as_view(template_name="products/index.html")),
] 