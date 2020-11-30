from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from main.models import *

# Create your views here.
def index(request):
	kitchen = KitchenCategory.objects.order_by("-pub_date")[0]
	living = LivingCategory.objects.order_by("-pub_date")[0]
	bedroom = BedRoomCategory.objects.order_by("-pub_date")[0]

	office = OfficeCategory.objects.order_by("-pub_date")[0]
	dinning = DinningCategory.objects.order_by("-pub_date")[0]
	door = DoorCategory.objects.order_by("-pub_date")[0]

	center = CenterCategory.objects.order_by("-pub_date")[0]
	tv = TvCategory.objects.order_by("-pub_date")[0]

	client = ClientCategory.objects.order_by("-pub_date")[0]
	wardrobe = WardrobeCategory.objects.order_by("-pub_date")[0]
	
	context = {"kitchen": kitchen, "living": living, "bedroom": bedroom, "office": office,
	 "dinning": dinning, "door": door, "wardrobe": wardrobe, "center": center, "tv": tv, "client": client}
	
	return render(request, "index.html", context)


def SingleCategoryView(request, slug):
	items = CategoryModel.objects.filter(category=slug)
	try:
		item = items[0]
		context = {"items": items, "category": slug, "item": item}
	except:
		context = {"items": items, "category": slug}
	
	return render(request, "single_category.html", context)


def about(request):
	
	context = {}
	return render(request, "about.html", context)


def service(request):
	
	context = {}
	return render(request, "service.html", context)



def contact(request):

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message)
		contact_model.save()

		response = "Thank You For Reaching Out!"

		context = {"response": response}
		return render(request, "contact.html", context)

	else:

	
		response = ""

		context = {"response": response}
		return render(request, "contact.html", context)



def projects(request):
	items = ProjectModel.objects.all()
	context = {"items": items}

	return render(request, "projects.html", context)


def factory(request):
	items = FactoryModel.objects.all()
	context = {"items": items}

	return render(request, "factory.html", context)


def category(request):
	bedrooms = CategoryModel.objects.filter(category='bedroom')
	dinnings = CategoryModel.objects.filter(category='dinning')
	doors = CategoryModel.objects.filter(category='door')
	kitchens = CategoryModel.objects.filter(category='kitchen')
	living_rooms = CategoryModel.objects.filter(category='living-room')
	offices = CategoryModel.objects.filter(category='office')
	wardrobes = CategoryModel.objects.filter(category='wardrobe')


	context = {"bedrooms": bedrooms, "dinnings": dinnings, "doors": doors, "kitchens": kitchens, "living_rooms": living_rooms, "offices": offices, "wardrobes": wardrobes}

	return render(request, "category.html", context)


def showroom(request):
	
	context = {}
	return render(request, "showroom1.html", context)
