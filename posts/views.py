from django.shortcuts import render,redirect
from posts.models import Comment
from posts.forms import CommentForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseForbidden

def main(request):
    return render(request, "main.html")

@require_POST 
def comment_add(request):
    form = CommentForm(data = request.POST)
    if form.is_valid():
        comment = form.save(commit = False)
        comment.user = request.user
        comment.save()

        return redirect("pass") #주소 추가
    
@require_POST
def comment_delete(request, comment_id):
    comment = Comment.objects.get(id = comment_id)
    comment.delete()

    if comment.user == request.user:
        comment.delete()
        return redirect("pass") #주소 추가
    
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다")