from django.urls import path
from hostels import views

urlpatterns = [
    path('listhostel/', views.list_hostel),
    path('details/', views.details),
    path('details/<int:id>', views.details),
    path('hostels/', views.hostels),
    path('edithostel/<int:id>', views.edit_hostel),
    path('review/<int:property_id>', views.post_review_hostel),
    # path('like/<int:comment_id>', views.like_comment),
    # path('reply/<int:comment_id>', views.reply_comment),
    path('bookinghostel/<int:hostel_id>', views.book_hostel),
    path('load-more/<int:start>/<int:end>', views.load_more),
    path('more-comments/<int:id>/<int:start>/<int:end>', views.more_comments),
    path('search/<str:search>', views.search)
]
