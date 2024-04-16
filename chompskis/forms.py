from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import GnomeChompskis, Swarm

class SignUpForm(UserCreationForm):
    class Meta:
        email= forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}))
        first_name= forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}))
        last_name= forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
        
        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
            
        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddChompskiForm(forms.ModelForm):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}))
    age = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Age'}))
    height = forms.FloatField(required=False, label="", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Height'}))
    weight = forms.FloatField(required=False, label="", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Weight'}))
    no_teeth = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Number of Teeth'}))
    #TODO fix
    swarm_id = forms.ModelChoiceField(queryset=Swarm.objects.all() , label="", widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = GnomeChompskis
        fields = ('name', 'age', 'height', 'weight', 'no_teeth', 'swarm_id')
           
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # If the instance is being created and no swarm_id is provided in the form,
        # or if the swarm_id is changed, update the swarm_id
        if not instance.pk or self.has_changed():
            instance.swarm_id = self.cleaned_data['swarm_id'].swarm_id
        
        if commit:
            instance.save()
        return instance

class AddSwarmForm(forms.ModelForm):
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}))
    latitude = forms.FloatField(required=False, label="", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Latitude'}))
    longitude = forms.FloatField(required=False, label="", widget=forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Longitude'}))
    class Meta:
        model = Swarm
        fields = ('name', 'latitude', 'longitude')