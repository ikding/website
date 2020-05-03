Tackling climate change with ML (ICLR Workshop 2020) - day 5
############################################################

:date: 2020-04-30
:tags: climate_tech, data_science
:slug: tackling-climate-change-with-ml-iclr-day-5
:authors: I-Kang Ding
:summary: Notes from day 5 (Cross-cutting Methods Day) of ICLR Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/ICLR2020_workshop#schedule>`__ on 2020-04-30.

.. image:: https://iclr.cc/static/admin/img/ICLR-logo.png
    :align: center
    :alt: iclr-conference-logo


Notes from day 5 (Cross-cutting Methods Day) of ICLR Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/ICLR2020_workshop#schedule>`__ on 2020-04-30.

The virtual conference spans five days. If you're interested, here are the notes I took for other days.

* `Day 1 (Main Workshop) <{filename}../climate_tech/2020-04-26_tackling_climate_change_with_ml_iclr_day_1.rst>`_
* `Day 2 (Energy Day) <{filename}../climate_tech/2020-04-27_tackling_climate_change_with_ml_iclr_day_2.rst>`_
* `Day 3 (Agriculture, Forestry, and Other Land Use (AFOLU) Day) <{filename}../climate_tech/2020-04-28_tackling_climate_change_with_ml_iclr_day_3.rst>`_
* `Day 4 (Climate Science and Adaptation Day) <{filename}../climate_tech/2020-04-29_tackling_climate_change_with_ml_iclr_day_4.rst>`_


Incorporating physics into deep models with implicit layers
-----------------------------------------------------------

Zico Kolter, CMU

Abstract: Despite their wide applicability, many deep networks often fail to exactly capture simple "known" features of real-world data sets, such as those governed by physical laws.  In this talk, I'll present methods for integrating constraints such as physical simulation requirements directly into the predictions of a deep network.  Our tool for doing this will be the use of so-called implicit layers in deep models, layers that are defined implicitly in terms of conditions we would like them to satisfy, rather than via an explicit computation graph.  I'll discuss how we can use these layers to embed (exact) physical simulation within deep networks, discuss several related approaches, and highlight directions for future work.


ML background

* A common theme in applying ML models to real world settings: it is often very useful to have some physics-based model of system dynamics
* E.g. if we were to use a generic NN to predict how the input / output of your car would work, it will not go well
* Physics simulation is hard (strict constraints, collisions, etc) but also (to a first approximation really well understood
* Let's integrate what we know about physics (basic Newtonian mechanics) inside of more complex deep architecture
* How do we actually do this?

Implicit model in deep learning

* Implicit layers // implicit models: certain layer will have a “hard constraint” about wha it does - very intentional, very constrained.
* Very lucrative (in terms of publications)!
* It turns out that any structure you want to incorporate to a NN has some well defined functions of f(x, y; theta) = 0
* Example: physics, optimizations can be expressed in this way.
* Problem: ML training typically use gradient based methods to train your NN. But when you have an implicit layer, the gradient based methods (back prop, etc) doesn't always work
* Implicit differentiation, goes back many decades. This powerful tool will allow us to use the physics based equations in our back prop.
* Important point: we are not advocating to unroll the solution procedure of the implicit function, then backdrop through that. Can work, but very it's memory intensive, creates long graphs
* Instead: find exact solution, and backprop (analytically) through it

  * Much more memory efficient
  * Often effective “free” after computing forward pass


Learning with differentiable physics

* Incorporate a differentiable physics simulator within an implicit layer in a deep network: enforce the requirement that these physical elements of the network
* Three steps to build differentiable physics engine

  * Express equations of rigid body motion as linear complementary problem (LCP)
  * Apply implicit function theorem
  * Efficiency computing backprop

* Application: system identification (ball collision with chain)
* Application: simulation for visual dynamics
* Application: model-based RL for breakout (Atari break out game)

Incorporating decision-making into deep models

* The real cost in sustainability domains: in training ML models, we have an internal loss function to get our model trained. However, for ML models in the real world, the loss function you use in model training may not reflect the real cost.
* Reference: OptNet - differentiation through a convex QP solver


Fireside chat on remote sensing and artificial intelligence
-----------------------------------------------------------

Speakers:

* Victoria Coleman (Atlas AI)
* Ram Rajagopal (Stanford)
* Rose Rustowicz (Descartes Labs)
* Jack Kelly (Open Climate Fix)
* Grega Milcinski (Sinergise)


* Ram - Remote sensing: there is a lot of need to validate what's going on in the field. Given the imperfect information you get from remote sensing, how to you make informed decisions based off uncertainty?
* Computer vision is a more well developed problem for natural images (photos of things in real world), but the remote sensing data is different - much fewer labelled data, things are closely packed together, features are smaller - it may not be as much a “solved” problem as people think.
* Random Forest does just as well as deep learning for agriculture, and much more scalable
* Victoria: in agricultural applications, random forest can achieve equal or better result as deep neural networks. Do you have any insights on what makes agricultural application different from other remote sensing applications that makes it much suitable to be handled with random forest models? Also, what are the feature (columns) you feed into the RF model? Would it be just the RGB channel values at each pixel (so # of features == # of pixels x # of channels)?

  * Answer: I suspect it's because we do multiple passes which breaks down a complex problem into a number of simpler ones that RF works well for. Crop classification is done at the pixel level using both spectral and temporal features.

* How does your model influence the world? (e.g. solar production forecast) - say you have a perfect model, the way that the model can make impact on climate change is through convincing stakeholders (e.g. grid operators) that they can use the model, and the model is trust-worthy.
* Jack Kelly: we're currently entirely focused on PV nowcasting.  In the near future, we hope to release a dataset of satellite imagery & solar PV data for the UK, and we'd love for people to work on that!  We'll also be releasing more open source tools to work with the data.
* Descartes platform has been super helpful for researchers and students to use that platform.
