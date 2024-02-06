from dataclasses import dataclass
from typing import List

from django import template

from apps.menu.models import Menu, MenuItem

register = template.Library()


@dataclass
class DrawMenuDataClass:
    menu_name: str
    menu_items: List[MenuItem]


@register.simple_tag(takes_context=False)
def draw_menu(menu_name: str) -> DrawMenuDataClass:
    menu_items = MenuItem.objects.filter(menu__name=menu_name, parent=None).select_related('menu')

    return DrawMenuDataClass(menu_name=menu_name, menu_items=menu_items)
