from django.shortcuts import render, redirect
from . import models

# Create your views here.


def index(request):
    if request.method == "POST":
        categoryName = request.POST.get("category_name")

        if categoryName:
            models.Category.objects.create(name=categoryName, balance=0)

        return redirect("/")

    categories = models.Category.objects.all()

    return render(request, "mysite/index.html", {"categories": categories})


def category(request, categoryId):
    category = models.Category.objects.get(id=categoryId)

    if request.method == "POST":
        if request.POST.get("action") == "delete":
            category.delete()
            return redirect("/")

        budgetName = request.POST.get("budget_name")
        if budgetName:
            models.Budget.objects.create(name=budgetName, balance=0, category=category)
        return redirect("/category/{id:d}".format(id=categoryId))

    budgets = models.Budget.objects.filter(category=category)

    return render(
        request, "mysite/category.html", {"category": category, "budgets": budgets}
    )


def budget(request, budgetId):
    budget = models.Budget.objects.get(id=budgetId)
    if request.method == "POST":
        action = request.POST.get("action")
        amount = request.POST.get("amount")
        transactionName = ""

        if action == "delete":
            category = budget.category
            budget.delete()
            return redirect("/category/{id:d}".format(id=category.id))

        try:
            amount = float(amount)
        except:
            return redirect("/budget/{id:d}".format(id=budgetId))

        if amount <= 0:
            return redirect("/budget/{id:d}".format(id=budgetId))

        if action == "withdraw":
            transactionName = "Withdrawal"
            budget.balance -= amount
            budget.category.balance -= amount
        elif action == "deposit":
            transactionName = "Deposit"
            budget.balance += amount
            budget.category.balance += amount

        models.Transaction.objects.create(
            name=transactionName, amount=amount, budget=budget
        )
        budget.save()
        budget.category.save()

        return redirect("/budget/{id:d}".format(id=budgetId))

    transactions = models.Transaction.objects.filter(budget=budget).order_by(
        "-created_at"
    )
    return render(
        request, "mysite/budget.html", {"budget": budget, "transactions": transactions}
    )
