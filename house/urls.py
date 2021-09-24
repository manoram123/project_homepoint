from django.urls import path
from . import views

urlpatterns = [
    path("", views.homes),
    path('list-home/', views.list_home),
    path('edithome/<int:id>', views.edit_home),
    path('rooms/<str:type>', views.rooms),
    path('flats/<str:type>', views.flats),
    path('load-more/<int:start>/<int:end>/<str:type>', views.load_more),
    # path('hostels/', views.hostels),
    path('search/<str:search>', views.search),
    path('details/<int:id>', views.details),
    path('review/<int:property_id>', views.post_review_home),
    # path('reply/<int:comment_id>', views.reply_comment),
    path('load-reviews/<int:id>', views.load_reviews),
    path('book-rent-home/<int:id>', views.book_rent_home),
    path('more-comments/<int:id>/<int:start>/<int:end>', views.more_comments),
]
