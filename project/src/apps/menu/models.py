from django.db import models


class Menu(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self) -> str:
        return f'Меню {self.name}'

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    url = models.CharField(verbose_name='URL элемента', max_length=255)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
    )

    menu = models.ForeignKey(
        Menu,
        related_name='menu_items',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.name}, parent: {self.parent}, menu: {self.menu.name}'

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'
