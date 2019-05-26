from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from itertools import zip_longest

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Category, HumanName, List
from .forms import ListForm


def show_list(request):
    human_list = HumanName.objects.all()
    all_list = List.objects.all().order_by("date")

    lend_list = List.objects.filter(state="Lend")
    borrow_list = List.objects.filter(state="Borrow")

    total_amount_list = []

    for human in human_list:
        total_amount = 0
        for lend, borrow in zip_longest(lend_list, borrow_list):
            if lend and lend.human_name.human_name == human.human_name or borrow and borrow.human_name.human_name == human.human_name:
                if lend and borrow:
                    lend = int(lend.money)
                    borrow = int(borrow.money)
                if lend is None:
                    lend = 0
                    borrow = int(borrow.money)
                if borrow is None:
                    borrow = 0
                    lend = int(lend.money)
                total_amount = total_amount + (lend - borrow)
        total_amount_list.append(total_amount)

    return render(request, "moneyrecord/moneyrecord_list.html",{
        "human_list": human_list,
        "all_list": all_list,
        "total_amount": total_amount_list,
    })


class ListCreateView(CreateView):
    model = List
    form_class = ListForm
    success_url = reverse_lazy("moneyrecord:moneyrecord_list")

    def from_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, "Your registeration was successfully done"
        )
        return result


class ListUpdateView(UpdateView):
    model = List
    form_class = ListForm
    success_url = reverse_lazy("moneyrecord:moneyrecord_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, "Updating data was successfully done"
        )
        return result


class ListDeleteView(DeleteView):
    model = List
    form_class = ListForm
    success_url = reverse_lazy("moneyrecord:moneyrecord_list")

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, "Deleting data was successfully done"
        )
        return result

