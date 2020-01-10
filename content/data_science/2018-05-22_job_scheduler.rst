Python job scheduler
####################

:date: 2018-05-22
:tags: data_science
:slug: python-lightweight-job-scheduler
:authors: I-Kang Ding

Question
--------

What's the most lightweight job scheduler for Python that can be used by a data scientist?

Answer
------

cron should work if you are looking to just run some python script at a scheduled time.

If you are doing something more complex in your job scheduler, such as chained tasks that are best expressed as directed acyclic graphs (DAGs) of tasks, you should checkout airflow or luigi.

(Original answered on quora: `What's the most lightweight job scheduler for Python that can be used by a data scientist? <https://www.quora.com/Whats-the-most-lightweight-job-scheduler-for-Python-that-can-be-used-by-a-data-scientist/answer/I-Kang-Ding>`_)
