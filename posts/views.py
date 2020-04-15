from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm


def get_posts(request):
    """"
    Create a view that will return a list of posts published prior to now
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single Post object based on the post ID (pk) and render it to the 'postdetail.html' template. Or return a 404 erro if the post is not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def create_or_edit_post(request, pk=None):
    """
    Create a post or edit it if a pk is passed in
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.Files, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
