analysis:
	# See https://stackoverflow.com/questions/1803628/raw-list-of-person-names
	curl http://deron.meranda.us/data/census-dist-female-first.txt |    awk '{print $$1}' > girl-names
	curl http://deron.meranda.us/data/census-dist-male-first.txt | awk '{print $$1}' > boy-names

	cat girl-names | ./elements.py > girl-names-elemental

	cat girl-names-elemental |
	sort -f  | # sort ignoring case
	uniq -ci | # count unique rows, ignoring case
	sort -r  | # sort in descending order
	tail -n +2 | # remove initial line (total count)
	sed "s/^[ \t]*//" > girl-names-elemental-counted # remove initial whitespace


	cat boy-names  | ./elements.py > boy-names-elemental

	cat boy-names-elemental |
	sort -f  | # sort ignoring case
	uniq -ci | # count unique rows, ignoring case
	sort -r  | # sort in descending order
	tail -n +2 | # remove initial line (total count)
	sed "s/^[ \t]*//" > boy-names-elemental-counted # remove initial whitespace

report:
	pandoc -o README.pdf README.md