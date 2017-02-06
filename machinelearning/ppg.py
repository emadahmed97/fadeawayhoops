import pandas
import math
import random
from numpy.random import permutation
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsRegressor

### PREDICTING NBA PLAYER'S POINTS PER GAME USING K NEAREST NEIGHBORS


with open("nba_2013.csv", 'r') as csvfile:
    nba_raw = pandas.read_csv(csvfile)

nba = nba_raw.fillna(0)


#print ("nba.columns.values:", nba.columns.values)



selected_player = nba[nba["player"] == "LeBron James"].iloc[0]

distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb',
'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']


# calculating euclidean distance

def euclidean_distance(row):

    value = 0

    for k in distance_columns:
        value += (row[k] - selected_player[k]) ** 2

    return math.sqrt(value)


lebron_distance = nba.apply(euclidean_distance, axis=1)
#print("lebron_distance[:5]:\n", lebron_distance[:5])

# Normalize columns by making the mean for each category 0 and set the standard
# deviation to 1

nba_numeric = nba[distance_columns]
nba_numeric.head(5)

nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()
nba_normalized.head(5)


# finding euclidean distances that are closest to lebron


nba_normalized.fillna(0, inplace=True)

lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)
distance_frame = pandas.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
distance_frame.sort_values(by="dist", inplace=True)

second_smallest = distance_frame.iloc[1]["idx"]

most_similar_to_lebron = nba.loc[int(second_smallest)]["player"]
print("most_similar_to_lebron:", most_similar_to_lebron)



random_indices = permutation(nba.index)

test_cutoff = math.floor(len(nba)/3)

test = nba.loc[random_indices[1:test_cutoff]]

train = nba.loc[random_indices[test_cutoff:]]


print ""
print ""

# use sklearn to implement k nearest neighbors


x_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf',]

y_column = ["pts"]

knn = KNeighborsRegressor(n_neighbors=5)

knn.fit(train[x_columns], train[y_column])

predictions = knn.predict(test[x_columns])


x = test[x_columns][:1]["x2p."]

g = test[x_columns][:1]["mp"]

for y in x:
    x = y

# get player from dataset who's ppg we are predicting

players = nba[nba["x2p."] == x ]




if len(players) > 1:
    print "Length is > 1"
    exit()

else:
    print players["player"]


print "prediction is: "
points = predictions[:1] / 82
pointspergame =  str(points).replace('[','').replace(']','')
print pointspergame + ' ppg for upcoming season'



actual = test[y_column]

#mean squared error
mse = (((predictions - actual) ** 2).sum()) / len(predictions)



#print("mse:", mse)
