from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin
from django.utils.html import format_html

from .models import Category, Tag, Post, Recipe, Comment


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "photo",
        "short_title",
        "colored_category",
        "author",
        "create_at",
    ]
    list_display_links = ["photo", "short_title"]
    prepopulated_fields = {"slug": ("title",)}

    save_on_top = True
    fields = [
        "author",
        "post_photo",
        "title",
        "slug",
        "text",
        "image",
        "tags",
        "category",
        "create_at",
    ]

    readonly_fields = ["post_photo", "create_at"]
    inlines = [RecipeInline]

    @admin.display(description="photo")
    def photo(self, obj: Post):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=80>")
        return "No Photo"

    @admin.display()
    def post_photo(self, obj: Post):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width=280>")
        return "No Photo"

    @admin.display(description="title")
    def short_title(self, obj: Post):
        return obj.title[:47] + "..." if len(obj.title) > 50 else obj.title

    @admin.display(description="category")
    def colored_category(self, obj: Post):
        if obj.category.name == "Vegan":
            color_code = "00FF00"
        else:
            color_code = "000000"
        html = '<span style="color: #{};">{}</span>'.format(color_code, obj.category.name)
        return format_html(html)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
