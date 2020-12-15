from django import forms

from designs.models import Designs, Post


class CreateDesignForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control()

    def add_form_control(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Designs
        exclude = ('created_by',)
        # fields = "__all__"


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control()

    def add_form_control(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ('name', 'email', 'text')
