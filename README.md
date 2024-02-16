# Delivery Route Algorithm with Python
<img width="1329" alt="Code Execution" src="https://github.com/culturedmold/Delivery-Route-Algorithm/assets/122142361/e2d7e9a5-c013-4ef8-9c47-67dc4e659dc8">

## About
This project presents a solution where all 40 packages will be delivered on time while meeting each package’s requirements (such as package specific delivery deadline. Distance traveled must be kept under 140 miles for two of the trucks. The specific delivery locations are provided based on real addresses around Salt Lake City, UT and are provided via CSV.

This project showcases proficiency with Data Structures and Algorithms. 

## Data Structures
A custom hashmap with hashing function is utilized to store, insert, and update package objects in memory. The custom hashmap uses the formula "key modulo (length of package list)" to determine the "buckets" of the hashmap. The initial size of the hashmap is set to 16, which is the amount of packages a single truck in our simulation can hold. This provides a logical starting point for initilizing our hashmap and keeps size, lookup, and insertions from getting unnecessarily large. Each bucket holds a list of key/value pairs, where package ID is the key, paired to the package object. 

When the create_pkg_hashmap() method is called, it parses a CSV of package data and creates the hashmap from that data utilizing the package ID as the "key" parameter in the insert() function. 

## Delivery Algorithm
Our delivery algorithm operates on 3 trucks - this was an external requirement, as the simulated delivery company only has three trucks. Packages have been loosely sorted onto trucks by zip code.
The algorithm utilizes a "greedy" approach. Taking a truck object, hashmap of package objects, address adjacency matrix, and a starting address, the algorithm runs through each package on the truck and uses a "nearest-neighbor" approach to determine the next best package to visit in order to minimize miles traveled. The package object is then updated with the delivery time and delivery status. Delivery time is simulated at an average truck speed of 18 miles per hour. Miles traveled for the truck object is updated. The truck is then rerouted back to the delivery hub after all it's packages have been delivered. 

The delivery algorithm needed to deliver all packages within their deadlines, before EOD, and within 140 miles across two trucks. Our algorithm accomplishes all these requirements well within requirements by keeping miles traveled at 120 miles across all three trucks. 
