from django.shortcuts import render
def calcs_churn(request):
    initialCust = float(request.POST.get('initial_customer', '0'))
    PresentCust = float(request.POST.get('present_customer', '0'))
    churn = (initialCust/PresentCust)*100 if request.method == 'POST' else 0
    print("initial customer =",initialCust)
    print("fnal customer =",PresentCust)
    print("Churn rate =",churn)
    return render(request, 'myapp/math.html',{'initialCust': initialCust, 'PresentCust': PresentCust, 'churn': churn})

