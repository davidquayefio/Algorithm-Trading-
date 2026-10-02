from django.db import models

class Stock(models.Model):
    symbol = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()
    market_cap = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PriceData(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='price_data')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

class MomentumScore(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='momentum_scores')
    calculation_date = models.DateField(db_index=True)
    momentum_score = models.DecimalField(max_digits=10, decimal_places=4)
    rank = models.IntegerField(null=True, blank=True)
    quintile = models.IntegerField(null=True, blank=True)
    is_top_quintile = models.BooleanField(default=False)
    period_start_date = models.DateField()
    period_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class TradeSignal(models.Model):
    SIGNAL_TYPE_CHOICES = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
        ('HOLD', 'Hold')
    ]
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='trade_signals')
    signal_date = models.DateField()
    signal_type = models.CharField(max_length=4, choices=SIGNAL_TYPE_CHOICES)
    momentum_score = models.DecimalField(max_digits=10, decimal_places=4)
    target_quantity = models.IntegerField(null=True, blank=True)
    target_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    is_executed = models.BooleanField(default=False)
    executed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('stock', 'signal_date', 'signal_type')
    indexes = [
        models.Index(fields=['signal_date']),
        models.Index(fields=['signal_type']),
    ]

class RebalanceEvent(models.Model):
    date = models.DateField(unique=True)
    total_stocks_analyzed = models.IntegerField()
    buy_signals_generated = models.IntegerField()
    sell_signals_generated = models.IntegerField()
    total_portfolio_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    executed_status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('EXECUTED', 'Executed'), ('FAILED', 'Failed')], default='PENDING')