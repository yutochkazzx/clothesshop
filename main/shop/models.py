from django.conf import settings
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
    ('XS', 'XS — Очень маленький'),
    ('S', 'S — Маленький'),
    ('M', 'M — Средний'),
    ('L', 'L — Большой'),
    ('XL', 'XL — Очень большой'),
    ('XXL', 'XXL — Огромный размер'),
)  
class Product(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Владелец',
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )
    name = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField('Ссылка (slug)', max_length=100, unique=True)
    image = models.ImageField('Изображение', upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    available = models.BooleanField('В наличии', default=True)
    createddate = models.DateField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)
    size = models.CharField('Размер', max_length=3, choices=SIZE_CHOICES, default='M')
    discount_percentage = models.PositiveSmallIntegerField(
        'Процент скидки',
        default=0,
        help_text='Процент скидки (0–100). Цена со скидкой отобразится в каталоге.',
    )




    @property
    def discounted_price(self):
        """Рассчитать цену с учетом скидки."""
        if self.discount_percentage > 0:
            return round((1 - self.discount_percentage / 100) * float(self.price), 2)
        return self.price
    



    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
    

