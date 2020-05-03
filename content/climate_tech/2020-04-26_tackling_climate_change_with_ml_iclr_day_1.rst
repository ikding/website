Tackling climate change with ML (ICLR Workshop 2020) - day 1
############################################################

:date: 2020-04-26
:tags: climate_tech, data_science
:slug: tackling-climate-change-with-ml-iclr-day-1
:authors: I-Kang Ding
:summary: Notes from day 1 (Main workshop) of ICLR Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/ICLR2020_workshop#schedule>`__ on 2020-04-26.


.. image:: https://iclr.cc/static/admin/img/ICLR-logo.png
    :align: center
    :alt: iclr-conference-logo

I attended day 1 (Main workshop) of ICLR Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/ICLR2020_workshop#schedule>`__ remotely on 2020-04-26. Below are the notes I took from the talks that I attended. Day 1 of the conference had a jam-packed schedule, but because of the time zone difference, I was only able to attend a small subset of the talk.


Panel: intersection of climate change and machine learning
----------------------------------------------------------

Dan Kammen, Dan Morris, Jessica Thorn, John Platt, Nana Ama Browne Klutse, Stefano Ermon

Join us for a panel discussion on the theory and practice of doing work at the intersection of climate change and machine learning. Panelists include:

* Dan Kammen: Dr. Daniel M. Kammen is a Professor at the University of California, Berkeley, with parallel appointments in the Energy and Resources Group where he serves as Chair, the Goldman School of Public Policy where he directs the Center for Environmental Policy, and the department of Nuclear Engineering.
* Dan Morris: Dan Morris is a Principal Scientist at Microsoft, where he runs the AI for Earth program, focused on accelerating innovation at the intersection of machine learning and environmental sustainability. His work includes computer vision applications in wildlife conservation, for example the AI for Earth Species Classification API.
* Jessica Thorn: Dr. Jessica Thorn is a Research Associate working with Prof. Marchant on the Development Corridors Partnership, supported by the Global Challenges Research Fund. Concurrently, she holds an African Women in Climate Change Science fellowship (AWiCCS), and Climate Research 4 Development fellowship hosted by the African Climate and Development Initiative at the University of Cape Town.
* John Platt: John Platt currently leads the Applied Science branch of Google Research, which works at the intersection between computer science and physical or biological science. His latest goal is to help to solve climate change. Previously, he was Deputy Director of the Microsoft Research Redmond lab, and was Director of Research at Synaptics.
* Nana Ama Browne Klutse: Dr. Nana Ama Browne Klutse is currently an AIMS-Canada Research Chair in Climate Change Science with AIMS Rwanda, and a Senior Lecturer at the Department of Physics, University of Ghana. She is also a Lead Author in Working Group 1 of the Intergovernmental Panel on Climate Change Sixth Assessment Report (2018 to 2021).
* Stefano Ermon: Stefano Ermon is an Assistant Professor of Computer Science in the CS Department at Stanford University, where he is affiliated with the Artificial Intelligence Laboratory, and a fellow of the Woods Institute for the Environment.

**Question**: Places where ML can make impact on climate change?

**Answers**:

* Better climate / weather models
* Use remote sensing to have better evaluation of economic activities, and impact of policies on economies and climate change.
* Google sunroof: example of computer vision being applied to make impact on climate science
* Helping domain experts more productive through computer vision and tool building

**Question**: Challenges of ML models in Machine Learning world

**Answers**:

* ML models often have had a hard time being "believed" by domain experts, unless there's way to use models on synthetic data and show that the models matches with what the experts agree on physics-based principles.
* There's no way for non-technical experts (e.g. policy makers) to really become "co-equals" with ML researchers, unless the non technical stakeholders have way to "play / tweak" models themselves without writing code. This may involve more efforts on building simplified version of your model, and allow non technical people to use it with a UI to play with different scenarios. This takes more time (and different sets of expertise) than what ML researchers are used to.

**Question**: Applications that can help with negative emissions

**Answers**:

* Preserving wetlands, restorative agriculture


Measuring Economic Development from Space with Machine Learning - Stefano Ermon (Invited talk)
----------------------------------------------------------------------------------------------

Abstract: Recent technological developments are creating new spatio-temporal data streams that contain a wealth of information relevant to climate adaptation strategies. Modern AI techniques have the potential to yield accurate, inexpensive, and highly scalable models to inform research and policy. A key challenge, however, is the lack of large quantities of labeled data that often characterize successful machine learning applications. In this talk, I will present new approaches for learning useful spatio-temporal models in contexts where labeled training data is scarce or not available at all. I will show applications to predict and map poverty in developing countries, monitor agricultural productivity and food security outcomes, and map infrastructure access in Africa. Our methods can reliably predict economic well-being using only high-resolution satellite imagery. Because images are passively collected in every corner of the world, our methods can provide timely and accurate measurements in a very scalable end economic way, and could significantly improve the effectiveness of climate adaptation efforts.

* Data issue:

  * Developing countries are likely to be negatively impacted by climate change
  * But data on the ground is sparse at developing countries
  * If you can't see it, you can't solve it
  * Solution: remote sensing. Landsat -> satellite now, the spatial resolution has been greatly improved! From 30m to 3-5m resolution.

* Ermon's group is working on using satellite images to estimate poverty measures

  * Off the shelf technique often don't work because there are very small amount of labelled data
  * Technical challenges: lots of images, very few labels
  * Need to use methods like semi-supervised learning, transfer learning, etc

* Tile2Vec:

  * Good example of transfer learning: Word2Vec, continuous word vector representations. Assumes "words that appear in similar contexts have similar meanings"
  * Tile2Vec: extension of that concept to geospatial data. Extends distribution hypothesis to geospatial data. "Everything is related to everything else, but near things are more related than distant things" (Similar location <-> similar meaning)
  * Train triplet loss on tiles close to vs away from each other
  * Example task: classify crop types. RGBN images -> predict 57 crop types
  * Tile2Vec can outperform state-of-art CV algorithms such as ResNet, DenseNet, inception models in the sparsely labelled data regime.
  * This method have ~ R^2 of 0.7 of Uganda asset-price (proxy for poverty) using only satellite images from space

* Highlighted Projects:

  * use geo-tagged pictures from wikipedia to help with building classification from satellite images
  * remote sensing data -> deep gaussian process -> USDA soy bean production


Climate, biodiversity, and land: using ML to protect and restore ecosystems - Dan Morris
----------------------------------------------------------------------------------------

Abstract: When we think "ML for climate change", we often think of climate forecasting, energy grid optimization, greenhouse gas reduction, and other opportunities for ML to impact the direct causes and effects of global warming. But in this talk, I will present the close relationships among climate, biodiversity, and land use, and I will discuss opportunities for ML to support climate change mitigation by accelerating efforts in all three of these areas. Furthermore, this workshop's mission states that "many in the ML community wish to take action on climate change, yet feel their skills are inapplicable"; I hope to convince the audience that one of the best ways we can put ML to work – and often the easiest way for ML students and practitioners to get hands-on experience with environmental sustainability – is to focus on some of the "small" problems whose solutions will make the day-to-day work of conservation scientists and practitioners more efficient.

Key takeaways:

* Climate, biodiversity, and land use are intertwined
* ML can help in all three areas: go play with the data!
* Don't sleep on the small problems that make the experts more efficient
* AL for Earth is a thing and we want to help you

`AI for Earth <https://www.microsoft.com/en-us/ai/ai-for-earth>`_:

* Grants
* Data Programs - especially global / geospatial program
* Building open source software


Part 1: ML for Climate Change
=============================

* Carbon markets. Highlighted company: `Silviaterra basemap <https://silviaterra.com>`_. Making forest inventory for every acre in America. 500 M acres at 0.5 acre resolution
* Sub-seasonal forecasting

  * Between days long weather forecasts vs. seasonal forecasts. 20-40 days
  * `Subseasonal Rodeo dataset <https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IHBANG>`_

* Making climate scientists more efficient with the tools of DS community - `Pangeo <https://pangeo.io>`_, `OOICloud <https://www.ooicloud.org>`_


Part 2: ML for monitoring / protection / conservation of biodiversity
=====================================================================

* Biodiversity is in severe decline

  * 25% of species are threatened with extinction
  * Extinction rate tens to hundreds times higher than baseline

* Climate change is a direct driver of biodiversity loss and land use change
* Healthy ecosystem are our strongest defense against climate change - Marine terrestrial ecosystem sequester 5.6GT of CO2!
* Monitoring biodiversity:

  * lots of raw data about wildlife, especially remote sensing data & tedious labeling process
  * `Wild Me <https://www.wildme.org>`_: ML to scale scientific effort
  * `iNaturalist <https://www.inaturalist.org>`_: ML to up-level everyone's expertise - scaling expertise
  * Finding penguins from space: ML to do surveys at unprecedented scale

* Lots of AI tools that Microsoft built are on monitoring:

  * Accelerating camera trap image processing: `cameratraps <https://github.com/microsoft/CameraTraps>`_
  * Species classification is a sexy problem, but we focus on more mundane problems (but occurred far more often: classify vehicle, animal, humans
  * `lila.science <http://lila.science>`_: open data repository which hosts labelled conversation datasets

* Protection

  * `OceanMind <https://www.oceanmind.global>`_: ML to detect illegal fishing. Apply ML in sensor data on transponding vessels, or satellite on non-transponding vessels
  * ML to detect poaching threats: `Wildlife protection solutions <https://wildlifeprotectionsolutions.org>`_, `Peace Parks <https://www.peaceparks.org>`_. Prioritize staff time when they review camera footage.

* ML for Land Conservation

  * Land use and CC are intertwined (reference: `IPCC special report on Climate Change and Land <https://www.ipcc.ch/srccl/>`_, 2019)
  * The reverse is true - climate change impacts agriculture (land use) too!
  * Optimizing the land we protect

    * `NatureServe <https://www.natureserve.org>`_ - map of biodiversity importance, identifying high priority protection targets
    * `Nature Conservancy <https://www.nature.org/en-us/>`_: last chance ecosystems
    * Optimizing protection of wild life species: `https://www.imageclef.org/GeoLifeCLEF2020 <https://www.imageclef.org/GeoLifeCLEF2020>`_

  * minimize the land we use for food

    * `Ag Analytics <https://analytics.ag>`_: improving agricultural forecasting and conservation practices
    * Identifying field level agricultural practices from remote sensing data
    * `Crop yield prediction from remote sensing data <https://cs.stanford.edu/~ermon/papers/cropyield_AAAI17.pdf>`_ - done by Stanford Ermon group

  * make land surveys more efficient

    * Land cover mapping from aerial and satellite imaging
    * Need to scale human effort
    * Data: NAIP, high-res; Landsat, low-res.
    * Demos: `Land cover training <aka.ms/landcoverdemo>`_, `Land cover mapping <aka.ms/landcovermapping>`_.
    * Dataset: `Chesapeake Land Cover <http://lila.science/datasets/chesapeakelandcover>`_
    * Re-tweak priorities, Build tools that help geospatial analysts get their land cover mapping modelled

* Q & A:

  * Trust problems in both directions: Dan is actually more worried about organizations trusting ML models too much - there might be systematic biases that we have not captured in the process, and stakeholders who are strained for resources or expertise in ML may be too keen to trust the ML output.
  * Tons of potential in finding insights from satellite imagery because of the wide-spread data availability and longer history of researchers making use of satellite imagery.
  * Maintainability of conservation data science work is likely in the large NGOs that can host their own data science teams.
