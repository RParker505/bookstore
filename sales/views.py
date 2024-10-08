from django.shortcuts import render
# To protect function-based views
from django.contrib.auth.decorators import login_required
# Import the form created in forms.py
from .forms import SalesSearchForm
# Import the model to access its records
from .models import Sale
# Import pandas for data processing
import pandas as pd
# Import from utils.py
from .utils import get_bookname_from_id, get_chart

# Create your views here.

# Define home function that takes a request as an argument and returns a rendered object using the imported render function
def home(request):
   # render() requires two arguments, “request” and “template”, and it returns an “HttpResponse” object.
   return render(request, 'sales/home.html')

# Define function-based view - records()
# Keep protected
@login_required
def records(request):
   # Create an instance of SalesSearchForm that you defined in sales/forms.py
   form = SalesSearchForm(request.POST or None)
   sales_df = None      #initialize dataframe to None
   chart = None         #initialize chart to None

   # Check if the button is clicked
   if request.method =='POST':
       # Read book_title and chart_type
       book_title = request.POST.get('book_title')
       chart_type = request.POST.get('chart_type')
       
       # Apply filter to extract data
       qs = Sale.objects.filter(book__name=book_title)
       if qs:      # If data found
           # Convert the queryset values to pandas dataframe
           sales_df = pd.DataFrame(qs.values())
           # Convert the ID to Name of book
           sales_df['book_id']=sales_df['book_id'].apply(get_bookname_from_id)
           # Call get_chart() from utils file
           chart = get_chart(chart_type, sales_df, labels=sales_df['date_created'].values)
           # Make dataframe readable as html
           sales_df = sales_df.to_html()

   # Pack up data to be sent to template in the context dictionary
   context={
           'form': form,
           'sales_df': sales_df,
           'chart': chart
   }

   # load the sales/records.html page using the data that you just prepared
   return render(request, 'sales/records.html', context)