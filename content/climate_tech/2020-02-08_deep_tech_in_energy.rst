"Shelves of cans of worms" - why deep-tech in energy is tough
#############################################################

:date: 2020-02-08
:tags: climate_tech
:slug: deep-tech-in-energy
:authors: I-Kang Ding
:summary: Reminiscing about first decade of my career in materials science and deep-tech energy companies, and what I learned about the sector. (Also: what software companies and fruit flies have in common, and why working on deep tech energy technologies can feel like opening cans of worms all day.)


.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Swansons-law.svg/2560px-Swansons-law.svg.png
    :align: center
    :alt: swansons-law

Climate change is one of the most important problems of of 21st century. After many investors having been burned in the clean tech 1.0 wave in the late 00's, there has recently been a resurgence of interest from investors in things related to "climate tech".

As a person who spent first decade of my career in materials science and deep-tech energy companies (Stanford '06-'11, Alta Devices '11-'12, Lumileds '12-'15), I’d like share with people who are new to this field some learnings and my personal beliefs, shaped not just from my personal experience, but from talking to many folks in the same field.


Software vs. Deep-tech energy companies: a tale of two industries
-----------------------------------------------------------------

When I was at Stanford, I took a class from Stanford GSB (graduate school of business) called `Formation of New Ventures <https://www.gsb.stanford.edu/experience/learning/entrepreneurship/courses/formation-new-ventures>`_. The professor shared a tidbit about his research that stuck with me. Paraphrasing his quote below:

    "Software companies to us business school professors are like fruit flies to biologists. Biologists study fruit flies because they have very short life cycles, are not time- and resource-intensive to breed, and are therefore the model organism to do research on. We in business schools like to study software companies for largely the same reasons."

To extend this analogy further, the consumer electronics hardware companies are like small mammals (mice), energy materials companies are medium-sized mammals (monkeys), and pharmaceutical companies are large-sized mammals (sheep). There is a reason that venture capital like software companies too - they are usually less capital intensive, can operate at a high operating margin, and you typically do not need to plunge billions of dollars and wait for two decades to know if it works.

Typical software startups have the following milestone as they scale: (source: `The Most Important Startup Question <https://www.forentrepreneurs.com/most-important-startup-question/>`_)

* Search for product/market fit
* Search for a repeatable, scalable, & profitable growth model
* Scaling the business

.. image:: https://dskok-wpengine.netdna-ssl.com/wp-content/uploads/2017/07/Three-phases-of-a-Startup-1200x422.png
    :align: center
    :alt: three-phases-of-a-startup

However, this list is neglecting two additional steps that are crucial for deep-tech energy startups:

* **Technology development**
* Search for product/market fit
* **Scale-up manufacturing**
* Search for a repeatable, scalable, & profitable growth model
* Scaling the business

The additional steps can make deep-tech energy companies drastically more expensive and time-consuming to build. Let me elaborate.


Shelves of cans of worms: the triple whammy of deep-tech energy startups
------------------------------------------------------------------------

Technology development is time-consuming and expensive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Technology development for deep-tech energy startup is expensive and time-consuming. Let us take a look at some successful technologies in this space and take stock of how much time it took for these technologies to reach commercialization (benchmarked by a company being founded to focus exclusively on that particular technology

* `Silicon solar cells <https://en.wikipedia.org/wiki/Crystalline_silicon>`_: invented in 1954 by researchers at Bell Labs; consumer-facing commercialization started the 1980's. (Example company: `Sunpower <https://en.wikipedia.org/wiki/SunPower>`_, founded in 1985)
* `Cadmium Telluride (CdTe) solar cells <https://en.wikipedia.org/wiki/Cadmium_telluride_photovoltaics>`_: invented in 1960s; consumer-facing commercialization started in the 1990's. (Example company: `First Solar <https://en.wikipedia.org/wiki/First_Solar>`_, whose predecessor company, SCI, was founded in 1990)
* `White LEDs <https://en.wikipedia.org/wiki/Light-emitting_diode#White>`_: the key component, efficient blue LED, was invented in 1993; rose to commercial prominence in 2000's. (Example company: `Lumileds <https://en.wikipedia.org/wiki/Lumileds>`_, founded in 1999)
* `Lithium-ion batteries <https://en.wikipedia.org/wiki/Lithium-ion_battery>`_: invented in 1979; first commercial lithium-ion battery was released in 1991 by Sony and Asahi Kasei.
* `Quantum dots <https://en.wikipedia.org/wiki/Quantum_dot>`_: discovered in the late 1980s; consumer-facing commercialization for displays started in 2010's. May also have commercial application for solar cells and LEDs eventually.

The materials science breakthrough that enabled these commercial opportunities took researchers decades to develop. Even after the respective companies were founded, it took decades still to scale up to its success today.

Moreover, after the technology is scoped and developed, there's still considerable capital expenditure needed in order to bring a product to large scale manufacturing. Unlike the software startups that can use "shared infrastructure" such as cloud service providers and open source software, deep-tech hardware startups do not have these shared services at their disposal.

Thirdly, if you have to thread the needle on more than one area of "novel innovations", the risk of your startup goes up exponentially. My cynical measure of this is the "cans-of-worms" meter. Check first how many criteria a startup satisfies:

* New materials (as opposed to commonly used and studied materials)
* New manufacturing processes (as opposed incompatible with existing state-of-art manufacturing processes)
* New, custom-designed equipment (as opposed to off-the-shelf equipments from a reputed equipment manufacturer)

Now, consult the table below to map the number of boxes you checked, to the "cans-of-worms" meter:

1. a can of worms
2. a shelf of cans of worms
3. a room full of shelves, each full of cans of worms

I should note, however, that time-consuming and expensive product development cycles are not unique to deep-tech energy companies. Semiconductor fabs and pharmaceutical companies also share the same attributes - for example, in semiconductor fabrication, it routinely takes billions of dollars to build a new fab for the next gen node; and pharmaceutical companies routinely spends billions of dollars and 10+ years of time to bring a new drug to market.

**But wait, there's more!**


Your product can easily become a commodity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the things that makes deep-tech energy startup different from other high CapEx businesses like pharmaceutical and semiconductor fabs is that your product can easily become commodity if you are not careful. The examples being made below are primarily drawn from the solar cell industry, but the same lesson also applies to others.

One of the notable causalities from from the clean tech 1.0 bust were the thin film solar cell companies - there were literally `more than 100 of them <https://www.greentechmedia.com/articles/read/the-mercifully-short-list-of-fallen-solar-companies-2015-edition>`_ that closed shop in 2010-2015. But before we talk about what happened to these solar cell companies, we have to learn about a concept called "experience curve".

`Experience curve <https://en.wikipedia.org/wiki/Experience_curve_effects>`_ (aka. learning curve) can be described as the mathematical relationship between the number of times a task has been performed vs. the time/resource required on each subsequent iteration. In the solar cell example, there's `Swanson' law <https://en.wikipedia.org/wiki/Swanson's_law>`_, which described a learning rate of 20% - that is, the price of solar photovoltaic modules tends to drop 20 percent for every doubling of cumulative shipped volume.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Swansons-law.svg/2560px-Swansons-law.svg.png
    :align: center
    :alt: swansons-law

Empirically, many of the clean energy technologies follow this principle. Below is from an analysis from Bloomberg New Energy Finance:

.. image:: https://pbs.twimg.com/media/EKYwbu_W4AAmpo4?format=jpg&name=4096x4096
    :align: center
    :alt: bnef-learning-rate

What that means for new technologies entering the space is that they are at an inherent cost disadvantage. Established technologies (e.g. silicon solar cells) have spent a long time marching down the experience curve and benefits from the accumulative effect of learning rate over the course of decades, and if you are hoping to break into the market by undercutting established players on cost, you are going to have a bad time.

So, what does a deep-tech startup do? You find the differentiating value proposition that allow you to *not* compete in the commodity market, at least not in the beginning. Even if you have the aspirations to *eventually* take on matured technologies on cost (which is something that absolutely needs to be done if you were to make a dent on climate change), you still need high-margin markets in the beginning to get a chance to grow and march down the experience curve.

For example, Tesla started by selling high performance roadsters that cost $100,000+; then, as they get their manufacturing operations ramped up and drove cost down, they start selling cheaper and cheaper cars and are able to compete with established car companies on mass-market cars. Similarly, white light LED started out in high-margin, low-volume applications such as camera and smartphone flash, display back-lighting, etc (where you simply cannot use a compact fluorescent lamp or incandescent bulb), before moving on to illumination applications.


Innovation on atomic world is often incremental
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Lastly, deep-tech energy startups are often facing the physical constraints of the systems they deal with; many of the technologies are contending with theoretical limits and there's no space to make 10x improvements. This is in contrast to `Moore's law <https://en.wikipedia.org/wiki/Moore%27s_law>`_ in semiconductors, where you have a marching order to make the features smaller and smaller and get exponentially better performances year-over-year.

For example, in solar cells, there's a physical limit that dictates the maximum achievable efficiency. For single junction solar cells, that efficiency limit (`Shockley–Queisser limit <https://en.wikipedia.org/wiki/Shockley–Queisser_limit>`_) is about 33.7%, and the world record efficiency for single junction solar cell is about 29.1%, not that far off from theoretical limits.

.. image:: https://www.nrel.gov/pv/assets/images/best-research-cell-efficiencies.20200203.png
    :align: center
    :alt: best-research-cell-efficiencies

More concretely on the production line, you'll be often looking at 3-5% relative performance improvement year-over-year, at least for mature technologies like solar cells and LEDs.

Incremental performance improvement has another implication. sIf you don't have a way to achieve higher price through higher performance (or bette customer experience), you will need to rely more heavily on the cost reduction through experience curve, which put pressures on your margins. The incremental performance improvement also means that customers won't rush to replace your product every 3-5 years, and you'll need to rely on the expansion of new markets and customer segments. Fortunately, for deep-tech new energy startups, market saturation is the least thing to worry about.


So, where does that leave us?
-----------------------------

.. image:: https://imgs.xkcd.com/comics/so_it_has_come_to_this.png
    :align: center
    :alt: xkcd-it-has-come-to-this

I did not want this post to end on a note of defeatism. Rather, the purpose of this post is to highlight notable differences on the risk profile and resource requirements between software companies and deep-tech hardware companies in energy.

Furthermore, there are still many areas in climate tech that would be profoundly impacted by deep-tech materials breakthroughs, such as grid scale energy storage, geothermal, industrial heat (used in cement & steel manufacturing), etc. But these breakthroughs will take longer and more resources than what most of silicon valley VC's are used to. While the recent resurgence of interest and startup activities in climate change is extremely encouraging and much needed, I hope we are all being clear-eyed about what the journey entails, especially if we were to take on the deep-tech breakthroughs in energy.
