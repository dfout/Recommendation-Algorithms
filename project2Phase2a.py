import copy
import random as rd
import numpy as np
import math

def createUserList():
    fusers = open("u.user", "r")

    userList = []
    for line in fusers:
        userInfo = line.strip().split("|")
        userList.append({"age": int(userInfo[1]), "gender": userInfo[2], "occupation": userInfo[3], "zip": userInfo[4]})

    fusers.close()
    return userList

def createMovieList():
    fitems = open("u.item", "r", encoding="windows-1252")
    itemList = []
    for line in fitems:
        itemInfo = line.strip().split("|")
        itemList.append({"title": itemInfo[1], "release date": itemInfo[2], "video release date": itemInfo[3], "IMDB url": itemInfo[4],
                     "genre": [int(x) for x in itemInfo[5:]]})

    fitems.close()
    return itemList


def readRatings():
    ratings = []
    f = open("u.data", "r")

    for line in f:
        data = tuple([int(x) for x in line.split()][:3])
        ratings.append(data)

    f.close()
    return ratings




def make_rLu(ratingTuples, numUsers):
    rLu = []
    l = list(range(numUsers + 1))
    l.pop(0)
    for x in l:
    # a dictionary per user
        dict = {}
        for values in ratingTuples:
            if values[0] != x:
               break
            dict[values[1]] = values[2]
        rLu.append(dict)
        ratingTuples = ratingTuples[(ratingTuples.index(values)):]
    return rLu

def make_rLm(numMovies, ratingTuples):
    rLm = []
    movies = list(range(numMovies + 1))
    movies.pop(0)
    for x in movies:
        dict = {}
        for values in ratingTuples:
            if values[1] == x:
                dict[values[0]] = values[2]
        rLm.append(dict)
    return rLm


def createRatingsDataStructure(numUsers, numItems, ratingTuples):
    # Initialization of rating lists
    ratingsList1 = []
    ratingsList2 = []
    for i in range(numUsers):
        ratingsList1.append({})

    for i in range(numItems):
        ratingsList2.append({})

    # Read each line in the rating file and store it in each
    # of the two data structures
    for rating in ratingTuples:
        ratingsList1[rating[0] - 1][rating[1]] = rating[2]
        ratingsList2[rating[1] - 1][rating[0]] = rating[2]

    return [ratingsList1, ratingsList2]

def createGenreList():
    f = open("u.genre", "r")

    L = []
    for line in f:
        L.append(line.split("|")[0])

    f.close()
    return L

def movie_to_genre(movieList,genreList):
    mg ={}
    iter = 0
    for dict in movieList:
        iter += 1
        genres = []
        i = 0
        while i < len(dict["genre"]):
            if dict["genre"][i] == 1:
                genres.append(genreList[i])
            i += 1
        key = iter
        mg[key] = genres
    return mg


def demGenreRatingFractions(userList, movieList, rLu, gender, ageRange, ratingRange):
    # Initialize the numerators and denominator of the to-be-computed fractions for all 19 genres
    numGenres = len(movieList[0]["genre"])
    numerator = [0] * numGenres
    denominator = 0

    # Walk down the user IDs, keeping in mind that they range from 1 through numUsers
    for i in range(len(userList)):

        # Check if this user fits the demographic constraints
        # If gender is "A", it does not matter what the user's gender is.
        # Note that the user's age has to be strictly less than ageRange[1] for the user to qualify
        if ((gender == "A") or (userList[i]["gender"] == gender)) and (ageRange[0] <= userList[i]["age"] < ageRange[1]):

            # Update denominator by the number of movies this user has rated
            denominator = denominator + len(rLu[i])

            # Walk down the ratings provided by this user by using the provided ratings list rLu
            for movie in rLu[i]:

                # Store the rating user i+1 provides to movie in a variable called rating
                rating = rLu[i][movie]

                # Check if this rating is in the given range
                if (ratingRange[0] <= rating <= ratingRange[1]):

                    # movieList[movie-1] contains 19 bits representing the genres
                    # For each genre, update the denominator and if in rating range,
                    # update the numerator as well
                    j = 0
                    for bit in movieList[movie - 1]["genre"]:
                        numerator[j] = numerator[j] + bit
                        j = j + 1

    return [numerator[i] / denominator if denominator > 0 else None for i in range(len(numerator))]


# END OF PHASE 1

def randomPrediction(u,m):
    return rd.randint(1,5)

def meanUserRatingPrediction(u,m,rLu): #so I'm not actually using m?
    user_index = u - 1
    ratings = 0
    user_ratings = rLu[user_index]
    denominator = len(user_ratings)
    if user_ratings:
        for key in user_ratings:
            ratings += user_ratings[key]
        return ratings / denominator
    else:
        return None

def meanMovieRatingPrediction(u,m,rLm):
    movie_index = m - 1
    ratings = 0
    movie_ratings = rLm[movie_index]
    denominator = len(movie_ratings)
    if movie_ratings:
        for key in movie_ratings:
            ratings += movie_ratings[key]
        return ratings / denominator
    else:
        return None


def demRatingPrediction(u, m, userList, rLu):
    user = userList[u-1]
    age = user['age']
    gender = user['gender']
    ageRange = (age-5, age+5)
    indexes_U = []
    for i in range(len(userList)):
            if (userList[i] != user) and (userList[i]['age'] <= age+5) and (userList[i]['age'] >= age-5) and (userList[i]['gender'] == gender): #if the person's age is in the range
                   indexes_U.append(i)
    total_U_ratings = []
    for index in indexes_U:
              for movie, rating in rLu[index].items():
                    if movie == m:
                            total_U_ratings.append(rating)
    if len(total_U_ratings) == 0:
          return None
    else:
            return sum(total_U_ratings)/len(total_U_ratings)

def genreRatingPrediction(u,m,movieList, rLu):
    M = []
    m_index = m - 1
    genres = movieList[m_index]['genre']

    for i in range(len(movieList)):
        if i != m_index:
            genres_for_movie = movieList[i]['genre']
            for j in range(len(genres_for_movie)):
                if genres_for_movie[j] == 1 and genres[j] == 1:
                    M.append(i + 1)
        else:
            continue
    user_index = u - 1
    user_ratings = rLu[user_index]
    ratings = []
    for movie in user_ratings:
        if movie in M:
            ratings.append(user_ratings[movie])
    if ratings:
        return sum(ratings) / len(ratings)

def partitionRatings(rawRatings,testPercent):
    ratio = testPercent / 100
    amount_to_take = round(ratio * len(rawRatings))
    rawL = list.copy(rawRatings)
    rd.shuffle(rawL)
    testSet = rawL[:amount_to_take]
    trainingSet = rawL[amount_to_take:]
    return [trainingSet, testSet]

def rmse(actualRatings, predictedRatings):
    # testingSet = partitionRatings(rawRatings,testPercent)
    if len(actualRatings) == len(predictedRatings):
        list_of_differences = []
        denominator = len(predictedRatings)
        for i in range(len(actualRatings)):
            if predictedRatings[i] and actualRatings[i]:
                list_of_differences.append((actualRatings[i] - predictedRatings[i]) **2)
            if predictedRatings[i] == None or actualRatings[i] == None:
                denominator -= 1
        #squared_error = [(actualRatings[i] - predictedRatings[i]) **2 for i in range(len(actualRatings)) if predictedRatings[i]]
        mse = sum(list_of_differences) / denominator
        rmse = math.sqrt(mse)
        return rmse
    else:
        return 1
















