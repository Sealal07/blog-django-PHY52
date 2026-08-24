from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок', 
        help_text='Введите заголовок поста'
    )
    content = models.TextField(
        verbose_name='Содержание',
        help_text='Введите текст поста'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, #фиксирует один раз при добавлении
        verbose_name='Дата создания'
    )
    update_at = models.DateTimeField(
        auto_now=True,#фиксирует каждый раз при обнов.
        verbose_name='Дата обновления'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

        ordering = ['-created_at']

