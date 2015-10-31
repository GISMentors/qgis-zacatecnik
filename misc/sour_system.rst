.. |set_crs| image:: ../images/icon/mActionSetProjection.png
   :width: 1.5em

Souřadnicový systém
-------------------
Definice  souřadnicového systému, kartografického zobrazení a příbuzných tém je detailně popsáno v podkladech školení `Open Source GIS <http://training.gismentors.eu/open-source-gis/soursystemy/index.html>`_ .

.. _sour-system:

Souřadnicový systém projektu
============================
Po instalaci je nastaven souřadnicový systém projeku na *WGS 84*.
Pokud budete pracovat s daty pro území ČR, tak je pravděpodobné, že budou v souřadnicovém systému s EPSG 5514. 
Pro další práci je vhodné nastavit souřadnicový systém projektu, aby se systém pokaždé otevřel s požadovaným nastavením.

Toto nastavení je v :menuselection:`Settings --> Options...` záložka :item:`CRS`. V části *Default CRS for new projects* je položka *Always start new projects with following CRS*.

    .. figure:: images/set_crs.png
       :class: large
       :scale-latex: 80
 
       Menu pro nastavení CRS projektu.

Přez ikonku |set_crs| se vyvolá menu pro výběr souřadnicového výběru. Konkrétní souřadnicový systém je možné vybrat z nabídky, nebo použít filtrovací pole pro rychlejší vyhledání. Filtrovat lze pomocí EPSG kódu, nebo také dle názvu systému.

    .. figure:: images/choose_crs.png
 
       Okno pro výběr CRS.

    .. important:: Takováto změna se projeví při dalším spuštění systému.
    
.. _sour-system-vrstvy:

Souřadnicový systém nové vrstvy
===============================
Pokud budete vytvářet novou vrstvu, nebo přidávat novou vrstvu bez definovaného souř. systému, tak je možné určit jim předdefinovaný souřadnicový systém.

Toto nastavení je dostupné v :menuselection:`Settings --> Options...` záložka :item:`CRS` v části :item:`CRS for new layers`.
Lze zvolit konkrétní souřadnicový systém (stejný postup jako u :ref:`projektu <sour-system>`), vynutit si pokaždé dotaz pro adání nebo vztáhnout nastavení k aktuálnímu projektu.
