from decimal import Decimal


class Order(object):
    def __init__(
        self,
        product_name: str,
        base_price: Decimal,
        fee: Decimal,
        discount_strategy=None,
    ):
        self.product_name = product_name
        self.base_price = base_price
        self.fee = fee
        self.discount_strategy = discount_strategy

    def price_incl_fee(self) -> Decimal:
        """
        Base price with fee added
        """
        ret = self.base_price + self.fee
        return ret

    def price_after_discount(self) -> Decimal:
        """
        Final price after discount applied (if any) and fee added
        """

        if self.discount_strategy is not None:
            total = (self.base_price - self.discount_strategy(self)) + self.fee
            return total
        else:
            return self.price_incl_fee()

    def __str__(self):
        return f"{self.product_name} : {self.price_after_discount()}"


def twenty_percent_discount(order: Order):
    """
    20% discount for any product
    :param order:
    :return discount:
    """
    disc = order.base_price * Decimal("0.20")
    return disc


def fixed_discount(order: Order):
    """
    5k discount fixed amount discount
    :param order:
    :return:
    """
    return Decimal("5000")


if __name__ == "__main__":
    order_pulsa_perc_disc = Order(
        "Pulsa 50k",
        base_price=Decimal("50000"),
        fee=Decimal("1000"),
        discount_strategy=twenty_percent_discount,
    )
    order_pulsa_without_disc = Order(
        "Pulsa 50k", base_price=Decimal("50000"), fee=Decimal("1000")
    )

    order_emoney_fixed_disc = Order(
        "Emoney 200k",
        base_price=Decimal("200000"),
        fee=Decimal("1000"),
        discount_strategy=fixed_discount,
    )

    print(order_pulsa_perc_disc)
    print(order_pulsa_without_disc)
    print(order_emoney_fixed_disc)
