# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 100.0, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available() is True


def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    assert product.total_value() == 1000.0


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (100, 110),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    with pytest.raises(ValueError, match="Nie można usunąć więcej produktów niż jest w magazynie."):
        product.remove_stock(15)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    with pytest.raises(ValueError, match="Ilość do dodania nie może być ujemna."):
        product.add_stock(-5)

# --- Testy zadania dodatkowego ---

@pytest.mark.parametrize("percent, expected_price", [
    (0, 100.0),
    (50, 50.0),
    (100, 0.0),
])
def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price

@pytest.mark.parametrize("invalid_percent", [-10, 110])
def test_apply_discount_invalid_raises(product, invalid_percent):
    with pytest.raises(ValueError, match="Procent rabatu musi być w zakresie 0-100."):
        product.apply_discount(invalid_percent)
