from django.shortcuts import render, redirect, get_object_or_404
from .forms import TransactionForm
from .models import Transaction


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all()

    return render(request, 'home.html', {
        'form': form,
        'transactions': transactions
    })


def edit_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'home.html', {'form': form})


def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    transaction.delete()
    return redirect('add_transaction')