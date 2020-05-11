from django.shortcuts import render, redirect
from .models import Content, Comment
from django.utils import timezone
from .forms import ContentForm, CommentForm
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    posts=Content.objects.all
    return render(request, 'mydiary/home.html', {'posts_list': posts})

def new(request):

    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = ContentForm()

    return render(request, 'mydiary/new.html', {'form': form})

def detail(request, pk):
    post = get_object_or_404(Content, pk=pk) 
    comment_list = Comment.objects.filter(post=post) 
    if request.method == "POST":
        comment_form = CommentForm(request.POST) 
        if comment_form.is_valid():
            comment = comment_form.save(commit=False) 
            comment.published_date = timezone.now() 
            comment.post = post
            comment.save()
            return redirect('detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'mydiary/detail.html', {'post': post,
'comment_list': comment_list, 'comment_form': comment_form})
def edit(request, index):
    post = get_object_or_404(Content, pk=index)
    if request.method == "POST":
        form = ContentForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now
            post.save()
            return redirect('detail', index=post.pk)
    else:
        form = ContentForm(instance=post)
    return render(request, 'mydiary/edit.html', {'form': form})
def delete(request, pk):
    post = get_object_or_404(Content, pk=pk)
    post.delete()
    return redirect('home')
def delete_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    comment.delete()
    return redirect('detail', pk=pk)