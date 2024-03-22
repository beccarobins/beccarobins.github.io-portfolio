---
layout: post
title: Site navigation
published: true
# subtitle: Excerpt from Soulshaping by Jeff Brown
thumbnail-img: ../images/20.png
share-img: /images/social-share-logo.png
gh-repo: beccarobins/beccarobins.github.io-portfolio
# gh-badge: [star, fork, follow]
gh-badge: [follow]
tags: [DataCamp, Information Architecture]
---

For my first few months as a Content Developer, I didn't even know we had instructor-facing documentation—and once I was finally introduced to "Authoring," I understood why the site was mysteriously left out of my onboarding. It turned out that our instructors were introduced to Authoring during the course design phase (i.e., the pre-Becca phase) and gave up on our documentation long before they ever reached development. This resulted in many hours spent regurgitating content guidelines in instructor 1:1s and focusing more on style suggestions than narrative in feedback. Following this revelation, I lobbied to overhaul Authoring and won! I led and managed the project and worked together with key stakeholders to get the new site launched on time.

## Problems
### Site navigation
Navigating Authoring was incredibly difficult. There was no real homepage or obvious structure—the site consisted of a long sidebar menu that you could scroll; you needed to keep your fingers crossed that the section heading matched what was in your head. Furthermore, headings were written using internal terminology and were frequently repeated, which further decreased clarity.

<div>
<img src="../images/bad instructor sentiment.JPG" alt="TBD Sorry." width="50%" height="50%" class="center">

<figcaption class="caption"> Frequent sentiment heard from instructors when discussing Authoring.
</figcaption>
</div>


<br>
<div>
<img src="../images/authoring navigation.png" alt="TBD Sorry." width="100%" height="100%" class="center">
<figcaption class="caption"> A sitemap of Authoring's navigation structure.
</figcaption> 
</div>

### Poor copy
The copy in Authoring was usually lackluster, often confusing, and occasionally, downright rude. Even if the reader could manage to find what they were looking for, it took real effort to read through the information.

<div>
<img src="../images/authoring welcome page.JPG" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> The "Welcome" page from Authoring, which provides the reader with a fairly confusing experience including a vague introduction to "our tools", an incentive to leave the site, and a call to action to create "premium" content without any explanation of what that means.
</figcaption> 

### Impossible maintenance
Maintaining Authoring was not easy...in fact, I never managed to figure it out! The documentation was built using GitBook, which is only easy for those with the necessary technical chops. GitBook requires knowledge of Git, a version control system, and comfort using the command line. If you're not familiar with Git or the command line, say, in the case that your sole responsibility is recruiting instructors, this tool poses a giant barrier to creating and maintaining documentation

<div>
<img src="../images/Authoring instructions.png" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> The instructions for getting started with GitBook on the README in the Authoring repo. There was a separate set of instructions for creatining and maintaining content. 
</figcaption> 

## Process
### Stakeholder interviews
Before diving into rewriting articles, it was necessary to meet with stakeholders to gather requirements and determine the scope of the project. I met with individuals who managed key products and processes from Product, Content, & Engineering as well as our Head of Support, who had very successfully rebuilt the Support Team's knowledge base just months before. While the number of stakeholders I met with may seem excessive, it proved to be the right decision. Not only did I have overwhelming buy-in from the team, but I was also able to secure additional resources to get the project done on time.

​Stakeholders

- Chief Experience Officer
- Product Manager, Teach
- Head of Content Engineering
- Head of Content Development
- Head of Curriculum
- Head of Content Quality
- Curriculum Lead, Projects, 
- Product Manager, Mobile
- Curriculum Lead, Courses
- Head of Support

### Competitive analysis
Following stakeholder interviews, I had a list of high-level requirements for the project. I used these requirements to perform a competitive analysis to compare different tools we could use for our new documentation. Intercom quickly rose to the top of the list, largely because we had just purchased an account for Intercom's chat widget feature. Furthermore, the widget was being used by our Product team to engage directly with instructors, our target audience, so the timing could not have been more perfect.

<div>
<img src="../images/competitive analysis.JPG" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> A competitive analysis of the documentation tools considered.
</figcaption> 

### Content audit
Lastly, an audit of Authoring's content was necessary. While several articles were headed for the scrap heap, reusable content was in there and any help to get this project across the finish line was welcome. The audit resulted in a list of articles that could be ported to the new site, articles that were destined for "the cull", and articles that were completely missing. It also produced an organized list of categories for the new site's structure.

## Outcome
In less than six weeks, instructor-support.datacamp.com was rolled out to instructors. The initial launch contained seven "collections," 95 articles, and Google Analytics tracking from day 1. In addition to the several benefits of using a purpose-built tool for documentation, our new knowledge base almost immediately wiped out the horrors we experienced with Authoring. It was the dawn of a new era!

### Improved navigation
The new instructor documentation had a distinct homepage with specific categories that allowed site visitors to quickly drill down into a topic of interest. Instructor Support's top-level navigation was broken into "product and process" collections, which were further divided into sections. It was now enough to know that you were designing a course to find the information you needed.

<div>
<img src="../images/instructor support site map.jpg" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> A sitemap of Instructor Support's original navigation structure.
</figcaption> 

### Easy maintenance
Creating and maintaining articles in Instructor Support required zero technical expertise, only an account, and the ability to click "new article." Articles in development were clearly labeled "draft", while live articles were labeled "published"; a simple toggle switched the article from one state to the other.

An added benefit of such a simple-to-use application is that crappy copy could be quickly updated—and hey, they're not all winners! Anytime you saw an error, whether it be a typo, a poorly constructed sentence, or just an out-of-date process, the only barrier was remembering your password.

<div>
<img src="../images/Article example.png" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> An example article from Instructor Support.
</figcaption> 

### Bonus: professional design
An additional win was that Intercom's native features gave Instructor Support a substantially more professional look than Authoring. The customizable background (a fairly standard knowledge base feature) allowed easy branding of the site, which also helped lend credibility to our documentation—it now looked like the Content Team actually spent time on documentation!

<div>
<img src="../images/Before after instructor support - arrow.JPG" alt="TBD Sorry." width="100%" height="100%" class="center">
</div>

<figcaption class="caption"> DataCamp's external-facing instructor documentation before (left) and after (right).
</figcaption> 

## Takeaway
Documentation isn't sexy and it is a lot of work (that never really ends) BUT if done carefully, it is very rewarding. In addition to receiving recognition for a job well done, I amassed A TON of institutional knowledge during this project. The skills and information gained during this project led to an incredible amount of growth and opportunities during my time at DataCamp. If you want my (unsolicited) advice: if you have the opportunity to rebuild your team's documentation from the ground up, do it! Future you will thank you.

<div>
<img src="../images/colleague quote.JPG" alt="TBD Sorry." width="25%" height="25%" class="left">
<img src="../images/Instructor quote good.JPG" alt="TBD Sorry." width="70%" height="70%" class="right">
</div>

<figcaption class="caption"> Quotes from a colleague (left) and an instructor (right) following the launch of "Instructor Support". Feedback was overwhelmingly positive.
</figcaption> 