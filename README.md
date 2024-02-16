# Delivery Route Algorithm with Python
<img width="1329" alt="Code Execution" src="https://github.com/culturedmold/Delivery-Route-Algorithm/assets/122142361/e2d7e9a5-c013-4ef8-9c47-67dc4e659dc8">

## About
This project presents a solution where all 40 packages will be delivered on time while meeting each package’s requirements (such as package specific delivery deadline. Distance traveled must be kept under 140 miles for two of the trucks. The specific delivery locations are provided based on real addresses around Salt Lake City, UT and are provided via CSV.

This project showcases proficiency with Data Structures and Algorithms. 

## Data Structures
A custom hashmap with hashing function is utilized to store, insert, and update package objects in memory. The custom hashmap uses the formula "key modulo (length of package list)" to determine the "buckets" of the hashmap. The initial size of the hashmap is set to 16, which is the amount of packages a single truck in our simulation can hold. This provides a logical starting point for initilizing our hashmap and keeps size, lookup, and insertions from getting unnecessarily large. Each bucket holds a list of package objects. When the create_pkg_hashmap() is called, it parses a CSV of package data and creates the hashmap from that data utilizing the package ID as the "key" parameter in the insert() function. 
