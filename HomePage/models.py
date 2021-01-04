from django.db import models
from django.conf import settings

# Create your models here.
CATEGORY_CHOICES = (
    ('S', 'Stickers'),
    ('P', 'Prints'),
    ('A', 'Aparrel'),
    ('O', 'Other')
)

class Item(models.Model): 
    title = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, default='O', max_length=2)
    image = models.ImageField(default="static/img/defaultsticker.png", upload_to='static/img', height_field=None, width_field=None, max_length=None)
    description = models.TextField(default=None, null=True, blank=True)

    def __str__(self): 
        return self.title

    def getPrice(self): 
        priceWith2Decimals = '{:0.2f}'.format(self.price)
        return priceWith2Decimals

    def getRating(self): 
        reviews = Review.objects.filter(item=self)
        sum = 0
        for review in reviews: 
            sum += review.rating
        avg = sum / len(reviews)
        return round(avg, 2) 

class Review(models.Model): 
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    rating = models.FloatField()
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Order(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

