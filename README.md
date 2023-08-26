# Analysis Of Algorithm Projects

## GREEDY ALGORITHM

Based on given problem statement discuss various greedy approaches to solve this problem. These approaches are also restricted by their time complexities.
### PROBLEM STATEMENT
You are a house painter that is available from day 1 . . . n (inclusive). You can only paint one house in a day. It also only takes one day to paint a house. You are given m houses. For each house i, you are also given startDayi and endDayi for i = 1, . . . , m. The house i can only be painted on a day between startDayi and endDayi (inclusive). The given houses are already sorted primarily on startDay and secondarily on endDay (in case of equality of the startDay). You are tasked to find the maximum number of houses that you can paint.
We have discussed all the given 4 strategies, their design in required time complexity and implementation in the below sections, followed by comparative study of each of the implementation. We have also implemented the STRAT4 which we found to be optimal greedy in Ɵ(m logm )

#### STRAT 1 - O(n) 
Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses that are available to be painted on that day, paint the house that started being available the earliest.

##### Analysis
The Strat 1 algorithm iterates for all the days and picks the first eligible house for that day. For any day where there is no suitable house, the algorithm skips the day. Similarly for the houses which are past the deadline in the list, the algorithm will skip those houses. Since each iteration, we can assign a house for that day, skip the house or skip the day, in the best case the algorithm will run in O(n) complexity. In some cases the algorithm would have to skip over a large number of houses and the complexity might go above O(n), but still the main variable component for the algorithm is the parameter n, as small n means early termination and large n means we have to go over all houses to make sure we schedule something on maximum number of days. Therefore we can assume the algorithm is
θ(n). Apart from the input (Space - O(m)), the algorithm uses a
list variable to store indices of the scheduled houses, therefore the space
complexity is O(m).

#### STRAT 2 - O(n+mlog(m)) 
Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses that are available that day, paint the house that started being available the latest.

##### Analysis
The Strat 2 algorithm iterates for all the days and picks the first eligible house for that day from the priority queue. For every iteration, the algorithm adds all the houses that can be scheduled on the day. Since a house can only be added to the queue once, it takes O(mlog(m)) time to add houses to the priority queue. Now since for each day we poll the best house from the priority queue, it takes O(log(m)) time to remove a house. Since every house can be polled at max once from the priority queue, the complexity of polling is O(log(m)). Therefore in the worst case, we would end up adding all the houses to the priority queue on the first day, but since no new add operation will happen for the following days there would be just poll operations. The overall worst complexity would be O(n+m*log(m)+m*log(m)), which would be O(n+m*log(m)).
Apart from the input (Space - O(m)), the algorithm uses a list variable to store indices of the scheduled houses and a priority queue which at max would have
m houses in it, therefore the space complexity is O(m).

#### STRAT 3 - O(n+mlog(m)) 
Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses that are available that day, paint the house that is available for the shortest duration.

##### Analysis

The Strat 3 algorithm is similar to the one discussed in strat 2, only the priority in the priority queue is different. Therefore, the overall worst complexity would be O(n+m*log(m)+m*log(m)), which would be O(n+m*log(m)).
Apart from the input (Space - O(m)), the algorithm uses a list variable to store indices of the scheduled houses and a priority queue which at max would have m
houses in it, therefore the space complexity is O(m).


#### STRAT 4 - O(n+mlog(m)) 
Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses that are available that day, paint the house that will stop being available the earliest.

##### Analysis

The Strat 4 algorithm is similar to the one discussed in strat 3, only the priority in the priority queue is different. Therefore, the overall worst complexity would be O(n+m*log(m)+m*log(m)), which would be O(n+m*log(m)).
Apart from the input (Space - O(m)), the algorithm uses a list variable to store
indices of the scheduled houses and a priority queue which at max would have
m houses in it, therefore the space complexity is O(m).

#### EXPERIMENTAL COMPARITIVE STUDY
We created different data sets For n = 1000 to 5000 and m = n/4 to 5n/4 for each n and ran different strategies on those datasets. Following figures 1 to 4 show respective graphical representation of results obtained.

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/2636c452-f9d9-4ab1-a7e5-6fc577939618" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/47b0c845-ab58-47bb-aae4-96f02921e105" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/7497d094-bbec-4c26-9410-4e434ff04b59" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/acc4be85-e4e8-4433-a5bb-b06dd97d7f0b" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/4635dab6-ce06-49dc-9008-c9ecd2afda4c" width="50%" height="50%">
</picture>

To summarize above finding, we created datasets for n =1000 to 5000 and ran different strategies on those datasets for n = m. The results can be seen in the following figure 6, that strategy 4 schedules the maximum number of houses for painting in each set of inputs. No clear relationship between the other strategies is found but the results of this extended study on a larger dataset support our hypothesis that strategy 4 indeed is an optimal strategy.

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/ffc4eab2-aab2-4c2c-867e-c7ee1a078fcb" width="50%" height="50%">
</picture>




#### OPTIMAL SOLUTION - (mlog(m))
Design and analyze (time, space and correctness) of an Θ(mlog(m)) algorithm based on the greedy strategy

##### Analysis

1. The above algorithm would one by one pick a house and find all the eligible
houses which are eligible to be painted on the same day.
2. It then adds them to a min heap, and picks the house with the lowest
deadline.
3. Since we don't fret over what day it would be scheduled, we decide it by the
gap between two consecutive houses.
4. Adding houses to a min heap cost Log(m) and since m houses at max would
be added, the time taken by the algorithm would be O(m*log(m))
4. Similarly while polling at max m houses will be polled from the pq and
therefore O(m*log(m)) is the polling time complexity.
5. Overall the time complexity si O(2*m*log(m)) which is O(m*log(m)).
6. We only maintain a list of houses scheduled therefore the space complexity
is O(m).
7. In the best case the heap size will always be 1,i.e only open ended houses are present in our dataset. Which certainly brings down the overall time but
the complexity would still be Θ(m log(m)) as we have.

#### EXPERIMENTAL COMPARITIVE STUDY
We compare strat 4 with Optimal solution 

1. We analyzed the run time of both the algorithms, and observed that for sufficiently larger input size i.e n, we get 2 times the efficiency as compared to the Strat4 algorithm.
2. We plot a line graph for n=m when n varies from 1000-10000 and then a plot when n varies from 105 to 106.
3. As the input size increases, the difference in the time taken to run by the algorithms widens and conclude that our optimal algorithm performs better as compared to algorithm described in strat4.
4. In order to further analyze the time difference, we plot a graph where we keep m as constant and we change our input sizes, so that both the algorithms now have increasingly higher search space for similar amounts of houses.
5. Since both the algorithms output the same houses, the optimal algorithm is able to navigate the search space better and schedule the jobs as it only goes through the constant number of houses every time regardless of the size of n.
6. On the other hand, the strat4 algorithm loops through the n houses, which makes it more time bound on n and hence loses time as n increases.
7. This trend can be seen from the following plots figure 10 to 13 where we keep m as constant and change n on the x axis.

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/3b289642-a443-49e6-a22e-507eb3fd268d" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/60e9f9bc-bc14-4ee3-be33-8c05ceda6e02" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/60af26f5-3f21-4d7e-accb-25766daa1e31" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/e51cc6cc-edac-4775-87b5-aaf7cc089880" width="50%" height="50%">
</picture>

<picture>
   <img alt="Home" src="https://github.com/vedantspatil/AOAProject/assets/37808420/e0a486b9-ccbb-4026-93a2-52d18225038b" width="50%" height="50%">
</picture>


