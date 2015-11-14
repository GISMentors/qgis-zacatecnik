****
Úvod
****

.. only:: html

   .. image:: images/intro_logo.png
      :width: 140px
      :align: left

.. index::
   single: GIS
   single: geografický informační systém

`QGIS <http://qgis.org/en/site/>`_  je Open Source *geografický informační systém*
(:wikipedia:`GIS`) publikovaný pod všeobecnou licencí GNU GPL.
Projekt QGIS vznikl v roce 2002, verze s označením 1.0 vyšla však v roce 2009.
Mezi hlavní výhody patří zejména rychlost vývoje a rozšiřování jeho funkcionality.
Tato licence umožňuje používání software i na komerční účely, ale umožňuje i modifikaci zdrojového kódu a jeho následné šíření.

Současným konceptem ve vývoji je pravidelné a intenzivní publikování nových verzí.
Dlouhodobá stabilní verze je doplěna dvěma krátkodobými verzemi.



.. only:: html

.. tip::

      Text školení je dostupný i v tisknutelné formě `PDF
      <./skoleni-qgis-zacatecnik.pdf>`_.
   
.. warning:: :red:`Toto je pracovní verze školení, která je aktuálně ve vývoji!`

.. important:: Školení je zaměřeno na aktuální verzi `QGIS 2.8 Wien
               <https://www.qgis.org/en/site/forusers/download.html>`_. V
               jiných verzích není zaručena funkčnost uvedených příkladů. Dále
               předpokládáme zapnutou *anglickou lokalizaci*, viz
               :ref:`volba lokalizace <volba-lokalizace>`.



QGIS je psán v programovacím jazyce C++ a uživatelské prostředí je naprogramováno
pomocí knihovny Qt. Díky použití těchto rozšířených programovacích prostředků je
QGIS multiplatformní, tudíž jej lze využívat na většině používaných operačních
systémech jako je Windows, Linux nebo OS X. QGIS využívá pro práci s prostorovýmy
daty knihovnu GDAL pro rastrová data a OGR pro vektorová data, díky tomu je možné
v QGISu pracovat se širokým spektrem OGC, ale i jiných formátů.

.. figure:: images/intro_qgis.png

   Ukázka uživatelského rozhraní QGIS

Program nabízí přehledné uživatelské prostředí. Uživatel má k dispozici širokou
škálu nástrojů pro prohlížení, modifikaci a export dat.
Od verze 2.0 QGIS obsahuje \"Print Composer\", tedy nástroj pro vytváření map.
V tiskovém modulu lze vytvářet z nahraných dat výstupy se všemy kartografickými
náležitostmi. Výsledky je možné exportovat do pdf, nebo obrázku.

.. figure:: images/intro_map.png

   Ukázka mapového výstupu vytvořeného v QGIS

QGIS je populární i pro svou rozšiřitelnost pomocí takzvaných \"pluginů\".
Pluginy jsou dílčí nástroje, které jsou vyvíjeny komunitou kolem QGIS.
Pomocí pluginů je možné vložit pod data v mapovém okně mapové podklady Google,
Bing nebo Open Street Map. Pro připojení k WFS poskytovaným ČÚZK je možné použít
plugin \"WFS 2.0\" a pro prohlížení souborů vfk slouží plugin
`VFK <http://freegis.fsv.cvut.cz/gwiki/VFK_/_QGIS_plugin>`_.

.. figure:: images/intro_vfk.png

   Ukázka práce s katastrálními daty v QGIS

.. only:: html
             
   #####   
   Obsah
   #####

.. toctree::
   :maxdepth: 2

   intro/index
   vektorova_data/index
   rastrova_data/index
   webove_sluzby/index
   mapovy_vystup/index
   ruzne/index

*******
Dodatky
*******

O dokumentu
===========

Text dokumentu je licencován pod `Creative Commons
Attribution-ShareAlike 4.0 International License
<http://creativecommons.org/licenses/by-sa/4.0/>`_.

.. figure:: images/cc-by-sa.png 
   :width: 130px
   :scale-latex: 120
              
*Verze textu dokumentu:* |release| (sestaveno |today|)

Autoři
------

Za `GISMentors <http://www.gismentors.cz/>`_:

* `Oto Kaláb <http://www.gismentors.cz/mentors/kalab/>`_ 
* `Alžbeta Gardoňová <http://www.gismentors.cz/mentors/gardonova/>`_
*  Ľudmila Furtkevičová
* `Vojtěch Dubrovský <http://www.gismentors.cz/mentors/dubrovsky/>`_

Text dokumentu
--------------

.. only:: latex

   Online HTML verze textu školení je dostupná na adrese:

   * http://training.gismentors.eu/qgis-zacatecnik/

Zdrojové texty školení jsou dostupné na adrese:

* https://github.com/GISMentors/qgis-zacatecnik


