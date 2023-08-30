from django.contrib import admin

from catalog.models import Genre, Language, Country, Author, Book, BookInstance


class BookInline(admin.TabularInline):
    madel = Book


class BookInStanceInline(admin.StackedInline):
    madel = BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'pseudonym']
    search_fields = ['pseudonym', 'first_name']


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    search_fields = ['title', 'author__pseudonym']


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'borrower', 'due_back', 'isbn']
    fieldsets = (
        ('Group1', {
            'fields': ('book', 'isbn', 'status', 'language')
        }),
        ('Group2', {
            'fields': ('borrower', 'due_back')
        }),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
