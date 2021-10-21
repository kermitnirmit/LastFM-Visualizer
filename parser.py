import csv
from collections import defaultdict
from os import read
from collections import Counter
from itertools import accumulate
import datetime
import pandas as pd

class Artist:
    name=""
    plays = []

    def sumUp(self):
        self.plays = list(accumulate(self.plays))

    def __init__(self, n, dayCount) -> None:
        self.name = n
        self.plays = [0] * dayCount
    def __eq__(self, o: object) -> bool:
        return isinstance(o, Artist) and o.name == self.name
    def __hash__(self) -> int:
        return hash(self.name)

def better_handling(day_data):
    new_dict = {}
    for key, val in day_data.items():
        artists = [x[0] for x in val]
        c = Counter(artists)
        new_dict[key] = c
    return new_dict

with open("full_data.csv") as csvfile:
    artists = {}

    all_data = []
    reader = csv.reader(csvfile)
    for line in reader:
        all_data.append((line[0:-1], line[-1][:-6]))
    all_data = all_data[1:]

    all_data = all_data[::-1]


    day_data = defaultdict(list)
    for val, date in all_data:
        day_data[date].append(val)


    something = better_handling(day_data)

    start_date = datetime.date(2015, 10, 12)
    end_date = datetime.date(2021, 10, 19)
    diff = end_date - start_date
    dayCount = diff.days + 1
    curr = start_date
    index = 0
    dates = []


    while curr <= end_date:
        dates.append(curr)
        key_check = curr.strftime("%d %b %Y")
        if key_check not in something:
            pass
        else:
            counter = something[key_check]
            for artist, count in counter.items():
                if artist in artists:
                    artists[artist].plays[index] = count
                else:
                    toInsert = Artist(artist, dayCount)
                    toInsert.plays[index] = count
                    artists[artist] = toInsert
        curr += datetime.timedelta(days=1)
        index += 1
    # for artist in artists:
        # artists[artist].sumUp()
    
    finalArtistDict = {}
    for artist in artists:
        finalArtistDict[artist] = artists[artist].plays

    
    print(len(finalArtistDict["Lindsey Stirling"]))
    print(len(dates))

    df = pd.DataFrame.from_dict(finalArtistDict, orient='index').transpose()

    afterSum = df.rolling(180, axis=0).sum()



    # df.to_csv("parsed.csv")

    # asdf = afterSum.head(50)

    afterSum.to_csv("rolling_sum_180.csv")
    # asdf.to_csv("just_50.csv")
    # print(asdf) # will print out the first 5 rows
