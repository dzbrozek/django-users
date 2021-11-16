import datetime

from dateutil.relativedelta import relativedelta
from django import template
from django.utils import timezone

register = template.Library()


@register.filter
def is_allowed(value: datetime.date) -> str:
    """Removes all values of arg from the given string"""
    fourteen_years_ago = timezone.now().date() - relativedelta(years=14)
    is_old_enough = value <= fourteen_years_ago

    return "allowed" if is_old_enough else "blocked"


@register.filter
def bizz_fuzz(value: int) -> str:
    if value % 3 == 0 and value % 5 == 0:
        return "BizzFuzz"
    if value % 3 == 0:
        return "Bizz"
    elif value % 5 == 0:
        return "Fuzz"
    return str(value)
