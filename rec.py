import numpy as np
import math
import time
from collections import OrderedDict
from operator import itemgetter

def pearson(user1, user2):
    """
    This method calculates the pearson coefficient between user1 and user2
    for the items that are rated by both the users1.

    :param user1: array containing rating values by user1
    :param user2: array containing rating values by user2
    :return: the pearson coefficient value between two users.
    """

    #calculate the mean for user1 and user2 for common rated items
    sum_u1 = 0
    sum_u2 = 0
    n = 0
    for i in range(len(user1)):
        if user1[i] != 0 and user2[i] != 0:
            sum_u1 += user1[i]
            sum_u2 += user2[i]
            n += 1

    #incase the users have rated no common items
    if n ==0:
        return 0.0

    mean_u1 = float(sum_u1)/n
    mean_u2 = float(sum_u2)/n

    num = 0
    dem1 = 0
    dem2 = 0
    for i in range(len(user1)):
        if user1[i] != 0 and user2[i] != 0:
            #print user1[i],mean_u1,user2[i],mean_u2
            num += (user1[i]-mean_u1)*(user2[i]-mean_u2)
            dem1 += math.pow((user1[i]-mean_u1),2)
            dem2 += math.pow((user2[i]-mean_u2),2)
    #print num,dem1,dem2,n
    if dem1 == 0.0 or dem2 == 0.0:
        return 0.0
        
    
    sim = (float(num)/math.sqrt(dem1))/math.sqrt(dem2)
    #print num,dem1,math.sqrt(dem1),dem2,math.sqrt(dem2),sim
    return sim

def main():

    #start_time = time.time()
    fname = raw_input("Please enter the file name with its complete path\n")
    no_of_users = int(raw_input("Please enter the number of users\n"))
    no_of_items = int(raw_input("Please enter the number of items\n"))
    matrix = np.zeros((no_of_users,no_of_items),dtype=int)
    with open(fname) as f:
        for line in f:
            user,movie,rating = line.split()
            matrix[int(user)-1][int(movie)-1] = int(rating)


    matrix1 = np.copy(matrix)
    file = open("final_output.txt","w")

    for i in range(len(matrix)):
        #calculating mean rating of user i
        sum_i = 0
        n_i = 0
        for item in matrix[i]:
            if item != 0 :
                sum_i += item
                n_i += 1
        mean_i = float(sum_i)/n_i
        simi = {}  #map containing similarity values for each user i with each user j
        print "Processing user: "+str(i+1)
        for j in range(len(matrix)):
            simi[j] = pearson(matrix[i],matrix[j])
        simi = OrderedDict(sorted(simi.items(),key=itemgetter(1),reverse=True))
        #print simi
        #using weighted mean for predicting ratings where weights being the
        #similarity measures
        for k in range(0,len(matrix[i])):
            if(matrix[i][k] == 0):
                s1=0.0
                s2=0.0
                #ccount=0
                for elem in simi:
                    if matrix[elem][k] != 0 and simi[elem]>0.0: #and ccount<=100:
                        #print elem,simi[elem],matrix[elem][k]
                        s1 += simi[elem]*matrix[elem][k]
                        s2 += simi[elem]
                        #ccount = ccount + 1
                if s2!=0:
                    rat = s1/s2
                    #print s1,s2,rat
                    matrix1[i][k] = round(rat,0)
                else: #incase of cold start problem setting the value as the mean rating of user i
                    matrix1[i][k] = round(mean_i,0)
            
            file.write(str(i+1)+" "+str(k+1)+" "+str(matrix1[i][k])+"\n")
        #print mean_i,np.mean(matrix1[i,:])

    file.close()
    #print("--- %s min ---" % ((time.time() - start_time)/60))

if __name__ == "__main__":
    main()