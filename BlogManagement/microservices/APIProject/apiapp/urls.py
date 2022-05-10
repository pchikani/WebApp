from django.urls import path
#from .views import article_list, article_details
from .views import ArticleList, ArticleDetails, UserList, UserDetails

urlpatterns = [
    ##Below is for function based api_view
    #path('articles/', article_list),
    #path('articles/<int:pk>/', article_details),

    ##Below is for Class based APIView
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>/', ArticleDetails.as_view()),

    ## Below is for User Class based APIView
    path('users/', UserList.as_view()),
    path('users/<int:id>/', UserDetails.as_view()),

]
