from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('listhostel/', views.list_hostel),
    path('details/', views.details),
    path('details/<int:id>', views.details),
    path('deleteHostel/<int:pk>/', views.deleteHosel),
    path('hostels/', views.hostels),
    path('edithostel/<int:id>', views.edit_hostel),
    path('review/<int:property_id>', views.post_review_hostel),
    # path('like/<int:comment_id>', views.like_comment),
    path('reply/<int:comment_id>', views.reply_comment)
]
