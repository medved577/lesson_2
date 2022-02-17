from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def products(request):
    context = {
        'title' : 'Geekshop - тестовый контекст',
        'header' : 'Welcome !',
        'username': 'Иван Ивановов',
        'products':[
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'is_promotion': False,
    }
    #return render(request, 'products/test-context.html', context)
    return render(request, 'products/products.html', context)

def test_context(request):
    context = {
        'title' : 'Geekshop - тестовый контекст',
        'header' : 'Welcome !',
        'username': 'Иван Ивановов',
        'products':[
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'is_promotion': False,
    }
    return render(request, 'products/test-context.html', context)
