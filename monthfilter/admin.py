#!/usr/bin/env python
# encoding: utf-8
# vim:ft=python.django:
# --------------------------------------------------------------------------

import calendar

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class MonthListFilter(admin.DateFieldListFilter):
    title = _('Month')

    def choices(self, cl):
        yield {
            'selected': None,
            'query_string': cl.get_query_string({}, [self.field.name]),
            'display': _('All'),
        }

        for month in range(1, 13):
            yield {
                'selected': None,
                'query_string': cl.get_query_string(
                    {'{}__month'.format(self.field.name): month},
                    [self.field.name]),
                'display': _(calendar.month_name[month])
            }
