
import os;
import json; #Because why do more work than needed?
import sys;
class Sortable_Solver:
		#Pythons version of a HashTable= Dictionary


		#Takes the Json Title as Key, enters a List of Listings as value
		dictionary_Listings = {};



		def __init__(self, path_Products, path_Listings, path_Results="results.txt"):
			#Step 1: Take in our Listings and form a HashTable
			#Why: Because each product will need to be cross checked with Listings
			#It will then need to be stored/recorded in the results file
			
			if(not self.IsValidPath(path_Products)):
				print("File not found:"+ path_Products);
				return;

			if(not self.IsValidPath(path_Products)):
				print("File not found:"+ path_Listings);
				return;				

			self.Setup_Listings(path_Listings);
			self.CrossCheck(path_Products, path_Results);

		def IsValidPath(self,path):
			return os.path.isfile(path);

		def Setup_Listings(self, path_Listings):
			#Both files exist now to Parse the input File and setup the Dictionary
			# pFile =open(path_Listings,'r') 

			# row = pFile.readlines()
			# #For each line in Row parse the JSON into a Listing Object
			# for line in row:
			# 	print(line);
			# 	listing = json.loads(line);
			# 	print(listing);

			#Force Encoding to UTF-8 to avoid Ascii undefined errors due to weird symbol use
			with open(path_Listings,'r',encoding="UTF-8") as f:
				#in the event the Text file contains corrupt lines a re-read is needed
				for line in f:
					listing = json.loads(line)

					#Format Titles for easier CrossReferencing later.
					listing['title']=self.Format_String(listing['title'],'_',' ');
					listing['title']=self.Format_String(listing['title'],'-',' ');
					listing['title']=listing['title'].upper();

					#if our dictionary has an entry for this Key
					if ( listing['manufacturer'] in self.dictionary_Listings ):
						#Do nothing
						# print("Key Exists")

						#This title already exists so just append the new listing to it.
						self.dictionary_Listings[ listing['manufacturer']].append(listing);
						
					else:
						#create a List
						listing_List =[]
						listing_List.append(listing);
						# self.dictionary_Listings = { (str)(listing['title']), listing_List};
						self.dictionary_Listings[ listing['manufacturer']] = listing_List


		def CrossCheck(self, path_Products, resultsFile):

			#This is used to avoid rechecking duplcates
			duplicate_Checker={}

			#Clear Contents
			f_Results = open(resultsFile, 'w')
			f_Results.close()

			#Append Contents
			f_Results = open(resultsFile, 'a')

			with open(path_Products,'r',encoding="UTF-8") as f:
				#in the event the Text file contains corrupt lines a re-read is needed
				for line in f:
					product = json.loads(line);

					if(product['product_name'] in duplicate_Checker):
						continue; #We already analyzed this product, therefore we can skip it.
					else:
						duplicate_Checker[product['product_name']]=True; #This is an arbitrary value used to optimize via dictionary
																		 #Hashmap

					result_ListingMatch = []

					#First Grab the List of Listings from Manufacterer

					#Incase the manufacturer has no listings
					if( product['manufacturer'] in self.dictionary_Listings):
						manufacturer_Listing = self.dictionary_Listings[ product['manufacturer']];


						#Now we can perform a check if any of the titles contains our products full name as a
						#substring

						#Some items have various formatting, therefore simply convert the names to match
						name= self.Format_String(product['product_name'],'_',' ');
						name= self.Format_String(name,'-',' ');
						name=name.upper();

						#Create a List to store the matching Listings

						for item in manufacturer_Listing:
							if (item['title'].find(name) != -1):
								result_ListingMatch.append(item) #Add the Json Object as it matches both manufacterer and name


					json_Result = {
						"product_name": name,
						"listings": result_ListingMatch
					}

					f_Results.write( json.dumps(json_Result)+"\n")
			f_Results.close();	


		def Format_String(self, _string, char_LookFor, char_Replace):
			newString=""
			for c in _string:
				if(c == char_LookFor):
					newString+= char_Replace;
				else:
					newString+=c;
			return newString;

print("\n\nRunning SortableSolver....");

#This class uses 3 Arguments
#Argument one: The path to Products.txt
#Arg two : The path to Listings.Txt

if (len(sys.argv)<3):
	print ("Error: Please run script with arguments to both Products & Listings txt files.");
	print ("Ex: python Solver.py ./Path1.txt ./Path2.txt")


#Alright 2 arguments were passed Lets Rock and Roll!
elif(len(sys.argv)<4):
	Sortable_Solver(sys.argv[1], sys.argv[2]);
elif(len(sys.argv)<5):
	Sortable_Solver(sys.argv[1], sys.argv[2],sys.argv[3]);

print("\n");