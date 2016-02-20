# import django_filters
#
# from .models import BikewayCategory, Bikeway
#
#
# class BikewayFilterSet(django_filters.FilterSet):
#     min_length = django_filters.NumberFilter(name='length',
#                                              lookup_type='gte')
#     max_length = django_filters.NumberFilter(name='length',
#                                              lookup_type='lte')
#
#     class Meta:
#         model = Bikeway
#         fields = ('condition', 'category',
#                   'min_length', 'max_length')
#
#
# class BikewayCategoryFilterSet(django_filters.FilterSet):
#
#     class Meta:
#         model = BikewayCategory
#         fields = ('bikeways__condition',)
#
#     def __init__(self, *args, **kwargs):
#         super(BikewayCategoryFilterSet, self).__init__(*args, **kwargs)
#         # Here we add distinct attribute to this filter.
#         # Now the distinct method of queryset will be called
#         # if this filter is applied. It's necessary because
#         # this is a filter on a related model.
#         self.filters['bikeways__condition'].distinct = True
