Software engineer salary: a statistical approach
################################################

:date: 2016-03-31
:tags: career
:slug: software-engineer-salary-statistics
:authors: I-Kang Ding

Question
--------

What percentage of software engineers make at least $200,000?

Answer
------

Edit 2016-03-31: The bureau of labor statistics published the 2015 annual data on 3/30. The original answer included only 2014 data, but the updated answer include both 2014 and 2015.

-----------------------------------

I originally was interested in this question and clicked "Follow", but then the curiosity got the better of me so I decided to do the analysis myself.

Before answering this question, I'd like to make a few qualifier statements:

1. Let's assume you are asking about $200,000 base salary, not the total package (with 401k match, RSUs, ESPPs, bonuses... etc) - those things can vary widely
2. You didn't say which geographical area you are looking for, so let me assume that it is the United States.
3. I tried to find "official" sources as opposed to anecdotal statements ("yeah, my friend says all his/her friends in software are just raking in money")

It turned out that U.S. Bureau of Labor Statistics (BLS) published, on a regular basis, the `Occupational Employment Statistics <http://www.bls.gov/oes/home.htm>`_ that breaks down the wages of each occupation by region. The most recent data is from May 2015 and can be found `here <http://www.bls.gov/oes/current/oessrcma.htm>`_.

The html table only contains the mean annual salary of each occupation by area, which is a good start, but we still need the distribution! Fortunately, that number is in the a zipped file that you can download. Using quantiles of the annual wage (10%, 25%, 50%, 75%, 90%), if we assume that the wages follow normal distribution (which may be a big if), we can calculate the metrics you are interested in, for the top 9 metros with the highest software engineer employment.

Percentage of software engineers that makes at least $200,000 (base salary).

=============== =========== ===========
    metro_area      2014        2015
=============== =========== ===========
Atlanta         0.06%       0.09%
Boston          0.84%       0.74%
Chicago         0.01%       0.07%
Dallas          0.03%       0.06%
New York        1.13%       1.51%
San Francisco   2.09%       1.96%
San Jose        6.47%       8.70%
Seattle         0.35%       0.59%
Washington      1.06%       1.59%
=============== =========== ===========

How much base salary do you need to be the 1% engineer (in terms of base salary) in a particular metro.

=============== =========== ===========
    metro_area      2014        2015
=============== =========== ===========
Atlanta         $ 169,763   $ 173,444
Boston          $ 197,591   $ 195,898
Chicago         $ 161,412   $ 171,802
Dallas          $ 167,756   $ 172,522
New York        $ 201,857   $ 206,651
San Francisco   $ 211,968   $ 210,098
San Jose        $ 232,678   $ 240,306
Seattle         $ 188,763   $ 194,143
Washington      $ 200,862   $ 207,315
=============== =========== ===========

As a bonus, we can also plot the normal distribution of salary in each metro:

.. image:: https://qph.fs.quoracdn.net/main-qimg-60df3d6a971d5e8526f892f7a3c6b8b0
    :align: center
    :alt: nominal-salary-distribution

A few other observations:

1. San Jose (more precisely, "San Jose-Sunnyvale-Santa Clara, CA MSA") appears to have the best base salary. A whopping 8.7% of software engineers there earn > $200,000 base salary in 2015, compare with < 0.1% for Atlanta, Chicago and Dallas!
2. San Francisco ("San Francisco-San Mateo-Redwood City, CA Metropolitan Division") has comparable median salary with Seattle and Boston, but distribution is wider - perhaps because of many startups in the area?
3. Software engineers in Atlanta, Chicago and Dallas are underpaid related to other big metros (but they also have lower cost of living)

However, if you take into account the cost of living, than the story changed - drastically. After adjusting the salary for cost of living (using
`C2ER COLI <https://www.coli.org/>`_ annual average data for 2014 and 2015, respectively), here is what the salary distribution looks like. Dallas and maybe Atlanta now appears to have the highest earning (adjusted for cost-of-living), with Seattle and San Jose area close behind. SF and NY folks appear to get the shorter end of the stick because their cost of living is so expensive.

.. image:: https://qph.fs.quoracdn.net/main-qimg-b0b7db148172874b6751c43596e53a75
    :align: center
    :alt: coli-adjusted-salary-distribution

But if you really adjusted for cost of living, the metro with highest median wage for software engineer (with at least 2,000 total employment) is neither of the 9 big metros above. Instead, here is the ranking - I am surprised myself!

Metro area (coli-adjusted median annual salary) - 2014:

1. Durham-Chapel Hill, NC ($110,404)
2. Huntsville, AL ($108,334)
3. Colorado Springs, CO ($106,387)
4. Baltimore-Towson, MD ($106,359)
5. San Antonio-New Braunfels, TX ($103,386)
6. Fort Worth-Arlington, TX ($102,289)
7. Austin-Round Rock-San Marcos TX ($101,521)
8. Charlotte-Gastonia-Rock Hill NC-SC ($101,248)
9. St. Louis MO-IL ($100,953)
10. Houston-Sugar Land-Baytown TX (99,725)

Metro area (coli-adjusted median annual salary) - 2015:

1. Huntsville AL ($115,853)
2. Colorado Springs CO ($112,156)
3. Raleigh NC ($105,147)
4. Houston-The Woodlands-Sugar Land TX ($104,649)
5. Fort Worth-Arlington TX ($104,539)
6. St. Louis MO-IL ($104,012)
7. Austin-Round Rock TX ($103,381)
8. San Antonio-New Braunfels TX ($103,278)
9. Charlotte-Concord-Gastonia NC-SC ($102,624)
10. Baltimore-Columbia-Towson MD ($101,774)

(Originally answered on quora: `What percentage of software engineers make at least $200,000? <https://www.quora.com/What-percentage-of-software-engineers-make-at-least-200-000/answer/I-Kang-Ding>`_)
