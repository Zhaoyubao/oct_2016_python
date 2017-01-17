from django.shortcuts import render, redirect
from .models import *
from django.urls import reverse
from django.contrib import messages

def index(request):
    if 'user' in request.session:
        return redirect('/books')
    return render(request, 'books/index.html')

def register(request):
    if request.method == 'POST':
        result = User.objects.validate_reg(request.POST)
        if result[0]:
            request.session['user'] = result[1]
            messages.success(request, 'Successfully registered!')
            return redirect('/books')
        print_messages(request, result[1])
    return redirect('/')

def login(request):
    if request.method == 'POST':
        result = User.objects.validate_log(request.POST)
        if result[0]:
            request.session['user'] = result[1]
            messages.success(request, 'Successfully logged in!')
            return redirect('/books')
        print_messages(request, result[1])
    return redirect('/')

def home(request):
    user = User.objects.get(id=request.session['user'])
    # users = User.objects.all()
    # authors = Author.objects.all()
    # books = Book.objects.all()
    reviews = Review.objects.order_by('-id')[:3]
    # print '*'*60
    # print "Users:", users.values('id', 'name', 'alias', 'email')
    # print "Authors:", authors.values('id', 'name')
    # print "Books:", books.values('id', 'title', 'author')
    # print "Reviews:", reviews.values('id', 'content', 'user', 'book', 'rating')
    # print '*'*60
    book_id = []
    for review in reviews:
        book_id.append(review.book.id)
    books = Book.objects.exclude(id__in=book_id).order_by('-id')
    context = {
        'user' : user,
        'reviews' : reviews,
        'books' : books
    }
    return render(request, 'books/home.html', context)

def new(request):
    authors = Author.objects.order_by('name')
    return render(request, 'books/new.html', {'authors' : authors})

def create(request):
    if request.method == 'POST':
        result = validate_add_all(request, request.POST)
        if not result[0]:
            for error in result[1]:
                messages.error(request, error)
            return redirect('/books/new')
    url = '/books/show/{}'.format(result[1])
    return redirect(url)

def show_book(request, book_id):
    b = Book.objects.get(id=book_id)
    reviews = b.review_set.order_by('-id')
    # reviews = Review.objects.filter(book=b).order_by('-id')
    context = {
        'book' : b,
        'reviews' : reviews
    }
    return render(request, 'books/show.html', context)

def create_review(request, book_id):
    if request.method == 'POST':
        review = request.POST['review']
        rating = request.POST['rating']
        valid = True
        if not review or review.isspace():
            messages.error(request, "Please enter the book review!")
            valid = False
        if not rating:
            messages.error(request, "Please input rating from 1 to 5!")
            valid = False
        if valid:
            u = User.objects.get(id=request.session['user'])
            b = Book.objects.get(id=book_id)
            Review.objects.create(content=review, user=u, book=b, rating=rating)
    return redirect(reverse('show_book', kwargs={'book_id' : book_id}))

def delete_review(request, review_id):
    r= Review.objects.get(id=review_id)
    book_id = r.book.id
    r.delete()
    return redirect(reverse('show_book', kwargs={'book_id' : book_id}))

def show_user(request, user_id):
    user = User.objects.get(id=user_id)
    # reviews = user.review_set.all()
    reviews = Review.objects.filter(user=user)  #(user=user_id) (user=user.id) (user_id=user_id)
    count = len(reviews)
    # titles = {}
    # for review in reviews:
    #     titles[review.book.id] = review.book.title
    books = Book.objects.filter(review__user=user)
    context = {
        'user' : user,
        'count' : count,
        'books' : books
        # 'titles' : titles
    }
    return render(request, 'books/profile.html', context)

def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect('/')

def print_messages(request, error_list):
     for error, tag in error_list:
        messages.error(request, error, extra_tags=tag)

def validate_add_all(request, input):
    errors = []
    title = request.POST['title']
    preset = request.POST['preset']
    author = request.POST['author']
    review = request.POST['review']
    rating = request.POST['rating']
    if not title or title.isspace():
        errors.append("Please enter the book title!")
    elif Book.objects.filter(title__iexact=title).exists():
        errors.append("This book already exists!")
    if (not preset and not author) or (preset and author):
        errors.append("Please enter a new author or choose from the list!")
    elif author:
        if Author.objects.filter(name__iexact=author).exists():
            errors.append("This author already exists, just choose from the list!")
        else:
            curr_author = author
    else:
        curr_author = preset
    if not review or review.isspace():
        errors.append("Please enter the book review!")
    if not rating:
        errors.append("Please input rating from 1 to 5!")

    if errors:
        return (False, errors)
    u = User.objects.get(id=request.session['user'])
    a = Author.objects.create(name=curr_author)
    b = Book.objects.create(title=title, author=a)
    r = Review.objects.create(content=review, user=u, book=b, rating=rating)
    return (True, b.id)
