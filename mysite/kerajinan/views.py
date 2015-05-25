from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import PostForm, CategoryForm
from .models import Product, Category, Static, Variation, Cart, CartItem
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
# from pprint import pprint

# Create your views here.
@login_required
def profile(request):
    return render(request, template_name='kerajinan/profile.html')

def home(request):
    sliders     = Static.objects.all()
    posts       = Product.objects.all().order_by("-created_date")[:6]
    paginator   = Paginator(posts,6)
    page        = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'kerajinan/home.html', {
        'posts'         : posts,
        'sliders'       : sliders,
        'categories'    : Category.objects.all(),
    })

    # return render(request, template_name='kerajinan/home.html')

def product_list(request):
    posts = Product.objects.all().order_by("-created_date")
    paginator = Paginator(posts,9)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render(request, 'kerajinan/product_list.html', {
        'posts'         : posts,
        'categories'    : Category.objects.all(),
    })


def add_product(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.userprofile = request.user
            post.save()
            return redirect('/kerajinan/add_product/', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'kerajinan/add_product.html', {'form': form})

def product_detail(request, pk):
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'kerajinan/product_detail.html', {'post': post})

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = CategoryForm()
    	return render(request, 'kerajinan/add_category.html', {'form': form}, context_instance=RequestContext(request))

def view_category(request,slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('kerajinan/category_detail.html',{
        'category'      : category,
        'categories'    : Category.objects.all() ,
        'product'       : Product.objects.filter(category__slug=slug)
    })

def static_page(request,slug):
    page = Page.objects.get(slug=slug)
    return render_to_response('kerajinan/profile.html',{
        'category'      : category,
        'categories'    : Category.objects.all() 
    })

def product_single(request, slug):
    product  = Product.objects.get(slug=slug)
    context  = {'product' : product, 'categories': Category.objects.all() }
    template = 'kerajinan/product_single.html'
    return render(request, template, context)

def view(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None

    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.product.price) * item.quantity
            item.line_total = line_total
            item.save()
            new_total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is Empty, please keep shopping."
        context = {"empty": True, "empty_message": empty_message}
    
    template = "kerajinan/cart.html"
    return render(request, template, context)

def remove_from_cart(request, pk):
    cartitem = get_object_or_404(CartItem, pk=pk)
    cartitem.delete()
    return redirect('kerajinan.views.view')


def add_to_cart(request, slug):
    request.session.set_expiry(120000)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart =Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id 
        the_id = new_cart.id 

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    product_var = []
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
                product_var.append(v)
            except:
                pass
        cart_item = CartItem.objects.create(cart=cart, product=product)
        if len(product_var) > 0:
            cart_item.Variation.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()

        return HttpResponseRedirect(reverse("cart"))
    return HttpResponseRedirect(reverse("cart"))

# def checkout(request):
    

