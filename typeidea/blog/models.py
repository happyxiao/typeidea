from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEFAULT = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEFAULT, '删除')
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.SmallIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEFAULT = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEFAULT, '删除')
    )
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.SmallIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DEFAULT = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DEFAULT, '删除'),
        (STATUS_DRAFT, '草稿')
    )
    title = models.CharField(max_length=10, verbose_name='名称')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='标题')
    content = models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')
    status = models.SmallIntegerField(choices=STATUS_ITEMS, default=STATUS_NORMAL, verbose_name='状态')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-id']


