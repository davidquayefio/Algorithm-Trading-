from django.contrib import admin

from .models import (
    MomentumScore,
    PriceData,
    RebalanceEvent,
    Stock,
    TradeSignal,
)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['symbol', 'name', 'price', 'volume', 'market_cap', 'created_at']
    search_fields = ['symbol', 'name']
    list_filter = ['created_at']

@admin.register(PriceData)
class PriceDataAdmin(admin.ModelAdmin):
    list_display = ['stock', 'date', 'open_price', 'close_price', 'volume']
    list_filter = ['date', 'stock']
    search_fields = ['stock__symbol']

@admin.register(MomentumScore)
class MomentumScoreAdmin(admin.ModelAdmin):
    list_display = ['stock', 'calculation_date', 'momentum_score', 'rank', 'quintile', 'is_top_quintile']
    list_filter = ['calculation_date', 'is_top_quintile']
    search_fields = ['stock__symbol']


@admin.register(TradeSignal)
class TradeSignalAdmin(admin.ModelAdmin):
    list_display = ['stock', 'signal_date', 'signal_type', 'momentum_score', 'is_executed']
    list_filter = ['signal_date', 'signal_type', 'is_executed']
    search_fields = ['stock__symbol']


@admin.register(RebalanceEvent)
class RebalanceEventAdmin(admin.ModelAdmin):
    list_display = ['date', 'total_stocks_analyzed', 'buy_signals_generated', 'sell_signals_generated', 'executed_status']
    list_filter = ['date', 'executed_status']
    search_fields = ['date']