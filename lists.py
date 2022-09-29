#The list num_customers contains the number of customers who came into your restaurant every day over the last month (which lasted thirty days).
#Fill in values for each of the following:

#avg_first_seven - average number of customers who visited in the first seven days
#avg_last_seven - average number of customers who visited in the last seven days
#max_month - number of customers on the day that got the most customers in the last month
#min_month - number of customers on the day that got the least customers in the last month

num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7]) / 7 
avg_last_seven = sum(num_customers[-7:]) / 7 
max_month = max(num_customers)
min_month = min(num_customers)

#Create two Python lists:

# DO not change: Define two Python strings
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

# TODO: Convert strings into Python lists
letters = alphabet.split(".")
formatted_address = address.split(",")



#Use this list comprehension to define a function percentage_liked() that takes one argument as input:

#ratings: list of ratings that people gave to a movie, where each rating is a number between 1-5, inclusive
#We say someone liked the movie, if they gave a rating of either 4 or 5. Your function should return the percentage of people who liked the movie.
#For instance, if we supply a value of [1, 2, 3, 4, 5, 4, 5, 1], then 50% (4/8) of the people liked the movie, and the function should return 0.5.
#Part of the function has already been completed for you. You need only use list_liked to calculate percentage_liked

def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked) / len(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])