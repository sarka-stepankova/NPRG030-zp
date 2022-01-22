# Hra 2048

Zápočtový program na předmět Programování I v Pythonu, ZS 2021/22. Jedná se o hru 2048 s grafickým rozhraním v Tkinteru.

## Návod ke spuštění

Hra začne běžet po spuštění souboru `main.py`. Je potřeba mít nainstalovanou knihovnu Tkinter.

Pro tahy ve hře můžete využívat *klávesy s šipkami*, nebo klávesy *W, A, S, D*. 

## Pravidla hry

**Hra 2048** je desková hra, v níž ovládáte dlaždice umístěné na hrací pole 4x4. Dlaždice na sobě mají číslo, kterým je vždy nějaká mocnina 2. Na začátku hry je na ploše umístěná jen jedna dlaždice, ale po každém tahu je na nějaké volné místo na ploše umístěna nová dlaždice s číslem 2 nebo 4 (pravděpodobnost čísla 2 je mnohem vyšší, než čísla 4).

Hráč může v každém tahu ovlivnit stav hry (hrací plochy) jedním za čtyř tahů: *nahoru, dolů, doleva, doprava*. Výsledkem povelu je "sesypání" dlaždic na požadovanou stranu. Při tomto sesypání se každé 2 dlaždice se stejnou hodnotou spojí do jedné s hodnotou součtu dlaždic (dvojnásobkem jedné původní).

**Cílem hry** je dosáhnout stavu, kdy se na ploše vyskytne *dlaždice s číslem 2048*. Hráč prohrává ve chvíli, kdy je celá plocha zaplněná dlaždicemi a *neexistuje žádný tah* (tzn. nejsou 2 stejná políčka horizontálně nebo vertikálně vedle sebe).

## Programátorská část

### Použité knihovny

Pro program jsem použila 2 knihovny, bez kterých by funkčnost programu nebyla možná. Jedná se o:

* **Tkinter** - pro snadnější vytvoření grafického rozhraní,
* **Random** - díky knihovně Random jsou vybírány náhodné pozice umístění nových políček a jejich hodnoty.

### Návrh

Kód je rozdělený na dvě části. Jedna řeší herní logiku, druhá grafické rozhraní. Nejprve jsem naprogramovala část s logickými funkcemi a zprovoznila hru v terminálu, potom jsem přidala funkce řešící vykreslení hry v Tkinteru.

### Funkce

Většina herních fuknkcí je okomentovaná v kódu a měla by být srozumitelná.

Za podrobnější rozbor asi stojí funkce *mergeNoodle()*. Ta počítá s tím, že hra má pole neměnné velikosti (4x4), proto na vstupu dostane 4 čísla z políček z jednoho řádku/sloupce. Funkce vždy smrskává čísla k n1 (první zadané hodnotě). Nejdřív si funkce nastrká nenulová čísla do proměnných co nejblíž k n1 (tedy např. vstup 4,0,4,4 -> 4,4,4,0), pak postupně porovnává dvojice od n1 a když narazí na stejná čísla, tak je smrkne do jednoho dvojnásobně většího (-> 8,0,4,0), pak je ještě potřeba znovu přeuspořádat nenulová čísla k n1 (-> 8,4,0,0). Tuhle funkci pak dál využívají funkce up(), down(), left(), right().

## Zásluhy
Paleta barev byla převzata ze stránky flatuicolors.com (https://flatuicolors.com/).