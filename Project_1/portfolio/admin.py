from django.contrib import admin

from .models import PerformanceMetric, Portfolio, Position, Trade


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_value', 'current_cash', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'stock', 'quantity', 'average_cost', 'current_price', 'unrealized_pnl', 'last_updated')
    search_fields = ('portfolio__name', 'stock__symbol')
    list_filter = ('portfolio', 'last_updated')
    readonly_fields = ('last_updated', 'created_at')


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'stock', 'trade_type', 'quantity', 'price', 'status', 'created_at')
    search_fields = ('portfolio__name', 'stock__symbol')
    readonly_fields = ('created_at', 'submitted_at', 'filled_at')
    list_filter = ('portfolio', 'status', 'trade_type', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(PerformanceMetric)
class PerformanceMetricAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'date', 'total_value', 'cash_value', 'positions_value', 'daily_return', 'created_at')
    search_fields = ('portfolio__name',)
    readonly_fields = ('created_at',)
    list_filter = ('portfolio', 'date')
    date_hierarchy = 'date'