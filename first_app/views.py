from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Books


# Create your views here.


def add_books():   # normal function
    """function that create the books"""
    name='geology'
    book_code=501
    auther='rohit'
    return (Books.objects.create(name=name, book_code=book_code, auther=auther))
# add_books()


def display(request):
    return HttpResponse('12234')

def show(request):
    print("-------------", request)   # <WSGIRequest: GET '/show'>
    # print("-------------", request.method)   # [GET - fetch data] & [POST - manipulation of data]

    return render(request, 'base.html')

def show_books(request):
    all_books = Books.objects.all()
    context = {'books': all_books}
    return render(request, 'homepage.html',context=context)

def edit_book(request, id):
    book = Books.objects.get(id=id)
    return render(request, 'book_cret.html', context={'single_data': book})

def delete_book(request, id):
    data = Books.objects.get(id=id)
    data.delete()
    return redirect('show_books')

def create_data(request):
    if request.method == 'POST':
        if not request.POST.get('bid'):
        # print(request.method)
        # print(request.GET)
        # print(request.POST)
            bname = request.POST['bname']
            bcode = request.POST['bcode']
            bauther = request.POST['bauther']
            # print(bname, bcode, bauther)
            Books.objects.create(name=bname, book_code=bcode, auther=bauther)
            return redirect('create_books')


        else:
            bid = request.POST.get('bid')
            book = Books.objects.get(id=bid)
            book.name = request.POST['bname']
            book.book_code = request.POST['bcode']
            book.auther = request.POST['bauther']
            book.save()
            return redirect('show_books')
    else:
        # print(request.method)
        return render(request, template_name='book_cret.html')

