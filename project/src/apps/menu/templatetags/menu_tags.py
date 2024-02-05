from dataclasses import dataclass
from typing import List

from django import template
from django.shortcuts import get_object_or_404

from apps.menu.models import Menu, MenuItem

register = template.Library()


@dataclass
class DrawMenuDataClass:
    menu: Menu
    menu_items: List[MenuItem]


@register.simple_tag(takes_context=False)
def draw_menu(menu_name: str) -> DrawMenuDataClass:
    menu = get_object_or_404(Menu, name=menu_name)
    menu_items = MenuItem.objects.all().select_related('menu').filter(menu=menu, parent=None)

    return DrawMenuDataClass(menu=menu, menu_items=menu_items)
