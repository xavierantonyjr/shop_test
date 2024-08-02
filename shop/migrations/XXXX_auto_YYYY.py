# shop/migrations/XXXX_auto_YYYY.py

from django.db import migrations, models

def create_demo_products(apps, schema_editor):
    Product = apps.get_model('shop', 'Product')
    Product.objects.create(name="Product 1", description="Description for Product 1", price=10.99)
    Product.objects.create(name="Product 2", description="Description for Product 2", price=15.99)
    Product.objects.create(name="Product 3", description="Description for Product 3", price=12.99)

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),  # Update this line
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RunPython(create_demo_products),
    ]
