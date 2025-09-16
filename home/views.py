from django.shortcuts import render
from django.db.models import Sum
from cart.models import Order
def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'home/index.html', {'template_data': template_data})
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {'template_data': template_data})

def subscription(request):
    # This line queries the Order model in your database
    user_spending = Order.objects.filter(user=request.user).aggregate(total_spent=Sum('total'))
    total_spent = user_spending['total_spent'] or 0

    # This logic determines the level based on the calculated total
    if total_spent >= 30:
        level = "Premium"
        description = "You have exclusive access to new releases and premium content."
    elif total_spent >= 15:
        level = "Medium"
        description = "You get early access to sales and special promotions."
    else:
        level = "Basic"
        description = "Thank you for being a customer! Spend more to unlock new perks."
        
    context = {
        'total_spent': total_spent,
        'level': level,
        'description': description,
    }
    
    # This sends the final data to a *new* template
    return render(request, 'home/subscription.html', context)
# Create your views here.
