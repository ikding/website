The New Business of AI (and How It's Different From Traditional Software) - a16z
################################################################################

:date: 2020-03-01
:tags: data_science
:slug: new-business-of-ai-a16z
:authors: I-Kang Ding
:summary: This is my personal highlights from reading "The New Business of AI (and How It's Different From Traditional Software)", which was published on Andreessen Horowitz blog. This article is superbly written, and is a great resource for machine learning professionals evaluating their next job opportunities.

**Note**: this is my personal highlights from reading `The New Business of AI (and How It's Different From Traditional Software) <https://a16z.com/2020/02/16/the-new-business-of-ai-and-how-its-different-from-traditional-software/>`_, which was published on Andreessen Horowitz blog. This article is superbly written, and is a great resource for machine learning professionals evaluating their next job opportunities.

Anecdotally, I had a similar discussion with my former manager at Capital One who has thought about this a lot; our discussion mirrors a lot of the points that this article pointed out, but this article summarized the differences in a much more structured way.

My notes are literally copy-and-pasted from sections that I consider "highlights"; if you find the highlights interesting, you should definitely read the articles yourself.

* In many cases that AI companies simply don't have the same economic construction as software businesses:

  * Lower gross margins due to heavy cloud infrastructure usage and ongoing human support
  * Scaling challenges due to the thorny problem of edge cases
  * Weaker defensive moats due to the commoditization of AI models and challenges with data network effects
  * Anecdotally, we have seen a surprisingly consistent pattern in the financial data of AI companies, with gross margins often in the 50-60% range – well below the 60-80%+ benchmark for comparable SaaS businesses.

* The beauty of software (including SaaS) is that it can be produced once and sold many times. This property creates a number of compelling business benefits, including recurring revenue streams, high (60-80%+) gross margins, and – in relatively rare cases when network effects or scale effects take hold – superlinear scaling.

* Service businesses occupy the other end of the spectrum. Each new project requires dedicated headcount and can be sold exactly once. As a result, revenue tends to be non-recurring, gross margins are lower (30-50%), and scaling is linear at best.

* Gross Margins, Part 1: Cloud infrastructure is a substantial – and sometimes hidden – cost for AI companies

  * AI is very demanding on cloud infrastructure: model training, model inference, training on rich media data, more complex cloud operations
  * These forces contribute to the 25% or more of revenue that AI companies often spend on cloud resources.
  * Model complexity is growing at an incredible rate, and it's unlikely processors will be able to keep up. Moore's Law is not enough.

* Gross Margins, Part 2: Many AI applications rely on "humans in the loop" to function at a high level of accuracy

  * Training most of today's state-of-the-art AI models involves the manual cleaning and labeling of large datasets. This process is laborious, expensive, and among the biggest barriers to more widespread adoption of AI.
  * For many tasks, especially those requiring greater cognitive reasoning, humans are often plugged into AI systems in real time.
  * The need for human intervention will likely decline as the performance of AI models improves. It's unlikely, though, that humans will be cut out of the loop entirely.

* Scaling AI systems can be rockier than expected, because AI lives in the long tail

  * For AI companies, it's deceptively easy to think you've gotten product-market fit – only to see the backlog for your ML team start to balloon and customer deployment schedules start to stretch out ominously, drawing resources away from new sales. The culprit, in many situations, is edge cases. Many AI apps have open-ended interfaces and operate on noisy, unstructured data (like images or natural language).
  * Handling this huge state space tends to be an ongoing chore. Since the range of possible input values is so large, each new customer deployment is likely to generate data that has never been seen before.
  * Put another way, users can – and will – enter just about anything into an AI app.
  * AI startups often end up devoting more time and resources to deploying their products than they expected. Identifying these needs in advance can be difficult since traditional prototyping tools – like mockups, prototypes, or beta tests – tend to cover only the most common paths, not the edge cases.

* The playbook for defending AI businesses is still being written

  * Great software companies are built around strong defensive moats. Some of the best moats are strong forces like network effects, high switching costs, and economies of scale. Being the first to implement a complex piece of software can yield major brand advantages and periods of near-exclusivity.
  * In the AI world, technical differentiation is harder to achieve. New model architectures are being developed mostly in open, academic settings. Reference implementations (pre-trained models) are available from open-source libraries, and model parameters can be optimized automatically.
  * Data is the core of an AI system, but it's often owned by customers, in the public domain, or over time becomes a commodity.
  * This does not necessarily mean AI products are less defensible than their pure software counterparts. But the moats for AI companies appear to be shallower than many expected.

* Building, scaling, and defending great AI companies – practical advice for founders

  * **Eliminate model complexity as much as possible**: We've seen a massive difference in COGS between startups that train a unique model per customer versus those that are able to share a single model (or set of models) among all customers. The "single model" strategy is easier to maintain, faster to roll out to new customers, and supports a simpler, more efficient engineering org.
  * **Choose problem domains carefully – and often narrowly – to reduce data complexity**: Many companies are finding that the minimum viable task for AI models is narrower than they expected. There is a large class of problems, like these, that are hard for humans to perform but relatively easy for AI.
  * **Plan for high variable costs**: we suggest building a business model and GTM strategy with lower gross margins in mind. Understand deeply the distribution of data feeding your models. Treat model maintenance and human failover as first-order problems. Track down and measure your real variable costs – don't let them hide in R&D. Make conservative unit economic assumptions in your financial models, especially during a fundraise. Don't wait for scale, or outside tech advances, to solve the problem.
  * **Embrace services**: There are huge opportunities to meet the market where it stands. Building hybrid businesses is harder than pure software, but this approach can provide deep insight into customer needs and yield fast-growing, market-defining companies.
  * **Plan for change in the tech stack**: Modern AI is still in its infancy. The tools that help practitioners do their jobs in an efficient and standardized way are just now being built. Tightly coupling an application to the current way of doing things may lead to an architectural disadvantage in the future.
  * **Build defensibility the old-fashioned way**: While it's not clear whether an AI model itself – or the underlying data – will provide a long-term moat, good products and proprietary data almost always builds good businesses.
