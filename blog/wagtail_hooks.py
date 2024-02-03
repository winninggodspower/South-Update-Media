from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet


from .models import Category


class CategoryAdmin(SnippetViewSet):
    model = Category
    # base_url_path = 'bookadmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Category'  # ditch this to use verbose_name_plural from model
    menu_icon = 'folder'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'slug')
    list_filter = ('name',)
    search_fields = ('name')

# Now you just need to register your customised ModelAdmin class with Wagtail
register_snippet(CategoryAdmin)