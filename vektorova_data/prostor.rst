.. |checkbox| image:: ../images/icon/checkbox.png
   :width: 1.5em
.. |selectstring| image:: ../images/icon/selectstring.png
   :width: 1.5em

Prostorové analýzy
==================

V prostředí QGIS máme k dispozici širokou škálu funkcí pro prostorové analýzy 
vektorových dat. Základní funkce nalezneme v hlavním menu 
:menuselection:`Vektor --> Nástroje geoprocessingu`.

.. noteadvanced:: Další možností jak 
    spouštět analýzy je pomocí okna :item:`Nástroje zpracování`, které sdružuje 
    funkce z knihovny OGR/GDAL a dalších dostupných externích nástrojů jako jsou 
    například GRASS, SAGA nebo R. Jednotlivé funkce lze rychle vyhledávat 
    pomocí filtru v horní části oknu (nutno zadat anglický název funkce)

    .. figure:: images/geoprocess.png
       :scale: 70%
        
       Okno :item:`Nástroje zpracování` (Pokročilé zobrazení)


Obalová zóna (buffer)
---------------------

Jednou z nejzákladnějších prostorových analýz je obalová zóna. Obalové zńoy jsou
reprezentovány polygony s hranicí o dané vzdálenosti od prvků. U bodových 
prvků má obalová zóna tvar kruhu (nebo aproximace kruhu), u linií a polygonů se 
kružnice generují kolem uzlů. Cílem analýzy je tedy vytvořit novou polygonovou 
vrstvu obalových zónVytváření obalových zón nalezneme v menu 
:menuselection:`Vektor --> Nástroje geoprocessingu --> Obalové zóny...`


.. figure:: images/prost_buffer.png
    :scale: 90%
       
    Dialogové okno obalové zóny
    

- :item:`Vstupní vektorová vrsvta` |selectstring| - vstupní vrstva pro 
  vytvoření obalových zón
- |checkbox|:option:`Použít pouze vybrané prvky` - vytvoří obalovou zónu jen pro 
  prvky ve výběru
- :item:`Segmentů proaproximaci` |checkbox| - míra aproximace kruhu při tvorbě 
  obalové zóny (:num:`aprox`)
    
    - nízká hodnota (min. 5) - méně uzlů - rychlejší výpočty, ale méně přesné
    - vysoká hodnota (max. 99) - více uzlů - pomalejší výpočty, více odpovídá 
    kruhu 

.. _aprox:

.. figure:: images/prost_buffer_seg.png
    
    Obalová zóny s rozdílným počtem segmentů pro aproximaci 
    (vlevo 5, vpravo 50)

- |checkbox|:option:`Vzdálenost obalové zóny`  - vzdálenost v metrech 
  (v závislosti nastavení QGIS a použitého SRS)
- |checkbox|:option:`Pole vzdálenosti obalové zóny` - aktivujeme pokud máme v 
  atributové tabulce sloupec, ve kterém máme definovanou vzdálenost. Vhodné 
  pokud potřebujeme pro různé prvky různě velké obalové zóny (např. kategorie 
  vodních toků, nebo komunikací)
- |checkbox|:option:`Rozpustit výsledky obalové zóny` - zaškrtneme, pokud 
  nechceme aby se nám výsledné obalové zóny překrývaly, výsledkem analýzy je 
  jeden prvek.
- :item:`Vstupní vektorová vrsvta` - zadáme cestu a název výstupního souboru
- |checkbox|:option:`Přidat výsledek do mapového okna` - výsledná vrstva se 
  nahraje do projektu


V následujícím příkladu jsme vytvořili obalovou zónu 10 km kolem dálnic 
(s možností rozpuštění výsledků).

.. figure:: images/prost_buffer_dalnice.png
       
    Příklad obalové zóny 10 km okolo dálnic

Překryvné analýzy
-----------------

Další skupinou prostorových analýz jsou tzv. překryvné anlýzy. Princepem je 
interakce prvků jedné nebo více vektorových vrstvev. Pro dosažení 
správného výsledku je nutné aby vrstvy byly ve shodném souřadnicovém systému. 
Překryvné operace opět nalezneme v menu 
:menuselection:`Vektor --> Nástroje geoprocessingu -->`

.. todo:: popsat okno

.. todo:: uvézt příklady

Průsečík...
^^^^^^^^^^^

Sjednotit...
^^^^^^^^^^^^

Symetrický rozdíl...
^^^^^^^^^^^^^^^^^^^^

Ořezávač...
^^^^^^^^^^^

Rozdíl...
^^^^^^^^^

Rozpustit...
^^^^^^^^^^^^

