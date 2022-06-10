from django.shortcuts import render,  HttpResponseRedirect, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin
from django.urls import reverse, reverse_lazy

from mainsite.models import HomePageSettings
from news.models import Category, News

from taggit.models import Tag


class HomeView(TemplateView):
    template_name = 'site/noticia/index.html'

    def get_home_page_post_list(self):
        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(
            category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(
            category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(
            category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(
            category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(
            category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        return (home_page_settings.hot_news, post_catalog_one, post_catalog_two, post_catalog_three,
                post_catalog_four, post_catalog_five, home_page_settings.trending, home_page_settings.editor_choice)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = self.get_home_page_post_list()
        context['hot_news'] = results[0]
        context['post_catalog_one'] = results[1]
        context['post_catalog_one_title'] = results[1][:1]
        context['post_catalog_two'] = results[2][:2]
        context['post_catalog_three'] = results[3][:2]
        context['post_catalog_four'] = results[4][:2]
        context['post_catalog_five'] = results[5]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['categories'] = Category.objects.all()

        return context


class SingleView(TemplateView):
    template_name = 'site/pages/single.html'


class BlogView(TemplateView):
    template_name = 'site/pages/blog.html'


# MultipleObjectMixin for adding paginate..
class CategoryView(DetailView, MultipleObjectMixin):
    model = Category  # Functionality for news
    paginate_by = 6
    context_object_name = 'category'
    template_name = 'site/noticia/partials/category.html'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        news_list = News.objects.filter(category=self.object.id, is_published=True).order_by('-id')

        context = super().get_context_data(object_list=news_list, **kwargs)
        context['post_top'] = news_list[1:3]
        context['post_all'] = news_list[3:]
        context['categories'] = Category.objects.all()

        return context


class PostSingleView(DetailView, FormMixin):
    model = News
    context_object_name = 'news'
    success_url = reverse_lazy('newspaper:blog')
    template_name = 'site/noticia/partials/single.html'

    def get_related_post_by_category(self):
        return super().get_queryset().filter(is_published='True', category=self.object.category.id).exclude(id=self.object.id).order_by('-id')

    # def get_related_post_filter_by_tag(self):
    #     for tag in Tag.objects.all():
    #         return self.get_related_post_by_category().filter(tags__name__in=[tag])[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = self.get_related_post_by_category()
        context['categories'] = Category.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('newspaper:single-post', kwargs={'slug': self.kwargs['slug']})


def FilterByTag(request, tag):
    news_list = News.objects.filter(
        tags__name__in=[tag], is_published=True).order_by('-id')
    context = {
        'news_list': news_list,
        'tag': tag
    }
    return render(request, 'site/pages/tag.html', context)
