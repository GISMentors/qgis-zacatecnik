************************
Práce s vektorovými daty
************************

V systému QGIS lze pracovat s různými formáty vektorových dat. 
Vektorová data se standardně dělí dle typu geometrie na bodové, liniové a plošné.
To jakým způsobem se data ukládají a co daný způsob přináší za možnosti se může velice lišit.

QGIS s daty pracuje v jejich původním formátu a nepřevádí je. Převod do jiných formátů je možný pomocí knihovny nástrojů.

Pro převod mezi formáty se používá knihovna `GDAL <http://gdal.org/>`_.  
`Zde <http://gdal.org/ogr_formats.html>`_ je dostupný seznam podporovaných vektorových formátů i s doplňujícími informacemi.



.. toctree::
   :maxdepth: 2

   vektor_data_prace.rst
   edit.rst
   import_delim.rst
   join.rst
   atr_dotaz.rst
   buffer.rst
   prekryv.rst



   


