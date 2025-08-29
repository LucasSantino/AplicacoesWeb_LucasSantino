from django.contrib import admin
from .models import User, Token, UserToken, Transaction, Play


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "cpf", "rg", "birth_date", "phone")
    search_fields = ("username", "email", "cpf", "rg")
    list_filter = ("birth_date", "city", "state")


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code", "mangecoin_value", "inserted_at")
    search_fields = ("name", "code")
    list_filter = ("inserted_at",)


@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "token", "amount")
    search_fields = ("user__username", "token__name")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "from_token", "to_token", "amount", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "from_token__code", "to_token__code")


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "won", "amount", "played_at")
    list_filter = ("won", "played_at")
    search_fields = ("user__username",)
