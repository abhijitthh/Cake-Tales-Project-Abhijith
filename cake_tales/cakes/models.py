from django.db import models

# Create your models here.
import uuid

class BaseClass(models.Model):

    uuid=models.UUIDField(unique=True,default=uuid.uuid4)

    active_status=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    class Meta:

        abstract=True

# class CategoryChoice(models.TextChoices):

#     WEDDING_CAKES = "Wedding Cakes","Wedding Cakes"

#     BIRTHDAY_CAKES = "Birthday Cakes","Birthday Cakes"

#     PLUM_CAKES = "Plum Cakes","Plum Cakes"

#     CUP_CAKES = "Cup Cakes","Cup Cakes"

class Category(BaseClass):

    name=models.CharField(max_length=30)

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name='Catergories'

        verbose_name_plural='Catergories'

# class FlavourChoice(models.TextChoices):

#     VANILLA = 'Vanilla','Vanilla'

#     CHOCOLATE = 'Chocolate','Chocolate'

#     BUTTERSCOTCH = 'Butterscotch','Butterscotch'

#     STRAWBERRY = 'Strawberry','Strawberry'

#     RED_VELVET = 'Red Velvet','Red Velvet'

#     BLACK_FOREST = 'Black Forest','Black Forest'

#     WHITE_FOREST = 'White Forest','White Forest'

#     PINEAPPLE = 'Pineapple','Pineapple'

#     BLUEBERRY = 'Blueberry','Blueberry'

#     MANGO = 'Mango','Mango'

#     OREO = 'Oreo','Oreo'

class Flavor(BaseClass):

    name=models.CharField(max_length=30)

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name='Flavors'

        verbose_name_plural='Flavors'


class Shape(BaseClass):

    name=models.CharField(max_length=30)

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name='Shapes'

        verbose_name_plural='Shapes'

# class WeightChoice(models.TextChoices):

#     HALF_KG = '1/2 kg','1/2 kg'

#     ONE_KG = '1 kg','1 kg'

#     TWO_KG = '2 kg','2 kg'

#     THREE_KG = '3 kg','3 kg' 
class Weight(BaseClass):

    name=models.CharField(max_length=30)

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name='Weights'

        verbose_name_plural='Weights'

class Cake(BaseClass):

    name = models.CharField(max_length=50)

    description = models.TextField()

    photo = models.ImageField(upload_to='cakes-images')

    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    flavour = models.ForeignKey('Flavor',on_delete=models.CASCADE)

    shape = models.ForeignKey('Shape',on_delete=models.CASCADE)

    weight = models.ForeignKey('Weight',on_delete=models.CASCADE)

    egg_added = models.BooleanField(default=True)

    is_available = models.BooleanField(default=True)

    price = models.FloatField()

    def __str__(self):

        return self.name
    
    class Meta :

        verbose_name='Cakes'

        verbose_name_plural='Cakes'