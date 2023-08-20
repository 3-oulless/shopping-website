from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from .models import Article,ArticleCategory,ArticleComment,ArticleVisit
from modul.modul import get_client_ip

class ArticleListView(ListView):
    model = Article
    paginate_by = 5
    queryset = Article.objects.filter(is_active=True).order_by('-visit_count')
    context_object_name = 'Articles'
    template_name = 'Article/article_list.html'

    def get_queryset(self):
        query = super().get_queryset()
        category = self.kwargs.get('category')
        if category is not None:
            query = query.filter(selected_categories__url_title__iexact=category)
        return query


class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "Article/article_detail.html"
    queryset = Article.objects.filter(is_active=True)
    context_object_name = "Articles"

    def post(self,request,pk,slug):
        if request.user.is_authenticated:
            message = request.POST.get('message')
            user = request.POST.get('user')
            article_id = request.POST.get('article_id')
            parent_id = request.POST.get('parentid')

            if parent_id is not "":
                ArticleComment.objects.create(article_id=article_id,user_id=user,parent_id=parent_id,text=message)
                return redirect('article:articles_detail',pk=pk,slug=slug)

            else:
                ArticleComment.objects.create(article_id=article_id,user_id=user,text=message)

            return redirect('article:articles_detail',pk=pk,slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = kwargs['object']

        #create visit count
        request = self.request
        user_ip = get_client_ip(request)
        user_id = None
        if request.user.is_authenticated:
            user_id = request.user
        has_been_visited = ArticleVisit.objects.filter(ip__iexact=user_ip,article=article).first()
        if has_been_visited:
            p_data = Article.objects.get(id=has_been_visited.article.id)
            visit_count = ArticleVisit.objects.filter(article=article).count()
            p_data.visit_count = visit_count
            p_data.save()
        else :
            ArticleVisit.objects.create(ip=user_ip,user=user_id,article=article)
            

        #end visit count
        context['comments'] = ArticleComment.objects.filter(article__id=article.id,parent=None).order_by('-create_date').prefetch_related('article_parent')
        return context






def grouping_article_component(request):
    category = ArticleCategory.objects.filter(is_active=True,parent_id=None)
    context = {
        'article_categorys' : category
    }
    return render(request,'Article/grouping_article.html',context)