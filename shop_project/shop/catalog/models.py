from django.db import models
from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Discount(models.Model):
    percent = models.IntegerField()
    name = models.CharField(max_length=20)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name


class Promocode(models.Model):
    name = models.CharField(max_length=10)
    percent = models.IntegerField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    is_cumulative = models.BooleanField()

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.country}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    articul = models.CharField(max_length=20)
    description = models.TextField()
    count_on_stock = models.IntegerField()
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(null=True, blank=True)


class Order(models.Model):
    DELIVERY_METHODS = (
        ('Courier', 'Courier'),
        ('Self-delivery', 'Self-delivery'),
        ('Post', 'Post')
    )

    DELIVERY_STATUSES = (
        ('Delivery', 'Delivery'),
        ('In progress', 'In progress'),
        ('Lost', 'Lost')
    )

    PAYMENT_METHOD = (
        ('Card', 'Card'),
        ('Cash', 'Cash'),
        ('Card online', 'Card online')
    )

    PAYMENT_STATUSES = (
        ('Paid,', 'Paid'),
        ('In progress', 'In progress')
    )

    DELIVERY_NOTIF_IN_TIME = (
        (24, 24),
        (6, 6),
        (1, 1)
    )

    created_at = models.DateTimeField(auto_now_add=True)
    promocode = models.ForeignKey(Promocode, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL)
    result_price = models.DecimalField(max_digits=15, decimal_places=2)

    delivery_adress = models.CharField(max_length=200, null=True, blank=True)
    delivery_method = models.CharField(choices=DELIVERY_METHODS, max_length=15, default='Courier')
    delivery_status = models.CharField(choices=DELIVERY_STATUSES, max_length=15, default='In progress')
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=15, default='Card online')
    payment_statuses = models.CharField(choices=PAYMENT_STATUSES, max_length=15, default='In progress')
    delivery_notif_in_time = models.IntegerField(choices=DELIVERY_NOTIF_IN_TIME, null=True, default=None)
    delivery_time = models.DateTimeField()


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()


class Cashback(models.Model):
    percent = models.IntegerField()
    treshold = models.IntegerField()
