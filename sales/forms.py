from django import forms

# Define chart choices
CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

# Define class-based Form imported from Django forms
class SalesSearchForm(forms.Form): 
   book_title= forms.CharField(max_length=120)
   chart_type = forms.ChoiceField(choices=CHART__CHOICES)