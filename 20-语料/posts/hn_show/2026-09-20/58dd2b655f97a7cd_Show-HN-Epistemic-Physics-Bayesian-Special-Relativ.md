---
type: "corpus"
item_id: "58dd2b655f97a7cd"
title: "Show HN: Epistemic Physics: Bayesian Special Relativity"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49713322"
project_url: "https://raia.fun/blog/ep-001-bayesian-special-relativity"
author: "viamiraia"
published_at: "2026-09-15T14:44:09Z"
captured_at: "2026-09-20T14:06:14+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_viamiraia
  - story_49713322
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:90d"
---

# Show HN: Epistemic Physics: Bayesian Special Relativity

> [!info] 一句话导读
> Published: 2026-09-15

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49713322>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：viamiraia　|　发布：2026-09-15T14:44:09Z
> 项目链接：<https://raia.fun/blog/ep-001-bayesian-special-relativity>
> 采集：2026-09-20T14:06:14+08:00　|　id：`58dd2b655f97a7cd`

## 正文

Published: 2026-09-15

Epistemic Physics 1: Bayesian Special Relativity · raispace

# Epistemic Physics 1: Bayesian Special Relativity

Published Sep 15 '26 · 45 min epistemic-physics

n N o ai AI was used for the writing and structure of this article, nor for the primary ideas behind it. i I used ai AI in three ways - guiding it to create interactive demos the way i I wanted, double checking work, and making more connections with fields i I'm less familiar with.

## c C onnecting e E pistemology, s S tatistics, p P hysics, and m M ore

i I n this series on epistemic physics, i I'll show you how treating probability as relativistic velocity and evidence as spacetime leads to all sorts of wonderful connections. h H ere are some highlights!

- a A sensible physical interpretation of belief (as b B eta distributions on propositions):

- absolute certainty is the speed of light, meaning you need infinite evidence to reach it.
- beliefs backed by more evidence have greater inertia, meaning each additional observation changes the velocity (probability) less.
- b B ayes' rule with log-odds is rapidity addition (for point probabilities)
- t T he likelihood ratio or b B ayes factor is a d D oppler shift.
- e E instein velocity addition is n N aive b B ayes.
- c C onstant natural selection is constant acceleration.
- r R apidity becomes a unified way to describe b B ayesian updating, natural selection, e E lo ratings, n N ernst membrane equilibria, p h H, logistic regression, psychometrics, enzyme kinetics and ligand binding, spin magnetization, binary softmax in machine learning, llr LLR and tanh rule in coding theory, evolutionary game theory, f F ermi- d D irac occupancy, k K elly bets, ion channel gating, prediction markets, and more!
- t T he e E sscher transform of b B ernoulli outcomes is a l L orentz boost..
- t T otal evidence is inverse temperature, learning is cooling, the h H aldane prior

B

e

t

a

⁡

(

0

,

0

)

$\operatorname{Beta}(0,0)$

 is infinite temperature, the j J effreys prior

B

e

t

a

⁡

(

1

2

,

1

2

)

$\operatorname{Beta}\left( \frac{1}{2}, \frac{1}{2} \right)$

 is the neutral, or "room-temp" state of belief, and the ground state is rapidity mode.
- b B eliefs at zero velocity are random walks and act similar to b B rownian motion, and b B rownian bridges are related to the r R iemann zeta (see this youtube video by a A lmost s S ure). i I investigated and found that the difference between or fusion of the distribution of draws of rapidity-transformed uniform beliefs has the r R iemann zeta function in it!

- t T reating beliefs as waves can get you the zeros, which relate to complex phase cancellation.

𝐸

[

𝐷

]

2

−

𝑠

𝑠

−

1

+

Φ

−

Φ

2

Φ

+

Φ

2

$$ E[D^s] = 2^{1-s}(s-1)\Gamma(s+1)\zeta(s), \qquad D=|\Phi_1-\Phi_2|=|\Phi_1+\Phi_2| $$

- i I n addition, multiplying uniform beliefs together can result in "increasing" zetas (increasing n) too:

𝐸

[

1

−

]

$$ E\left[\frac1{1-B_1B_2}\right] = \zeta(2) = \frac{\pi^2}{6} $$

𝐸

]

,

>

$$ E\left[ \frac1{1-\prod_{i=1}^nB_i} \right] = \zeta(n), \qquad n>1 $$

- t T his is the waiting time until two-coin flips come up with two heads. h H ave fun mathematicians (and ai AI agents i I guess)!

- i I hope to expand on how epistemic physics relates to the r R iemann h H ypothesis, if it doesn't get solved by then, in a future post.

a A nd check out the f F un p P redictions section below! i I won't prove all these connections in this first introductory article, but feel free to explore yourself! l L uckily, the essentials of epistemic physics are extremely easy to understand with some basic knowledge of statistics and relativity.

a A bout my other websites…

a A s of 2026-09-15:

https://epistemicphysics.com is my ai AI slop website on epistemic physics, i I use it as a dumping ground for ideas with little curation; almost all of it is ai AI generated and rather difficult to understand. e E nter at your own risk. i I may de-slopify it someday if i I have the time.

https://sloth.ink is currently heavily outdated - i I am in the process of overhauling the underlying mathematics in light of epistemic physics - but the articles may still provide interesting insights on beliefs on propositions.

### b B eta d D istribution with p P rior

d D efine a belief

𝐵

$B$

 distributed according to a b B eta distribution

𝐵

∼

B

e

𝛼

,

.

$$ B\sim\operatorname{Beta}(\alpha,\beta), \qquad \alpha,\beta>0. $$

with mean

𝜇

𝐵

]

$$ \mu = E[B] = \frac{\alpha}{\alpha + \beta} $$

d D efine the total evidence and signed evidence balance by

𝜏

E

−

.

$$ \tau_{\mathrm E}=\alpha+\beta, \qquad x_{\mathrm E}=\alpha-\beta. $$

h H ere, upright subscript

E

 stands for "epistemic." n N ow, linearly recenter the distribution between

[

−

,

1

]

$[-1,1]$

. d D efine the centered random variable

𝐵

E

2

𝐵

−

$$ B_{\mathrm{E}} = 2B-1 $$

t T he recentered mean is thus:

𝑣

E

E

1

−

1

2

𝛼

−

+

+

−

+

𝜏

$$ \begin{aligned} v_\mathrm{E} &= \mathbb E[B_{\mathrm{E}}] \\ &= 2\mu-1 \\ &=2\frac{\alpha}{\alpha+\beta}-1 \\ &=\frac{2\alpha-(\alpha+\beta)}{\alpha+\beta} \\ &=\frac{\alpha-\beta}{\alpha+\beta} \\ &= \frac{x_{\mathrm{E}}}{\tau_{\mathrm{E}}}\\ \end{aligned} $$

Beta vs Velocity

The same Beta distribution, original vs recentered.

↺ Jeffreys prior

 density over probability μ same belief over velocity v E — twice as wide, half as tall

+1 support +1 opposition each observation adds one full unit of evidence

α = 0.50 β = 0.50 τ E = 1.00 μ = 0.500 v E = 0.000

f F or a

1

+

$1+1$

 dimensional light cone,

𝑑

𝑠

$$ ds^2 = c^2dt^2 - dx^2 $$

𝑠

 is the spacetime interval,

𝑡

 is time, and

𝑥

 is position. a A t the origin,

𝑠

$$ s^2 = c^2t^2 - x^2 $$

t T he light-cone coordinates, or null coordinates are:

+

$$ x^+= ct+x, \qquad x^-=ct-x $$

#### e E vidence cones

r R ecall the mean of our recentered b B eta distribution:

𝑣

$$ v_\mathrm{E} =\frac{\alpha-\beta}{\alpha+\beta} = \frac{x_{\mathrm{E}}}{\tau_{\mathrm{E}}} $$

t T he prior-inclusive b B eta parameters are proportional to the null coordinates of a light cone:

𝜏

+

$$ \tau_{\mathrm E}=\alpha+\beta, \qquad x_{\mathrm E}=\alpha-\beta. $$

h H owever, the inverse transformation also looks like the null coordinates of a light cone:

$$ \alpha=\frac{\tau_{\mathrm E}+x_{\mathrm E}}{2}, \qquad \beta=\frac{\tau_{\mathrm E}-x_{\mathrm E}}{2}. $$

w W hich representation do we choose? n N ote that the inverse relations are derived by

$$ \begin{aligned} \tau_{\mathrm E}+x_{\mathrm E} &=(\alpha+\beta)+(\alpha-\beta) \\ &=2\alpha \\ \tau_{\mathrm E}-x_{\mathrm E} &=(\alpha+\beta)-(\alpha-\beta) \\ &=2\beta \end{aligned} $$

t T hese both look like conic coordinates, and both possible coordinate constructions result in valid geometry. h H owever, only one configuration preserves beta evidence semantics.

| p P roperty | s S emantics-preserving geometry | a A lternate geometry |
| --- | --- | --- |
| c C one coordinates | (𝜏 E,𝑥 E)$(\tau_{\mathrm E},x_{\mathrm E})$ | (𝛼,𝛽)$(\alpha,\beta)$ |
| n N ull coordinates | 𝛼,𝛽$\alpha,\beta$ | 𝜏 E,𝑥 E$\tau_{\mathrm E},x_{\mathrm E}$ |
| m M etric | 𝜏 2 E−𝑥 2 E= 4𝛼𝛽$\tau_{\mathrm E}^2-x_{\mathrm E}^2=4\alpha\beta$ | 𝛼 2−𝛽 2=𝜏 E𝑥 E$\alpha^2-\beta^2=\tau_{\mathrm E}x_{\mathrm E}$ |
| n N ull boundary | 𝛼= 0$\alpha=0$ or 𝛽= 0$\beta=0$ | 𝜏 E= 0$\tau_{\mathrm E}=0$ or 𝑥 E= 0$x_{\mathrm E}=0$ |
| c C ausal sector | 𝛼,𝛽≥ 0$\alpha,\beta\ge 0$, equivalently 𝜏 E≥ | 𝑥 e E |
| b B alanced evidence | 𝑥 E= 0$x_{\mathrm E}=0$, interior centerline | 𝛼=𝛽$\alpha=\beta$, hence 𝑥 E= 0$x_{\mathrm E}=0$, a null boundary |
| c C omplement 𝛼↔𝛽$\alpha\leftrightarrow\beta$ | p P reserves the interval | r R everses the sign of the interval |

i I n the alternate geometry,

𝛼

$\alpha$

 is timelike and

𝛽

$\beta$

 is spacelike (you could also define

𝑥

E

$x_{\mathrm{E}}=\beta-\alpha$

 to swap those). e E ach success outcome, or event observation, results in time progression, while each failure outcome, or null observation, results in space progression. o O nly probabilities where

𝑝

>

.

5

$p>0.5$

 would be causal, and failure-dominant probabilities become spacelike. t T his seems arbitrary, privileging one evidential outcome. i I n addition, balanced evidence, or conflict, becomes indistinguishable from no evidence, or vacuity, since

𝛼

$\alpha^2-\beta^2=0$

o O n the other hand, if we set

𝛼

$\alpha$

 and

 to be the null coordinates, we gain a coherent interpretation. h H ere,

𝜏

$\tau_{\mathrm{E}}$

, interpreted as total observations, is timelike, and signed evidence balance

$x_{\mathrm{E}}$

, interpreted as net support, is spacelike (alternatively you could use net opposition, but net support is more intuitive). t T he epistemic velocity

𝑣

/

𝜏

$v_{\mathrm{E}}=x_{\mathrm{E}}/\tau_{\mathrm{E}}$

 becomes recentered on

$0$

 between

−

1

$-1$

 and

1

$1$

. o O ver time you gain evidence, while a change in net support moves you. c C onflict is distinguishable from vacuity, since more conflict moves you further in the timelike direction. f F or a proper b B eta distribution,

𝛼

,

>

$\alpha,\beta>0$

, and therefore every proper b B eta state lies strictly inside the future l L orentz cone.

h H ow i I got here

o O n a A ugust 12, 2026, while exploring the concepts of negative and complex evidence in the context of stochastic valence networks (neural networks using b B eta distributions and mixtures), i I noticed the connection between special relativity and b B eta-distributed evidence. i I've been thinking about evidence, b B etas and d D irichlets for a while now, thanks to my other project, g G ated e E pistemic c C alculus and the currently outdated s S lothink website, which aim to reduce misinformation and encourage empathy by helping people make their subjective beliefs consistent and free of hypocrisy. i I n valence networks, membrane potential of valence networks is analogous to position, the current is analogous to time, and the mean firing rate is analogous to velocity.

#### e E nergy-momentum c C ones

t T he energy-momentum relation is

𝐸

+

$$ \begin{aligned} E^2 &= (pc)^2 + (mc^2)^2 \\ \left(\frac{E}{c}\right)^2 - p^2 &= m^2c^2 \\ \end{aligned} $$

t T he corresponding null coordinates are

+

−

$$ p^+ = \frac{E}{c}+p, \qquad p^- = \frac{E}{c}-p $$

e E nergy-momentum space thus shares the same l L orentz-cone geometry as spacetime and the evidence cone. t T o compare energy-momentum space to evidence space, use natural units with

𝛽

𝑚

2

E

$$ \begin{aligned} m^2&=E^2-p^2\\ &=\tau_{\mathrm{E}}^2-x_{\mathrm{E}}^2\\ &=(\alpha + \beta)^2 - (\alpha - \beta)^2 \\ &=\alpha^2 + 2\alpha\beta + \beta^2 - \alpha^2 + 2\alpha\beta - \beta^2 \\ &=4\alpha\beta \\ &=m_{\mathrm{E}}^2 \end{aligned} $$

a A s an analogy, one can interpret

𝜏

𝐸

$\tau_{E}$

 as energy-like,

𝑥

E

$x_{\mathrm{E}}$

 as momentum-like,

𝑚

E

2

𝛼

𝛽

$m_{\mathrm{E}} = 2\sqrt{ \alpha\beta }$

 as mass-like, and

𝑣

E

$v_{\mathrm{E}}$

 still as epistemic velocity. h H owever, in physics, energy-momentum describes interactions, such as the change in momentum in a collision. o O ther differences from spacetime include additivity, where the total momentum of system is the sum of parts, and tangency, where momentum is tangent to the worldline while position is a point on the worldline. t T hus the better analogy is to consider incremental changes in evidence:

𝑑

𝜏

E

+

𝑑

,

𝑑

𝑑

−

𝑑

$$ \begin{aligned} d\tau_{\mathrm{E}} = d \alpha +d \beta, \qquad dx_{\mathrm{E}}=d \alpha -d \beta \end{aligned} $$

t T his preserves the notion that energy and momentum are conserved and exchanged during interactions.

#### v V ariance

n N ow we can derive some identities for the variance of a recentered belief:

V

a

𝐵

+

+

+

𝜏

𝜏

+

$$ \begin{aligned} \operatorname{Var}(B_{\mathrm E}) &=\frac{4\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}\\ &=\frac{1-v_{\mathrm E}^2}{\tau_{\mathrm E}+1}\\ &=\frac{m_{\mathrm E}^2}{\tau_{\mathrm E}^2(\tau_{\mathrm E}+1)}\\ \end{aligned} $$

Two cones, One geometry

Evidence spacetime: the worldline

Energy-momentum

observe support ↗ ↖ observe opposition or drag either dot

Y = 0 N = 0 τ E = 1.0 x E = 0.0 v E = 0.000 m E = 1.00 γ E = 1.000

$$m_{\mathrm E}^2=\tau_{\mathrm E}^2-x_{\mathrm E}^2=4\alpha\beta$$

### e E vidence n N otation

i I t is often useful to separate raw evidence from the prior. d D efine a neutral symmetric prior concentration

𝑛

0

$n_0$

𝛼

∼

$$ \alpha_{0}=\beta_{0}=\frac{n_{0}}{2}, \qquad B\sim \operatorname{Beta}\left( \frac{n_{0}}{2},\frac{n_{0}}{2} \right) $$

d D efine the total evidence accumulated over the prior

𝑡

E

$t_\mathrm{E}$

 as trials

𝑌

, for support, and

𝑁

, for opposition:

𝑡

E

𝑌

+

𝑁

$$ t_\mathrm{E} = Y+N $$

w W hile b B eta evidence trials may be continuous, one can interpret integer-valued trials as b B ernoulli outcomes. o O ur previous notation can thus be defined like:

𝛼

𝑌

+

𝑛

2

,

𝛽

𝑁

+

2

𝜏

𝑌

+

𝑁

+

𝑌

+

2

−

𝑁

𝑌

−

−

𝑁

𝑛

$$ \begin{aligned} \alpha &= Y+\frac{n_{0}}{2}, \qquad \beta=N+\frac{n_{0}}{2}\\ \tau_{\mathrm{E}} &= Y+N+n_{0} \\ x_{\mathrm{E}} &= Y+\frac{n_{0}}{2} - N - \frac{n_{0}}{2}\\ &=Y-N \\ v_{\mathrm{E}} &= \frac{Y-N}{Y+N+n_{0}} \\ &=\frac{x_{\mathrm{E}}}{t_{E} + n_{0}} \end{aligned} $$

### t T he j J effreys p P rior

t T he j J effreys prior, denoted as

𝜛

$\varpi$

 below, or the arcsine distribution, is a particularly suitable prior for epistemic physics.

𝛼

+

+

𝜏

𝜛

$$ \begin{aligned} \alpha&=Y+\frac12, \qquad \beta=N+\frac12 \\ \tau_{\mathrm E}&=Y+N+1\\ v_{\mathrm E}&=\frac{Y-N}{Y+N+1}\\ \varpi &= \operatorname{Beta}\left( \frac{1}{2}, \frac{1}{2} \right) = \frac{1}{\pi \sqrt{ \mu(1-\mu) }} \\ \varpi_{\mathrm{E}} &= \frac{1}{\pi \sqrt{ 1-v_{\mathrm{E}}^2 }} \end{aligned} $$

t T he reasoning is as follows. f F irst, using a j J effreys prior assigns equal prior probability to equal lengths in f F isher information. g G iven 1000 coin flips, changing the heads probability from 49% to 50% changes the expected heads count from 490 to 500. c C hanging from 1% to 2% goes from 10 heads to 20 heads. a A lthough both situations add 10 heads, the scales are different. t T he former requires only 1.02 times the heads rate, while the latter requires doubling the rate of heads. f F isher information states:

𝐼

$$ I(\mu) = \frac{1}{\mu(1-\mu)} $$

t T he f F isher length element, is

$$ d\ell=\sqrt{I(\mu)}\,|d\mu| =\frac{|d\mu|}{\sqrt{\mu(1-\mu)}} $$

a A short interval near probability 0 or 1 covers more f F isher length than an equally wide interval near the center. c C ompare the scales - 0 to 1 for probability versus 0 to

 for f F isher length. f F isher length allows for a fixed interval along the entire distance from 0 to

, while the interval varies on the probability scale.

s S econd, consider the identity

𝜏

$\tau_{\mathrm E}^2 - x_{\mathrm E}^2 = m_{\mathrm E}^2$

 , which can be rearranged a la p P ythagoras:

𝜏

$$ \tau_{\mathrm E}^2 = x_{\mathrm E}^2 + m_{\mathrm E}^2 $$

e E pistemic position and mass lie on a circle of radius

$\tau_\mathrm{E}$

 (imagine position on the x-axis and mass on the y-axis). s S ince epistemic mass is positive for proper beliefs, the upper semicircle contains the normally reachable states.

𝜏

o

,

𝜃

<

𝜋

2

.

$$ x_{\mathrm E} = \tau_{\mathrm E}\sin \theta, \qquad m_{\mathrm E} = \tau_{\mathrm E}\cos \theta, \qquad -\frac{\pi}{2} < \theta < \frac{\pi}{2}. $$

i I n this construction, the uniform, or l L aplace prior, is uniform only along the x-axis, while the j J effreys prior is uniform along

𝜃

$\theta$

, and thus uniform along the semicircle. t T he j J effreys prior has no preference for how evidence is split between mass and position. t T his construction also clearly illustrates that the

𝜋

$\pi$

 that appears is the angular distance of the semicircle's arc.

t T hird, when we extend from 1+1 d D to higher dimensions, the natural extension to the j J effreys prior works well. s S ee the multidimensional extension section for more details.

Jeffreys vs Uniform

fair along the arc · Jeffreys fair along the axis · uniform

v E = 0.643 μ = 0.821 m E /τ E = 0.766 γ E = 1.305 ϖ E = 0.416

$$x_{\mathrm E}=\tau_{\mathrm E}\sin\theta,\qquad m_{\mathrm E}=\tau_{\mathrm E}\cos\theta,\qquad \varpi_{\mathrm E}=\frac{1}{\pi\cos\theta}=\frac{\gamma_{\mathrm E}}{\pi}$$

### r R apidity

w W e can relate epistemic velocity to rapidity. d D efine epistemic rapidity as

𝜙

E

=

a

r

t

a

n

h

𝑣

E

2

l

o

+

−

+

−

𝛼

o

𝛼

𝛽

$$ \begin{aligned} \phi_{\mathrm E}&=\operatorname{artanh}v_{\mathrm E} \\ &=\frac{1}{2}\log\frac{1+v_{\mathrm{E}}}{1-v_{\mathrm{E}}} \\ &= \frac12\log \frac{ 1+\frac{\alpha-\beta}{\alpha+\beta} }{ 1-\frac{\alpha-\beta}{\alpha+\beta} }\\ &= \frac12\log \frac{ \frac{\alpha+\beta+\alpha-\beta}{\alpha+\beta} }{ \frac{\alpha+\beta-\alpha+\beta}{\alpha+\beta} }\\ ​&= \frac12\log \frac{ 2\alpha }{ 2\beta} \\ &=\frac{1}{2}\log\frac{\alpha}{\beta} \\ \end{aligned} $$

t T his is half the log-odds. n N ote that rapidity is related to b B ondi's k-factor, thus forming the connection between the square root of the likelihood ratio and the d D oppler effect. o O ne can also define:

𝜏

E

𝑚

o

𝜙

+

𝜙

E

$$ \begin{aligned} \tau_{\mathrm{E}}&=m_{\mathrm{E}} \cosh \phi_{\mathrm{E}} = \alpha+\beta\\ x_{\mathrm{E}}&=m_{\mathrm{E}}\sinh \phi_{\mathrm{E}}=\alpha-\beta\\ \end{aligned} $$

w W e can go a step further and transform the entire belief, not only the mean:

Φ

E

a

)

o

+

E

−

𝐵

$$ \Phi_{\mathrm E}=\operatorname{artanh}(B_{\mathrm E}) =\frac12\log\frac{1+B_{\mathrm E}}{1-B_{\mathrm E}} =\frac12\log\frac{B}{1-B} $$

n N ote that this distinction between translating the velocity versus the whole belief is very important - some connections from earlier only work for one transformation and not the other. t T he inverse transformation is:

𝐵

E

t

a

n

h

Φ

E

,

𝐵

+

t

a

h

Φ

E

2

.

$$ B_{\mathrm E}=\tanh\Phi_{\mathrm E},\qquad B=\frac{1+\tanh\Phi_{\mathrm E}}{2}. $$

n N ote that

𝔼

[

𝐵

E

]

𝔼

t

a

Φ

E

]

a

𝜙

E

,

𝔼

Φ

]

𝜙

E

$$ \mathbb E[B_{\mathrm{E}}] = \mathbb E[\tanh\Phi_{\mathrm E}] =v_{\mathrm E}=\tanh\phi_{\mathrm E},\qquad \mathbb E[\Phi_{\mathrm E}]\ne\phi_{\mathrm E} $$

m M ore specifically,

𝐸

[

Φ

]

𝜓

−

𝜓

,

Φ

𝜓

′

+

𝜓

′

𝛽

$$ E[\Phi_{\mathrm{E}}]=\tfrac12(\psi(\alpha)-\psi(\beta)), \qquad \operatorname{Var}\Phi_{\mathrm{E}}=\tfrac14(\psi'(\alpha)+\psi'(\beta)) $$

Rapidity across fields

↺ back to φ = 0.55

φ E = 0.550 μ = 75.0% v E = 0.501

special relativity

$v/c=\tanh\phi_{\mathrm E}$

special relativity: of the speed of light of the speed of light

logistic regression · softmax · LLR

$\ell=\log\tfrac{\mu}{1-\mu}=2\phi_{\mathrm E}$

logistic regression · softmax · LLR: natural-log odds natural-log odds

chess rating

$\Delta_{\mathrm{Elo}}=\tfrac{800}{\ln 10}\,\phi_{\mathrm E}$

chess rating: Elo points of advantage Elo points of advantage

acid-base chemistry

$\mathrm{pH}-\mathrm{p}K_a=\tfrac{2}{\ln 10}\,\phi_{\mathrm E}$

acid-base chemistry: pH units past the pKₐ pH units past the pKₐ

prediction market

$\text{price}=100\,\mu$

prediction market: ¢ per yes-share ¢ per yes-share

psychometrics (Rasch)

$\theta_{\text{ability}}-b_{\text{difficulty}}=2\phi_{\mathrm E}$

psychometrics (Rasch): logits logits

ion-channel gating

$V-V_{1/2}=2k\,\phi_{\mathrm E},\ k=6\,\mathrm{mV}$

ion-channel gating: mV above the midpoint mV above the midpoint

Nernst equilibrium

$E=\tfrac{2RT}{zF}\,\phi_{\mathrm E}$

Nernst equilibrium: mV (z = 1, 37 °C) mV (z = 1, 37 °C)

ligand binding (Hill, n = 2)

$[L]/K=e^{2\phi_{\mathrm E}/n}$

ligand binding (Hill, n = 2): × the half-occupancy dose × the half-occupancy dose

Fermi-Dirac occupancy

$(E_F-\varepsilon)/k_BT=2\phi_{\mathrm E}$

Fermi-Dirac occupancy: thermal units below the Fermi level thermal units below the Fermi level

spin magnetization

$\bar s=\tanh\!\left(h/k_BT\right),\ h/k_BT=\phi_{\mathrm E}$

spin magnetization: field in thermal units field in thermal units

Kelly betting

$f^{*}=\tanh\phi_{\mathrm E}$

Kelly betting: of bankroll on even odds of bankroll on even odds

natural selection

$\phi_{\mathrm E}(t)=\phi_0+\tfrac{s}{2}\,t,\ s=5\%$

natural selection: generations from even odds generations from even odds

### e E pistemic i I nterpretations

i I'm making a deliberate simplification in choosing to model fuzzy beliefs on propositions as b B eta distributions. i I n reality, beliefs may also include additional properties such as how underspecified the proposition is (naturally leading to a nested b B eta or d D irichlet interpretation), or encompass more than propositions (such as numerical estimates, though those can arguably be reduced to propositions). h H owever, the simplification leads to a useful epistemic world with constraints and physical and statistical interpretations. f F or example, one can interpret approaching the speed of light as approaching absolute certainty of belief.

#### t T he s S peed l L imit of b B elief

e E pistemically, the speed of light plays several roles. o O ne interpretation says that a belief with mass can never reach absolute certainty. a A nother interpretation says that once you see evidence, you can't unsee it. w W e can try a fun thought experiment - what happens epistemically or probabilistically when we try breaking the speed limit? w W e get probabilities less than 0 or greater than 1, or superluminal probability, corresponding to negative evidence (retractions), and leading to split-complex probability and tachyonic or spacelike states.

#### b B ernoulli p P hotons

c C onsider b B ernoulli observations as trials, with success as a unit of support and failure as a unit of opposition. a A success can be considered as

𝑑

𝛼

=

1

,

𝑑

𝛽

=

0

$d\alpha=1, d\beta=0$

 . t T herefore the change in epistemic spacetime interval is

𝑑

𝑠

2

E

4

𝑑

𝑑

𝛽

4

$ds_{\mathrm{E}}^2 = 4 \, d\alpha \, d\beta = 4 \cdot 1 \cdot 0 = 0$

. l L ikewise, a failure would be

𝑑

𝛼

,

𝑑

𝛽

1

$d\alpha=0, d\beta=1$

 and also

𝑑

𝑠

$ds_{\mathrm{E}}^2 = 4 \cdot 0 \cdot 1 = 0$

. i I n special relativity, an object with

𝑑

𝑠

2

0

$ds^2 = 0$

 is traveling at the speed of light, aka a null or lightlike trajectory, and only photons - massless particles - travel like this. t T hus a trial is analogous to a photon.

n N ext, let's take a look at the formula for epistemic mass

2

√

𝛼

𝛽

$2\sqrt{ \alpha \beta }$

 . t T his is the geometric mean scaled by 2, and might be interpreted as a measure of conflict. w W hen two photons collide, they can produce massive particles, and when opposing photons are treated collectively, they have an invariant mass. l L ikewise, a belief gains epistemic mass when epistemic photons collide, which makes sense - a belief that doesn't lie at absolute certainty has some internal conflict. t T o generate mass, each success needs failures to "interact with" and vice versa.

#### i I nterpreting d D istributions as b B eliefs

b B eta distributions describe fuzzy beliefs well when the beliefs are about propositions, due to the b B ernoulli- b B inomial- b B eta connection and the t T rue- f F alse nature of propositions. t T he mode is the agent's single most likely degree of confidence (not the variance)! t T he variance is malleability or "sway-ability" of the belief. t T he mean is the "average belief on repeated draws", as if you elicited belief from an agent multiple times in either nearly the same conditions or multiple worlds. t T his merges the b B ayesian and frequentist interpretations of probability. 50% is unsure, 99% is very sure the proposition is true, 1% is very sure it's false. t T he trials are how resistant an agent, component, or neuron is to changing its mind. m M any trials at 99% mode is " i I'm sure that i I'm sure that it's true" while few trials at 99% mode are " i I think it's true but i I would be easily swayed." m M any trials at 50% are " i I'm conflicted" or " i I'm sure that i I'm not sure" and few trials at 50% are nearly vacuous - " i I'm not sure at all."

d D irichlets would represent beliefs on multiple-choice questions. i I've also re-derived an obscure derivation to allow for nonparametric beliefs on number lines, making d D irichlet processes more flexible, though that's beyond the scope of this article. a A lso, a common misconception is that studies themselves have beliefs or provide evidence as beliefs - in my framework only agents hold beliefs, and beliefs about studies should be about a proposition about the study, such as a belief on " s S tudy a A showed x X".

### l L orentz f F actor

n N ow that we have an evidence cone, we can relate probability to the l L orentz factor, typically defined as

𝛾

=

1

√

−

/

2

$$ \gamma=\frac{1}{\sqrt{ 1-(v/c)^2 }} $$

w W e can define an epistemic l L orentz factor

𝛾

E

√

−

$$ \gamma_{\mathrm{E}}=\frac{1}{\sqrt{ 1-v_{\mathrm{E}}^2 }} $$

t T o relate back to the physical l L orentz factor, simply multiply the j J effreys prior by

𝑚

𝑐

𝛾

𝜛

$$ \frac{E}{mc^2} = \gamma = \pi\varpi_{\mathrm{E}} $$

t T he epistemic l L orentz factor is related to several other equations. f F or example, f F isher information can be defined as

𝐼

−

$$ I(\mu) = \frac{1}{\mu(1-\mu)} $$

c C onvert

$\gamma_{\mathrm{E}}$

 back to normal probability coordinates

−

+

−

−

+

𝜇

−

$$ \begin{aligned} \gamma_{\mathrm{E}} &= \frac{1}{\sqrt{ 1-(2\mu-1)^2 }}\\ &=\frac{1}{\sqrt{ 1-4\mu^2+4\mu-1 }}\\ &=\frac{1}{\sqrt{ 4\mu(-\mu+1)}}\\ &=\frac{1}{2\sqrt{ \mu(1-\mu)}}\\ \end{aligned} $$

t T hen,

𝛾

2

𝜇

−

$$ \begin{aligned} \gamma_{E}^2&=\frac{1}{4\mu(1-\mu)}\\ &=\frac{1}{4}I(\mu) \end{aligned} $$

a A s another example, consider a spring with normalized position between -1 and 1:

𝜃

$$ x=\cos\theta $$

s S uch a spring spends its time as

𝑓

(

𝑥

)

−

2

$$ f(x) = \frac{1}{\pi \sqrt{ 1-x^2 }} $$

Jeffreys, springs, E/mc^2

▶ play & photograph 📸 200 random photos clear photos n = 0

 photos of the mass Jeffreys prior ϖ E Lorentz factor γ E /π — the same curve

$$x/A=\cos\theta,\qquad \gamma_{\mathrm E}=\frac{E}{mc^2}=\pi\,\varpi_{\mathrm E}(v_{\mathrm E})$$

w W hy

$\pi$

?

i I f we use the l L orentz factor as a recentered probability density, we have to divide by the integral from

𝑣

−

−

1

 to

𝑣

+

𝑐

1

1

−

1

1

√

−

𝑣

2

𝜋

$$ \int_{-1}^{1} \frac{1}{\sqrt{ 1- \frac{v^2}{c^2} }} dv = \pi $$

## f F uture c C ontent

i I f you're inspired and understand the basics, maybe you could make content about your explorations in epistemic physics!

### m M ultidimensional e E xtension by a A nalogy

s S tart with a 1 d D b B eta distribution. t T he null directions are

−

1

$-1$

 and

1

$1$

, or

𝑌

$Y$

 and

𝑁

, since in

𝑆

0

 there are only two possible spatial directions. t T o extend the spatial b B eta naturally, start by assigning directions to the categories of a d D irichlet distribution. f F or example, for

𝐾

=

4

$K=4$

, the four categories could be n N orth, s S outh, e E ast, and w W est.

t T here is a problem however - this d D irichlet distribution forms a diamond where velocities lie, and it excludes

3

6

.

3

$36.3\%$

 of valid velocities, which can lie in a circle. i I ncreasing

𝐾

 leads to more coverage, but to achieve

1

$100\%$

 coverage, we need to take

𝐾

 to infinity, thus leading to a directional d D irichlet process.

a A similar construction to the j J effreys prior still works here - a prior concentration of 1 on the d D irichlet - both are

/

𝐾

$1/K$

 per category, and imagine cutting the disk in half; each half carries

/

2

$1/2$

, matching

B

e

t

a

(

/

2

,

1

/

2

)

$\operatorname{Beta}(1/2,1/2)$

. g G oing to 3- d D and considering spatial, time, and complex dimensions is beyond the scope of this article.

### o O ther p P otential t T opics

- m M ore connections and predictions

- s S pecific topics - kl KL divergence, b B hattacharyya coefficient, h H ellinger distance, am AM/ gm GM inequality, the g G udermannian, aic AIC, time vs spatial dimensions, photon rocket science, m M oran process, and way more.
- w W ide variety of fields, especially sub-fields in physics, statistics, information theory, and philosophy, but there are even connections with fields you might not expect, like music.
- i I ndependence of evidence, fuzzy logic, opinion pooling and probability fusion, and b B eta mixtures
- g G amma-distributed evidence, and the l L ibby- n N ovick, g G auss-hypergeometric, and g G eneralized b B eta p P rime distributions
- g G roup theory
- w W ave-like and quantum beliefs
- e E xpansive speculation for fun
- d D eriving a c C auchy "mean and variance" and showing equivalence with m M c c C ullagh's parameterization. y Y ou can take a look at the ai AI slop version here (i I curated the demo though).

## f F un p P redictions

h H ere's a small selection of potential predictions; i I hope to expand this list + details in future content. a A lot of these can be further formalized with equations.

- i I n natural selection, curvature of rapidity should correspond to frequency-dependent selection or changing environmental conditions.
- c C onfirmation bias - as confidence increases, the diversity of sources an agent samples reduces as

1

/

𝛾

=

√

1

−

𝑣

2

E

$1/\gamma=\sqrt{ 1-v_{\mathrm{E}}^2 }$

- f F or multidimensional beliefs, photons against a belief are blueshifted and compressed into an angle

1

/

𝛾

$1/\gamma$

, while photons confirming a belief are redshifted and spread out. t T herefore highly confident agents view opponents as a small, loud, homogeneous group while viewing supporters as diverse with many positions.
- e E cho chambers, or polarized communities, have a c C urie temperature - adding independent evidence shifts the c C urie point while shared (dependent) evidence doesn't, though the direction of shift depends on evidence balance.

- h H ysteresis appears - the entrance to and exit from polarized states are different.
- l L et older evidence be forgotten at some rate. i I f we model social amplification, independent evidence, and forgetting rate, we can predict how much independent evidence is needed to eliminate polarization, as well as the echo chamber recovery time.
- m M otivated reasoning - say an agent weighs incoming evidence by its current belief:

𝑒

𝜅

𝑣

$e^{\kappa v}$

 for a success, and

𝑒

−

𝜅

𝑣

$e^{-\kappa v}$

 for a failure. m M otivated reasoning is harmless, in the long run, as long as

𝜅

<

1

$\kappa<1$

, but if

𝜅

>

1

$\kappa>1$

, the agent becomes overly confident.
- o O rder effects in 2 d D or higher - consider two beliefs a A and b B. a A-then- b B vs b B-then- a A should have w W igner rotation

𝑅

≈

1

2

𝜙

𝐴

𝜙

𝐵

s

i

n

⁡

𝜃

$R\approx\tfrac12\phi_A\phi_B\sin\theta$

.

### s S peculation

- t T here might be a r R indler horizon and u U nruh effect affecting beliefs - perhaps there's a boundary where evidence can no longer catch up to a changing belief, and rapidly changing beliefs see illusory weak evidence as u U nruh radiation.

- rapidly persuaded agents may see more patterns in ambiguous evidence as compared to gradually persuaded agents.
- an epistemic black hole may be created if current belief influences what kinds of evidence is possible to receive, or with other models of information dynamics.
- t T he figures in this paper about w W eyl fermions, especially the correspondence between spacetime and energy-momentum cones, seems related. n N ot that i I really know much about w W eyl fermions.

## p P otential s S ources and c C itations

t T his is not an academic paper, but i I wouldn't mind developing this section further. f F eel free to suggest corrections to my article, as well as potentially useful citations and sources (i I'll credit you)!

- https://www.mathpages.com/home/kmath216/kmath216.htm

- v V ery similar, but doesn't treat the evidence behind the probability as first-class

## a little conversation

Leave a thought, ask a question, or select words in a paragraph to reply to that passage.

No published comments yet. You’re welcome to start the conversation.

# Maelic/RelateAnything

## 评论（2/2）

> **viamiraia** · 2026-09-15T15:08:05.000Z　
> also, bonus connections: kl divergence is the ln of the lorentz factor (log(gamma)), the Bhattacharyya coeeficient is 1/gamma, and Jeffreys divergence is velocity times rapidity!

---

> **viamiraia** · 2026-09-15T15:18:58.000Z　
> please note there's precedence https://www.mathpages.com/home/kmath216/kmath216.htmthe difference is i approach it through the lens of evidence, allowing more insights and connections.

## 关联链接

- https://epistemicphysics.com
- https://sloth.ink
- https://www.mathpages.com/home/kmath216/kmath216.htm

## 导航

- 项目页：[[10-项目/raia.fun_09b6f4c8]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
