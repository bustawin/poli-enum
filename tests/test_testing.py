from enum import unique

import pytest

from poli_enum.continent import Continent
from poli_enum.country import Country
from poli_enum.currency import Currency, Symbol
from poli_enum.layout import Layout
from poli_enum.subdivision import Subdivision


def test_currency():
    unique(Currency)
    assert Currency.EGP.value == 31
    assert format(Currency.EUR, 's') == '€'


def test_currency_symbol_property():
    assert Currency.EUR.symbol == '€', 'Shows Symbol.EUR.value'
    assert Currency.BDT.symbol == 'BDT', 'BDT has no symbol.'


def test_currency_symbol():
    assert Symbol.AZN.value == '₼'


def test_continent():
    unique(Continent)
    assert Continent.AF.value == 'Africa'


def test_country():
    unique(Country)
    assert Country.PH.value == 'Philippines'


def test_subdivision():
    unique(Subdivision)
    assert Subdivision['ES-CA'].value == 963


def test_subdivision_in_country():
    assert Subdivision['ES-CA'] in Country.ES
    assert Subdivision['ES-CA'] not in Country.PH


def test_country_only_has_countries():
    with pytest.raises(TypeError):
        Country.ES in Country.AD


def test_layout():
    assert Layout.IN
