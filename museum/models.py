from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Новость')
    short_text = models.TextField(default='none', verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Текст новости')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='Дата создания')
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Дата опубликования')
    photo = models.ImageField(upload_to='news', default='news.png', verbose_name='Превью фото')
    photo_alt = models.CharField(max_length=200, default='none', verbose_name='Описание фото')
    photo_title = models.CharField(max_length=200, default='none', verbose_name='Описание фото при наведении')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'    

class Exposition(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экспозиции')
    subtitle = models.CharField(max_length=200, null=True, blank=True, verbose_name='Подназвание')
    description = models.TextField(verbose_name='Описание')
    add_text = models.TextField(null=True, blank=True, verbose_name='Дополнительный текст')
    photo = models.ImageField(upload_to='exp', default='exp.png', verbose_name='Превью фото')
    photo_alt = models.CharField(max_length=200, default='none', verbose_name='Описание фото')
    photo_title = models.CharField(max_length=200, default='none', verbose_name='Описание фото при наведении')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Экспозиция'
        verbose_name_plural = 'Экспозиции'

class Message(models.Model):
    sender_name = models.CharField(max_length=100, verbose_name='Имя отправителя')
    sender = models.EmailField(max_length=254, verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')
    reply = models.NullBooleanField(verbose_name='Рассмотрено')

    def __str__(self):
        return self.message
        
    def __unicode__(self):
        return self.message

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Post_img(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Новость')
    img = models.ImageField(upload_to='news', default='news.png', verbose_name='Фото')
    img_alt = models.CharField(max_length=200, default='none', verbose_name='Описание фото')
    img_title = models.CharField(max_length=200, default='none', verbose_name='Описание фото при наведении')

    def publish(self):
        self.save()

    def __str__(self):
        return self.img_alt
    
    class Meta:
        verbose_name = 'Фото новости'
        verbose_name_plural = 'Фото новости'
        
class Exposition_img(models.Model):
    exp = models.ForeignKey('Exposition', on_delete=models.CASCADE, verbose_name='Экспозиция')
    img = models.ImageField(upload_to='exp', default='exp.png', verbose_name='Фото')
    img_alt = models.CharField(max_length=200, default='none', verbose_name='Описание фото')
    img_title = models.CharField(max_length=200, default='none', verbose_name='Описание фото при наведении')

    def publish(self):
        self.save()

    def __str__(self):
        return self.img_alt

    class Meta:
        verbose_name = 'Фото экспозиции'
        verbose_name_plural = 'Фото экспозиции'