"""
mamy ulice z latarniamy wlaczonymi i wylaczonymi
mamy ich indeksy, latarnie sa w rownych odleglosicach
chcemy najdluzszy ciag wl i wyl (oraz wlaczac i wyl chyba)

drzewo przedzialowe - z wykladu
w kazdym nodzie pamietamy ile zapalonych
w lisciach sa poszczegolne latarnie

jesli wszystkie nie sa zapalone to schodzimy lewym podd i szukamy max ciagu
jesli 0 to nie ma polaczenia miedzy ciagami
chyba z nastepnikami cos

max ze srodka lewego i prawego?

O(logn)
"""