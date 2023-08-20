from django.urls import path
from Article_Module import views

app_name = "article"

urlpatterns = [
    path('',views.ArticleListView.as_view(),name="articles"),
    path('category/<category>',views.ArticleListView.as_view(),name="articles_category"),
    path('<pk>/<slug>',views.ArticleDetailView.as_view(),name="articles_detail")

]