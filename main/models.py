from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 



class Setting(models.Model):

	STATUS = (
		('True', 'True'),
		('False', 'False'),
	)
	title = models.CharField(max_length=150)
	keywords = models.CharField(max_length=350)
	description = models.CharField(max_length=350)
	address = models.CharField(blank=True, max_length=150)
	company = models.CharField(blank=True, max_length=150)
	phone = models.CharField(blank=True, max_length=15)
	#fax = models.CharField(blank=True, max_length=20)
	email = models.CharField(blank=True, max_length=50)
	footer = models.TextField(blank=True)
	newsletter = models.CharField(blank=True, max_length=50)
	#smtppassword = models.CharField(blank=True, max_length=50)
	smtpport = models.CharField(blank=True, max_length=50)
	icon = models.ImageField(blank=True, upload_to='images')
	facebook = models.CharField(blank=True, max_length=50)
	instagram = models.CharField(blank=True, max_length=50)
	twitter = models.CharField(blank=True, max_length=50)
	aboutheader = models.TextField(blank=True)
	aboutus = models.TextField(blank=True, max_length=1500)
	ourvision = models.TextField(blank=True, max_length=1500)
	ourmision = models.TextField(blank=True, max_length=1500)
	corevalues = models.TextField(blank=True, max_length=1500)
	overview = models.TextField(blank=True, max_length=500)
	references = models.TextField(blank=True,  max_length=500)
	status = models.CharField(max_length=10, choices=STATUS)
	project = models.CharField(blank=True, max_length=50)
	awards  = models.CharField(blank=True, max_length=50)
	services  = models.TextField(blank=True)
	years = models.CharField(blank=True, max_length=50)
	showroom = models.TextField(blank=True)
	measurement = models.TextField(blank=True)
	design = models.TextField(blank=True)
	delivery = models.TextField(blank=True)
	installation = models.TextField(blank=True)
	brand = models.TextField(blank=True)
	image = models.ImageField(upload_to='images', default="none")
	factory = models.TextField(blank=True, max_length=250)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title



# Create your models here.
class HeaderCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class Brand(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class ServiceOne(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class ServicePage(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	number = models.CharField(max_length=60, default="none")
	#image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


# Create your models here.
class AbujaShowroom(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class LagosShowroom(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class KadunaShowroom(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class ServiceTwo(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class AboutOne(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title

# Create your models here.
class AboutTwo(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class QuoteModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=60, default="none")
	email = models.CharField(max_length=60, default="none")
	phone = models.CharField(max_length=60, default="none")
	address = models.CharField(max_length=250, default="none")
	subject = models.CharField(max_length=250, default="none")
	message = models.TextField(default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name


# Create your models here.
class HeaderCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	caption = models.TextField()

	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class KitchenCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class LivingCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		

class BedRoomCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		

class OfficeCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class DinningCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		

class DoorCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		
		

class WardrobeCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class CenterCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		

class TvCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class ClientCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		
		




class ContactModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=60, default="none")
	email = models.CharField(max_length=60, default="none")
	phone = models.CharField(max_length=60, default="none")
	message = models.CharField(max_length=60, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name



class FactoryModel(models.Model):
	image = models.ImageField(upload_to='factory_images')
	title = models.CharField(max_length=60, default="factory image")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title



class ProjectModel(models.Model):
	image = models.ImageField(upload_to='factory_images')
	title = models.CharField(max_length=60, default="Project image")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title




class CategoryModel(models.Model):
	image = models.ImageField(upload_to='factory_images')
	category = models.CharField(max_length=60, default="category image")
	title = models.CharField(max_length=60, default="Project image")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.category

class Blog(models.Model):
	image = models.ImageField(upload_to='factory_images')
	title = models.CharField(max_length=60, default="Project image")
	blog = models.TextField(max_length=20, default="none")
	url =	models.CharField(max_length=60, default="link")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title



class Processes(models.Model):
	image = models.ImageField(upload_to='factory_images')
	title = models.CharField(max_length=60, default="Project image")
	process = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class StockContent(models.Model):
	title = models.CharField(max_length=60, default="stock content")

	image = models.ImageField(default="none", upload_to='image')
	content_one = models.TextField()
	content_two = models.TextField()

	def __str__(self):
		return self.title



class Stock(models.Model):
	image = models.ImageField(upload_to='image')
	title = models.CharField(max_length=60, default="Stock Image")
	description = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class Youtube(models.Model):
	head = models.CharField(max_length=60, default="header")
	title = models.CharField(max_length=60, default="Stock Image")
	url = models.CharField(max_length=300, default="youtub link")
	description = models.TextField()
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


