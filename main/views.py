from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from order.models import *
from main.models import *

# Create your views here.
def index(request):
	try:
		settings = Setting.objects.all()
		process = Processes.objects.all()
		header = HeaderCategory.objects.all().order_by('-pub_date')[:6]
		brand = Brand.objects.all()
		banner = ServiceTwo.objects.all().order_by('?')[:1]
		youtube = Youtube.objects.all()
		kitchen = KitchenCategory.objects.order_by("-pub_date")[0]
		living = LivingCategory.objects.order_by("-pub_date")[0]
		bedroom = BedRoomCategory.objects.order_by("-pub_date")[0]

		office = OfficeCategory.objects.order_by("-pub_date")[0]
		dinning = DinningCategory.objects.order_by("-pub_date")[0]
		door = DoorCategory.objects.order_by("-pub_date")[0]

		center = CenterCategory.objects.order_by("-pub_date")[0]
		

		client = ClientCategory.objects.order_by("-pub_date")[0]
		wardrobe = WardrobeCategory.objects.order_by("-pub_date")[0]

	except:
		kitchen = []
		living = []
		bedroom = []
		office = []
		dinning = []
		door = []
		center = []
		client = []
		wardrobe = []

	blog = Blog.objects.order_by("-pub_date")
	context = {"brand":brand, 
				"header":header, 
				"kitchen": kitchen, 
				"living": living, 
				"bedroom": bedroom, 
				"office": office,
	 			"dinning": dinning, 
	 			"door": door, 
	 			"wardrobe": wardrobe, 
	 			"center": center, 
	 			"blog": blog, 
	 			"client": client,
	 			"banner": banner,
	 			"settings":settings,
	 			'process':process,
	 			'youtube':youtube,
	 			}
	


	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		address = request.POST.get('address')
		subject = request.POST.get('subject')

		quote_model = QuoteModel.objects.create(name=name, email=email, phone=phone, message=message, subject=subject, address=address)
		quote_model.save()
		context = {
				"brand":brand, 
				"header":header, 
				"kitchen": kitchen, 
				"living": living, 
				"bedroom": bedroom, 
				"office": office,
	 			"dinning": dinning, 
	 			"door": door, 
	 			"wardrobe": wardrobe, 
	 			"center": center, 
	 			"blog": blog, 
	 			"client": client,
	 			"banner":banner,
	 			"settings":settings,
	 			'process':process,
	 			'youtube':youtube,

	 			}
	
		return render(request, "index.html", context)

		
	else:
	
		context = {"brand":brand, 
					"header":header, 
					"kitchen": kitchen, 
					"living": living, 
					"bedroom": bedroom, 
					"office": office,
	 				"dinning": dinning, 
	 				"door": door, 
	 				"wardrobe": wardrobe, 
	 				"center": center, 
	 				"blog": blog, 
	 				"client": client,
	 				"banner":banner,
	 				"settings":settings,
	 				'process':process,
	 				'youtube':youtube,
	 				}
	
	
		return render(request, "index.html", context)


def SingleCategoryView(request, slug):
	settings = Setting.objects.all()
	items = CategoryModel.objects.filter(category=slug)
	try:
		item = items[0]
		context = {"items": items, "category": slug, "item": item}
	except:
		context = {
					"items": items, 
					"category": slug,
					"settings":settings,

					}
	
	return render(request, "single_category.html", context)


def about(request):
	settings = Setting.objects.all()
	banner = ServiceTwo.objects.all().order_by('?')[:1]
	header = HeaderCategory.objects.all().order_by('?')[:1]
	about = AboutOne.objects.all()
	abt = AboutTwo.objects.all()
	context = {'header':header,
				'about':about,
				'abt':abt,
				'banner':banner,
				'settings':settings,
				}
	return render(request, "about.html", context)


def service(request):
	settings = Setting.objects.all()
	process = Processes.objects.all()
	servicepage = ServicePage.objects.all()
	header = HeaderCategory.objects.all().order_by('?')[:1]
	service = ServiceOne.objects.all()
	banner = ServiceTwo.objects.all().order_by('?')[:1]
	context = {'header':header, 
				'banner':banner,
				'service':service,
				'settings':settings,
				'servicepage':servicepage,
				}
	return render(request, "service.html", context)



def contact(request):
	header = HeaderCategory.objects.all().order_by('?')[:1]
	settings = Setting.objects.all()
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message)
		contact_model.save()

		response = "Submitted Successfully, We'll Get Back to You Shortly!"

		context = {"response": response, 
					"header":header,
					"settings":settings,					}
		return render(request, "contact.html", context)

	else:

	
		response = ""

		context = {
					"response": response, 
					"header":header, 
					"settings":settings,
					}
		return render(request, "contact.html", context)



def projects(request):
	header = HeaderCategory.objects.all().order_by('?')[:1]
	settings = Setting.objects.all()
	items = ProjectModel.objects.all()
	context = {"items": items, 
				'header':header,
				"settings":settings,
			}

	return render(request, "projects.html", context)


def factory(request):
	header = HeaderCategory.objects.all().order_by('?')[:1]
	items = FactoryModel.objects.all()
	settings = Setting.objects.all()
	context = {"items": items, 
				'header':header,
				"settings":settings,
				}

	return render(request, "factory.html", context)


def category(request):
	header = HeaderCategory.objects.all().order_by('?')[:1]
	settings = Setting.objects.all()
	bedrooms = CategoryModel.objects.filter(category='bedroom')
	dinnings = CategoryModel.objects.filter(category='dinning')
	doors = CategoryModel.objects.filter(category='door')
	kitchens = CategoryModel.objects.filter(category='kitchen')
	living_rooms = CategoryModel.objects.filter(category='living-room')
	offices = CategoryModel.objects.filter(category='office')
	wardrobes = CategoryModel.objects.filter(category='wardrobe')


	context = {'header':header, 
				"bedrooms": bedrooms, 
				"dinnings": dinnings, 
				"doors": doors, 
				"settings":settings,
				"kitchens": kitchens, 
				"living_rooms": living_rooms, 
				"offices": offices, 
				"wardrobes": wardrobes}

	return render(request, "category.html", context)


def showroom(request):
	abuja = AbujaShowroom.objects.all().order_by('pub_date')
	lagos = LagosShowroom.objects.all().order_by('pub_date')
	kaduna = KadunaShowroom.objects.all().order_by('pub_date')
	header = HeaderCategory.objects.all().order_by('?')[:1]
	settings = Setting.objects.all()
	context = {'header':header,
				'abuja':abuja,
				'lagos':lagos,
				'kaduna':kaduna,
				"settings":settings,
			}
	return render(request, "showroom1.html", context)


def quote(request):
	settings = Setting.objects.all()
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		address = request.POST.get('address')
		subject = request.POST.get('subject')

		quote_model = QuoteModel.objects.create(name=name, email=email, phone=phone, message=message, subject=subject, address=address)
		quote_model.save()

		response = "Submitted Successfully, We'll Get Back to You Shortly!"
		context = {"response": response,
					"settings":settings
					}
	
		return render(request, "quote.html", context)

	else:

		context = {"settings":settings}
		return render(request, "quote.html", context)


def stock(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		settings = Setting.objects.all()

		stock = Stock.objects.all()
		selected_item = ""

		for item in stock:
			if request.POST.get(str(item.id)) == "on":
				obj = Stock.objects.get(id=item.id)
				selected_item = selected_item + (obj.title) + ", "
				
			else:
				pass


		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=selected_item)
		contact_model.save()



		settings = Setting.objects.all()
		current_user = request.user
		#shopcart = ShopCart.objects.filter(user_id=current_user.id)
		stock = Stock.objects.all()
		content = StockContent.objects.all().order_by('?')[:1]
		#current_user = request.user

		
		response = "Submitted Successfully, We'll Get Back to You Shortly!"
		context = {'settings':settings,
					'stock':stock,
					'content':content,
					'response': response,
					#'shopcart':shopcart,
		}
					
		return render(request, "stock.html", context)
		
	else:
		settings = Setting.objects.all()
		current_user = request.user
		#shopcart = ShopCart.objects.filter(user_id=current_user.id)
		stock = Stock.objects.all()
		content = StockContent.objects.all().order_by('?')[:1]
		#current_user = request.user

		
		context = {'settings':settings,
					'stock':stock,
					'content':content,
					#'shopcart':shopcart,
		}
					
		return render(request, "stock.html", context)

