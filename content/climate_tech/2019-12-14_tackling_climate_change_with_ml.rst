Tackling climate change with ML
###############################

:date: 2019-12-14
:tags: climate_tech, data_science
:slug: tackling-climate-change-with-ml
:authors: I-Kang Ding

.. image:: https://upload.wikimedia.org/wikipedia/commons/d/d1/20181204_Warming_stripes_%28global%2C_WMO%2C_1850-2018%29_-_Climate_Lab_Book_%28Ed_Hawkins%29.png
    :align: center
    :alt: warming-stripes

I attended the NeurIPS 2019 Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/NeurIPS2019_workshop.html>`_ remotely on 2019-12-14. Below are the notes I took from the talks that I attended (which is just a small subset).

Note: Many of the discussions on this workshop is a follow-up to the `paper <https://arxiv.org/abs/1906.05433>`_ of the same name, published on arXiv.

The recording for the full workshop is available here: https://www.climatechange.ai/NeurIPS2019_workshop.html#schedule


Computation + Systems vs Climate Change (Invited talk) - Jeff Dean (Google AI)
------------------------------------------------------------------------------

* We are rapidly running out of carbon budget
* Google's (many) goals: getting to zero-carbon computation
* They have been able to use 100% renewable energy - averaged over entire year and all location
* Computation and ML can help with climate change
* Bayesian inference to drive interesting insights from observation in the world. Tensorflow probability framework is used to help research on nuclear fusion energy (in conjunction with TAE)
* Improving climate models: Simulation -> TPU -> Flood forecasting

  * "Google flood forecasting initiative"
  * Flood forecasting in a nutshell: physical measurements -> hydrologic models -> hydraulic model (involving soil, elevation maps, etc)
  * Hydraulic model is key in improving the flood forecasting
  * Challenge: each doubling of resolution means compute goes up by 8X
  * Solution: TPU can drastically speed up these sorts of computations
  * Ultimate goal: flood warnings via Google Public Alerts

* Simulation -> Neural network proxies -> Tensorflow -> Weather prediction

  * PDE models the world: weather and climate, aerodynamics, combustion
  * Neural network vs PDE simulation: NN has faster compute, higher spatial and temporal resolution. PDE has better medium to longer term precision.

* "Climate is the problem of 21st century"
* Can we use technology to help people making better choices? (What information do people need to make good decisions?)

  * Environment insights explorer
  * Project sunroof

* Challenge to the community: build climate decision tools for AI & ML, while tackling all the high leverage points


Leveraging digitalization for urban solutions in the Anthropocene - Felix Creutzig (MCC Berlin, TU Berlin)
----------------------------------------------------------------------------------------------------------

* PV is now the least cost technology in many parts of the world
* Key barrier to widespread adoption is cost of finance (> 10% interest rate)
* Solution: getting finance guarantees (loan guarantees, etc)
* 12 Leverage points (place to intervene in a system, Donella Meadows, 1999)

  * #4: Foster self-organization
  * #6: Create new feedback loop
  * #7: Dampen positive feedback loop
  * #10 leverage points: physical structure - urban layout that influence energy usage

* What we plan now will translate into futures emissions
* Urban form determines usage and efficiency
* AI for geographically explicit solutions
* Optimize infrastructure

  * making use of unbiased and spatially complete remote sensing data
  * Train with ground tough data
  * use generalized learning to calculate spatialized energy use or intermediate metrics
  * Model urban planning scenarios and predict associated GHG emissions

* Example: block level energy prediction from ANN
* Example: estimate building energy use at scale
* Example: simulate role of fuel taxes


Panel: Climate Change: A Grand Challenge for ML - Yoshua Bengio, Andrew Ng, Carla Gomes, Lester Mackey, Jeff Dean
-----------------------------------------------------------------------------------------------------------------

**Question**: exciting developments in algorithms for climate change?

**Answers**:

* Andrew Ng: AI on small datasets. Example: transfer learning
* Carla Gomes: scale up solutions for unsupervised learning

**Question**: we read the paper, now what?

**Answers**:

* Andrew: Small steps. The problem is big and intimidating. It's important to take small steps.
* Jeff: be willing to collaborate with people who may know different things we do
* Yoshua: ML community has a tendency to tackle the problem with hubris. We need to approach problem with humility. Otherwise, we're at the risk of "reinvent the wheel badly".

**Question**: reconciliation of misaligned incentives: e.g. # of publications vs. tonnes of CO2

**Answers**:

* Andrew: Our job is not done when we published a paper; our job is done when we actually make an impact. Lots of work needs to happen to deploy your fancy ML models to make real-world impacts.
* Yoshua: change your objective function! ML community also chase the ML publication.
* Andrew: find your principles!

**Question**: AI can also enable solutions to increase CO2 emission - e.g. help find more oil. What can we do about that?

**Answers**:

* Yoshua: "public shaming" :)
* Andrew: same question on the "ethics of AI" can be applied to many fields outside of climate change

**Question**: How do you make sure that AI solutions are actually matching the problem? How do you find solutions that maximize GHG emission reductions?

**Answers**:

* Yoshua: each of us should ask "how I can help". As an AI researcher I think about how I can make impact to climate change. It's not for everyone though.

**Question**: What will you say to the room?

**Answers**:

* Yoshua: Climate change will also force us to ask and introspect how the things are done in our society / construct. Maybe this problem will force humanity to rethink how our society is organized.
* Andrew: "Importance of community: genuinely celebrate other people's success. Each of us to spend time to help other on favors, celebrate others' successes, etc
* Carla: I have full respect for researchers in this climate change field because it's a difficult problem.
* Lester: don't be afraid to work on something that may not further your career, but help the planet.
* Jeff: ML is a great tool that we can use to help many fields. Be open to collaborate with others, celebrate successes when we can.


Panel: Practical Challenges in Applying ML to Climate Change - John Platt, Jennifer Chayes, James Kelloway, Marta Gonzalez, Matt Horne
--------------------------------------------------------------------------------------------------------------------------------------

Panelists:

* Jennifer Chayes - Microsoft research
* James Kelloway (National Grid ESO)
* John Platt - Google AI
* Matt Horne - City of Vancouver
* Marta Gonzalez (UC Berkeley, LBNL)

Bottleneck for applying ML to climate change:

* Jennifer: Misaligned incentive as researcher to chart your own territory vs doing interdisciplinary work
* James Kelloway: think about how the ML solution you built is meant to be used in the real world. e.g. optimization solution can't really be implemented in a world where your solution involved having a human being tweaking a button 5 times a second
* Marta Gonzalez: data availability and inter-operability. Just because the data can be found / downloaded doesn't mean that they are ready to be used.
* John Platt: collaborate with other fields and speak on the same language takes a long time.
* Matt: balancing ML & data needs vs privacy

Two types of models:

* Discovery model, business intel models
* Model that makes automatic decisions - needs to be closely monitored and and maintained

What keep you optimistic?

Jennifer: there is this sea of change among young people (students in UC Berkeley) who wants to work on climate change, despite the fact that they are working on different fields.

She doesn't think it'll be professors who drag students into the climate change research field; she thinks it'll be the other way around of having graduate students dragging their professors.

Example:

UC Berkeley stats PhD program asked incoming students what they would like to work on (free form, not multiple choice). A third of them said they wanted to work on climate change, and that's in statistics! (This is extremely encouraging)
