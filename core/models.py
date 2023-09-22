from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.core.validators import RegexValidator
import uuid 
import os 



class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email: 
            raise ValueError('user harus mempunyai email')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, email, password): 
        user = self.create_user(email, password)
        user.set_password(password)
        user.is_staff = True 
        user.is_superuser = True 

        user.save(using=self._db)
        return user


phone_regex = RegexValidator(
    r'^628[0-9]{11,14}$',
    message="Nomor telepon harus dimulai dengan '628' dan memiliki panjang 11 hingga 14 digit",
)

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=10, choices=[('ADMIN','Admin'),('USER','User')])
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=14,
        unique=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email' 

    def __str__(self):
        return self.name
    
def product_image_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4}{ext}'

    return os.path.join('uploads', 'product', filename)

class Product(models.Model): 
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True, upload_to=product_image_path)
    stock_available = models.PositiveIntegerField()

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'), 
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user} - {self.order_date} - {self.status}'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)  

        # Dapatkan produk pertama pengguna (gantilah dengan logika yang sesuai)
        first_product = Product.objects.first()  # Ini hanya contoh, Anda perlu menggantinya dengan logika yang sesuai

        if first_product:
            # Buat OrderItem secara otomatis dengan produk pertama
            order_item = OrderItem.objects.create(
                order=self,
                product=first_product,
                quantity=1,
                price=first_product.price
            )
            order_item.save()


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product} - {self.order.user} - {self.price}'
    