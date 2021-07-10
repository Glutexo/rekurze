# Faktoriál #

## Popis ##

[Faktoriál na Wikipedii](https://cs.wikipedia.org/wiki/Faktoriál)

Faktoriál kladného celého čísla _n_ je součin všech kladných celých čísel menších, nebo rovných n. Faktoriál čísla 0 je 1. Značí se _n!_.

> n! = n · (n − 1) · (n − 2) · … · 1
> 
> 5! = 5 · 4 · 3 · 2 · 1 = 120
>
> 1! = 1
> 
> 0! = 1

## Řešení bez rekurze ##

Potřebujeme funkci _factorial_, která přijme kladné číslo _n_, nebo 0 (nezáporné číslo _n_) a vrátí jeho faktoriál.

```python
def factorial(n):
    ...
```

Faktoriál můžeme implementovat jako cyklus. Ten číslo _n_ postupně vynásobí každým číslem o jednu menším, dokud nedojde k jedničce.

```python
def factorial(n):
    vysledek = n
    while n > 1:
        n -= 1
        vysledek *= n
    return vysledek
```

Tato implementace ještě postrádá ošetření případu, kdy _n_ je 0. V tomto případě nedochází k násobení, hodnota faktoriálu pro číslo _0_ je definována jako _1_.

```python
def factorial(n):
    if n == 0:
        return 1
    
    vysledek = n
    while n > 1:
       n -= 1
       vysledek *= n
    return vysledek
```

Toto je hotové řešení. Neošetřuje případy, kdy je na vstupu jiné než nezáporné celé číslo, ale to už není otázka faktoriálu.

```python
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(3)
6
```

## Rekurze ##

Faktoriál čísla _n_ je součinem všech čísel jemu menších, nebo rovných. Jinými slovy je to součin čísla _n_ a všech kladných čísel jemu menších, nebo též číslo _n_ vynásobené součinem všech kladných čísel jemu menších. Součin všech kladných menších čísel je sám totéž, co faktoriál čísla _n − 1_.

> 5! = 5 · **4 · 3 · 2 · 1 = 120**
>
> 4! = **4 · 3 · 2 · 1 = 120**
>
> 5! = 5 · 4!
> 
> …
> 
> 5! = 5 · 4 · 3 · 2 · 1!

Protože faktoriál čísla 0 je definován jako 1, platí dokonce:

> 5! = 5 · 4 · 3 · 2 · 1 · 0!
> 
> 5! = 5 · 4 · 3 · 2 · 1 · 1

## Řešení s rekurzí ##

Rekurzivně můžeme faktoriál zapsat přesně tak, jak je ukázáno na příkladu výše. Tedy jako číslo _n_ vynásobené faktoriálem čísla o jednu menšího.

```python
# ⚠️ POZOR, nekonečná smyčka!

def factorial(n):
    return n * factorial(n - 1)
```

Tento kód ovšem poběží donekonečna, neboť se nezastaví ve chvíli, kdy odečítání dojde k jedničce.

```python
def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)
```

Opět však ještě nemáme vyřešený případ, kdy _n_ je _0_. Pro číslo _0_ je výsledek předem daný.

```python
def factorial(n):
    if n in (0, 1):
        return 1
    
    return n * factorial(n - 1)
```

Toto je již plně funkční implementace, samozřejm opět bez ošetření případu, kdy _n_ není nezáporné celé číslo. Je však stále zbytečně složitá. Můžeme totiž využít předchozího poznání, že faktoriál čísla _1_ zůstane stejný i pokud jej vynásobíme faktoriálem čísla _0_. Jinými slovy, nemusíme ručně definovat hodnotu faktoriálu pro číslo 1 jako 1. Stačí, když ji, stejně jako ostatní čísla vynásobené faktoriálem čísla o jednu menší. Zde nuly, jež už svou hodnotu definovanou má.

> 1 · 0! = 1 · 1 = 1  

```python
def factorial(n):
    if n == 0:
        return 1
    
    return n * factorial(n - 1)
```

Co se zde děje? Zavoláme-li funkci _factorial_ s číslem 3, její návratovou hodnotou je `3 * factorial(2)`. Návratová hodnota `factorial(2)` je `2 * factorial(1)`. A opět, návratová hodnota `factorial(1)` je `1 * factorial(0)`. No a protože `factorial(0)` vždy vrací 1 a sebe sama již nevolá, běh funkce je u konce. `1 * 1`, `2 * 1`, `3 * 2`, výsledkem je 6.

```python
>>> factorial(3)
6
```

## Testy ##

```bash
$ pipenv run pytest factorial/test.py
```
