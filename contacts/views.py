from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.db.models import Q

def contact_list(request):
    query = request.GET.get("q", "")

    if query:
        contacts = Contact.objects.filter(
            Q(full_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query) |
            Q(note__icontains=query)
        )
    else:
        contacts = Contact.objects.all()

    return render(request, 'contacts/list.html', {
        'contacts': contacts,
        'query': query
    })


def contact_detail(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    return render(request, 'contacts/detail.html', {'contact': contact})


def contact_add(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email", "")
        note = request.POST.get("note", "")

        Contact.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            note=note
        )

        return redirect('contact_list')

    return render(request, 'contacts/form.html')   # ← змінили add.html → form.html


def contact_edit(request, pk):
    contact = get_object_or_404(Contact, id=pk)

    if request.method == "POST":
        contact.full_name = request.POST.get("full_name")
        contact.phone_number = request.POST.get("phone_number")
        contact.email = request.POST.get("email", "")
        contact.note = request.POST.get("note", "")
        contact.save()

        return redirect('contact_detail', pk=contact.id)

    return render(request, 'contacts/form.html', {'contact': contact})  # ← було edit.html


def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')

    return render(request, 'contacts/confirm_delete.html', {'contact': contact})  # ← було delete.html
