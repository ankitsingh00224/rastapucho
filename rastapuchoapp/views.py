from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Card, TopCard, RecentCard, BlogSlug, Blog
from .forms import ReviewForm

# Create your views here.

def HomePage(request):

    card_details = Card.objects.all()

    top_card = TopCard.objects.all()

    recent_card = RecentCard.objects.all()

    all_blogs = BlogSlug.objects.all()

    return render(request,'index.html', {'cards': card_details,'top_card':top_card,'recent_card':recent_card,'all_blogs':all_blogs});

def category(request):

    card_details = Card.objects.all()

    return render(request,'cards.html',{'card_details':card_details});



def single_slug(request, single_slug):
    slug = [s.slug_title for s in BlogSlug.objects.all()]
    if single_slug in slug:
        this_blog = Blog.objects.filter(slug=single_slug)
        return render(request=request, template_name="blogs.html", context={"blogs": this_blog})
    else:
        return render(request,"error.html")


def review(request):

    form = ReviewForm(request.POST)

    data = {}

    if request.is_ajax():
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)

    return render(request,'review.html',{'form':form})
