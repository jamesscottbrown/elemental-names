#!/usr/bin/env python
import sys

elements = ["Ac", "Ag", "Al", "Am", "Ar", "As", "At", "Au", "B", "Ba", "Be", "Bh", "Bi", 
  "Bk", "Br", "C", "Ca", "Cd", "Ce", "Cf", "Cl", "Cm", "Co", "Cn", "Cr", "Cs", "Cu", "Db", 
  "Ds", "Dy", "Er", "Es", "Eu", "F", "Fe", "Fm", "Fr", "Ga", "Gd", "Ge", "H", "He", "Hf", 
  "Hg", "Ho", "Hs", "I", "In", "Ir", "K", "Kr", "La", "Li", "Lr", "Lu", "Md", "Mg", "Mn",
  "Mo", "Mt", "N", "Na", "Nb", "Nd", "Ne", "Ni", "No", "Np", "O", "Os", "P", "Pa", "Pb", 
  "Pd", "Pm", "Po", "Pr", "Pt", "Pu", "Ra", "Rb", "Re", "Rf", "Rg", "Rh", "Rn", "Ru", "S", 
  "Sb", "Sc", "Se", "Sg", "Si", "Sm", "Sn", "Sr", "Ta", "Tb", "Tc", "Te", "Th", "Ti", "Tl", 
  "Tm", "U", "Uuh", "Uun", "Uuo", "Uup", "Uuq", "Uus", "Uut", "Uuu", "V", "W", "Xe", "Y", 
  "Yb", "Zn", "Zr"]

def spell(spelt, toSpell, start):
	toSpell = toSpell.lower()

	if len(toSpell) == 0:
		return spelt + "\n"

	for i in range(start, len(elements)):
		element = elements[i]

		if toSpell.find(element.lower()) == 0:
			# This element matches

			# Try to finish spelling the word using it
			sol1 = spell(spelt + element, toSpell[len(element):], 0)
			if not sol1: sol1 = ""

			# Try looking for an alternative element to use here
			sol2 = spell(spelt, toSpell, i + 1)
			if not sol2: sol2 = ""

			return sol1 + sol2

def main():
	if len(sys.argv) > 1:
		result = spell("", sys.argv[1], 0)
		if result: print result
	else:
		for line in sys.stdin:
			result = spell("", line.strip(), 0)
			if result: print result

if __name__ == '__main__': main()
