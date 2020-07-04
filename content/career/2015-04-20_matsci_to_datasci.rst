From materials scientist to data scientist
##########################################

:date: 2015-04-20
:tags: career, data_science
:slug: matsci-to-datasci-transition
:authors: I-Kang Ding


Introduction
------------

This document is meant to share my experiences transitioning from a materials scientist by training (PhD in Materials Science and Engineering, worked in silicon valley in the optoelectronic industries as a process and characterization engineer for close to 4 years), before pivoting my career to data scientist. I made the transition first by taking a lot of courses on MOOC (Coursera), use R extensively during work, and attended a data science bootcamp (Data Incubator). I also spent some time talking about the interview experiences and the resources I used in preparing for those interviews.

This document is written in April 2015; the job hunting landscape will likely be different when you read this document, and what worked for me might not work for you. (Keep in mind that I only have sample size of one.) So, take everything I said with a grain of salt! Now, with that disclaimer out of the way...


Data Science and Big Data
-------------------------

What Is Data Science?
=====================

There are many different definition of data science, and you will be able to find at least a dozen different explanations online. But my own definition is pretty simple: **the data science is the field of extracting knowledge from data.** The data can vary from click streams in web traffic, the transaction data from financial institutions, the measurement and process data from semiconductor devices, or the reviews on the yelp website...etc.
Data scientist, in this regard, are the type of knowledge workers that can extract knowledge from data. The buzz started in 2012 when DJ Patil, in a Harvard Business Review article, called data scientist `the sexiest job of the 21st century <https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century/>`_. For a data scientist to do this job well, there are four different skill sets that are required, as extracted from the nice inforgraphic below:

* Math and Statistics (+ Probability)
* Programming & Database (+ Coding, Algorithms)
* Domain knowledge
* Communication and Visualization

.. image:: https://user-images.githubusercontent.com/7269845/86314472-c386e280-bbf5-11ea-9365-4ad54ebf1080.png
    :align: center
    :alt: ds-skills
    :width: 600 px


What is Big Data and Why is it So Popular?
==========================================

It has always been a good idea to collect and analyze data. With that said, the recent emergence of big data is really riding on the wave produced by the confluence of several trends, including (1) the ability to produce large **volume** of data, often with much **variety** and high **velocity**; (2) the ability to store large amount of data (enabled by cheap, distributed storage, managed by Hadoop ecosystem and the like; and (3) ability to analyze the said data with distributed computation / processing (Python/R, Spark, GraphLab, MapReduce)...

Business in different sectors are all trying to capitalize this trend; many of these business are trying to hire data scientists to extract insights from their data. A `McKinsey report published in 2011 <http://www.mckinsey.com/insights/business_technology/big_data_the_next_frontier_for_innovation>`_ estimated that,

    There will be a shortage of talent necessary for organizations to take advantage of big data. By 2018, the United States alone could face a shortage of 140,000 to 190,000 people with deep analytical skills as well as 1.5 million managers and analysts with the know-how to use the analysis of big data to make effective decisions.

However, during my interview with many companies, I definitely get the feeling that companies vary greatly in their expectation of what data scientists do. As previously mentioned, data scientists are people who can extract knowledge from data; furthermore, they are expected to work with cross-functional teams and business leaders to translate the knowledge into actionable insights.  With that in mind, let me elaborate a little bit about what data scientists are **not**:

1. Data engineers: data engineers are people who work with data scientists to make sure that the data pipeline is robust. They tend to focus more on building robust, scalable systems to make sure data scientists can get the data they need to. Data scientists, on the other hand, needs to know how to get data from the pipeline ("extract-transform-load", aka. "ETL" task) and perform analysis, but they often don't need to know the inner working of that pipeline. Without data engineers to build data pipelines, data scientists' jobs will be much harder. (However, in a startup environment, you might be expected to do both data science and data engineering.)
2. Software engineers: software engineers tends to have much stronger CS background. Their roles vary greatly in different companies and it's not the purpose of this document to cover what software engineers do. With that said, the jobs of software engineers tends to be more gear towards algorithms, coding, system design, and incorporation of new functionalities. On the other hand, the software engineers often don't have to analyze "data" per se, or communicate the results with stakeholders.
3. Business / data analysts: the distinction between data analyst and data scientist is less obvious than the comparisons above. Some companies will even call their "data analyst openings as "data scientists" to attract talent. In my mind, data analysts are most often tasked with answering concrete questions from business ("how many users visited our site last month? How did it break down by age / geographic locations / time?" … etc), whereas data scientists are expected to ask questions themselves, make predictions, and figure out action items ("Given the historical data, what is the expected server load next evening?", "What factors makes some users stay longer than others, and what can we do to make other users stay longer?"). In that sense, data analyst usually does "descriptive" analyses, whereas data scientist are tasked with "predictive" and sometimes even "prescriptive" analyses.  This added components of figuring out right questions to ask with little guidance and understanding concepts such as hypothesis testing and experimental design are the main things that separates data scientists from data analysts.


Outlook of the field
====================

With the 2014 Gartner hype cycle (below) listing "Big Data" as entering trough of disillusionment, it is natural to ask if we are entering a data science "bubble". I think my answer is, sure, there are some "frothy" layers in the big data industry, but there are also concrete values underneath.

The innovators and early adopters of data science are predominantly consumer web companies (Google, Facebook, LinkedIn, Amazon, Netflix, Twitter, etc), and the field is being greatly developed by these companies. For example, the Hadoop system was first introduced by engineers at Yahoo, Kafka is developed by LinkedIn, and Storm was developed by Twitter.

On the other hand, I think the "maturity" of data science is much lower at non web companies. However, that doesn't make the work there any less interesting. Many of the non-web companies are now starting to realize the importance and potential of big data and are rapidly expanding their teams. I truly think that big data is entering an even more exciting era – it is poised to make impact in many more sectors than before. These sectors include manufacturing (eg. Tesla, Intel, TSMC), biomedicine (eg. Merck, Pfizer), insurance (eg. GEICO, Allstate), automotive (eg. Tesla, BMW, Volkswagen), and healthcare (eg. Kaiser, McKesson), to name a few. The advent of internet of things (IoT) and personalized health is also leading to more data for us data scientists to extract insight from. The variety of applications in all the sectors is one of the reasons that I'm bullish on my data scientist career in the next 5-10 years.


Personal Background
-------------------

Academic Training
=================

Many of the PhD's-turned-data scientists dealt with a lot of data analysis in graduate school – think of physicists doing research in high-energy particle physics or astronomy. Myself, on the other hand, does not fit in this mold.

My academic training has been in chemistry (undergrad) and materials science (PhD), and my research projects has always been very experimental-oriented – from synthesizing nanomaterials in undergrad, to fabrication and characterization of solar cells in grad school. That means in my own research, every single piece of data point are from hands-on experiments, all the way from experimental design, processing, fabrications, characterizations, measurements, to final interpretations of the result. A learning cycle from beginning to end can often take days or weeks, and because the data is so expensive, there isn't really a lot of requirements for large-volume data analysis skills. Most of the data I dealt with can fit comfortably in Excel. I dabbled a little bit with coding in MATLAB when working on courses or file input/outputs, but honestly, my coding / programming skills was limited when I finished my PhD. However, during my PhD, I laid good foundations to the soft skills that are quite valuable in industry, such as teamwork, communication skills, and project management. For example, in my last project in grad school, I initiated and maintained collaborations with 4 research teams in 2 continents, and led the project all the way from ideation to final publication. I also gave research talks in multiple international conferences.


Industrial Experiences
======================

After academia, my first job out in industry was at a thin-film solar cell startup. My role at the company was still mainly hands-on experiments where I spent majority of my day fabricating the devices in clean rooms; I also started learning to code in MATLAB and Excel-VBA to work on the simulation and data analysis of solar cells. I found that I actually enjoy the coding component of my job as it was more intellectually challenging than many other hands-on tasks in the lab.

After working at the solar cell startup for close to one and half years, I landed a job at one of the top global LED manufacturers, to work in the technology characterization team. I was hired mainly because of my materials and semiconductors background, but the MATLAB and Excel VBA skills that I picked up at my previous job also came in handy.

This is my first job that primarily deals with data; as an engineer in an established company, I no longer have to do much of the hands-on experiments, and instead spent most of my time analyzing the data and authoring reports and presentations. In this job, the data I dealt with comes from a variety of sources (measurements, images, etc), but majority of the data are numerical, row & column (structured) data, and not "big data" by any stretch of imagination, since all the projects that I worked on had data that can comfortably fit in a laptop's memory.

I found myself enjoying the data analysis part of my job a lot! The analogy I used was that data analysis to me is like eating desserts. In grad school and my first job, I had to painstakingly do the hands-on work for weeks before doing my getting my favorite part (ie. the dessert) at the end, and at this job, my primary responsibility is to eat as much dessert as possible, so it was really like a dream come true.

With that said, I quickly found that the "old way" of doing things has a lot of room for improvement. When I started at the LED company, I was surprised to discover that the most commonly used software in data analysis (at least in R&D teams) is still Excel. There are some people who uses Minitab in the analysis, but both Excel and Minitab are inherently designed for "point-and-click" users, and provides only limited support for coding and automation. In carrying out the automation tasks, I initially was sticking with Excel VBA coding because (a) I already knew some VBA coding, and (b) it supports the best portability to other engineers since the output file is also an Excel file. However, it didn't take long for me to encounter the severe limitations of Excel Macro, both in terms of data processing and graph plotting.

Also around this time, I became more aware of the buzz surrounding big data. Therefore, both because of job necessity and personal interest, I decided to spend time and pick up R statistical programming language and other open source tools that are out there. This is my starting point in the world of data science. From there, I took a lot of MOOC courses, attended a data science bootcamp, and finally making the transition as a data scientist. In the next section, I will layout the resources I have used in making this transition.


Data Scientist Training Resources
---------------------------------

The good news for those who want to make the transition to data scientist career is that many of the resources can be accessed for little to no money. But it does take time and commitment to follow through – data science is such a new and evolving field that I don't think there will be adequate "crash courses" that can get you to employability in a short amount of time.

As a person who went through the PhD training, I have full confidence in my own ability and commitment to pick up new skills by myself. Furthermore, our financial situations didn't allow me to quit my industry job to go back of being a full-time student, so I was sticking with primarily MOOCs. With that said, in the past few years, there are quite a few on-site or on-line `master degrees in data science <http://www.mastersindatascience.org/schools/23-great-schools-with-masters-programs-in-data-science/>`_ that are popping up all over the US; there also has been an `Open Source Data Science Masters Program <http://datasciencemasters.org/>`_ that outlined a lot of the resources. But, because I haven't attend any of these programs, I can't speak much for its quality or employability. The informal feedbacks I received from the employers I talk to with respect to these programs (either MOOCs, data science master degrees, or bootcamps) is that all these programs looks promising, but they also are all fairly new such that neither has established a "track record" of churning out high-quality candidates. The employers are mostly still relying on their own screening criteria for the candidates, but if you have gone through any of these programs and have them on your resume, it is definitely a plus. For the rest of this section, I will talk a little bit about my own training from MOOC and data science bootcamps.


MOOCs
=====

MOOCs stands for Massive Open Online Courses. They are an ideal platform for those who are self-starters, has other commitments (eg. full-time job), or just want to "dip toes in the water". I really enjoyed the Coursera classes that I took because (a) it requires very little upfront financial commitment, (b) the flexible scheduling allows me to watch the lectures and work on the assignments at any time (in my case, usually during the commute, lunch, or after the kids has gone to sleep), and (c) most of the instruction has very good quality. On the other hand, the lack of student-teacher or peer-to-peer interactions means that it's up to you, and you alone, on how much you want to get out of the lectures.

MOOC platform are also quite effective in data science educations because most of the instructions and assignments are coding-based, and there are very little hardware requirements to get "hands-on" experiences. All you need is a modern laptop with internet connection. This is unlike the education in physical sciences, where the hands-on experiences require access to lab equipment and all the concomitant safety requirements.

Most of the data science related courses I have taken are through the Coursera platform. From what I understand, both Coursera and EdX are very good platforms that partner with a lot of the premier academic institutions (Coursera and EdX were founded by professors at Stanford and MIT, respectively), whereas Udacity is more focused on its affiliation with leading tech companies.

Here are the data science related courses I took on Coursera over the period of 1-1.5 years:

1. `Data Science Specialization <https://www.coursera.org/specialization/jhudatascience/1>`_, Johns Hopkins University: This is a very well organized series of 9 classes which covers the entire data science pipeline, including data wrangling, statistical analysis, machine learning, and data visualization. It is not as "math heavy" as some other classes that I took on Coursera, and is very much focused on the application (as opposed to theory) of the concepts. The entire series is conducted with the R programming language, which is one of the two de facto languages of choice in data science (the other being Python), so the skills that you learn here are very applicable to industry jobs. Coming from the biostatistics department of JHU, the classes provide very solid introduction to the traditional data analytics field, and the knowledge I acquired from this course was more than enough for me to do my data analysis tasks at the LED company. I was consciously migrating my projects from Excel to R to get more practice, which makes me much more adept at R and more productive at my job.

   What the specialization is slightly lacking is the more "contemporary" materials such as big data technologies and unstructured data analysis (eg. NLP). Then again, there are other classes that cover those topics, and it is perhaps unreasonable to expect the specialization to cover everything under the sun.

   The classes can be taken for free, but to get the "specialization" certificate, you will need to pay $450 to get "verified" certificate for all the 9 classes plus a capstone project.

2. `Statistics One <https://www.coursera.org/course/stats1>`_, Princeton University: This is a very good introductory statistics course (undergraduate-level). There are several stat-related courses on Coursera, and I simply picked this because it fit my schedule at the time. Most of the concepts in this course are "must-know" for data scientists. From what I heard, `Statistical Inference <https://www.coursera.org/course/statistics>`_ class by Duke University also has very good reviews.

3. `Introduction to Data Science <https://www.coursera.org/course/datasci>`_, University of Washington: this class covers a lot of the concepts in Big Data, at least from a high level. In my mind the course was a little bit too ambitious on the contents it covers in the assignments. For example, the first week's assignment was on using Python to analyze sentiments in Twitter feed data, and at the time, as one who has never been exposed to either Python or Natural Language Processing, I found the assignments quite challenging. Fortunately, even if you weren't able to complete all the assignments, the lectures still covers a lot of the big data concepts (SQL/NoSQL, Hadoop, MapReduce, parallel computing, etc) that can be very useful. It is definitely not enough instruction for one to be using those technologies hands-on, but at least you won't be totally lost when you hear those terms.

4. `Machine Learning <https://www.coursera.org/learn/machine-learning/>`_, Stanford University: this is widely regarded as one of the best introduction to machine learning courses available out there. The course uses MATLAB/Octave to take you under the hood in a lot of the machine learning algorithms – that means you often have to understand linear algebra enough to be able to implement the gradient descent / cost function yourself. It is more mathematically involved than other courses that I took on Coursera, but after you completed the course, you will have a much better appreciation about what goes under the hood when you run your machine learning algorithms.

5. `Mining Massive Datasets <https://www.coursera.org/course/mmds>`_, Stanford University: this teaches you a lot of the contemporary techniques in mining massive datasets (ie. data sets that you can't fit into the memory of a single computer). It is still a high-level overview course, not super mathematically intensive, and has a lot of overlap with the Intro to Data Science and Machine Learning classes mentioned earlier. It is also language agnostic –  you can pick your own language to use. (I did most of the homework in R).


Bootcamps
=========

In late 2014, I have finished most of the data science courses on Coursera, and I also felt that I was not learning and growing as much at my job, especially on the data analysis front. About this time, my wife has decided that she will quit her research program manager job of 6+ years to apply to PhD programs in her own field. Depending on where she ends up at, we are faced with a real possibility that we will need to move out of the San Francisco bay area next year. If we do, becoming a full-fledged data scientist will give me much better geographical flexibility than being a semiconductor materials scientist. Those two factors are the catalysts I needed to decide to make the transition in my career.

At the time, there are quite a few "bootcamps" that are available to aspiring data scientists. (`This article in 2014 <http://yet-another-data-blog.blogspot.com/2014/04/data-science-bootcamp-landscape-full.html>`_ provides a good overview.) These bootcamps are thematically similar – most of them last 6-12 weeks, assume that you at least have basic competency in the data science knowledge, and treat job placement as the primary end goal. The first program of its nature that I know of is Insight Data Science, but there has been a booming field of new programs in the past 1-2 years. The program I applied to was `Insight Data Science <http://www.insightdatascience.com/>`_ and `Data Incubator <https://www.thedataincubator.com/>`_ because both programs are geared exclusively toward PhDs (though, Data Incubator has opened their criteria to Masters as well), free for fellows, and appears to have good relationships with a wide array of employers. Long story short, I got into the Data Incubator bootcamp, took a leave of absence from my employer (I was open to my boss about my reasons to go through this and he was supportive – I was very lucky to have such a great boss), and spent seven weeks in DC in Jan/Feb 2015. I also am deeply indebted to my lovely wife who was extremely supportive of my decision, enough so that she was willing to be a single mom with two kids during those seven weeks.

In terms of the lecture and projects, I found the experience to be much more intense than I expected, especially given my foundation in the subject from all the Coursera courses. I spent most of my waking hours coding in Python, weekends included. It was not unusual to spend 10 hours per day working on your code, then do another 2 hours of job hunting activities after dinner. The program attempts to cover materials in a week that a more leisurely-paced MOOC course may cover in 4-6 weeks. However, as ambitious as the program is, there are only so much new materials you can digest in such a short amount of time. The MOOC courses that I took definitely prepared me for the data science / machine learning fundamentals, which gives me a leg up compared to other people. What I was lacking was the coding chops in Python, which I had to pick up fairly quickly through a never-ending browsing session on StackOverflow… Later in the interview process I also found that I lack many of the computer science / algorithm fundamentals, but more on that later.

The data incubator program at DC was structured in such a way that it covers a set of subjects each week – first week was SQL, web scraping, and network/graph data analysis; second week and third week on machine learning and natural language processing; and fourth week on big data technologies such as Hadoop, MapReduce, and Spark. Each week, there are a few mini projects that you are expected to complete, based on what was covered that week. This track is different from the New York City program (or the Insight Data Science program) that focused more on the "project" (web-app) which you have to churn out on 4 weeks. There are pros and cons for each approach.

The pros of having multiple people working on the same "mini-project" is that it is much easier to get help from your peers; and the mini-projects are well-rounded and covers a lot of the knowledge base that you should pick up along the way. This is in contrast to the "individual projects" where (a) everyone is working on different things so it was hard to get help from one another, and (b) if your project scope is too limited, you may not learn much from the process.

The cons, on the other hand, was that most of the mini-projects are focused on "getting the result right", but by the end, we don't have a nice, interactive data product that we can showcase to perspective employers. But that interactivity comes at an expense that you have to spend a significant chunk of your time learning and fine-tuning the front-end web development elements (HTML/CSS/d3.js) that may or may not help you much on the data science job interviews.

Aside from working on the projects, the Data Incubator also afforded us **amazing** networking opportunities, both with the employers and other aspiring data scientists. The networking aspect was especially important in my regard because, having done job search in industry, I realize how important the networking is.

On the employer side, the bootcamp partners with a long list of companies in a variety of sectors, and most of these companies are actively hiring data scientists. For almost every day in the first 3-4 weeks, anywhere from 1-3 employers will have panel discussions with us fellows regarding the company, what data science projects they are working on, and what skills they are looking for in data scientists. The presenters ranges from practicing data scientists, team managers, or VPs / CEOs. Without this bootcamp, it will be nearly impossible for me to get informational interview like this across such a wide spectrum of employers.

There are plenty of opportunities to network with employers in a social event as well – there were several happy hours based in DC and NYC that gives fellows and employers plenty of opportunity to get to know each other and ask more in depth questions related to the job that can't be covered in panel discussions. In fact, I met my future hiring manager at two separate happy hour event, which allowed us to explore the job-skill fit much more than what's possible during a 30-60 minute meeting in an on-site interview.

On the peer networking side, there are few things that can substitute a strong connection with other fellows built through "working in the trenches together" for several weeks and hanging out with one other in lunch, dinner, and weekends. A few years down the road, all these people could be your colleague at another company, so I felt very glad to have known these people!


Data Scientist Job Search Resources / Interview Processes
---------------------------------------------------------

Now that you have the skills and knowledge in data science, how do you go about finding a job? In this section I will outline the job search resources that I have found helpful, and break down the interview processes.


Importance of Networking and Connections
========================================

First of all, just to make it very clear from the beginning, I can summarize the three best ways to find job openings and to land interviews: connections, connections, connections! In all my job search process so far (I have done it three times after PhD, first two times as a materials scientist and third time as a data scientist), I haven't had a single interview from the company that I applied without some form of connections. I hope that gives you a better sense of how important connections are.

Where do you get the connections? You might think that, as an aspiring data scientist, you don't know anyone in this new industry. While that might be true, you are bound to know someone who know someone in the companies you are interested in. The way to find out is through LinkedIn. Assuming you identified the company you are interested in, but you have no 1st-order contact in that company, you can search that company in LinkedIn and find out if you have any 2nd-order contact in that company. Then, email your 1st-order contact for an intro. This works much better than cold-emailing people. When you actually get the chance to talk to the company insider, treat this as an informational interview. Offer to buy them lunch or coffee if the company is close, or give them a phone call if the person is far away. Things you could ask them about include: how did you find this job, how do you like the company, what do you work on in general, where do you think the hiring situation is going to be in the next couple of months, etc.

Another way to make connections includes attending data-science related meet-ups to get to know people. Identify the companies or people that you are interested in, find out if they are attending meet-ups / talks, and just go ahead and introduce yourself. Don't start the conversation by "are you hiring"; you can ask a few educated questions about their talks or posters, asking about their approaches and perspectives in the particular field, then ease into self-introduction and ask for job opportunities. You are your own advocate – if you don't go out and talk to people, you will not be able to make connections.


Social Networks in Job Search
=============================

I employ several different social network sites in job search – this is not limited to data science, but applicable to technical jobs in general.  Here is how each social networks / website complement each other in my case:

1. `Indeed <https://www.indeed.com>`_: you can set up job alerts here; this is a very good job aggregator, and you can set up the job alerts so that it will be delivered daily to your email. I set up alerts for "data scientist" jobs in San Francisco bay area, that would be a pretty wide net in itself. If you have companies that you are particularly interested in, you can set up company specific alerts such as: "Company:(Tesla) (Scientist OR Engineer) jobs".

2. `LinkedIn <https://www.linkedin.com>`_: LinkedIn: I use LinkedIn to find connections after I narrow down on a company that I am interested in. From there, I try to get informational interview from insiders; if timing is right, I can also ask for job referrals.  See the section on "Importance of Networking and Connections", above.

3. `Glassdoor <https://www.glassdoor.com>`_: Glassdoor let employees publish anonymous reviews of the employers. I use this website when I am doing research on the company that I am interested in, often before the information and on-site interviews. Check out both the Company Reviews and the Interviews to get to know people's experiences.

4. `Hired <https://hired.com>`_: this site is mostly geared toward software engineers and data scientists. If you can get your profile approved, you will be able to enter a reverse auction where companies look at your profile, names a price for you before you start interviewing. I haven't used it myself.

5. `AngelList <https://angel.co>`_: this is a job posting site that is more focused on startups. You can establish a profile there, and browse relevant job openings.


Types of Skill Sets and Job Functions in Data Science
=====================================================

As mentioned in an earlier section, data science is still a fairly new and evolving field. The result is that different companies may have different understanding and interpretation about what a data scientist should know or do. The analogy I have heard is that this situation is a bit like the medical field in the early/mid 20th century, where the concept of "specialization" had not yet been defined. In time this situation might change – I think we will see data scientist specializing in different domains, since the domain knowledge in finance is worlds apart from bioinformatics. But for now, the data scientist skillset can be usually divided into three aspects: Statistics / Probability, Coding / Algorithms, Domain Knowledge.

On top of the varied skill sets, a Data Scientist can also potentially focus on one (or more) of the many overlapping job functions. On the continuum of research vs. application roles, you could be a research scientist on machine learning (usually reserved for CS-PhDs willing to work at tech giants), an "applied" data scientist that are tasked to use existing algorithms to solve business problems, (I classify myself as this one), or a "business intelligence" professional that are more focused on presenting analysis results to stakeholders.

When you start job hunting, it is important to have a good idea about your strengths and weaknesses, as well as the job function you are mostly interested in. In my case, I was not trained as a CS-person, and I am far more interested in applying data science skills in solving business problems, so I was primarily applying to application-oriented data scientist openings.


Interview Prep Resources
========================

I'd like to list out the resources I found helpful in each of the "skill set" that you may be asked on data science. This is by no means an exhaustive list, and others have written great articles on this topic.

**Stats / Probability**: Most of the questions that I encountered during the interviews are can be covered with undergraduate-level statistics. You should be familiar with basic concepts such as:

* Independence
* Conditional probability
* Bayes Rule
* Common probability distributions (binomial, geometric, Poisson, normal, etc)
* Confidence intervals & p-values
* t-tests
* Anova (analysis of variances)

I found the undergraduate probability textbook by Ross (A First Course in Probability) a good resource. As for the statistics, I mainly reviewed the lecture notes from the Statistics One on Coursera. But honestly, any introductory statistics text should do.

**Coding / Algorithms**: This is the area that I had the largest gap to fill, since I've never received formal training in CS. But the good news is the knowledge you are expected to pick up is mostly freshmen- to sophomore-level CS, nothing harder. On the algorithm side, there are two highly recommended algorithm courses on Coursera, offered by Princeton and Stanford, respectively. At the minimum, you should understand these core concepts:

* Data structures: stacks, queues, deques, lists
* Sorting algorithms: hash table, bubble sort, selection sort, insertion sort, shell sort, merge sort, quick sort
* Tree algorithms: binary trees, priority queues with binary heaps, binary search trees
* Graph algorithms: breadth first search, depth first search, shortest path
* Recursion and dynamic programming

If you don't have time to attend the lectures on Coursera, then I recommend this interactive python-based algorithm tutorial, which contains enough materials for me to get through the interviews. I was never asked to implement any of the sorting techniques through whiteboard coding, but your mileage may vary.

**Machine Learning**: I found the Coursera machine learning class more than adequate in getting through the data scientist interviews that I had. Most of the questions I got on this aspect is less about the math under the hood, and more on the implementation or explanation level. (For example, "Can you explain how k-means clustering works to people with no math / engineering background?" "Explain two different classification algorithm (eg. naïve Bayes and decision trees), and give me an example scenario where one algorithm may be more appropriate than the other."

**Domain Knowledge**: Most of the data science interviews I had didn't ask much domain-specific questions at all, because companies that I've interviewed with were not expecting me to possess domain knowledge. Still, you should walk interview knowing at least what the company's business are, the general directions of the problems they are solving (recommendation engines, prediction algorithms, fraud detection… etc), and how your background fits in. If you were asked, "why do you want to work for our company?" You better have a clear and concise answer that shows that you've given this some serious thought.


Type of Interviews
==================

I have had several different "types" of interviews in my data scientist interviews, as explained below:

**Coding Challenge**: This is very much like the type of interviews that you will get as a software engineer. Most of the cases, you are expected to solve some computation or data manipulation problem, using a language of your choice (Python is better than R for this purpose – often, I couldn't even choose R in the platform the employers used). Ideally, your solution not only have to be correct, but also have to scale well. If you can solve a problem in O(n) time, don't solve it in O(n2).

The best sites for the practice questions is HackerRank or leetcode. Some example questions include:

* Write code that will calculate the n-th number in Fibonacci sequence.
* Write code that will pick out all the pairs of amalgams (eg: amy, may, yam) in a sentence and delete the duplicates

**Data Analysis Challenge**: This type of challenge is more specific to data scientists, and will test your skills on data manipulation, cleaning, and predictive modeling. Most often, the employer would give you a small dataset which you can easily deal with in modern laptops, and ask you to analyze the data and answer some specific questions that they asked. The questions often contain both descriptive and predictive components. For example, one of the dataset that I dealt with was the bike share ridership info, which contains information for tens of thousands bike share sessions across a 1-month span. For each entry, there are the date/time, starting/ending station ids, and bike ids. The descriptive questions may ask for "average amount of time a bike spends at a station in seconds", whereas the predictive question will ask for "predict the number of bicycles arriving at a specific station during a specific time span." In terms of level of difficulty, I found that most of the data challenges that I dealt with are either similar or slightly more difficult than the kaggle Titanic challenge.

There are a few things that are important to know when it comes to data analysis challenges:

* You often can stick with simpler models (eg. linear or logistic regression) to solve the problem – I didn't need use any of the more advanced algorithms (random forest, neural networks, etc) during any of the data challenges I had. But again, your mileage may vary.
* At the end of the analysis, your goal was not only to have good grasp on the modeling, but also provide a written document to explain, in laymen's terms, what you have found. This is because, as a data scientist, you are often expected to communicate the results with other non-data scientists, and employers want to test your communication ability.
* You must be able to analyze data with code (eg. R, python, and maybe MATLAB) – point-and-click programs such as Excel won't cut it! I did all my analysis in R and wrote reports in RMarkdown, but Python / iPython notebook will probably work too.

**Technical Interview (Phone or On-site)**: the technical components of the phone and on-site interviews are usually less hands-on. The interviewers will usually not ask you to derive things since there is not enough time; they may ask you to write short codes on the fly (via screen share or white board) as a mini-version of the coding / data analysis interviews. The questions ranges widely depending on the interviewer, the company, and the position you are applying to. No matter what the questions are asked, it is important to make the interview "interactive". You are talking with a live human being, so most of the time, you not only have to solve the problems correctly, but also have to "think out loud" so that the interviewer can follow your line of thought. This is the conversational version of "show your work".

There is a lot of resources available on the data science interview prep, so I won't bother repeating it here. I have used `120 data science interview questions <http://www.datasciencequestions.com/>`_ during my technical interview prep, but there are probably similar resources available for free.

**Business Interview**: I have encountered business/case interviews only in some of the companies I interviewed with. The questions ranges from more number-specific (breakeven analysis: given the following assumptions on fixed and variable costs, how many units of product do you need to sell to break even?) to more open ended questions that involved a lot of back-and-forth discussions with the interviewers (example: imagine that you have access to half of the US credit card transaction data. How do you use this data to consult your client, a big cafe chain, on which city in US to open their new branches?)

In terms of preparation: most of the companies I interviewed with didn't have business case interviews, so you should only prepare for it if it was specifically mentioned that this will be included. There are nice case interview tutorials available online, which gives you a flavor of the questions that may be involved.

**Behavioral Interview**: The behavioral questions are asked to figure out if you work will with others, how you handle conflicts, etc. Employers would prefer to have a crystal ball to figure out how you will behave in the future, but since they don't have that, the next best thing they can do is to see how you behaved in the past in order to predict your future with them. But, when you answer this kind of question, it is important to think of examples that back up your answer. Saying "I work well with others" is one thing; saying "in my last project I worked with three different research groups to bring the project to completion" is much better. One popular approach to answer this kind of questions is to use the STAR (Situation / Task / Action / Result) format. There are a wide array of internet resources available on this topic, which I won't bother repeating.

**Your questions for them**: During the phone and on-site interview, it is also your best chance to ask questions about the company and the job. This not only shows them that you are genuinely interested in the job (and have done your homework before the interview), but also is your best chance to collect information about the company. Remember, a job interview is a two-way process in which two parties (you and your potential employer) decide if they want to "go steady". Once you take their job offer you will likely spend several years with them, so this is not a decision to be taken lightly. They can't tell you what they are working on in detail because of the proprietary nature of their work, but hopefully you have done some homework before your on-site interview so that the Q&A time can be spent on things that aren't public knowledge (example of public knowledge: when they were founded, what are their business, who are the investors and what round of investment are they operating on, etc).

Sample questions that I asked include:

1. What would be my main responsibility if I am hired? What are some of the example projects I may be working on?
2. What is your day to day like?
3. What are the personal attributes that set a successful employee apart from others?
4. What does a successful first-year look like for new hire in this position?
5. How did you start in this company / why did you decide to work here?
6. Things that you like the most and the least about working at this company?
7. When can I expect to hear from you after this interview? – ask either the hiring manager or the HR this question to have a better sense about the timeline they make hiring decisions.

Note that the interview is NOT the time to ask about salary and benefits package, stock options, etc. That is something you negotiate AFTER you have formally received the job offer. (There is a nice, short book in compensation negotiation called "Negotiating Your Salary: How To Make $1000 a Minute" (Chapman). Highly recommended read, especially if you think there will be offers coming.)


Where Should You Work?
======================

Given that the data scientist job market is on employee's side (at least this was the case in 2015), you may end up having several offers to choose from. But, even before you start the interview process, you could use certain criteria in deciding which companies you want to apply. I thought about this question a lot during my job search interviews. My most important criteria at that time was that

1. I want to care about what the company is doing.
2. I want to optimize for my own learning opportunities in hands-on data science. (This, to me, means joining a company with an existing data science team)

Near the end of my job search, I came across this `article by StitchFix <http://technology.stitchfix.com/blog/2015/03/31/advice-for-data-scientists/>`_ that presents very good set of criteria:

1. Work for a Company that Leverages Data Science for its Strategic Differentiation
2. Work for a Company with Great Data
3. Work for a Company with Greenfield Opportunities

Anyway, this eventually boils down to personal preference, and you may be able to find out more about your own preference by talking to people. But you should be open-minded about learning what opportunities are available – for example, half a year ago I hadn't imagined that I would be working for my current employer! But as I have gotten to know more about the company's unique history and its mission, and have spoken with the team, I begin to realize that the opportunity fits the criteria very well. If I hadn't kept an open mind and be willing to learn more about prospective employers, this opportunity wouldn't have happened.


Conclusion
----------

Thank you for reading this far; I hope this document gives you the full picture of why and how I made the transition to data science. Now that I am officially hired as a data scientist, I am excited about the beginning of a new chapter in my career, and if you are thinking about making the same transition, I hope you find this document helpful on how one goes about making the leap!
