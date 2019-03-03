from django import forms
from django.core import validators


# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError(
#             'Name must start with letter "z"'
#         )


class FormName(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    verifyemail = forms.EmailField(label='Please verify your email')
    text = forms.CharField(widget=forms.Textarea)

    # check for bots
    # botcatcher = forms.CharField(
    #     required=False,
    #     widget=forms.HiddenInput,
    #     validators=[
    #         validators.MaxLengthValidator(0)
    #     ]
    # )

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verifyemail']

        if email != vemail:
            raise forms.ValidationError(
                'Uh oh! The emails you entered don\'t match'
            )
