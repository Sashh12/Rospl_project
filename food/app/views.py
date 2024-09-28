
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Reservation, Feedback  # Replace with your actual model
from .forms import ReservationForm, CustomerProfileForm  # Ensure you have a form defined
from decimal import Decimal
from django.db.models import Count, Q, F
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"app/home.html")


class aboutview(View):
    def get(self,request):
        return render(request,"app/about.html")
    
class cartview(View):
    def get(self,request):
        return render(request,"app/cart.html")

class wishlistview(View):
    def get(self,request):
        return render(request,"app/wishlist.html")
    
class contactview(View):
    def get(self,request):
        return render(request,"app/contact.html")
    
class homeview(View):
    def get(self,request):
        return render(request,"app/home.html")
    
# @method_decorator(login_required,name='dispatch')    
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            village = form.cleaned_data['village']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['pincode']

            reg = Customer(user=user,name=name,village=village,city=city,mobile=mobile,state=state,pincode=pincode)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/profile.html',locals())


class blogview(View):
    def get(self,request):
        return render(request,"app/blog.html")

class shopview(View):
    def get(self,request):
        return render(request,"app/shop.html")
    
def feedback(request):
    return render(request, 'app/feedback.html')

class reservation_view(View):
    def get(self,request):
        form = ReservationForm()
        return render(request, 'app/reservation_form.html',locals())
    def post(self,request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! Table Booked Successfully")
        else:
            messages.warning(request,"Inavalid Input Data")
        return redirect("/success")


# def reservation_view(request):
#     if request.method=="POST":
#         reservation=Reservation()
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         message=request.POST.get('message')
#         date=request.POST.get('date')
#         time=request.POST.get('time')
#         guests=request.POST.get('guests')
#         # data, time, guests
#         reservation.name=name
#         reservation.email=email
#         reservation.message=message
#         reservation.date=date
#         reservation.time=time
#         reservation.guests=guests
#         reservation.save()
#         # return HttpResponse("<center><h1>THANKS FOR YOUR FEEDBACK</h1><center>")
#         return redirect("/success")
#     return render(request, 'app/reservation_form.html',locals())

def success_view(request):
    return render(request, 'app/success.html')

def search(request):
    query = request.GET.get('search')
    # Check if the query is a valid decimal for price
    try:
        price = Decimal(query)
        products = Product.objects.filter(
            Q(food_name__icontains=query) |
            Q(food_category__icontains=query) |
            Q(sub_category__icontains=query) |
            Q(price__lte=query)  # Exact match for price
        )
    except:
        # If the query is not a valid decimal, filter without price
        products = Product.objects.filter(
            Q(food_name__icontains=query) |
            Q(food_category__icontains=query) |
            Q(sub_category__icontains=query)
        )

    return render(request, "app/search.html", {'products': products, 'query': query})

def feedback(request):
    if request.method=="POST":
        feedback=Feedback()
        name=request.POST.get('name')
        email=request.POST.get('email')
        comment=request.POST.get('comment')
        feedback.name=name
        feedback.email=email
        feedback.comment=comment
        feedback.save()
        # return HttpResponse("<center><h1>THANKS FOR YOUR FEEDBACK</h1><center>")
        return redirect("/")
    return render(request, 'app/feedback.html',locals())

class ProductDetail(View):
    def get(self, request, pk):
        try:
            # Fetch the product from the database using the provided primary key (pk)
            product = Product.objects.get(id=pk)
            
            # Fetch the wishlist items for the current user and the specific product
            # wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
            
            # # Get recommendations for the current product
            # recommendations = recommend(product.food_name)
            
            # # Get same category recommendations for the current product
            # same_category_recommendations = same_recommend1(product.food_name)

            context = {
                'product': product,
                # 'wishlist': wishlist,
                # 'recommendations': recommendations,
                # 'same_category_recommendations': same_category_recommendations,
            }
            return render(request, 'app/productdetail.html', context)
        except Product.DoesNotExist:
            # Handle the case where the product with the given primary key doesn't exist
            return HttpResponseNotFound("The requested product does not exist.")
        