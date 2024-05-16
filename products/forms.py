from django.forms import ModelForm

from products.models import Review
from users.models import CustomUser


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'password')