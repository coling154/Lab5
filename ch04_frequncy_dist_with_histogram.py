#!/usr/bin/python3
# Ch04_frequncy_dist_with_histogram.py

import turtle

def frequencyChart(alist):
    countDict = {}

    for item in alist:
        if item in countDict:
            countDict[item] = countDict[item] + 1
        else:
            countDict[item] = 1
    itemList = list(countDict.keys())
    minItem = 0
    maxItem = len(itemList) - 1
    itemList.sort()

    countList = countDict.values()
    maxCount = max(countList) + 1

    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1, -1, maxItem+1, maxCount)
    chartT.hideturtle()

    chartT.up()
    chartT.goto(0, 0)
    chartT.down()
    chartT.goto(maxItem, 0)
    chartT.up()
    for i in range(maxCount):
        chartT.goto(-1, i)
        chartT.write(str(i), font=("Helvetica", 16, "bold"))
    itr = 0
    for index in range(min(itemList), max(itemList)):
        chartT.goto(index, -1)
        # write the bottom number
        if index in itemList:
            chartT.write(str(itemList[itr]), font=("Helvetica", 16, "bold"))
            chartT.goto(index, 0)
            chartT.down()
            chartT.goto(index, countDict[itemList[itr]])
            chartT.up()
            itr += 1
        else:
            chartT.goto(index, -1)
    wn.exitonclick()

#frequencyChart([0, 0, 3, 5, 3, 2, 2, 3, 5, 3, 5, 4, 4, 6, 7, 6, 7, 5, 7, 8, 3, 8, 2, 3, 4, 5, 6, 7])