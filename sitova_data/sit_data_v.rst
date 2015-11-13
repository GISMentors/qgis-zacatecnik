Vektorová síťová data
=====================

Pro připojení síťových prostorových dat je připraven formát WFS. Správce WFS
vrstev se aktivuje buď ikonkou vlevo, nebo v záložce
:menuselection:`Vrstva --> Přidat vrstvu --> Přidat vrstvu WFS` [obr 13].

.. figure:: images/qgis_ogc_addwfs_icons.png
	    
   Obr 13

Okno správce [obr 14] umožňuje přidání, odebrání služby nebo slouží k výběru
vrstev.


.. figure:: images/qgis_ogc_addwfs_manager.png

   Obr 14

Formulář přidání nové služby se aktivuje tlačítkem :item:`Nové`. Ve formuláři [obr 15]
stačí v případě nezaheslované služby vyplnit pouze URL a pojmenování služby.
V případě zaheslované služby jsou vyžadovány přihlašovací údaje.

.. figure:: images/qgis_ogc_addwfs_add.png

   Obr 15

Po potvrzení a připojení ke službě ze správce tlačítkem :item:`Připojit` se zobrazí
poskytované vrstvy WFS serverem [obr 16]. Tak jako v případě WMS lze změnit
souřadnicový systém sloužící ke stahování dat. Změna se provádí pod tlačítkem
:item:`změnit` ve spodní pravé části. Výběr více vrstev pro přidání lze uskutečnit
pomocí klávesy :kbd:`CTRL`. Potvrzením :item:`ok` proběhne přidání vrstev do mapy.



.. figure:: images/qgis_ogc_addwfs_choose.png

   Obr 16
   
Vkládání síťových dat pomocí panele prohlížeče
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Obdobně jako u lokálních dat lze dvojitým kliknutím nebo přetažením z datového katalogu (prohlížeče) přidat do projektu také síťové služby. Pomocí datového katalogu můžeme pomocí kontextového menu také editovat stávající připojení nebo vytvářet nová [obr 17].

.. figure:: images/qgis_ogc_addwms_browser.png

    Obr 17
