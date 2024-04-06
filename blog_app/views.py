from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from rest_framework import generics, filters, viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from .models import *
from django.contrib.auth.models import User
from rest_framework.pagination import LimitOffsetPagination
from django.core.mail import send_mail


class UserRegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        existing_user = authenticate(username=username, password=password)
        print("get user", existing_user)
        if existing_user:
            login(request, existing_user)
            return Response("Login successfully")
        return Response("Invalid login credentials", status=status.HTTP_400_BAD_REQUEST)


class BlogPostGenericView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer
    # Allows read only access to anonymous users
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backend = [filters.SearchFilter]
    search_fields = ["title", "content"]
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 10


class BlogUpdateGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogpostSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = BlogPost.objects.get(pk=post_id)
        if not post:
            raise ValidationError("Invalid post ID")
        serializer.save(author=self.request.user, post=post)
        # Send email notification to the author of the post
        send_mail(
            subject=f'New Comment on Your Blog Post "{post.title}"',
            message=f'Hello {post.author.username},\n\nYou have received a new comment on your blog post "{post.title}"',
            from_email='raj.kanani1487@gmail.com',
            recipient_list=[post.author.email],
            fail_silently=True,
        )

        return Response("Comment created successfully", status=status.HTTP_201_CREATED)
