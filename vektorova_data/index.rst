************************
Práce s vektorovými daty
************************

V systému QGIS lze pracovat s různými formáty vektorových dat.
Vektorová data se standardně dělí dle typu geometrie na bodové,
liniové a plošné.  To jakým způsobem se data ukládají a co daný způsob
přináší za možnosti se může velice lišit.

QGIS s daty pracuje v jejich původním formátu a nepřevádí je. Převod
do jiných formátů je možný pomocí knihovny nástrojů.

Pro převod mezi formáty se používá knihovna `GDAL
<http://gdal.org/>`_.  Seznam podporovaných vektorových formátů i s
doplňujícími informacemi je dostupný na `stránce projektu
<http://gdal.org/ogr_formats.html>`_.

.. toctree::
   :maxdepth: 2
   
   vektor_import.rst
   vektor_data_prace.rst
   editace.rst
   import_delim.rst
   join.rst
   dotazovani.rst
   prostorove_analyzy.rst



   


