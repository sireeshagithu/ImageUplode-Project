from django.shortcuts import render
from django.http import HttpResponse
from imageuplodeapp.models import ImageUplodeModel
from imageuplodeapp.forms import ImageUplodeForm
# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form=ImageUplodeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>image uploade successfully....</h2>")
    else:
        form=ImageUplodeForm()
        images=ImageUplodeModel.objects.all()
    return render(request,'index.html',{'form':form,'images':images})
