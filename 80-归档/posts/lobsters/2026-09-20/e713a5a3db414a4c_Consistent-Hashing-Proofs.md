---
type: "corpus"
item_id: "e713a5a3db414a4c"
title: "Consistent Hashing Proofs"
source: "lobsters"
source_name: "Lobsters"
url: "https://lobste.rs/s/eplmed/consistent_hashing_proofs"
project_url: "https://ch.terabyteoff.com/"
published_at: "2026-09-19T09:24:51.480-05:00"
captured_at: "2026-09-20T09:20:20+08:00"
lang: "en"
kind: "post"
tags:
  - 语料
  - lobsters
  - compsci
  - math
metrics: {"score": 5, "comments": 0}
comments_count: 0
comments_total: 0
discovered_via: "lobsters:hottest"
archived: true
archived_at: "2026-09-20T09:21:34+08:00"
archive_reason: "渠道停用"
---

# Consistent Hashing Proofs

- **来源**：Lobsters　|　**kind**：post
- **原帖**：https://lobste.rs/s/eplmed/consistent_hashing_proofs
- **指标**：得分=5 · 评论=0
- **作者**：—　|　**发布**：2026-09-19T09:24:51.480-05:00
- **项目链接**：https://ch.terabyteoff.com/
- **采集**：2026-09-20T09:20:20+08:00　|　**id**：`e713a5a3db414a4c`

## 正文

Consistent Hashing Proofs

# Consistent hashing math #

And more than you wanted to know about it

 Kevin Guthrie

This is a derivation of the formulas that describe the distribution of work in systems using consistent hashing to share work. It is part technical paper, part demo and part blog post, so there is a lot of math, some web assembly, but also some jokes. My hope is that it will be complete and compelling but also approachable (and interesting?) for any reader regardless of background.

This is a companion piece to this blog post I wrote for Cloudflare, so check it out if you want to hear the complete story and how we used the math here to safely reclaim 100+ TB of RAM on the edge. It also has a basic primer on what consistent hashing even is.

## Motivation #

The main reason I'm writing this is to help out anyone in the future who is interested in this subject. When I first started researching the subject of consistent hashing and how its accuracy changes based on the number of hashes, I was frustrated by the resources that came up when googling. The results ranged from detailed (but utterly opaque to me) technical papers on the subject or understandable but incomplete derivations from online computer science class resources.

The payoff in both of these cases is an upper bound on the error in how evenly tasks are distributed with consistent hashing given in terms of asymptotic, "Big-O" limits

$O(1k) \mathcal{O}\left( \sqrt{\frac{1}{k}} \right)$ O(k 1​​)

where $kk$ k is the number of hashes per server. It's not clear how closely the actual error matches that limit, so I set out to derive the actual formula and find out for myself. What I found was that all you need to solve this problem analytically is some high-school math and a little creativity.

## TLDR #

If you are here for a quick answer, I won't make you wait. The formula for consistent-hashing error for $NN$ N servers with $kk$ k hashes each is

$Errk=N−1kN+1 \text{Err}_k = \sqrt{\frac{N-1}{kN+1}}$ Err k​= k N+ 1 N− 1​​

Which is very close to $1k \sqrt{\frac{1}{k}}$ k 1​​ if $NN$ N is large. In a system where the number of servers is 50 or more, the difference between the actual error value and the approximation is ~1%. It's a useful approximation, but without seeing what went into it, it's impossible to see what its other implications are. For instance, how do things change if each server has a different number of hashes? We will answer that question and more, so now let's prove it!

## Part 1 - Single hashes #

In order to get to the above equation, we need to start with a simpler entry point. When we use consistent hashing in practice, we operate on integers (normally 32 or 64-bit). This makes computations easier and faster as well as giving us access to well-behaved hash functions, but for our purposes it's going to be easier to consider hashes as real numbers between zero and 1 instead of a bounded range of integers.

Unfortunately, this does mean that the result I've already stated above is also an approximation (and thus I have already lied to you), but as you will see, this is a good approximation as long as your number of hashes and servers is not too big.

### Baby Steps #

Let's ease our way in and start with something small. Let's say we have a single server with a single hash that's part of a consistent hash setup with at least 1 more server. How do we determine the distribution for the workload that our server will handle? One easy way to think about this is geometrically. Recall from above that we are remapping the integer hash space to real numbers between 0 and 1; in this representation, the fraction of the work handled by our server is the same as the length of the segment assigned to it (assuming the hashes of the tasks have a uniform distribution). Below is an interactive demo showing how the size of the region associated with our server can vary compared to the average size.

Total Hashes 20

20

# Rerun

The error percentage shows how far off from the expected size our server's region is.

$L−1/H1/H \frac{L - 1/H}{1/H}$ 1/ H L− 1/ H​

where $HH$ H is the total number of hashes.

After rerunning a few times you can see that the size of the region associated with our server varies wildly and that variation does not seem to depend on the total number of hashes. We'll see why that is in a moment.

### Loop unrolling #

One important thing to notice that I've glossed over so far is that the region between the first and last hash is connected making the hash domain effectively a ✨circle✨. That's why most posts about consistent hashing feature a graphic like the one below showing the angular ranges assigned to each server as a different color.

Looking at the ranges like this reinforces a fact we have already used. The absolute positions for the hashes for the servers do not matter. It's only their positions relative to each other that affect the distribution. In other words, there are no "special" points in the hash output, so we can choose our "zero" point to be anywhere. Setting zero to be equal to one of the hashes has the nice property that we no longer have to consider the circular aspect of the hash ring.

Naturally the best point to choose to be our "zero" for simplicity is the hash associated with our server.

Total Hashes 20

20

# Rerun

This reorientation of the hash space means that the length of the segment associated with our server is only determined by the minimum of all other hashes.

$L=min{h2,h3,...,hH} L = min\left\{ h_2, h_3, ..., h_H \right\}$ L= min{ h 2​, h 3​,..., h H​}

This is something we can calculate a statistical distribution for.

### A little statistics #

Statistics was the only class in college that I got a C in (Maybe I would have gone to class if it wasn't at 8am), so I don't feel like I have any right to lecture anyone on it ... but I'm going to anyway.

Ultimately we would like to be able to get the mean and standard deviation for the length of the segment associated with our server, and those are defined in terms of the probability-density function (PDF) for the length of the first segment. In order to get to the PDF we will start by first deriving its cumulative-distribution function (CDF).

Consider a point $xx$ x somewhere on our number line from 0 to 1. The CDF for the length of our segment is the probability that the length is $≤x\le x$≤ x. That probability is the same as the probability that the length is not $>x> x$> x which is

$P(L≤x)=1−P(L>x) P \left( L \le x \right) = 1 - P \left( L > x \right)$ P(L≤ x)= 1− P(L> x)

This is true because $P(L≤x)P \left( L \le x \right)$ P(L≤ x) and $P(L>x)P \left( L > x \right)$ P(L> x) are "complementary events" which is just a fancy way of saying that one or the other is always true, but never both. We make this change because $P(L>x)P \left( L > x \right)$ P(L> x) is the same as the probability that all the hashes ${h2,h3,...,hH}\left\{ h_2, h_3, ..., h_H\right\}${ h 2​, h 3​,..., h H​} are $≥x\ge x$≥ x. Since each hash is independent (meaning the value of one hash doesn't affect any other), we can say this probability of all being true is the product of the probability of each being independently true.

$P(L≥x)=P({h2,h3,...hH}>x)=P(h2>x)×P(h3>x)×...×P(hH>x)⏟H−1 Terms \begin{align*}
 P \left(L \ge x\right) &= P\left( \left\{ h_2, h_3, ... h_H \right\} > x\right) \\
 &= \underbrace{
 P\left(h_2 > x\right) \times
 P\left(h_3 > x\right) \times ... \times
 P\left(h_H > x\right) }_{H-1\text{ Terms}}\\
 \end{align*}$ P(L≥ x)​= P({ h 2​, h 3​,... h H​}> x)= H− 1 Terms P(h 2​> x)× P(h 3​> x)×...× P(h H​> x)​​​

Determining the probability that an individual hash is $>x> x$> x is simply $1−x1 - x$ 1− x. We could prove this by integrating the PDF of the uniform distribution, but that's a bit boring (and we'll end up doing that later). Instead, here is another interactive demo that calculates the probability empirically via simulation.

x 20

0.2

Total Hashes 6

64

# Rerun

So now that we know $P(hi>x)=1−xP \left(h_i > x\right) = 1 - x$ P(h i​> x)= 1− x and we know that that probability is the same for every hash, we can put everything together to get the CDF for the length of our segment $LL$ L.

$CDF(L)=P(L≤x)=1−P(L>x)=1−P(h2>x)×P(h3>x)×...×P(hH>x)=1−P(h>x)H−1=1−(1−x)H−1 \begin{align*}
 \text{CDF}\left(L\right) &= P \left(L \le x\right) \\
 &= 1 - P \left(L > x\right) \\
 &= 1 - P\left(h_2 > x\right) \times
 P\left(h_3 > x\right) \times ... \times
 P\left(h_H > x\right) \\
 &= 1 - P\left(h > x\right)^{H-1} \\
 &= \boxed{1 - \left(1 - x\right)^{H - 1}}
 \end{align*}$ CDF(L)​= P(L≤ x)= 1− P(L> x)= 1− P(h 2​> x)× P(h 3​> x)×...× P(h H​> x)= 1− P(h> x) H− 1= 1−(1− x) H− 1​​

### A little calculus 😅 #

Getting from CDF to PDF is a matter of differentiating the CDF by $xx$ x. So buckle up, this is where the calculus starts. Here we just need to use the distributive property and the power rule.

$PDF(L)=ddxCDF(x)=ddx(1−(1−x)H−1)=ddx(1)−ddx(1−x)H−1=0−(−(H−1))(1−x)H−2=(H−1)(1−x)H−2 \begin{align*}
 \text{PDF} \left(L\right)
 &= \frac{d}{dx}\text{CDF} \left( x \right) \\
 &= \frac{d}{dx}\left( 1 - \left(1 - x\right)^{H - 1} \right) \\
 &= \frac{d}{dx}\left( 1 \right) - \frac{d}{dx}\left(1 - x\right)^{H - 1} \\
 &= 0 - \left(-\left( H - 1 \right)\right)\left(1-x\right)^{H-2} \\
 &= \boxed{\left(H - 1 \right)\left(1-x\right)^{H-2}}
 \end{align*}$ PDF(L)​= d x d​ CDF(x)= d x d​(1−(1− x) H− 1)= d x d​(1)− d x d​(1− x) H− 1= 0−(−(H− 1))(1− x) H− 2=(H− 1)(1− x) H− 2​​

Which if we plot, looks like this.

Total Hashes 7

128

### Reality vs probability #

Let's pause for a second before we use the PDF above to calculate the expected value and standard deviation to bring things back to reality. As you might have noticed, the PDF has values above 1. This should be a good clue that the PDF does not give you a way to look up the probability of a specific value ... so then like what good is it? ... and how do you find out the probability of a specific value?

The answer to both of those questions is histograms. As an answer to a purely mathematical problem it's maybe a little unsatisfying. Histograms are exceedingly practical tools that we typically use when measuring or visualizing things in the real world like latency or dB levels. The reason they come up here is because of the simplification we made at the very beginning. Our CDF and PDF above are based on the continuous range between 0 and 1 instead of the discrete length that will actually appear in our hash output. That simplification means that each specific length has infinite precision and therefore an infinitesimal probability by itself. In order to get an appreciable/useful value for probability, we have to look at the probability within a specific range of lengths. Plotting the probability between a bunch of different ranges is essentially the definition of a histogram, and the way we calculate the probability in that range is with the PDF (or CDF).

$P(xmin<x≤xmax)=∫xminxmaxPDF(x)dx=CDF(xmax)−CDF(xmin) \begin{align*}
 P\left(x_{min} < x \le x_{max}\right)
 &= \int_{x_{min}}^{x_{max}}\text{PDF}(x)dx \\
 &= \text{CDF}\left(x_{max}\right) - \text{CDF}\left(x_{min}\right)
 \end{align*}$ P(x min​< x≤ x ma x​)​=∫ x min​ x ma x​​ PDF(x) d x= CDF(x ma x​)− CDF(x min​)​

Using that definition we can create a new plot based on the derived PDF that shows the probability of a single-segment length with a variable histogram resolution.

Total Hashes 7

128

Histogram Bins 4

16

Notice the plot still follows the same shape as the pdf. This makes sense since the expression $CDF(xmax)−CDF(xmin)\text{CDF}\left(x_{max}\right) - \text{CDF}\left(x_{min}\right)$ CDF(x ma x​)− CDF(x min​) is just a scaled approximation of the PDF at $xx$ x. Calculating the probability of our single segment having a value within a discrete range has the advantage that we can now compare our calculated distribution to some 

real-world

 simulated results. Is this necessary? No ... math is math ... but sometimes it's helpful to prove to yourself that your math is the right math.

Below is an interactive demo that allows you to simulate a bunch of single-segment lengths and compare the empirical distribution with the derived one for a given number of hashes.

Total Hashes 8

256

Histogram Bins 4

16

Sample Count 10

1024

# Rerun

Excellent! After playing around with the possible values in the experiment above, it should be possible to convince yourself that our math does in fact math. Let's finish off this section by calculating the mean and standard deviation for the single-hash setup.

### Single-hash distribution finale #

We'll make this quick since we still have a long way to go. To get the expected value and standard deviation for the single-hash distribution, we can apply the definitions directly based on the PDF we derived above.

The expected value for the length of a single hash segment when there are $HH$ H total hashes is:

$Exp(L)=∫x⋅PDF(x)dx=∫01x(H−1)(1−x)H−2dx \begin{align*}
 \text{Exp}\left(L\right)
 &= \int{x\cdot\text{PDF}(x)dx} \\
 &= \int_0^1{x \left( H - 1 \right)\left(1 - x\right)^{H-2}dx} \\
 \end{align*}$ Exp(L)​=∫ x⋅ PDF(x) d x=∫ 0 1​ x(H− 1)(1− x) H− 2 d x​

To evaluate that we'll need to use one of the secret dark arts of calculus: integration by parts. It looks confusing...

$∫u⋅dv=u⋅v−∫v⋅du \large{ \int u\cdot dv = u\cdot v - \int{v\cdot du} }$∫ u⋅ d v= u⋅ v−∫ v⋅ d u

... and it feels illegal, but it's really just the chain rule in reverse. First we need to define our $uu$ u and $dvdv$ d v

$u=xv=−(1−x)H−1⟹du=dx⟹dv=(H−1)(1−x)H−2dx \begin{align*}
 u &= x \\
 v &= -\left(1-x\right)^{H-1} \\
 \end{align*}

 \begin{align*}
 \Longrightarrow du &= dx \\
 \Longrightarrow dv &= \left( H - 1 \right)\left(1 - x\right)^{H-2}dx \\
 \end{align*}$ u v​= x=−(1− x) H− 1​⟹ d u⟹ d v​= d x=(H− 1)(1− x) H− 2 d x​

Now with a little algebra and calculus autopilot we get the expected value in terms of $HH$ H.

$Exp(L)=∫01x(H−1)(1−x)H−2dx=∫x=0x=1u⋅dv=u⋅v∣x=0x=1−∫x=0x=1v⋅du=[x(1−x)H−1]∣01+∫01(1−x)H−1dx=(0−0)−1H[(1−x)H]∣01=−1H(0−1)=1H \begin{align*}
 \text{Exp}\left(L\right) &= \int_0^1{x \left( H
 - 1 \right)\left(1 - x\right)^{H-2}dx} \\
 &= \int_{x=0}^{x=1}{u\cdot dv} \\
 &= \left.u\cdot v\right|_{x=0}^{x=1}
 - \int_{x=0}^{x=1}{v\cdot du} \\
 &= \left.\left[x\left(1-x\right)^{H-1}\right]\right|_{0}^{1}
 + \int_0^1{\left(1-x\right)^{H-1} dx} \\
 &= \left(0 - 0\right)
 - \frac{1}{H}\left.\left[\left(1-x\right)^H\right]\right|_0^1 \\
 &= - \frac{1}{H}\left(0 - 1\right) \\
 &= \boxed{\frac{1}{H}}
 \end{align*}$ Exp(L)​=∫ 0 1​ x(H− 1)(1− x) H− 2 d x=∫ x= 0 x= 1​ u⋅ d v= u⋅ v∣ x= 0 x= 1​−∫ x= 0 x= 1​ v⋅ d u= [x(1− x) H− 1]​ 0 1​+∫ 0 1​(1− x) H− 1 d x=(0− 0)− H 1​ [(1− x) H]​ 0 1​=− H 1​(0− 1)= H 1​​​

Which is ... a little underwhelming given the amount of manipulation it took to get there, but it does at least make sense. The expected value is what you get when the whole hash space is split up evenly between all $HH$ H segments.

Let's move on to the standard deviation calculation which is just the square root of the variance,

$SD(L)=Var(L) \text{SD}\left(L\right) = \sqrt{\text{Var}\left(L\right)}$ SD(L)= Var(L)​

So we are actually going to calculate $Var(L)\text{Var}\left(L\right)$ Var(L) and save ourselves some radicals. Variance is defined as

$Var(L)=∫[x−Exp(L)]2⋅PDF(x)dx=∫01[x−1H]2(H−1)(1−x)H−2dx \begin{align*}
 \text{Var}\left(L\right)
 &= \int{\left[x
 - \text{Exp}\left(L\right)\right]^2
 \cdot \text{PDF}\left(x\right) dx} \\
 &= \int_0^1{\left[x
 - \frac{1}{H}\right]^2
 \left( H - 1 \right)\left(1 - x\right)^{H-2}dx}
 \end{align*}$ Var(L)​=∫ [x− Exp(L)] 2⋅ PDF(x) d x=∫ 0 1​ [x− H 1​] 2(H− 1)(1− x) H− 2 d x​

We are going to do integration by parts again, but because our $uu$ u term has an $x2x^2$ x 2 in it, we will have to integrate by parts twice.

$u1=(x−1H)2u2=2(x−1H)v1=−(1−x)H−1v2=−1H(1−x)H⟹du1=2(x−1H)dx⟹du2=2dx⟹dv1=(H−1)(1−x)H−2dx⟹dv2=(1−x)H−1dx \begin{align*}
 u_1 &= \left(x - \frac{1}{H}\right)^2 \hspace{10px} \\
 u_2 &= 2\left(x - \frac{1}{H}\right)\hspace{10px} \\
 v_1 &= -\left(1-x\right)^{H-1} \hspace{10px} \\
 v_2 &= -\frac{1}{H}\left(1-x\right)^{H} \hspace{10px} \\
 \end{align*}

 \begin{align*}
 \Longrightarrow \hspace{10px} du_1 &= 2\left(x - \frac{1}{H}\right)dx \\
 \Longrightarrow \hspace{10px} du_2 &= 2dx \\
 \Longrightarrow \hspace{10px} dv_1 &= \left( H - 1 \right)\left(1 - x\right)^{H-2}dx \\
 \Longrightarrow \hspace{10px} dv_2 &= \left(1-x\right)^{H-1}dx \\
 \end{align*}$ u 1​ u 2​ v 1​ v 2​​=(x− H 1​) 2= 2(x− H 1​)=−(1− x) H− 1=− H 1​(1− x) H​⟹ d u 1​⟹ d u 2​⟹ d v 1​⟹ d v 2​​= 2(x− H 1​) d x= 2 d x=(H− 1)(1− x) H− 2 d x=(1− x) H− 1 d x​

Now we can let the autopilot run again and find the variance for the length of single segment out of $HH$ H total hashes.

$Var(L)=∫01[x−1H]2⏟u1(H−1)(1−x)H−2⏟dv1dx=u1v1∣x=0x=1−∫x=0x=1v1du1=u1v1∣x=0x=1+∫012(x−1H)⏟u2(1−x)H−1⏟dv2dx=[u1v1+u2v2]∣x=0x=1−∫x=0x=1v2du2=[−(x−1H)2(1−x)H−1−2(x−1H)1H(1−x)H]∣01+2H∫01(1−x)Hdx=[−0−0+1H2−2H2]+2H[−1H+1(1−x)H+1]∣01=−1H2+2H(H+1)=H−1H2(H+1) \begin{align*}
 \text{Var}\left(L\right)
 &= \int_0^1{\underbrace{\left[x
 - \frac{1}{H}\right]^2}_{u_1}\underbrace{
 \left( H - 1 \right)\left(1 - x\right)^{H-2}}_{dv_1}dx} \\
 &= \left.u_1v_1\right|_{x=0}^{x=1} - \int_{x=0}^{x=1}v_1 du_1 \\
 &= \left.u_1v_1\right|_{x=0}^{x=1}
 + \int_0^1{\underbrace{2\left(x-\frac{1}{H}\right)}_{u_2}
 \underbrace{\left(1-x\right)^{H-1}}_{dv_2}dx} \\
 &= \left.\left[u_1v_1 + u_2v_2\right]\right|_{x=0}^{x=1}
 - \int_{x=0}^{x=1}{v_2du_2} \\
 &= \begin{align*} &\left.\left[
 -\left(x - \frac{1}{H}\right)^2\left(1-x\right)^{H-1}
 - 2\left(x - \frac{1}{H}\right)\frac{1}{H}\left(1-x\right)^{H}
 \right]\right|_0^1 \\
 &+ \frac{2}{H}\int_0^1{\left(1-x\right)^Hdx}
 \end{align*} \\
 &= \left[
 -0-0+\frac{1}{H^2}-\frac{2}{H^2}
 \right]
 + \frac{2}{H}\left.\left[
 -\frac{1}{H+1}\left(1-x\right)^{H+1}
 \right]\right|_0^1 \\
 &= -\frac{1}{H^2}+\frac{2}{H\left(H+1\right)} \\
 &= \boxed{\frac{H-1}{H^2\left(H+1\right)}}
 \end{align*}$ Var(L)​=∫ 0 1​ u 1​ [x− H 1​] 2​​ d v 1​(H− 1)(1− x) H− 2​​ d x= u 1​ v 1​∣ x= 0 x= 1​−∫ x= 0 x= 1​ v 1​ d u 1​= u 1​ v 1​∣ x= 0 x= 1​+∫ 0 1​ u 2​ 2(x− H 1​)​​ d v 2​(1− x) H− 1​​ d x= [u 1​ v 1​+ u 2​ v 2​]∣ x= 0 x= 1​−∫ x= 0 x= 1​ v 2​ d u 2​=​ [−(x− H 1​) 2(1− x) H− 1− 2(x− H 1​) H 1​(1− x) H]​ 0 1​+ H 2​∫ 0 1​(1− x) H d x​= [− 0− 0+ H 2 1​− H 2 2​]+ H 2​ [− H+ 1 1​(1− x) H+ 1]​ 0 1​=− H 2 1​+ H(H+ 1) 2​= H 2(H+ 1) H− 1​​​

Now we can take the square root and get to the standard deviation.

$SD(L)=Var(L)=1HH−1H+1 \begin{align*}
 \text{SD}\left(L\right)
 &=\sqrt{\text{Var}\left(L\right)}\\
 &=\boxed{\frac{1}{H}\sqrt{\frac{H-1}{H+1}}}
 \end{align*}$ SD(L)​= Var(L)​= H 1​ H+ 1 H− 1​​​​

It's worth pausing here at the end to think about what that standard deviation says in practical terms. Remember that (even if we've strayed into the abstract world a bit) this distribution is about how evenly we are sharing work between servers in the physical world. Standard deviation tells us the distance from the mean for most of the values in our distribution. In a sense it's a prediction of how much more or less load a server will handle than expected.

The drawback for standard deviation is that it's defined in absolute terms. You can see from the formula that the standard deviation goes down as the inverse of the total number of hashes. It would be easy to think that you could make a single-hash consistent hashing system more accurate by adding more total hashes, but that is forgetting that the portion of the range covered by a single segment also decreases as the inverse of the total number of hashes. So at $H=100H=100$ H= 100 the standard deviation is about $0.99%0.99\%$ 0.99%, the expected size of the segment is $1%1\%$ 1%, so the size of error on either side of the expected value is almost equal to the expected size.

A more useful analog for error in our consistent hashing systems (and the one I have been using until now without explanation) is coefficient of variation. CV is simply the standard deviation divided by the expected value or more simply, it's the error margin transformed to match the scale of what we expect. In our case the CV is

$Err≔CV(L)=SD(L)Exp(L)=H−1H+1 \text{Err} \colonequals \text{CV}(L) = \frac{\text{SD}(L)}{\text{Exp}(L)}=\boxed{\sqrt{\frac{H-1}{H+1}}}$ Err:= CV(L)= Exp(L) SD(L)​= H+ 1 H− 1​​​

Which for our $H=100H=100$ H= 100 example gives a much more meaningful error of $CV(L)=99%\text{CV}(L)=99\%$ CV(L)= 99%, and allows us to put a finger on just how bad single-hash consistent hashing is. For almost all values of H, the error rate is constant, and about 100%!

Luckily this single-segment derivation was only the tutorial boss for consistent hashing. Seeing how (and how much) we can improve consistent hashing is what we'll work on in the next section.

## Interlude - Making $kk$ k hashes solvable #

Deriving the distribution for consistent hashing scenarios with more than one hash per server on its face seems like a complicated and labor intensive problem. I think this is the main reason the articles I found on the subject make appeals to Chebyshev's inequality to establish an upper bound.

Looking at the literature that's out there (at least what's easy to find by googling) makes it seem like this problem is too difficult to be worth solving directly. Luckily for us, the analytical solution to the multi-segment case is not much more difficult than the single-segment case as long as you are willing to get onboard (with a sketch of a proof) a major simplification, and like I said before, it only takes some high-school level math (by which I mean calculus and statistics).

### What exactly are we doing here? #

Recall that in order to determine the percentage of work our server will handle in the single-segment case, we need to find the fraction of the hash output space assigned to our server. When we scaled our output space to fit between zero and one (and pretending it was continuous), all we needed to find was the length of the segment associated with our server. The only thing that changes in the multi-hash case is we need to find the probability distribution for the sum of the length of all the segments associated with our server.

Total Hashes 20

20

# Rerun

Now we can shift our hashes around just like we did before so that the "zero" point falls on one of our servers hashes ... but it's not obvious which hash we should pick, nor is it obvious if that even buys us anything. Even with one hash nestled at the start of the number line, we still have a bunch of messy gaps to deal with. Getting rid of that messiness is going to require taking a step into the unknown. This is going to feel like that one weird trick to calculate your consistent hashing distribution, and I'll admit it doesn't seem like it should be legal. To help get you onboard, we'll condense the essence of our weird trick into one small step so that hopefully the subsequent steps feel logical (if not obvious).

### Marbles and wires #

What if we have just 2 hashes associated with our server? We can choose one of them to be the zero of our number line. The "zero" hash creates a segment $S1S_1$ S 1​ that sits nicely at the beginning of the number line, but it leaves one more floating around out there creating a second segment at some random position index $mm$ m with some random size $SmS_m$ S m​.

Total Hashes 20

20

# Rerun

It's tempting to think that we could use the same formula above that we slogged through to describe the distribution for this second segment, and in a way we can. The formula we have is for the distribution for any single segment, so if we were looking at our second segment alone without any other information, its length would follow the same distribution we found in the single segment case. Unfortunately if we're considering it by itself, it isn't really "second" anymore.

Considering both segments at the same time leads us into the world of conditional probability. It exists to cover the gray area between when you know more than nothing and less than everything about a system. The classic example is removing colored marbles from a bag containing an equal number of red and green marbles. The first marble chosen has an equal chance of being red, but its removal means the second marble is less likely to have the same color as the first simply because there is 1 fewer of that color to choose from.

Number of each color 10

10

Trials 50

50

# Rerun

In general, the relationship between dependent random events (call them $AA$ A and $BB$ B) is characterized by this equation:

$P(A and B)=P(B∣A)⏟⋅P(A)        Prob of B given A already happened P(A \text{ and } B) = \underbrace{P(B|A)} \cdot P(A) \\
 \text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\text{ }\scriptsize{
 {\text{Prob of }B\text{ given } A \text{ already happened}}
 }$ P(A and B)= P(B∣ A)​⋅ P(A) Prob of B given A already happened

We can see an analog in our 2-segment case in how the length of segment 1 affects the possibilities for the second. If segment 1 is really big, it leaves less room for the rest of the segments to occupy, so the second will be more likely to be smaller. Similarly if segment 1 is really small, the distribution for the second will approach what it would be if segment 1 wasn't even there. There is an important difference with the 2-segment distribution that we can exploit to make our math easier. The randomness in the marble scenario is in which marble is drawn. The randomness in our hash segment case is about the random length of a specific segment. We could think of the segments as being formed from taking a single wire and cutting it into $HH$ H parts, but we aren't really interested in pulling random wires out of a bag (or a drawer).

It's more like we have $HH$ H numbered bags, and each bag has a single wire of a random length where the total length is known. What's important here is that there are no "special" bags. We can exchange any one bag for another, so the probability distribution for the length of the segment in each unopened bag must be the same!

### Avoid empty space #

If you'll recall that in the beginning of the previous section we were trying to find the sum of the lengths of two segments. One on the far left of the number line with length $S1S_1$ S 1​ and one at a random index $mm$ m with length $SmS_m$ S m​. In terms of our $HH$ H wires in bags, we can find the sum of $S1S_1$ S 1​ and $SmS_m$ S m​ with a 2-step process

1. Take the wire from bag 1
2. Add segment 1 to the segment in bag $mm$ m

We know from our discussion above that the length of the wire in bag 1 will be distributed like $(H−1)(1−x)H−2(H-1)(1-x)^{H-2}$(H− 1)(1− x) H− 2, and that knowing the length of $S1S_1$ S 1​ will affect the distribution of $SmS_m$ S m​ (even if we don't know exactly how). But we also know there is nothing special about bag $mm$ m, so the distribution of all the other bags is changed in the same way meaning we could have chosen from any wire from any bag and the resulting distribution would be the same. So how about bag 2? Let's jump back to our original setup and apply what we just learned. Choosing bags 1 and 2 is the equivalent to measuring the 2 left-most segments in our number line.

Total Hashes 20

20

# Rerun

This simplifies things considerably because we no longer have a random amount of space in between to account for. We can take this a step further by realizing that this "no special bags" trick works for any number of segments. The distribution for the sum of any $kk$ k segments is the same as the distribution for the first $kk$ k consecutive segments.

Total Hashes 20

20

Summed hashes (k) 10

10

# Rerun

 With this fact in hand, we can use almost exactly the same process to get the distribution for the sum of k segments as we did for a single segment. 

## Part 2 - More than a single hash #

Depending on your perspective, this is where things either get really interesting or this will feel like déjà vu. Thanks to some logic and (somehow) legit probability shell game, we now know the shape of the problem we need to solve to determine the consistent hashing error for a server with $kk$ k hashes out of a total of $HH$ H. What is the distribution for the sum of the first $kk$ k segments on the number line? We already solved this with $k=1k=1$ k= 1 by cleverly defining a CDF using a little calculus to get from there to a PDF, variance and then finally to the error. Let's forget about being DRY and repeat ourselves.

### Multi-hash CDF #

Recall the definition for a CDF is that it tells us the probability that the thing we are looking for is smaller than a value $xx$ x. We'll denote our CDF for $kk$ k hashes as

$CDFk(x)=P(∑i=1kLi≤x)\text{CDF}_k(x) = P\left(\sum_{i=1}^{k}{L_i} \le x\right)$ CDF k​(x)= P(i= 1∑ k​ L i​≤ x)

But in order to write an expression for it, we'll need to do some leg work. Also notice we're bringing "sigma" notation, so now you know things are getting serious.

Recall that we used " complementary" events to write the CDF for the single-hash case. That was how we were able to put the probability that the length of the first segment is less than $xx$ x framed in terms of the probability that all hashes are greater than $xx$ x. This reframing of the problem was important because it put a limit on the location of individual hashes, and each hash has a known uniform and independent distribution. That same complementary event trick works here, but not quite as cleanly. The complementary event for the sum of the first $kk$ k segments $≤\le$≤ $xx$ x is simply that sum of the first $kk$ k segments is > $xx$ x.

$CDFk(x)=P(∑i=1kLi≤x)=1−P(∑i=1kLi>x)\begin{align*}
\text{CDF}_k(x) &= P\left(\sum_{i=1}^{k}{L_i} \le x\right) \\
 &= 1 - P\left(\sum_{i=1}^{k}{L_i} > x\right)
\end{align*}$ CDF k​(x)​= P(i= 1∑ k​ L i​≤ x)= 1− P(i= 1∑ k​ L i​> x)​

That admittedly doesn't seem like a big step forward, but stay with me. Recall that we can pin the first hash $h1h_1$ h 1​ at zero, so we can simplify the expression for the sum of the first $kk$ k hash segments to just the position of the $k+1k+1$ k+ 1-th smallest hash:

$∑i=1kLi=hk+1\sum_{i=1}^{k}{L_i} = h_{k+1}$ i= 1∑ k​ L i​= h k+ 1​

Total Hashes 20

20

Summed Hashes (k) 3

3

# Rerun

We can use this to rewrite the CDF for the sum of k segments as

$CDFk(x)=1−P(hk+1>x)\text{CDF}_k(x) = 1-P \left( h_{k+1} >x\right)$ CDF k​(x)= 1− P(h k+ 1​> x)

While this insight doesn't give us a directly usable set of independent probabilities, it does allow us to simplify our length measuring problem in one of counting. Because if the $k+1k+1$ k+ 1-th smallest hash is $>x> x$> x, then it means the total number of hashes less than $xx$ x must be less than $k+1k+1$ k+ 1. Since we have pinned $h1h_1$ h 1​ at 0, we can go a little further and say the number of unpinned hashes (the only hashes that actually matter in our distribution) must be less than $kk$ k.

Let's introduce some new notation for this idea of counting the number of hashes that are $≤x\le x$≤ x. For a set of $HH$ H random hashes, we'll let $C(x)C(x)$ C(x) be the count of hashes that are $<x<x$< x. Or if we wanted to be cool, we could write this as

$C(x)≔∣{h∈H::h<x}∣C(x) \colonequals \left| \left\{ h \in H :: h

Error fetching https://www.reddit.com/r/SaaS/comments/1wi5qqv/i_built_the_saas_end_to_end_but_dont_know_about/: CRAWL_LIVECRAWL_TIMEOUT
