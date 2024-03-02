bench:
	@echo "Running benchmarks..."
	@hyperfine --warmup 3 'tail test.txt'
	@hyperfine --warmup 3 'python tail.py test.txt'

test-data:
	@echo "Generating test.txt with 2^25 lines..."
	echo "yes we have no bananas" > test.txt
	for i in {1..25}; do cat test.txt test.txt > test2.txt && mv test2.txt test.txt; done

clean:
	rm -f *.txt

.PHONY: test-data bench clean
