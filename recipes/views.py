from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

class CreatePost(LoginRequiredMixin, CreateView):
    """ Create post form view to allow users to add a new post
         while logged in"""
    model = Post
    form_class = CommentForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    """edit the items for the user"""
    model = Post

    def get_queryset(self):
        x = self.request.user.pk
        post = get_object_or_404(Item, id=item_id)


class DeletePost(LoginRequiredMixin, DeleteView):
    """delete the post for the user here"""
    def delete_post(request, item_id):
        form = get_object_or_404(Item, id=item_id)
        form.delete()
        return redirect("/create_post")
