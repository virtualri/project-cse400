# Project Repository 

> CSE-400

> This repository and contents are under development and update accordingly

## **Project Title**

**Sponsor based resource allocation using artificial feed-forward based neural network**

> Project title may change at the moment of final compile & with the advice of the supervisor


## Software development model

![Agile development model](/images/Agile-DevelopmentModel.png)


## Project Schedule

On-going from Wed Apr 17 2019 while the schedule under development and will publish within **week 38**


## Literacy and understanding under discussion and supervisor

### System view: Logitcal and J2EE distributed multitier architecture 

#### Multitier: logical view
![Logical View of the N-tier Architecture](/images/multitier-architecture.png)

#### Multitier and Java EE

![J2EE Distributed Multitier architecture](/images/distributed-j2eetiers.png)

### Aerial view of the proposed system

![UML Diagram of System View](/images/umlDiagram-project400.png)


### Neural Network : Feedforward-Backpropagation

![Neural Network : Feedforward-Backpropagation](/images/NeuralNetwork-Feedforward-Backpropagation.png)


### Optimization and Selecting Employee as SPONSORING the client 

#### Process A: Finding the model using tpot
![Genetic algorithm](/images/geneticAlgorithm.png)


#### Process B: Tpot is a technology as tool
![TPOT: Automated to finding the model and predict the output](/images/tpot.png)



### Resource ( room and employee) allocation

> Developing in JAVA EE, jscript, jsp, MySql Community Server, Apache Tomcat Server, github and project management and bug reporting tools

![Java EE, Multitier](/images/Use-of-the-MVC-Design-Pattern-in-the-Java-EE-Platform-based-web-application-architecre.png)


## Project cost


### Constructive Cost Model ( COCOMO ) intermediate model

#### Project complexity
Project complexity factor is ***VERY HIGH***

#### Calculated results

|Title of the program	                             |LOC    | Error or loss | Note | 
|---|---:|---:|:---|
|findingSponsor.py	                                 |94     | 0.17          | Generation 10, population 50|
|Feed_forward_Backpropagation-NeuralNetwork.ipynb	 |60     |               |Input layer 6, Output layer 6, Hidden layer 10|
|NeuralNetworkFeedForwardBackpropagation.py	         |72     |               |Core NN Engine |
|Designing diagram	                                 |109    |               |List of figures |
|Designing system view	                             |80     |               |Basic system view |
|Schedule of the project	                         |500    |               |Sample schedule for Agile Methodology|
|  Total loc score in thousand	                     |	0.915|               || 


#### Effort multiplier						

|Cost driver	           |very low 	|low	|normal	|high	|very high	|extra high|
|---|---|---|---|---|---|---|
|product complexity (EAF)  |0.7	        |0.85   |	1	|1.15   |	1.3     |	1.65|


#### Product complexity (EAF) is very high=1.3				


#### Intermediate model				

|Category	|a<sub>b</sub>	|b<sub>b</sub>	|c<sub>b</sub>	|d<sub>b</sub>	|Effort	|Schedule|
|---|---|---|---|---|---:|---:|	
|Organic	|3.2	|1.05	|2.5	|0.38	|E= a<sub>b</sub> x LOC<sup>b<sub>b</sub></sup>|DEV=c<sub>b</sub> x E<sup>d<sub>b</sub></sup>|
|Semidetached	|3	|1.12	|2.5	|0.35	|E= a<sub>b</sub> x LOC<sup>b<sub>b</sub></sup>	|DEV=c<sub>b</sub> x E<sup>d<sub>b</sub></sup>|
|Embedded	|2.8	|1.2	|2.5	|0.32	|E= a<sub>b</sub> x LOC<sup>b<sub>b</sub></sup>	|DEV=c<sub>b</sub> x E<sup>d<sub>b</sub></sup> |

#### Organic			

|Factors                        |Results                | Measurement unit |
|---|---|---:|
|Effort	                        |2.18626796145394       |	person per month|
|Development time in months	    |2.4170187776113        |	months|
|Labor rate	                    |20000                  | USD\m|			
|Productivity	                |418.521432931531	    |loc per person per month|
|Average staffing per month	    |0.904530813622636	    |full time software personnel| 		
|Cost of the project	        |105685.014314483       |USD|	

	
#### Semidetached	

|Factors                        |Results                | Measurement unit |
|---|---|---:|
|Effort	                        |3.78953113318683	    |person per month|
|Development time in months	    |4.14765372058999	    |months|
|Labor rate	                    |20000	                |USD|
|Productivity	                |241.454672845114	    |loc per person per month|
|Average staffing per month	    |0.913656584775786	    |full time software personnel| 		
|Cost of the project	        |314353.258077079	    |USD|
			
#### Embedded		
|Factors                        |Results                | Measurement unit |
|---|---|---:|
|Effort	                        |3.53066272382387	    |person per month|
|Development time in months	    |3.88767265623533	    |months|
|Labor rate	                    |15000	                |USD|		
|Productivity	                |259.158144397608	    |loc per person per month|
|Average staffing per month	    |0.908168726130052	    |full time software personnel| 		
|Cost of the project	        |205890.913946991	    |USD|

## References

---
title= "Fundamentals of Neural Networks: Architectures, Algorithms and Applications",
isbn= 9788131700532,
url= https://books.google.com.bd/books?id=vKM7KChXeKsC, 
year=2006
publisher= "Pearson Education"
---
---
  title="Software Architecture Design Patterns in Java",
  author= Kuchana, P.m
  isbn={9780203496213,
  url=https://books.google.com.bd/books?id=FqfKFl4Bm7UC,
  year=2004,
  publisher= "CRC Press"
---

---
  title="Java EE 8 Design Patterns and Best Practices: Build enterprise-ready scalable applications with architectural design patterns",
  author=Rocha, R. and Purifica{\c{c}}{\~a}o, J.,
  isbn=9781788837736,
  url=,https://books.google.com.bd/books?id=Q8JoDwAAQBAJ,,
  year=2018,
  publisher="Packt Publishing"
---

---
  title="The Art of Agile Development",
  author=Shore, J. and Warden, S. and Shore, J.,
  isbn=9780596527679,
  lccn=2009278263,
  series={Theory in practice,
  url=https://books.google.com.bd/books?id=2q6bAgAAQBAJ,
  year=2008,
  publisher="O'Reilly Media, Incorporated"
---

---
  title="Architecting Modern Data Platforms: A Guide to Enterprise Hadoop at Scale",
  author=Kunigk, J. and Buss, I. and Wilkinson, P. and George, L.,
  isbn=9781491969243,
  url=https://books.google.com.bd/books?id=2Kd9DwAAQBAJ,
  year=2018,
  publisher="O'Reilly Media"
---


# Project journal

| Date | Project status |
|---|---:|
|Wed Apr 17 16:52:01 BST 2019 	 |Initialization of the project|
|Sun Apr 21 10:01:45 BST 2019 	 |Initialization to find the topic|
|Wed Apr 24 06:36:08 BST 2019 	 |Picking topic title|
|Sat May 4 11:42:51 BST 2019 	 |Project Proposing version1.00.04-05-2019 topic for thesis|
|Tue Sep 3 08:09:16 BST 2019 	|Casual briefing the partial synopsis|	 
|Tue Sep 3 08:10:28 BST 2019 	|#communication: #discussion about the feedback and how the thesis and implementation will be done|
|Tue Sep 3 08:11:05 BST 2019 	|#scope_of_project 1st draft|
|Wed Sep 4 07:10:33 BST 2019 	|#UML_diagram of the app|
|Wed Sep 4 07:10:57 BST 2019 	|#Submission #UML_diagram of the app|
|Mon Sep 9 08:05:00 BST 2019 	 |#Open_discussion and answering question about the project and getting approval of the python modules|
|Tue Sep 10 08:50:22 BST 2019 	|#Open_discussion #Selecting SDLC as agile| 	 
|Wed Sep 11 05:05:47 BST 2019 	 |Project repository initialization| 	 
|Wed Sep 11 05:15:53 BST 2019 	 |Updating supervisor about the project and repository initialization|
|Wed Sep 11 05:54:57 BST 2019 	 |How it works: Distributed J2EE software development architecture along with N-tier MVC view|
|Fri Sep 13 17:44:54 BST 2019 	 |Project cost, effort, and development time according to COCOMO Intermediate model|

# Note
> The contents are populated only for supervisor
