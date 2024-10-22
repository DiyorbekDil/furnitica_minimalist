from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from products.validators import MaximumValidator, MinimumValidator


class CategoryModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Category name'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class TagModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Tag name'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class BrandModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Brand name'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class ColorModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Color name'))
    code = models.CharField(max_length=128, verbose_name=_('Color code'), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')


class SizeModel(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Size name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Sizes')


class ProductModel(BaseModel):
    image1 = models.ImageField(upload_to='products/', verbose_name=_('Image 1'))
    image2 = models.ImageField(upload_to='products/', verbose_name=_('Image 2'))
    name = models.CharField(max_length=128, verbose_name=_('Product name'))
    short_description = models.TextField()
    long_description = models.TextField()
    in_stock = models.BooleanField(verbose_name=_('In stock'), default=True)
    sku = models.CharField(max_length=10, unique=True)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'), default=1)
    discount = models.PositiveIntegerField(verbose_name=_('Discount'), default=0, validators=[MinValueValidator(0),
                                                                                              MaxValueValidator(100)])
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Price'))
    real_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Real Price'))

    categories = models.ManyToManyField(CategoryModel, verbose_name=_('Categories'), related_name='products')
    tags = models.ManyToManyField(TagModel, verbose_name=_('Tags'))
    colors = models.ManyToManyField(ColorModel, verbose_name=_('Colors'))
    sizes = models.ManyToManyField(SizeModel, verbose_name=_('Sizes'))

    brands = models.ForeignKey(BrandModel, on_delete=models.SET_NULL, null=True, verbose_name=_('Brands'),
                               related_name='products')

    def is_discount(self):
        return self.discount > 0

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/', verbose_name=_('Image'))

