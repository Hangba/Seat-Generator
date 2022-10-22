# SeatGenerator
A Simple Seat Generator
Use name lists to generate a new seat table. Allow users to customize the seat by using generation and judgment editor(in the future).
Just for fun :D

#Generation Examples
g1 StudentName Position #Generate a given student at a given position. If 'None' is given, that remains an empty seat.
g2 StudentList radius (circleCenterPosition) #Generate given students whose names are in the list in the circle with customized circle center(optional, or it will be a random point instead) and radius. Students in StudentList use comma to get partition.
g3 MainStudent StudentList radius circleCenterPosition #Generate given students whose names are in the list and a center student as circle center in the circle with customized circle center(compulsory) and radius. Students in StudentList use comma to get partition.
