@CS535 - Data Mining
@Project: Implementation of the Recommender Systems
@Author: Namrata Bajpai
@Date: 11th Dec, 2015

Project Description:

Implementation of the Recommender Systems where we have m different users and 
n different users for a specific application(Examples of such systems include 
the Movie Recommender System ,any E-Commerce application) where say a user i may
give an item j a rating value of k based on the user preference,
	 where i belongs to [1,...,m]
		   j belongs to [1,...,n]
		   k belongs to [1,...,k].
The user preference rating data is represented as a matrix of n x m where the 
matrix values are the ratings given by the users.

Initially all the matrix values are represented by zeros. This matrix is further 
loaded with the user ratings read from an input file provided by the user.
Using the collaborative filtering with the use of the Pearson coefficient to find
the similarity between the ratings of the users the items for which the ratings is
0 is predicted. In short, user-to-user collaborative filtering is used to perform
the rating prediction.

How to compile and execute the code:

The code is designed using Python language.
In the Python IDE(you can either use the linux command shell with python installed
or any Python IDE which includes Enthought Canopy,etc)
You can directly execute the python code with the run option provided in the IDE.
or 
If you are using the command shell you can use the below command to execute your python code,
python path/to/the/file_name.py
Make sure you add #!/bin/sh to the code if you are running through the linux or unix command shell.
I havent added it as i used the Python IDE "Enthought Canopy" interface for my execution.

The program makes use of the following libraries numpy, math, time. Make sure you have it 
installed.

Sample Input:
After you execute the program the programs prompts you to provide the complete path of your
input file, teh number of users and the number of items in your system,
Please enter the file name with its complete path
C:\Users\Namrata\Desktop\Python Project\train_all_txt.txt

Please enter the number of users
943

Please enter the number of items
1682
Processing user: 1
Processing user: 2
Processing user: 3
...
This way it makes the predictions and provide the missing values. It generates a matrix with the
ratings available for all the items against all the users.

The output file final_output.txt shows all the output of the recommender system code.

NOTE: In case of the cold start problem, where for an item say j no user has given any rating we calculate 
the mean of the ratings the user gave to the other items and assign that value for the item j.

Make sure you have your input file in the same folder as of your python code file.
If you are using the Python IDE then the output file will be generated in your workspace for that IDE.