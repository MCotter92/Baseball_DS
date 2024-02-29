# Goal 
The goal of this project is to learn about how KMeans Clustering works. I have chosen to follow a tutorial on how to build a KMeans clustering algorithm from scratch, adapt it to my use case and compare my results with Sci-Kit Learn's algorithm. 

The tutorial can be found here: [KMeans From Scratch](https://www.youtube.com/watch?v=lX-3nGHDhQg)

# The Data 
The data I have chosen is pitching statistics from MLB seasons 2020 - 2023. I hope to run the algorithms and find where each season's Cy Young winners are grouped. I expect all of the winners to be grouped with other winners. If this doesn't happen then I hope to find out why not. 

# Conclusion 
When making my algorithm from scratch I found that the supposed top pitchers per year were not being clustered together consistently. I learned a lot about the mathematics and iterative process of how KMeans works but I needed a way to refine my results. By moving over to SciKit-Learn's algorithms I found the same result. Employing the elbow method to determine the correct number of groups, I was able to achieve consistent clustering among the top pitchers. Using the silhouette score helped to confirm that my algorithm was working. 