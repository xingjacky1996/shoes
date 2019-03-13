from django.shortcuts import render,HttpResponse,reverse
from django.http import JsonResponse
from .models import User,Shoes
from .forms import Shoesform,Userform

# Create your views here.
def get(request):
    user=User.objects.all()
    return render(request,'demo/get.html',{'user':user})

def updateusershoes(request):
    if request.method=='GET':
        shoes = Shoesform()
        return render(request,'demo/post.html',{'shoes':shoes})
    else:
        newshoes=Shoesform(request.POST)
        uid=''
        if newshoes.is_valid():
        #     newshoes.save()
            uid = newshoes.cleaned_data['u'].id
        user = User.objects.filter(id=uid).first()
        shoes = Shoes.objects.filter(u=user)
        shoesid = []
        for item in shoes:
            shoesid.append(str(item.id))
        return JsonResponse({'success':True,'message':'OK','result':{'userid':uid,'shoesid':shoesid}})


def getusershoes(request,id):
    user=User.objects.filter(id=id).first()
    shoes=Shoes.objects.filter(u=user)
    shoesarr=[]
    for item in shoes:
        shoe={'id':item.id,"size":item.size,"color":item.color}
        shoesarr.append(shoe)
    return JsonResponse({"username":shoes[0].u.name,"shoes":shoesarr})
