Lessons learned from building a community of Python users among Capital One's analysts
######################################################################################

:date: 2020-01-08
:tags: data_science
:slug: building-python-community-among-analysts
:authors: I-Kang Ding

**Note**: the content of this blog article came mostly from `my PyCon 2019 talk <{filename}./2019-05-05_pycon_talk.rst>`_.

A lot has been written about Capital One's commitment to go all-in on the cloud and open source software for many of our core business operations, processes, and machine learning models. To support this transformation, we embarked on a multi-year journey to build an internal Python community with a critical mass of users to help scale adoption of Python in our business analyst and data analyst workforces.

This article will highlight our multi-pronged approaches to overcoming organizational inertia while building a community of Python users, providing Python and OSS training, and encouraging Python adoption. We'll also share the best practices that we coalesced around, and lessons learned along the way.

Among Capital One's more than 47,000 employees, there are over 2,500 analysts whose jobs involve using data analyses to solve a variety of business challenges, find new opportunities, and make strategic or tactical recommendations. More concretely, their jobs may involve periodic business metrics monitoring and reporting, as well as ad-hoc deep-dives to support business critical projects.


Why Analysts and Why Python?
----------------------------

Our analysts have been doing this type of work for a long time using a variety of tools, so why teach them Python instead of letting them use their existing tooling sets? To answer this question, let's take a look at the table below that compares analysts' workflow in a traditional route vs. a Python-based route:

.. image:: https://www.capitalone.com/assets/tech/tech-assets/python-workflow.png
    :align: center
    :alt: python-workflow

As one can see, the traditional workflow is almost entirely manual which makes it more error prone and repetitive. On the other hand, the Python-based route allows users to automate their workflow and facilitate sharing of the both the processes and output to multiple stakeholders.

Furthermore, there are three reasons why we think Python in particular is great for our analyst workforces:

1. Ease of learning: Python has a very easy to understand syntax and a "batteries included" philosophy, which means that it comes with a very powerful standard library that already does a lot out the box. And, if you are not satisfied with the standard library, Python has an extensive ecosystem of additional libraries that can help you do the things you need to do. It is also compatible with a variety of notebook-like tools (e.g. Jupyter notebook), which exposes a very powerful computing environment to analysts who may not be familiar with programming.
2. Data-centric tools: Python comes with a lot of data-centric tools which is incredibly useful for analysts who deal with data day-in and day-out. They can use Python on tasks such as data ingestion using SQL engines or API interfaces; data wrangling using open source libraries such as pandas, NumPy, and PySpark; building machine learning models using scikit-learn, XGBoost, or TensorFlow; and data visualization with a variety of static or interactive data visualization libraries.
3. Good software engineering support: Python is a general programming language. Having all stakeholders - including analysts, data scientists, and software engineers - use and work on the same language drastically speeds up the pace of deployment. Imagine a scenario where data scientists are writing machine learning code in Python but have to pass that code to engineers who rewrite the pipeline in Java in order to deploy to production. Or a scenario where analysts write queries in SQL engine but have to wrap them in Python in order to automate their scripts. All these translations can induce errors and cost time. Having your data scientists, analysts, and software engineers working in the same language can speed up deployment.

That all sounds great. How hard can it be?

.. image:: https://www.capitalone.com/assets/tech/tech-assets/how-to-get-analysts-to-use-python.png
    :align: center
    :alt: how-to-get-analysts-to-use-python

First of all, not all analysts have a technical background or are comfortable writing code. In fact, some of our analysts may have never seen a terminal window in their life. Learning a new programming language with the goal of becoming more productive at work is a daunting task. Add to this that they also have a lot on their plates and learning Python may mean taking time away from their main projects - a time use which their managers and teammates may not support. Lastly, it's also not just about learning the Python programming language itself; in order to become productive using Python they also have to learn things like Unix command line, Git or GitHub version control, cloud computing basics, etc. All these concepts are necessary for analysts to migrate to, and become productive in, a new Python workflow.


Creating a Python Learning Curriculum Tailored For Our Analysts
---------------------------------------------------------------

While there is a wealth of free and publicly available Python learning resources online, we decided to build our own content in an effort to maximize the relevancy for our analyst population. By tailoring the material to the audience and adding a Capital One spin, we hoped to make the learning experience more engaging and impactful, thereby increasing the rate of actual adoption. Besides mentioning Capital One specific tools and techniques, we were able to use examples and data from familiar domains, provide context and case studies from well-understood areas, and even connect people with useful points of contact or resources within the company. In addition, we made plans to curate the content carefully, spending time working on crafting the best presentation possible for the material (including a beautiful and functional UI) with interactive elements wherever possible.

We called this training program the Big Data Academy (BDA), and targeted it mainly at analysts and quants - associates who generally had a good background in the modeling and business context aspects of the problem but did not come from a software engineering background. It was designed to work hand in hand with other organizations within the company such as Tech College, which complements BDA by providing content for associates with strong software engineering skills who could benefit more from learning fundamental math and statistics concepts.

.. image:: https://www.capitalone.com/assets/tech/tech-assets/bda-process.png
    :align: center
    :alt: bda-process

Since its founding in 2014, BDA's curriculum has grown to 18 self-paced courses spanning topics such as machine learning fundamentals, cloud computing, data manipulation, model deployment and monitoring, and various other topics. Two Python courses featured prominently in the foundational series, and as of March 2019 there were over 8,000 overall recorded course completions across the curriculum from about 3,000 associates.

Notably, these courses were largely developed and maintained by volunteers, which had the double benefit of facilitating continued community engagement while also allowing us to better scale content creation efforts. Furthermore, by hosting the courses on our internal GitHub, we could more easily track issues and iterate on the courses over time. Taken together, these factors were instrumental in allowing us to scale up to the many thousands of associates we wanted to reach.


Lessons Learned Along the Way
-----------------------------

Lesson 1: It takes a village (or rather, a community of practitioners)
======================================================================

When it comes to actually moving the needle on Python adoption, it's important to put yourself in the shoes of someone trying to learn the language for the first time. For a new adopter, it might seem like a lot of work for unclear payoff and it might be particularly difficult to start the learning process on your own. We found that it really takes a village to support large-scale motivation and adoption and to overcome these hurdles.

Some of the major problems with starting a solo Python learning journey stem from a lack of support from peers or managers who may want to continue doing things "the way they've always been done." Overcoming that organizational inertia can be difficult without a critical mass of people on the journey with you. It's also harder to learn best practices (especially with the less technical skills) without a peer network to review and critique your work.

One approach the BDA team took to address these problems is to develop a support system for analysts outside of their immediate teams. By including Python training in the context of enterprise-wide programs, and especially cohort-based programs, we aimed to encourage cross-functional networking, collaboration, and resource sharing. This allows the networks to form organically from the ground up, while still having support from the highest levels of leadership.

Once a community of practice has formed, it's also important to make it easy to contribute to and extract value from that community. BDA leans on GitHub heavily to make projects editable by anyone and enable passive knowledge sharing through living documentation. On the flip side, we work hard on maximizing discoverability to allow people to take advantage of existing work and Capital One specific tooling.

Slack is just one example of a tool that serves this purpose well, because it addresses many of the pain points learners have.

.. image:: https://www.capitalone.com/assets/tech/tech-assets/python-painpoints.png
    :align: center
    :alt: python-painpoints

On average, 23 questions are asked and answered on our #Python channel every week. With almost 2,000 associates in the channel, 820 have posted at least one message.


Lesson 2: You are going to be trouble-shooting people's system issues a lot
===========================================================================

As large numbers of people started on their learning journeys we noticed the same kinds of early-stage problems over and over again. Issues like environment setup or installation issues are particularly trying because the solutions can be hard to generalize (different kinds of computers and starting environments) and therefore represent a fixed amount of time that has to be spent on each individual before they can become self sufficient.

Sometimes, the learners' resourcefulness will backfire when they proactively find and copy a solution to their problem that is suboptimal, which is then propagated to their network. Beginners can bork their systems in really creative ways, especially when copying and pasting solutions with no clear "right answer."

As much as possible, we try to support learners by taking setup issues off their plates. At first, BDA used one centralized location to aggregate all the setup best practices and provide that source of truth. However, the next level solution to this is to use technology to provision environments automatically and on-demand. Shared analytical environments give us the ability to spin up pre-made Linux sandboxes at will with pre-installed Python environments. Each particular course can come with its own instructions for how to set up the container, which automatically takes care of the GitHub interactions, data access, etc.


Lesson 3: Incentivize learning and adoption with real-world examples
====================================================================
Making the setup easier definitely helped more people to start the courses. But we wanted more than that: we wanted analysts not only to complete the courses, but also use what they learnt in their daily work. This is a challenging goal to achieve.

After our foundation courses had launched and been in use for a while we saw a pattern emerge: many students started the course but never finished. Some got distracted, others got stuck on a challenging exercise, and some just never clicked the "complete" button. The initial outcomes were similar to most MOOCs (massive open online courses), although our completion rates were higher. Additionally, some associates were excited about the courses but struggled to use Python in their daily work, especially under pressure from deadlines.

Our foundation courses taught some necessary basics, but there was still a gap in the knowledge, and lack of confidence when using it, that made the adoption harder. The solution to this problem was to focus on teaching analysts how to do their work with Python. We partnered with analysts to identify and scale some of the best practices and better understand their pain points. Doing that helped us to reimagine their workflow in Python, creating content with and for them, instead of just teaching abstract concepts. Based on this work, we now provide examples and code cookbooks relevant to their day-to-day work, which they can easily use and apply.

Another important aspect in succeeding in our goal was to align with senior leadership on the importance of training. It helped with finding the time and space for analysts to learn and to start applying new tools. Some leaders encouraged their teams to go through the training together, and even motivated Python adoption with prizes. We also created dashboards to provide visibility into the course completion rates of their organizations, because what can be measured can be improved. This helped to foster friendly competition and motivated leaders to better encourage their teams to complete the courses.


Lesson 4: Encourage cross-pollination of ideas
==============================================

In the example above, we needed analysts' inputs to create tutorials that are relevant to them. It worked well, but it required some time and our input. But with hundreds of talented and creative analysts, we needed scalability, and we wanted to take the process of sharing best practices one step further.

We were facing issues that many big organizations face: analysts on different teams often solved similar problems over-and-over again. Furthermore, analyst teams could easily become siloed, reusing bad scripts and practices amongst themselves. While it was easy to explain how these scenarios happened, overcoming tribal knowledge, and the occasional non-standard practices it caused, was not.

Some analysts may prefer to start with GitHub search, but some good solutions are never discovered because the code was never committed (because the code was "not ready") or lives in a private repo.

And this problem is really tricky to solve - and, it's still a work in progress for us - but here are some approaches that worked.

* Instead of just advocating for best practices, codifying and championing them makes a difference. Cookie cutters and templates help to reduce the mental load of making choices when getting started.
* Providing gentle yet clear introduction of best practices helps analysts to write better code and eventually build it into a package - especially if it solves a common problem. For instance, if an analyst just learned the basics and has a bunch of hard-coded variables it means encouraging them to turn those magic numbers into variables. Then, helping them turn that code into functions, add docstrings and unittest. And finally, help them make it into a package that lives on GitHub so others can easily use it.
* Discovering what other teams are working on and discussing common challenges is also crucial to avoiding siloed-solutions. And while GitHub helps with discoverability, holding data-community conferences and monthly demos facilitates cross-pollination of ideas. So analysts can learn from one another, build on top of the existing projects, and avoid hitting the same problems over-and-over again.


Results and Takeaways
---------------------

Here are some of the results we have achieved with our Python analyst community here at Capital One:

* Community-maintained, self-paced Python and programming curriculum, with over 8,000 overall recorded course completions across the curriculum from about 3,000 associates.
* Active Python slack channel with close to 3,000 associates and dozens of new discussions each week
* Python is intimately intertwined with our Analyst Development Program, so that all newly hired analysts have the opportunity to get exposed to Python during their first 6-9 months at Capital One.

And, to summarize once again, here are some takeaways that (hopefully) will help you:

* Adoption is easier when you start with a cohort (but top-down support helps to get resources and align incentives).
* You can't completely escape the pain of setup, but you can separate that from the joy of programming. Cloud/DevOps best practices can help.
* Put yourself in others' shoes - reimagine people's workflow in Python instead of just describing in abstract how great Python is.
* Use best practices in your own coding and codify them to simplify adoption. Provide gentle yet clear introduction to others.

(Originally published on Capital One tech blog: `Lessons Learned From Building a Community of Python Users Among Capital One's Analysts <https://www.capitalone.com/tech/software-engineering/building-python-user-community-among-capital-ones-data-analysts/>`_)
