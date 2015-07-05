# Sortable_Challange
The Coding Challange via Sortable


The program takes 2 arguments along with an optional one.

Arg1 = Path to products.txt
Arg2 = Path to listings.txt
ARg3 (optiona) = Path to Results.txt, it will create a a literal results.txt if no path/file is supplied.


To Run:
ex1.
	python Solver.py ./challenge_data_20110429/products.txt ./challenge_data_20110429/listings.txt 
ex2.
	python Solver.py ./challenge_data_20110429/products.txt ./challenge_data_20110429/listings.txt myresults.txt


The code matches results by formatting input wihin reasonable limits, and then matching via the datastructs used.

Process:
1. Create a Dictionary/Hashtable to store lists of listings using the Manufacterer as Key
2. Format the Listing "Title", and Product "Name" to convert lowercase to uppercase, and replace '-' & '_' with ' ' for consistency.

3. For each product in products.txt check if this product has already been analyzed (By crossreferencing a temp Dictionary)
	this speeds up calculation by ignoring duplicate products.
4. For each Manufacterer match from Products, to Listing, check if the Products "Name" exists as a substring within the ManufactererList's "Title".

Some items miss such as cases where the Product name is passed as:
	Canon-IXUS-310HS  which formats to : CANON IXUS 310HS
but in listing its stored as: 			 CANON IXUS 310 HS
                                                       ^ Note the space.

Additional Formatting can be supplied for consistency but then I would be making more assumptions than
I am confortable with when analyzing a large data pool, this simple script should not record false positives,
but it may miss a few due to irregularities as noted above.


