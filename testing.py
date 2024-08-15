import random as rd
l = [1,2,3,4,5,6]

rd.shuffle(l)



def partitionRatings(rawRatings,testPercent):
    trainingSet = []
    testSet = []
    testPercent = testPercent / 100
    indexes = list(range(len(rawRatings)))
    lenOfTestSet = round(len(rawRatings) * testPercent)
    for i in range(0,lenOfTestSet):
        pickedIndex = rd.choice(indexes)
        testSet.append(rawRatings[pickedIndex])
        indexes.remove(pickedIndex)
    trainingSet = [rawRatings[i] for i in indexes]
    return [trainingSet, testSet]




x = None
def check():
    if x:
        print("hi")

check()


d = [{1:2, 2:3, 4:5},{6:2, 7:8, 9:10}]
if 2 in d[1]:
    print("yes")




#     U  = []
#     ratings = []
#     value = 0
#     user_index = userList[u - 1]
#     user_age = user_index["age"]
#     user_gender = user_index["gender"]
#     for i in range(len(userList)):
#         if i != user_index:
#             if userList[i]["gender"] == user_gender:
#                 if userList[i]["age"] in range(user_age - 5, user_age + 6):
#                     U.append(i)
#     if U:
#         for i in U:
#             for key in rLu[i]:
#                 if key == m:
#                     ratings.append(rLu[i][m])
#         if ratings:
#             for rating in ratings:
#                 value += rating
#             return value / len(ratings)
#         else:
#             return None
#     else:
#         return None


    # # two movies have the same genre if they share at least one genre.
    # user_ratings = rLu[u - 1]
    #
    # for movie in user_ratings:
    #     # the key corresponds to the movie in MovieList.
    #     if movie != m:
    #         genres_for_movie = g[m]
    #         for genre in genres_for_movie:
    #             if genre in genres:
    #                 M.append(user_ratings[movie])
    #
    # if not M:
    #     return None
    # else:
    #     denominator = len(M)
    #     numerator = 0
    #     for element in M:
    #         numerator += element
    #     if numerator:
    #         return numerator / denominator
    #     else:
    #         return None




v = {100:4, 212:5, 12: 2, 16:8}

tupps = v.items()
print(tupps)

# similar = [(1,1),(2,0.89),(3,-1),(5,0.2),(3, 0.5)]
# similar = sorted(similar)
# print(similar)
# print(similar)
# # for tupp in similar:
# #     tupp[0],tupp[1] = tupp[1],tupp[0]
#
# print(similar)

t = (1,2)
print(t[0])

l = [[1,2],[3,4],[5,6],[7,8]]
for ind in range(len(l)):
    l[ind] = tuple(l[ind])
print(l)


f = [(1,2),(3,2)]
f = dict(f)
print(f)