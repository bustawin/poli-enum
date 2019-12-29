Poli-enum
#########
Several dead-simple political python Enums: ``pip install poli-enum``.

Python 3.6+ supported.

Enums
*****
Continent
=========
Continent codes from `Data hub <https://datahub.io/core/continent-codes#data>`_.

.. code-block:: python

  from poli_enum.continent import Continent
  Continent.EU.value == 'Europe'

Country
=======
Country codes as ISO 3166-1 alpha 2, taken from `iso-3616-1 commit
8e31d749b9ce331cfa50c280a29b04ae2d805b7e  <https://github.com/spoqa/
iso-3166-1/blob/master/iso3166/table.csv>`_.

.. code-block:: python

  from poli_enum.country import Country
  Country.ES.value == 'Spain'

Subdivision
===========
Subdivision country codes from ISO 3166-2. Taken from `GEFEG <http://www.gefeg.com/
edifact/d03a/s3/codes/cl1h.htm>`_.

.. code-block:: python

  from poli_enum.subdivision import Subdivision
  catalonia = Subdivision['ES-CA']

You can check whether a subdivision is part of a country:

.. code-block:: python

  from poli_enum.country import Country
  from poli_enum.subdivision import Subdivision
  Subdivision['US-FL'] in Country.US == True


Currency
========
Currency codes as for ISO 4217 and currency symbols as for
`xe.com <https://www.xe.com/es/symbols.php>`_.

.. code-block:: python

  from poli_enum.currency import Currency
  Currency.EUR.value == 34

You can get the currency symbol:

.. code-block:: python

  from poli_enum.currency import Currency
  Currency.EUR.symbol == '€'
  Currency.PHP.symbol == '₱'
  f'Cost: 54{Currency.EUR:s}' == 'Cost: 54€'

Symbol
------
.. code-block:: python

  from poli_enum.currency import Symbol
  Symbol.GBP.value == '£'

Layouts
=======
Keyboard layout codes. From Debian 9 */usr/share/X11/xkb/rules/evdev.lst*.

.. code-block:: python

  from poli_enum.layout import Layout
  Layout.US.value == 'English (US)'
  Layout.BRAI.value == 'Braille'

Testing
*******
1. ``git clone`` this project.
2. Execute ``python setup.py test`` in the project folder.

Contributing
************
Is a missing or wrong code? Say it in the issues! Feel free to contribute.
