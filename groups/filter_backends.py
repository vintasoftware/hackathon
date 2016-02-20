from rest_framework import filters


class LimitFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        try:
            limit = int(request.GET.get('limit', ''))
        except ValueError:
            limit = None

        if limit is not None and limit > 0:
            return queryset[:limit]
        else:
            return queryset
