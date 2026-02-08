from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
                                            #ускорить фильтрацию товаров
    slug = models.SlugField(max_length=100, unique=True, )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории' 

    def __str__(self):
        return self.name
    

SIZE_CHOICES = (
    ('XS', 'Очень маленький'),
    ('S', 'Маленький'),
    ('M', 'Средний'),
    ('L', 'Большой'),
    ('XL', 'Очень большой'),
    ('XXL', 'Огромный размер')
)  
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='продукты', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
                                #поставил decimal field для высчитывания скидки 
    available = models.BooleanField(default=True)
    createddate = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='M')
    discount_percentage = models.PositiveSmallIntegerField(default=0, help_text="Процент скидки")
    


    @property
    def discounted_price(self):
        """Рассчитать цену с учетом скидки."""
        if self.discount_percentage > 0:
            return round((1 - self.discount_percentage / 100) * float(self.price), 2)
        return self.price



    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name
    

