.. |mActionAddRasterLayer| image:: ../images/icon/mActionAddRasterLayer.png
   :width: 1.5em

***********************
Práce s rastrovými daty
***********************

Rastrová data reprezentují objekty a jevy rozdělením prostoru do matice
diskrétních buněk (pixelů). Tyto jsou součástí pravidelné mřížky (gridu),
přičemž každá z buněk gridu má hodnotu, která reprezentuje jednu vlastnost
charakteristickou pro dané místo. Většinou se jedná o spojité jevy, jakým je
například nadmořská výška reliéfu, teplota ovzduší či letecké a satelitní
snímky.

Tato část školení popisuje jak pracovat s takovýmito daty v prostředí
QGIS. Ten totiž podporuje množství rozličných rastrových formátů, díky
knihovně GDAL. Seznam podporovaných rastrových formátů i s
doplňujícími informacemi je dostupný na `stránce projektu
<http://gdal.org/formats_list.html>`_.

.. toctree::
   :maxdepth: 2

   rastr_import
   rastr_export
   rastr_vlastnosti
   rastr_terenni_analyzy
   rastr_kalkulator
   vrstevnice
