# Generated by Django 3.1.3 on 2020-11-30 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('caption', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AboutTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('caption', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='AbujaShowroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='BedRoomCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='factory_images')),
                ('title', models.CharField(default='Project image', max_length=60)),
                ('blog', models.TextField(default='none', max_length=20)),
                ('url', models.CharField(default='link', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='factory_images')),
                ('category', models.CharField(default='category image', max_length=60)),
                ('title', models.CharField(default='Project image', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CenterCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ClientCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=60)),
                ('email', models.CharField(default='none', max_length=60)),
                ('phone', models.CharField(default='none', max_length=60)),
                ('message', models.CharField(default='none', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DinningCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='DoorCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='FactoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='factory_images')),
                ('title', models.CharField(default='factory image', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('caption', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='KadunaShowroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='KitchenCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='LagosShowroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='LivingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='factory_images')),
                ('title', models.CharField(default='Project image', max_length=60)),
                ('process', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='factory_images')),
                ('title', models.CharField(default='Project image', max_length=60)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='QuoteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=60)),
                ('email', models.CharField(default='none', max_length=60)),
                ('phone', models.CharField(default='none', max_length=60)),
                ('address', models.CharField(default='none', max_length=250)),
                ('subject', models.CharField(default='none', max_length=250)),
                ('message', models.TextField(default='none')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('caption', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServicePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('number', models.CharField(default='none', max_length=60)),
                ('caption', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('caption', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=350)),
                ('description', models.CharField(max_length=350)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('company', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('footer', models.TextField(blank=True)),
                ('newsletter', models.CharField(blank=True, max_length=50)),
                ('smtpport', models.CharField(blank=True, max_length=50)),
                ('icon', models.ImageField(blank=True, upload_to='images')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('aboutheader', models.TextField(blank=True)),
                ('aboutus', models.TextField(blank=True, max_length=1500)),
                ('ourvision', models.TextField(blank=True, max_length=1500)),
                ('ourmision', models.TextField(blank=True, max_length=1500)),
                ('corevalues', models.TextField(blank=True, max_length=1500)),
                ('overview', models.TextField(blank=True, max_length=500)),
                ('references', models.TextField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('project', models.CharField(blank=True, max_length=50)),
                ('awards', models.CharField(blank=True, max_length=50)),
                ('services', models.TextField(blank=True)),
                ('years', models.CharField(blank=True, max_length=50)),
                ('showroom', models.TextField(blank=True)),
                ('measurement', models.TextField(blank=True)),
                ('design', models.TextField(blank=True)),
                ('delivery', models.TextField(blank=True)),
                ('installation', models.TextField(blank=True)),
                ('brand', models.TextField(blank=True)),
                ('image', models.ImageField(default='none', upload_to='images')),
                ('factory', models.TextField(blank=True, max_length=250)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('title', models.CharField(default='Stock Image', max_length=60)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='StockContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='stock content', max_length=60)),
                ('image', models.ImageField(default='none', upload_to='image')),
                ('content_one', models.TextField()),
                ('content_two', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TvCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WardrobeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='none', max_length=60)),
                ('image', models.ImageField(upload_to='images')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(default='header', max_length=60)),
                ('title', models.CharField(default='Stock Image', max_length=60)),
                ('url', models.CharField(default='youtub link', max_length=300)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
