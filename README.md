# GeoStrat

The aim of this project is to find the perfect location for a company in the gaming industry, given the following requirements: 

    - Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
    - 30% of the company have at least 1 child.
    - Developers like to be near successful tech startups that have raised at least 1 Million dollars.
    - Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
    - Account managers need to travel a lot
    - All people in the company have between 25 and 40 years, give them some place to go to party.
    - Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
    - The CEO is Vegan

For this purpose we should start working with a given .csv, with near 19K companies and their coordinates.
First of all, I imported the .csv to Mongodb in order to be able to filter it according to the requirements. 

In total I managed to do a couple of big queries in which the first, I could make a new collection while in the second one I just adjusted the filter in order to finally have a manageable number of 99 companies.

Once I had those, I could start doing the requests to the API I would use for this project, which is the Google Places API. Using this one I could get the location of the starbucks, nightclubs and pubs, schools and kindergarten, and vegetarian restaurant, all around the 99 companies. Woth the mention, I created a collection in Mongodb for every of these new entries. 

To get those airports closer to the preffered 99 companies, I used a .csv with 55K airports all around the world. However, I could filter these, using a Mongodb query, by large_airports, reducing the number of total airports to 614. 

In order to get the perfect location and while using geoqueries in PyMongo, I could get the number of starbucks, nightclubs, schools, vegetarian restaurants and airports around my company, adding this information to a dataframe. 
I did also use the Harversine function, since it takes a couple of coordinates and return the distance in between, it helped to conclude which of the 99 companies have an airport the closest.

By this point, I got a dataframe with 99 rows, and a column for the different requirements and distances. Once I had this, I calculated a weighing table regarding the number of employees in the company who wanted each of the requirements. Using the table below, I could get a dataframe with a total column, which I used to sort this dataframe and get the 5 preferred companies and locations. 

 	  num 	wot 	              they want 	        weighing
0 	20 	Designers 	          Design companies 	  0.229885
1 	5 	UI/UX Engineers 	    Post-its 	          0.057471
2 	10 	Frontend Developers 	Startups 1M$ 	      0.114943
3 	15 	Data Engineers 	      Projects 	          0.172414
4 	5 	Backend Developers 	  Startups 1M$ 	      0.057471
5 	20 	Account Managers 	    airport 	          0.229885
6 	1 	Maintenance guy 	    Basketball 	        0.011494
7 	10 	Executives 	          starbucks 	        0.114943
8 	1 	CEO 	                veggies 	          0.011494
9 	26 	Parents 	            schools 	          0.300000
10 	87 	All 	                party 	            1.000000

Getting the highest punctuation, 81 points, I could get the perfect location which is: 

Social Gaming Network - 431 Florence Street, Palo Alto, CA 94301

Same industry enterprise, 100 employees, and they are not locate there anymore. Well, I couldn not find the enterprise Social Gaming Network in Google, and nowadays if you are not in Google, you don't exist. What an opportunity!

If you would like to have a look of the area and see what I have told you with your own eyes, you can do it checking <map_paloalto.html> in the OUTPUT folder. 

Hope you like it!

Clara


