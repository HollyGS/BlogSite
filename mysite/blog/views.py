from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic.edit import FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import urls

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/home.html'

# This class is no longer needed. You can delete it
# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # List of active comments for this post
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post.slug)

    comments = post.comments.filter(active=True)
    new_comment = None
    form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post,
                                           'comments': comments,
                                           'form': form})


# I'm not really needed either!
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

