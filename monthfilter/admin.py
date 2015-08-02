#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:
# --------------------------------------------------------------------------

import calendar

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class MonthListFilter(admin.DateFieldListFilter):
    title = _('Month')

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s__month' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg)
        super(MonthListFilter, self).__init__(
            field, request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def choices(self, cl):
        yield {
            'selected': self.lookup_val is None,
            'query_string': cl.get_query_string({}, [self.field.name]),
            'display': _('All'),
        }

        for month in range(1, 13):
            yield {
                'selected': self.lookup_val == str(month),
                'query_string': cl.get_query_string(
                    {'{}__month'.format(self.field.name): month},
                    [self.field.name]),
                'display': _(calendar.month_name[month])
            }
