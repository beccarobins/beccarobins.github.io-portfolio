---
layout: post
title: Feedback messages
published: true
# subtitle:  The dos and the don'ts
# cover-img: /assets/img/path.jpg
thumbnail-img: ../images/14.png
share-img: /images/social-share-logo.png
gh-repo: beccarobins/beccarobins.github.io-portfolio
# gh-badge: [star, fork, follow]
gh-badge: [follow]
tags: [sample work]
---

Unlike typical product experiences, good learning experiences are not frictionless. Learners don't find value in experiences that don't challenge them and they hate courses they can't pass. Assessments are an integral part of learning and play a pivotal role in creating a good learner experience via feedback messages, the response a learner receives when they submit an answer to an assessment question. Good feedback: 1) clearly confirms or refutes whether the answer is correct, 2) provides meaningful information to the learner that affirms or corrects their mental model, and 3) when the learner is wrong, it does not give away the answer.

[![alt text](https://img.youtube.com/vi/video-id/0.jpg)](https://www.youtube.com/watch?v=syWOP_u37ZA)

<figcaption class="caption"> A demo of DataCamp's code submission. The red error messages in the console on the bottom right are written by developers of the programming language. The feedback messages appear in the instructions box (on the bottom left) along with a "Do you find this feedback helpful" prompt to assess whether the feedback message helped the learner understand their error.
</figcaption> 

## Process
I worked in tandem with content SMEs, external instructors who were an expert on the course topic. My input on feedback messages during development was a combination of editing, writing, and providing (meta) feedback on feedback messages. Following launch, I monitored the qualitative and quantitative data related to the feedback messages and made improvements as necessary.
Helpful feedback messages are quite difficult to write. Of course, you need to keep it brief because of both space and attention limitations, but you need an excellent understanding of the learner. A helpful feedback message is specific to the chosen response, in most cases you need a different feedback message for every possible incorrect response. To ensure the feedback is helpful, you need an understanding of why the learner chose that answer, that is, you need to ask "what mental model led to this choice?" and "how do I correct it?". This requires not only knowledge of the learning material, but also the anticipated audience.

<div>
<img src="../images/identifying decision boundaries.png" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> This feedback message refutes the learner's submission ("this is a legitimate decision boundary") and corrects the learner's mental model ("a decision boundary is found in the gap between clusters") without directing the learner to the correct answer.
</figcaption> 

### Hints and success messages
In addition to feedback messages, DataCamp assessments provided hints if a learner needed more help and success messages popped up in a modal when the correct answer was submitted. Success messages were fairly easy: confirm the learner is correct, congratulate them, and possibly provide an interesting tidbit. Hints are actually quite difficult. You need to give more away than you do in a feedback message while still not giving away the answer. Occasionally, feedback messages had to be "sacrificed" for hints because learners paid for hints: DataCamp's interactive platform subtracted 30 XP from learners when they took hints.

<div>
<img src="../images/success message.png" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> Success message from "Interactive Maps with leaflet in R that confirms the learner met the object, find the DataCamp office on a map in code, congratulates them, and gives a brief intro of what's next in the course.
</figcaption> 

## Outcome
I helped write feedback messages on 26 courses (listed at the end of this page) as a Content Developer at DataCamp. Crafting feedback messages helped me achieve the highest average course quality rating among my peers (4.6/5). Creating high quality course in turn led to several more opportunities during my time at DataCamp, many of which you can read about in this portfolio.

## Takeaways
Writing good feedback messages is hard.  Providing just enough information to be helpful without giving everything away is a very delicate balance and it's impossible to get right 100% of the time. However, it's a crucial part of the learner's experience; good feedback helps them understand where they went wrong and how to course correct. Good feedback turns a setback into a learning opportunity, which in turn creates value for the learner.

<div>
<img src="../images/instagram.png" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>
<figcaption class="caption"> From DataCamp's Instagram: Posing for a not-so-candid shot with a fellow Content Developer.
</figcaption> 

Analyzing Police Activity with pandas, Analyzing Survey Data in R, Analyzing US Census Data in R, Biomedical Image Analysis in Python, Building and Optimizing Triggers in SQL Server, Categorical Data in the Tidyverse, Error and Uncertainty in Spreadsheets, Experimental Design in R, Factor Analysis in R, Financial Forecasting in Python, Foundations of Functional Programming with purrr, Improving Query Performance in PostgreSQL, ​​​​​​​Improving Query Performance in SQL Server​​​​, Improving Your Data Visualizations in Python, Interactive Maps with leaflet in R, Intermediate Data Visualization with Seaborn, Intermediate Functional Programming with purrr, Model Validation in Python, Network Analysis in the Tidyverse, Python for MATLAB Users, Statistical Simulation in Python, Structural Equation Modeling with lavaan in R, Support Vector Machines in R, Writing Efficient Python Code, and Writing Functions in Python.