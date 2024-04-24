from django import forms
from .models import Photo


class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        widgets = {
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control",
                                                 'rows': 3,}),
            "time": forms.DateTimeInput(format="%Y-%m-%d %H:%M",
                                        attrs={"class": "form-control",
                                            #    "id": "datetimepicker1Input",
                                               "data-td-target": "#datetimepicker1"}),
            "place": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "image": "選擇照片",
            "title": "照片標題",
            "description": "照片描述",
            "time": "照片日期時間",
            "place": "照片地點"
        }

class LoginForm(forms.Form):

    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    password = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )