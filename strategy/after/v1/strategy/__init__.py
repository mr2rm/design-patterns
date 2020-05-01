__all__ = ['order', 'shipping_cost', 'fedex_strategy',
           'postal_strategy', 'ups_strategy']

from strategy.order import Order
from strategy.shipping_cost import ShippingCost
from strategy.fedex_strategy import FedExStrategy
from strategy.postal_strategy import PostalStrategy
from strategy.ups_strategy import UPSStrategy
