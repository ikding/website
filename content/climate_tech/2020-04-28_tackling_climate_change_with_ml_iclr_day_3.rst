Tackling climate change with ML (ICLR Workshop 2020) - day 3
############################################################

:date: 2020-04-28
:tags: climate_tech, data_science
:slug: tackling-climate-change-with-ml-iclr-day-3
:authors: I-Kang Ding
:summary: Notes from day 3 (Agriculture, Forestry, and Other Land Use (AFOLU) Day) of ICLR Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/ICLR2020_workshop#schedule>`__ on 2020-04-28.


.. image:: https://iclr.cc/static/admin/img/ICLR-logo.png
    :align: center
    :alt: iclr-conference-logo


Notes from day 3 (Agriculture, Forestry, and Other Land Use (AFOLU) Day) of ICLR Workshop - `Tackling Climate Change with Machine Learning <https://www.climatechange.ai/ICLR2020_workshop#schedule>`__ on 2020-04-28.


Fireside chat with Catherine Nakalembe
--------------------------------------

Fireside chat with Catherine Nakalembe on sustainable agriculture, food security and climate change

* Remote sensing imagery for agriculture climate change:

  * Need to pay attention to the in-growth season. Otherwise the ML models may not be able to be applied to agriculture appropriately.

* As a ML researcher:

  * Understand the remote sensing science will be a very good idea (understanding the data)
  * For the computer vision people - you need to understand how the field actually look like


Machine Learning and Agriculture: Precision Ag, Remote Sensing, and the Soil Microbiome
---------------------------------------------------------------------------------------


Steve Prager (International Center for Tropical Agriculture)
============================================================

* identify banana diseases through computer vision (photos at the banana and leaves)
* Climate change impact assessment for coffee and cacao crops
* Identifying substitute crops in the face of climate change
* Identifying / optimizing variables for crop yields
* Challenging the crowd for AI and ML solutions:

  * Recommendation engine for crop types
  * Data driven policy recommendations


Diane Wu (Trace Genomics): Generating soil data to power sustainable food production
====================================================================================

* Soil is living organism
* Food production systems in jeopardy
* Intensified agriculture reduces sustainability of our land

  * pesticides, fertilizers going in
  * Phosphorus and nitrogen leaching into groundwater
  * Plant diseases leads to $137 billion in economic losses per year

* Climate change challenges farming even further

  * Changing precipitation and weather patterns
  * In absence of data, farmers take the risk mitigation approach - use fertilizer and pesticides “just in case”

* Addressing root of the problem

  * Identify and quantify soil deficiencies and imbalances before planting anything in the ground

* Mission at Trace Genomics:

  * Understanding living soil using genomics and ML: genomics, bioinformatics, ML, soil science, agronomy
  * Digitize + decode + decide

* ML approach:

  * Metagenomic DNA sequences
  * Fungal + bacterial species
  * ML to model complex relations between microbial consortia
  * Predict outcome: model interpretability to help farmers improve productivity through a variety of interventions

* Data challenges

  * Problem definition is often the hardest part. Finding objective function is quite hard and you can easily lose users’ trust or confuse the users with complex models
  * Unmeasured variables: other factors influencing crops yield and disease, such as water, crop variety, input, farming decisions. This makes validation of the model quite tricky and time-consuming
  * Get labeled data. Getting data is expensive and delayed in agriculture - yield data happens once every year. What can be learn from tens of thousands of unlabelled soil samples?
  * Metagenomic structure and analysis: less than 50% of soil microbes have been identified, most are uncharacterized
  * Most microbes have interchangeable or evolving functionality over time
  * Interpretability


Panel: Machine Learning and Forests
-----------------------------------

What are the biggest challenges and opportunities for machine learning in forestry? Join us in a discussion-based session, in which our panelists discuss novel and effective tools from policy and industry to advance sustainable forest management.

Panelists:

* Max Nova (SilviaTerra)
* Simeon Max (ETH Zürich)
* Janina Grabs and Sam Levy (ETH Zürich)

* Max Nova from SilviaTerra highlighted the "misaligned incentive" problem. His startup partners with Microsoft AI for earth to use remote sensing to monitor deforestation, but for that knowledge to actually decrease deforestation, it would need to involve stakeholders in developing countries and give farmers an alternative to chop down trees. If there isn’t a way to pay people for not chopping down trees, they will continue to chop down trees for timber, agriculture, etc, because it is clear that they can get paid for that.
