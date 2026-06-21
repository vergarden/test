from django.db import models

class BoardSaying(models.Model):
    nickname = models.CharField('昵称', max_length=100)
    message = models.TextField('留言')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'boardsaying'
        verbose_name = '留言'
        verbose_name_plural = '留言板'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nickname}: {self.message[:20]}'


class EmailSending(models.Model):
    name = models.CharField('名字', max_length=100)
    email = models.EmailField('邮箱')
    subject = models.CharField('主题', max_length=200, blank=True)
    body = models.TextField('内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'emailsending'
        verbose_name = '邮件'
        verbose_name_plural = '邮件发送'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} <{self.email}>: {self.subject or "(无主题)"}'
