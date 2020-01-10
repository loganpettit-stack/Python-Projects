"""
Author: Logan Pettit
Date: 9/30/19
Class: CS 4500
Description: This program draws a grid of specified size by the user. The user will input a digit, N, to create an
N x N sized grid. The user will then specify the number of paintings they want to create. For the next K paintings
the program will create a random painting by dropping random blobs of paint into each square of the grid until
the grid is completely filled up. The grid locations choosen will be random and so will the colors of the blobs.
Once the painting is finished the user will be prompted to press ENTER in order to move on to the next painting
each paintings statistics will be kept track of as well as the total paintings statistics and displayed in the console
As the program is making the paintings it keeps track of the time and increases the speed of the brush the longer the
painting takes.
"""

import turtle
import random
import time

pen = turtle.Turtle()


# Function to draw the grid for each painting
def draw_grid(N, num):

    pen.speed("fastest")
    box_length = 30
    title = "Painting " + str(num + 1)
    pen.penup()
    pen.setx((int(N)/2) * box_length - ((int(N)/2) * box_length))
    pen.sety((int(N)/2) * box_length + 20)
    pen.write(title, False, "center", ("Arial", 15, "normal"))
    pen.pendown()
    x = -int((int(N) * box_length) / 2)
    y = -int((int(N) * box_length) / 2)
    pen.penup()
    pen.setx(x)
    pen.sety(y)
    pen.pendown()

    i = 0
    while i < int(N):
        pen.forward(box_length * int(N))
        pen.left(90)
        pen.forward(box_length)
        pen.left(90)
        pen.forward(box_length * int(N))
        pen.left(90)
        pen.forward(box_length)
        pen.left(90)
        y += 30
        pen.sety(y)
        i += 1

    j = 1
    while j < int(N):
        x += 30
        pen.setx(x)
        pen.right(90)
        pen.forward(box_length * int(N))
        pen.left(90)
        pen.sety((box_length * int(N) / 2))
        j += 1


# Function to check the grid and see if it is filled in
def matrix_check(matrix):
    i = 0
    while i < int(N):
        j = 0
        while j < int(N):
            if matrix[i][j] == 0:
                return False
            j += 1
        i += 1

    return True


# Function to randomly draw splashes on the grid, and check each time
# if the grid is filled in, also checks the time to increase speed based on
# how long has elapsed.
def draw_splashes(N):
    speed = 6
    pen.speed(speed)
    start = time.time()
    check = False
    box_length = 30
    half_length = (box_length / 2)
    neg_threshold = int(N) / 2
    pencolor_array = ["green", "red", "blue", "orange", "purple"]

    # Create matrix
    w, h = int(N), int(N)
    matrix = [[0 for x in range(w)] for y in range(h)]

    # algorithm to place the blobs randomly by associating each
    # array element with a point on the grid
    while not check:
        color = random.choice(pencolor_array)
        pen.color(color)
        random_value = random.randint(-4, 8)
        x = random.randint(1, int(N))
        y = random.randint(1, int(N))
        pen.penup()
        if x < neg_threshold:
            xcoord = ((x - neg_threshold) * box_length)
            pen.setx(xcoord - (half_length + random_value))
        else:
            xcoord = ((x - neg_threshold) * box_length)
            pen.setx(xcoord - (half_length + random_value))

        if y < neg_threshold:
            ycoord = ((y - neg_threshold) * box_length)
            pen.sety(ycoord - (half_length + random_value))
        else:
            ycoord = ((y - neg_threshold) * box_length)
            pen.sety(ycoord - (half_length + random_value))

        pen.pendown()
        pen.circle(5)

        matrix[x - 1][y - 1] += 1

        check = matrix_check(matrix)

        # algorithm to speed up after 5 seconds has elapsed
        end = time.time()
        time_check = end - start
        if time_check > 5.0:
            speed += 1
            pen.speed(speed)
            start = time.time()

    return matrix


# Function to determine the max blobs in a single cell
def painting_maximum(matrix):
    maximum = 0
    i = 0
    while i < int(N):
        j = 0
        while j < int(N):
            maximum = max(maximum, matrix[i][j])
            j += 1
        i += 1

    txt3 = "Maximum number of blobs in one cell: {}\n"
    print(txt3.format(maximum))
    return maximum


# Function to determine the total blobs used
def painting_total(matrix):
    total = 0
    m = 0
    while m < int(N):
        j = 0
        while j < int(N):
            total += matrix[m][j]
            j += 1
        m += 1

    txt4 = "Total number of blobs in one painting: {}\n"
    print(txt4.format(total))
    return total


#  Function to find the average blob in each cell in one painting
def painting_average(matrix):
    total = 0
    m = 0
    while m < int(N):
        j = 0
        while j < int(N):
            total += matrix[m][j]
            j += 1
        m += 1

    txt5 = "Average number of blobs in each cell: {}\n"
    average = total / (int(N) * int(N))
    print(txt5.format(average))
    return average


# Function to find the minimum number of blobs in a single painting
def painting_minimum(matrix):
    minimum = 10000
    k = 0
    while k < int(N):
        j = 0
        while j < int(N):
            minimum = min(minimum, matrix[k][j])
            j += 1
        k += 1

    txt2 = "Minimum number of blobs in one cell: {}\n"
    print(txt2.format(minimum))
    return minimum


# output the painting statistics to the console
def total_stats_output(avg, minmn, maxmn, tot):
    print("\nStatistics from every painting: \n")
    txt6 = "The average number of blobs in a square from every painting: {}\n"
    txt7 = "The minimum number of blobs in a square from every painting: {}\n"
    txt8 = "The maximum number of blobs in a square from every painting: {}\n"
    txt9 = "The total number of blobs in every painting: {}\n"
    print(txt9.format(tot))
    print(txt6.format(avg))
    print(txt7.format(minmn))
    print(txt8.format(maxmn))


# Main
N = 0
K = 0
flag = True
flag2 = True

# Run until correct input is given
while flag:
    N = input("Enter this size of the grid between 2 - 15")
    if N.isdigit() and 2 <= int(N) <= 15:
        flag = False
    else:
        print("ERROR: Please enter a digit a digit between 1 - 15 inclusive.")
        flag = True


# Run until correct input is given
while flag2:
    K = input("Enter the number of paintings you would like between 1 - 10")
    if K.isdigit() and 1 <= int(K) <= 10:
        flag2 = False
    else:
        print("ERROR: Please enter a digit between 1 - 10 inclusive.")
        flag2 = True

i = 0
total_min = 100000
total_max = 0
total_total = 0
total_average = 0

# algorithm to calculate total statistics on every painting and run
# the program for K specified times
while i < int(K):

    draw_grid(N, i)
    matrix = draw_splashes(N)

    txt1 = "\nPainting {} statistics: \n"
    print(txt1.format(i + 1))
    total_max = max(total_max, painting_maximum(matrix))
    total_min = min(total_min, painting_minimum(matrix))
    total_total += painting_total(matrix)
    painting_average(matrix)
    total_average = total_total / ((int(N) * int(N)) * int(K))
    print("The gird in matrix form: \n")
    print(matrix)

    if i < (int(K) - 1):
        print("\nPainting done press ENTER to move to the next painting\n")
        input()
    else:
        input("\nPaintings are done press enter to see statistics on each game.\n")

    pen.reset()
    i += 1

total_stats_output(total_average, total_min, total_max, total_total)




