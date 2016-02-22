from django import template

register = template.Library()


@register.simple_tag
def user_voted(user, link):
    return link.user_voted(user)
