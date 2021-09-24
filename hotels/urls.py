from django.urls import path
from hotels.models import Hotels
from hotels import views

urlpatterns = [
    path("list-hotel", views.list_hotel),
    path('edit-hotel/<int:id>', views.edit_hotel),
    path('details/<int:id>', views.details),
    path('review/<int:property_id>', views.post_review_home),
    path('more-comments/<int:id>/<int:start>/<int:end>', views.more_comments),
    path('book-hotel/<int:id>', views.book_hotel),

]
