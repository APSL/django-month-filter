# Django Month Filter

## Quickstart

Example::

    from monthfilter.admin import MonthListFilter

    class MyAdmin(admin.ModelAdmin):
        list_filter = (('monthfield', MonthListFilter),)
