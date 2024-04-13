from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    date_registr_client = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'Name: {self.name}, email: {self.email}, phone_number: {self.phone_number}, '
                f'address: {self.address}, date_registr_client: {self.date_registr_client}')


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(null=True)
    date_added = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return (f'Name: {self.name}, description: {self.description},price: {self.price},'
                f' quantity: {self.quantity}, date_added: {self.date_added} ')


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'customer: {self.customer}, total_price: {self.total_price}, date_ordered:{self.date_ordered} '
