from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    comments=BlogComment.objects.filter(post=post,parent=None)

    
    comments = comments.prefetch_related('blogcomment_set')
    

    context={
        'post': post,
        "comments":comments,
       
    }


    return render(request, 'blog/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postid=request.POST.get("postid")
        post=Post.objects.get(sno=postid)
        parentsno=request.POST.get("parentsno")

        if parentsno=="":
            comment=BlogComment(comment=comment,user=user,post=post)
            messages.success(request,"Your comment has been posted")
        
        else:
            parent=BlogComment.objects.get(sno=parentsno)
            comment=BlogComment(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"Your Reply has been posted")



        comment.save()

        

    return redirect(f"/blog/{post.slug}")

