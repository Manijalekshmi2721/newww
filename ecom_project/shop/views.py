# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
# from shop.models import Category
# # Create your views here.
# # def home(request):
# #     return HttpResponse('hellow')
# def allproductcat(request,c_slug=None):
#     c_page=None
#     products=None
#     if c_slug!=None:
#         c_page=get_object_or_404(Category,slug=c_slug)
#         products=products.objects.all().filter(category=c_slug,available=True)
#     else:
#         products = products.objects.all().filter(category=c_slug, available=True)
#     return render(request,"category.html",{'category':c_page,'products':products})
#
# def get_url(self):
#     return reverse('shop:products_by_categories',args=[self.slug])
#
