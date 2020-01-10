Data science in different industries
####################################

:date: 2016-07-03
:tags: career, data_science
:slug: data-science-in-different-industries
:authors: I-Kang Ding

Question
--------

What are data scientist's experiences in different industries?

Answer
------

I have worked as a data scientist in a semiconductor manufacturing industry, and as a data scientist in the financial service industry. I can compare and contrast these two industries, but keep in mind that I really only have a sample size of two companies...

The main difference I see in data science across these industries can be traced back to the type of data they deal with. In semiconductor manufacturing, the data point are devices (DUTs) and/or processes; in financial services, it is the customers and their behaviors. This seemingly obvious observation has ramifications on the relative importance of different types of models (**physics-based models vs. statistics-based models**).

In semiconductor manufacturing, physics-based models undoubtedly are treated as first-class citizens. We used simulation tools and physical models to guide our device design and roadmaps, and statistics-based models are often relegated to a secondary importance (use descriptive statistics to trouble shoot manufacturing excursions, for example). Furthermore, because we can *control* which devices to make and test, we can easily use design of experiment principles to figure out causation and not just inference.

For financial services, because the data points we deal with are actual people, there are no physics based models behind it. In this case, statistics-based model and inferential statistics is something we have to settle with. So it is a lot more similar to the machine learning problems that you see on kaggle challenges.

For the same reason, the financial services industry tend to have a lot more emphasis on the statistical modeling tools, best practices, and better infrastructure support, because being able to build a robust risk model is *literally* what makes the company tick. I’ve heard that semiconductor industry also started looking into the data science and statistics-based models. It is a transition I am looking forward to, but I think that the full embrace of this paradigm shift will take many years.

(Originally answered on quora: `What are data scientist's experiences in different industries? <https://www.quora.com/What-are-data-scientists-experiences-in-different-industries/answer/I-Kang-Ding>`_)
