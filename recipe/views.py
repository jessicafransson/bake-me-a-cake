from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, CreateRecipe
from django import forms
from django.contrib import messages


class PostList(generic.ListView):
    """ View published recipes and how many are viewable per page """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """ view comment and likes information """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ view and validate comments for recipes"""
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Comment Saved!')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """ allow to like posts """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CreateRecipe(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """User create recipes when logged in"""
    model = Post
    form_class = CreateRecipe
    template_name = 'create_recipe.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_message = 'Recipe added succesfully, await approval!'


class UpdateRecipe(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """edit the items for the user"""
    model = Post
    """form_class = CreateRecipe"""
    template_name = 'update_recipe.html'
    success_url = reverse_lazy('home')
    fields = [
        "title",
        "description",
        "content",
        "featured_image",
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_message = 'Recipe updated succesfully, await approval!'


class DeleteRecipe(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """delete the post for the user here"""
    model = Post
    form_class = DeleteView
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')

    def delete_post(request, item_id):
        form = get_object_or_404(Item, id=item_id)
        form.delete()
        return redirect("/create_recipe")
