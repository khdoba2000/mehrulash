from posts.humanize import naturalsize
from django import forms
from posts.models import Post
from django.core.files.uploadedfile import InMemoryUploadedFile
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'

    # Hint: this will need to be changed for use in the posts application :)
    class Meta:
        model = Post
        fields = ['title', 'description', 'section', 'region', 'phone_number', 'contact_info', 'picture']  # Picture is manual

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)
        print(instance.title)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        print(f)
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance
""" 
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    
    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'
        
    class Meta:
        model = Post
        fields=('title', 'picture', 'description', 'section', 'region', 'phone_number', 'contact_info')

    def clean(self):
            cleaned_data = super().clean()
            pic = cleaned_data.get('picture')
            if pic is None:
                return
            if len(pic) > self.max_upload_limit:
                self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    def save(self, commit=True):
            instance = super(CreateForm, self).save(commit=False)

            # We only need to adjust picture if it is a freshly uploaded file
            f = instance.picture   # Make a copy
            if True:#isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
                bytearr = f.read()
                instance.content_type = f.content_type
                instance.picture = bytearr  # Overwrite with the actual image data

            if commit:
                instance.save()

            return instance """