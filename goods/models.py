from django.db import models


class GoodsCategory(models.Model):
    """
    Goods类别
    """
    CATEGORY_TYPE = (
        (1, '新鲜水果'),
        (2, '海鲜水产'),
        (3, '猪牛羊肉'),
        (4, '禽类蛋品'),
        (5, '新鲜蔬菜'),
        (6, '速冻食品'),
    )
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='类目级别')
    category_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面图')

    class Meta:
        db_table = 'f_goods_category'


class Goods(models.Model):
    """
    商品
    """
    category = models.ForeignKey(GoodsCategory, verbose_name='商品类目', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='商品名')
    goods_sn = models.CharField(max_length=50, default='', verbose_name='商品唯一货号')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    sold_nums = models.IntegerField(default=0, verbose_name='销售量')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    goods_nums = models.IntegerField(default=0, verbose_name='商品库存')
    market_price = models.FloatField(default=0, verbose_name='市场价格')
    shop_price = models.FloatField(default=0, verbose_name='本店价格')
    goods_brief = models.CharField(max_length=500, verbose_name='商品简短描述')
    goods_desc = models.TextField(null=True)
    goods_front_image = models.ImageField(upload_to='goods/images/', null=True, blank=True, verbose_name='封面图')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = 'f_goods'


class GoodsImage(models.Model):
    """
    商品图片
    """
    goods = models.ForeignKey(Goods, related_name='images', verbose_name='商品', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='goods/images', verbose_name='图片', null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = 'f_goods_images'



