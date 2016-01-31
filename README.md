---
title: How many first-names can be spelt with Elements?
author: James Scott-Brown
---

I was recently in a pub, and saw a sign in which beer was written as **BeEr** in the style of the **BrBa** *Breaking Bad* logo.

This led to a question: if you were naming a child, how much would your choice be limited if you eliminated all names that could not be spelt using the symbols of chemical elements?

The names of most of those present would be excluded, so we concluded it was probably quite a severe restriction.

This document quantifies it some more.

## Results

![Proportion of names that can be spelt using elemental symbols. ](elemental-names.pdf)

Of the 4275 most common *female first names* reported in the 1990 US census (``girl-names``), 710 (16.6%) can be spelt using chemical symbols.

The following can be spelt in more than 2 ways:

    5 SINDy
    4 PrINCEsS
    4 NICOLa
    4 CONCePTiON
    4 CAtHErIN
    4 CAsSIDy
    4 CAsSI
    4 BIBI
    3 WINONa
    3 WINDy
    3 VINITa
    3 OSCAr
    3 INEs
    3 HSIU
    3 GeNEsIS
    3 FRaNCISCO
    3 CINDy
    3 CAtHErN
    3 BErNITa
    3 BErNICe


Of the 1219 most common *male first names* reported in the 1990 US census (``boy-names``), 195 (16.0%) can be spelt using chemical symbols.

The following can be spelt in more than 2 ways:

    5 FRaNCEsCO
    4 NICOLaS
    4 NICHOLaS
    4 BRuNO
    3 RuBIN
    3 OSCAr
    3 FRaNCISCO


## Files

Inputs are:

* ``elements.py`` is a script that accepts a list of words (one per line) on STDIN, or a single word as an argument, and for each word returns a list of possible ways it could be spelt using elemental symbols.
* ``Makefile`` 
* ``plotNames.R``
* ``README.md``

Running ``make analysis`` produces the folowing files:

* ``girl-names`` and ``boy-names`` are lists of names
* ``girl-names-elemental`` and ``boy-names-elemental`` are lists of names that can be spelt using elemental symbols, spelt in all possible ways
* ``girl-names-counted`` and ``boy-names-counted`` are lists of names that can be spelt using elemental symbols, spelt in all possible ways

The R script ``plotNames.R`` produces ``elemental-names.pdf``. 

Running ``make report`` produces ``README.pdf``
