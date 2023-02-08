from gc import get_objects
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post


class PostsView(ListView):
    template_name = 'blog/posts.html'
    queryset = Post.objects.all()
    paginate_by = 5


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']

        post = get_object_or_404(Post, slug=slug)
        context['post'] = post
        return context