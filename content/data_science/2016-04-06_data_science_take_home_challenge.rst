Data science take home challenges
#################################

:date: 2016-04-06
:tags: data_science
:slug: data-science-take-home-challenge
:authors: I-Kang Ding

Question
--------

What are some ways to prepare for a "data challenge" with a Silicon Valley tech company? How do I make sure I have sufficient fluency with data munging and ML in Python?

Answer
------

This type of challenge is more specific to data scientists, and will test your skills on data manipulation, cleaning, and predictive modeling. Most often, the employer would give you a small dataset which you can easily deal with in modern laptops, and ask you to analyze the data and answer some specific questions that they asked. The questions often contain both descriptive and predictive components. For example, one of the dataset that I dealt with was the bike share ridership info, which contains information for tens of thousands bike share sessions across a 1-month span. For each entry, there are the date/time, starting/ending station ids, and bike ids. The descriptive questions may ask for "average amount of time a bike spends at a station in seconds", whereas the predictive question will ask for "predict the number of bicycles arriving at a specific station during a specific timespan."

Here are what I learned through performing several rounds of data analysis challenges from interviewing with different companies a while back:

* Stick with the modeling method you are comfortable with, and be prepared to justify why you choose a particular set of modeling methods. The justification shows a deeper layer of understanding than just the scikit-learn's API.
* At the end of the analysis, your goal was not only to have good grasp on the modeling, but also provide a written document to explain, in laymen’s terms, what you have found. This is because, as a data scientist, you are often expected to communicate the results with other non-data scientists, and employers want to test your communication ability.
* You must be able to analyze data with code (eg. R, python, and maybe MATLAB) – point-and-click programs such as Excel won't cut it! I did all my analysis in R and wrote reports in RMarkdown; others have used Python / iPython notebook.

(Originally answered on quora: `What are some ways to prepare for a "data challenge" with a Silicon Valley tech company? How do I make sure I have sufficient fluency with data munging and ML in Python? <https://www.quora.com/What-are-some-ways-to-prepare-for-a-data-challenge-with-a-Silicon-Valley-tech-company-How-do-I-make-sure-I-have-sufficient-fluency-with-data-munging-and-ML-in-Python/answer/I-Kang-Ding>`_)
