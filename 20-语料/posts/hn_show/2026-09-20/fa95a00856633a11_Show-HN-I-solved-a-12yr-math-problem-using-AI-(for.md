---
type: "corpus"
item_id: "fa95a00856633a11"
title: "Show HN: I solved a 12yr math problem using AI (formalized; awaiting review) [pdf]"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49717545"
author: "kbr-"
published_at: "2026-09-15T19:24:06Z"
captured_at: "2026-09-20T14:17:39+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_kbr-
  - story_49717545
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:90d"
---

# Show HN: I solved a 12yr math problem using AI (formalized; awaiting review) [pdf]

> [!info] 一句话导读
> A superpolynomial lower bound for the bit pigeonhole principle in resolution over parities

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49717545>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：kbr-　|　发布：2026-09-15T19:24:06Z
> 项目链接：—
> 采集：2026-09-20T14:17:39+08:00　|　id：`fa95a00856633a11`

## 正文

Author: Kamil Braun

### A superpolynomial lower bound for the bit pigeonhole principle in resolution over parities

Kamil Braun kamilgbraun@gmail.com With substantial assistance from Claude and GPT models. More details in Section 8.3.

Preprint 15 September 2026

Abstract We prove that the usual bit pigeonhole principle with n + 1 pigeons and n = 2 ℓ holes requires superpolynomial-size DAG-like resolution-over-parities refutations, without regularity or proof-depth restrictions. An arbitrary short refutation yields polynomially many complete affine extension blocks admitting an ordinary polynomial-calculus refutation of degree O(log n). A simultaneous weighted coefficient substitution would produce a nonzero row-linear old-base consequence at degree O(√n(log n)2) = o(n). Matching-moment extension and a residual cube functional exclude that consequence. The theorem and its dependencies, including the required chessboard homology, have been formalized in Lean. We present the verified arguments with permanent links to the formal statements and proofs, and describe the open research framework in which they were developed. This manuscript is a preprint that has not yet been externally peer reviewed.

#### Contents

1 The claim and its setting 3
1.1 The bit pigeonhole principle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 The proof system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Prior results and the scope of the claim . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Proof organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Ordinary degree and polynomial calculus 4
3 Matching moments and a stable old filtration 6
4 The bit decoder and a separating functional 8
5 Excluding one complete affine extension level 11
5.1 Affine linear algebra and ordinary restriction . . . . . . . . . . . . . . . . . . . . . . 11
5.2 One simultaneous weighted substitution . . . . . . . . . . . . . . . . . . . . . . . . . 13
6 A direct PC simulation of the proof DAG 14
7 Closing the proof-size parameters 18
7.1 What the conclusion uses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
7.2 Relationship to the broader PHP project . . . . . . . . . . . . . . . . . . . . . . . . . 19
8 Evidence and the research framework 19
8.1 Mathematical provenance and component checks . . . . . . . . . . . . . . . . . . . . 19
8.2 An inspectable workflow for autonomous research . . . . . . . . . . . . . . . . . . . . 20
8.3 Contributions and development history . . . . . . . . . . . . . . . . . . . . . . . . . . 21
A The required chessboard homology 22
A.1 Augmented chains and their elementary operations . . . . . . . . . . . . . . . . . . . 22
A.2 The finite homological cover argument . . . . . . . . . . . . . . . . . . . . . . . . . . 24
A.3 Chessboard stars, arithmetic, and assembly . . . . . . . . . . . . . . . . . . . . . . . 25
2

#### 1 The claim and its setting

Resolution over parities augments ordinary resolution with affine equations over F2. The system was introduced by Itsykson and Sokolov [IS14, IS20]. Its unrestricted proof-size lower-bound problem remains an explicit open benchmark in the literature reviewed for this preprint [IPS26]. The contribution claimed here is a superpolynomial lower bound for the standard bit pigeonhole principle in unrestricted DAG-like Res(⊕).

1.1 The bit pigeonhole principle
Fix ℓ ≥ 2, put n = 2 ℓ and m = n + 1, and introduce
bit (i ∈ [m], t ∈ [ℓ]).
The row bi encodes one of the n labels in {0, 1} ℓ. For a label z, let [bit ̸= zt] denote bit when zt = 0
and ¬ bit when zt = 1. The usual CNF encoding is

BPHP n+1 n = ^ i 0, there is ℓ0(K) such that for
every ℓ ≥ ℓ0(K), every DAG-like Res(⊕) refutation of BPHP2 ℓ+1 2 ℓ has more than 2 Kℓ nodes. The
conclusion holds for both rule conventions above.
Thus the minimum line count is n ω(1) along powers of two. This also implies a superpolynomial
lower bound on total proof-description size. The input length in (1.1) is polynomial in n, so using
input length instead of n gives the same qualitative conclusion.

1.3 Prior results and the scope of the claim
Efremenko, Garlík, and Itsykson [EGI25] prove a 2Ω(n1/3/ log n) size bound for regular Res(⊕)
refutations of bit PHP. Their unrestricted DAG-like result is an affine-width bound. Bhattacharya,
Chattopadhyay, and Dvořák [BCD24] exhibit formulas that are exponentially hard for bottom
regular Res(⊕), although they have short proofs in general ordinary resolution. This separation
demonstrates the importance of removing regularity.
Bhattacharya and Chattopadhyay [BC25], Byramji and Impagliazzo [BI25], and the merged
STOC 2026 paper [BCBI26] obtain exponential bounds in regimes allowing nearly quadratic proof
depth. Their bounds retain a proof-depth restriction. Itsykson, Podolskii, and Shekhovtsov [IPS26]
explicitly distinguish this progress from the general superpolynomial size problem; their unrestricted
size consequence is quadratic.
Alekseev and Gaevoy [AG26] study constrained bit PHP. Their polynomial-depth bounds for
general Res(⊕) are conditional; their unconditional results retain either a reversible-system restriction
or a near-quadratic depth bound. They therefore do not give the unrestricted usual-bit-PHP size
conclusion considered here.
The theorem here removes both regularity and proof-depth restrictions. A targeted refresh of
the primary literature on 15 September 2026 found no preceding theorem with that scope; this
is not an exhaustive certification of novelty. The full AC0[p]-Frege lower-bound problem remains
outside the conclusion of Theorem 1.1.
1.4 Proof organization
The proof has three interfaces. First, matching moments give a stable ordinary-degree filtration for
functional unary PHP, and a residual cube-difference construction detects every nonzero row-linear
bit polynomial. Second, a restriction-dimension argument supplies a common polynomial for all
high-rank affine blocks, while low-rank blocks admit exact coefficient packing. A single weighted
substitution removes the whole affine family. Third, each source proof clause is assigned a complete
extension block; local PC derivations simulate the rules without a proof-height cost.
Sections 2–6 prove these interfaces in full. Section 7 closes the parameters. Appendix A includes
the precise homological input behind the matching extension. A companion online research notebook
records the development of the argument and supporting experiments [Repo]; Section 8 describes
these supplementary materials. The proofs presented here can be read independently of that
notebook: none of its lemmas is required as an unexpanded black box in this preprint.
Every [Lean] link points to a source file in the published revision 54f0937, rather than a moving
branch. The linked files identify their exported statements and dependencies. The mathematical
notation here is independent of Lean syntax.

#### 2 Ordinary degree and polynomial calculus

The PC and linear-algebra statements in this section hold over any field K, with arbitrary sets of variables. The Boolean reduction statement and the subsequent main argument use K = F2. Degree bounds and accuracy parameters are integers. Polynomials are ordinary commutative polynomials. In particular, powers are not silently reduced using Booleanity. We use the nonnegative total-degree convention deg 0 = 0. The Boolean equations are

BOOLx = { x2 j − xj : j} .

Every displayed generator is an equation with right side zero.
For a finite polynomial system F, write
I B(F) = spanK{ qF : F ∈ F , deg(qF) ≤ B} ⊆ P≤ B. (2.1)
The degree constraint is imposed on each generator multiple. Cancellation between larger-degree
multiples does not make them legal in I B.
Ordinary PC derives axioms of F, linear combinations of previous lines, and xjg from a previous
line g. A degree-B derivation has no line of degree exceeding B. Let C B(F) be the space of
polynomials derivable in this way. Refutation means deriving one. The space C B is closed under
linear combinations, but equality with I B requires a proof.
Lemma 2.1 (Multiplying a completed line). [Lean] If g has a degree-B PC derivation and q is any
polynomial, then qg has a PC derivation through max{ B, deg q + deg g}. Moreover I B(F) ⊆ C B(F),
and qI B(F) ⊆ I B+deg q(F).
Proof. Expand q into monomials. Starting from the already derived line g, multiply by the variables
of each monomial one at a time, and then take the indicated linear combination. Each new line
has degree at most deg g + deg q. The zero case is immediate. Applying this construction to each
legal axiom multiple in (2.1), then summing, proves the second assertion. Multiplying each legal
generator multiple by q proves the last assertion. There is no need to multiply the earlier derivation
of g.
Lemma 2.2 (Degree-controlled Boolean reduction). [Lean] For every polynomial R of degree at
most d, its squarefree remainder R satisfies

R − R ∈ I d(BOOLx). If R vanishes at every Boolean point, then R ∈ I d(BOOLx). In particular, if deg q ≤ k, then q2 − q ∈ I 2k(BOOLx).

Proof. For a ≥ 2,

x a − x = (x2 − x)(1 + x + · · · + x a−2). Apply this identity to the powers in each monomial of R, one variable at a time. Every generator multiple has degree at most the original monomial degree, so the first assertion follows. A squarefree polynomial that vanishes on {0, 1} v is zero. For example, write it as A + xvB with A, B independent of xv. Evaluations at xv = 0, 1, followed by induction on v, give A = B = 0. This proves the second assertion. Finally, every value of q at a Boolean point belongs to F2, where its square equals itself; apply the second assertion at degree 2k. We use this reduction lemma only when the required degree is explicitly available. The high-rank step below instead needs literal membership in an affine ideal; pointwise vanishing on a finite field does not by itself supply that stronger conclusion. Lemma 2.3 (Substitution and fixed-weight replay). [Lean] Let K be any field. Let ϕ substitute polynomials of degree at most T ≥ 0 for source variables. Then deg ϕ(p) ≤ T deg p, and ϕ carries degree-D PC derivations to degree-T D derivations from the substituted axioms. More generally, fix a target polynomial w and a target system G. If each source axiom F of degree at most D has its weighted image wϕ(F) derivable from G through T D + deg w, then so does the weighted image of every line of a degree-D source derivation.

Proof. Expand into monomials to obtain the degree inequality. Induct on primitive PC steps. Zero,
addition and scalar multiplication commute with the weighted map. At a nonzero multiplication
p 7→ xp, ordinary degree gives deg p + 1 ≤ D. The completed weighted line has degree at most
deg w + T deg p; multiplying it by ϕ(x) costs at most deg w + T(deg p + 1) ≤ T D + deg w, by
Lemma 2.1. A zero predecessor stays zero. Taking w = 1 and the substituted axioms as target
system gives ordinary substitution.
Lemma 2.4 (Separation and compatible extension). [Lean: extension · PC duality] Let U, S be
subspaces of a vector space V over any field K. A linear functional on U extends to one on V
vanishing on S if and only if it vanishes on U ∩ S. In particular, if p /∈ S, there is a linear functional
λ with λ(S) = 0 and λ(p) = 1. Consequently, for either S = I B(F) or S = C B(F), a normalized
annihilator on P≤ B exists exactly when 1 ∈ / S. No finite-dimensional hypothesis is needed for the
extension assertion.
Proof. Define the extension on U + S by λ(u + s) = λ(u). The intersection condition makes this
well-defined. Extend a basis of U + S to a basis of V , and assign zero on the added basis vectors.
For separation, start on Kp with λ(cp) = c; its intersection with S is zero. Necessity follows by
restricting a vanishing functional. The polynomial consequences follow by applying this construction
inside P≤ B.

#### 3 Matching moments and a stable old filtration

For m ≥ 0 and N ≥ 1, the functional unary system F fun m,N has variables Xij and generators

X2 ij − Xij ,

XijXij′ (j ̸= j′), XijXi′j (i ̸= i′),

ρi − 1, ρi =X

N j=1

Xij .

The row exclusions in the second line are part of this auxiliary system. They are not inferred from
a weaker unary encoding.
A matching T is a set of cells with distinct rows and distinct columns; write XT =
Q (i,j)∈ T Xij . The empty matching corresponds to the constant one.
Lemma 3.1 (Complete moment equations). [Lean: normal form · moment equations] A linear
functional on P≤ B annihilating I B(F

fun m,N ) is exactly a choice of matching moments zT , | T| ≤ B,

satisfying

X j /∈col(T) zT ∪{(i,j)} = zT for | T| < B, i /∈ row(T). (3.1) Its value on an ordinary monomial is the moment of its squarefree support if that support is a matching, and is zero otherwise. Normalization is the additional condition z∅ = 1. Proof. Boolean equations reduce powers within the original degree. A squarefree monomial whose support has a repeated row or column contains one of the exclusion generators as a factor. Thus every polynomial reduces, within its degree, to a linear combination of matching monomials. Conversely,

the stated rule for evaluating ordinary monomials annihilates every legal Boolean or exclusion
multiple.
It remains to check row equations. In a row-equation multiple q(ρi − 1) of degree at most B, we
may first put q into the matching normal form: any error is a Boolean or exclusion consequence
through B − 1, and multiplication by ρi − 1 keeps its certificate within B. For a matching multiplier
XT , if row i is already occupied, the product reduces to zero. Otherwise its reduction is
X j /∈col(T) XT ∪{(i,j)} − XT .

These are precisely (3.1), and they exhaust the constraints. No positivity or multiplicativity is imposed on the functional. Let ∆s,N be the chessboard complex whose faces are matchings on an s-row, N-column board. The following consequence of the chessboard connectivity theorem of Björner, Lovász, Vrećica, and Živaljević [BLVZ94] is proved, with its homological prerequisite, in Appendix A:

s ≥ 2, N ≥ 2s − 1 =⇒ H e

s−2(∆s,N ; F2) = 0. (3.2) Theorem 3.2 (Extension of prescribed matching moments). [Lean: extension · annihilators] Suppose m ≥ 0, N ≥ max{1, 2B − 1}, and 0 ≤ k ≤ B. Every functional annihilating I k(F

fun m,N ) extends to one annihilating I B(F

fun m,N ). The constant moment is preserved. In particular normalized functionals

exist through degree B.
Proof. Use Lemma 3.1. Starting from the prescribed moments, fill degrees s = k + 1, . . . , B. At
degree one choose moments in each row whose sum is the prescribed constant moment; a column
exists because N ≥ 1.
For s ≥ 2, fix a set S of s rows. Form the reduced (s − 2)-chain

zS = X T a matching on S×[N] | T|=s−1

zT [T]

in ∆s,N . This is a cycle. At s = 2, its augmentation is the sum of two equal row totals, which is
zero in F2. For s > 2, a face U of size s − 2 misses two rows of S. Its boundary coefficient is the
sum of the prescribed marginal sums for those two rows, hence zU + zU = 0.
Since N ≥ 2s − 1, equation (3.2) gives an (s − 1)-chain yS with boundary zS. Assign the
coefficients of yS as the new moments on full s-matchings of S × [N]. For a fixed (s − 1)-matching,
its boundary equation is exactly the missing-row equation in (3.1).
Different s-row sets have disjoint new unknowns: a size-s matching has a unique occupied row
set. Their shared lower faces retain their already assigned values. Thus these fillings are globally
consistent and complete the induction. If s > m, there are no new row sets or moments to fill. In
particular, no hypothesis m ≥ B is required. The argument works for either value of the constant
moment. Starting with z∅ = 1 at degree zero supplies a normalized functional.
Corollary 3.3 (Old filtration stability and PC closure). [Lean] Under m ≥ 0 and N ≥ max{1, 2B
−1},

I B(F

fun m,N ) ∩ P≤ k = I k(F fun m,N ) (0 ≤ k ≤ B), C B(F

fun m,N ) = I B(F fun m,N ). (3.3)

In particular 1 ∈ C / B(F

fun m,N ).

Proof. If a polynomial of degree at most k is outside I k, finite-dimensional linear duality gives a
functional vanishing on I k but not on that polynomial. Extend it by Theorem 3.2. The polynomial
is then outside I B as well. The reverse inclusion in the first equality is immediate.
To prove PC closure, induct over a degree-B derivation. Axioms and linear combinations lie in
I B. At a nonzero multiplication step g 7→ Xijg, the predecessor has ordinary degree at most B − 1.
If g ∈ I B, the first equality puts it in I B−1. Multiplication of its legal generator multiples by Xij
stays in I B. Hence C B ⊆ I B; the other direction is Lemma 2.1. A normalized annihilator excludes
one.
The equalities in (3.3) concern the old functional system. We will not use an analogous assertion
for a system augmented with extension blocks.

#### 4 The bit decoder and a separating functional

Here m ≥ 0 is arbitrary and n = 2 ℓ. We impose ℓ ≥ 2 only for the old-base transfer and separation theorem. The old compact bit system is

Q m,ℓ = { Eii′ : i < i′ ∈ [m]} ∪ BOOLb, Eii′ =Y

ℓ t=1

(1 − bit − bi′t). (4.1)

The degree of each collision generator is ℓ. Its vanishing asserts that the two bit rows encode
different labels.
Identify unary columns with labels z ∈ {0, 1} ℓ, and define the ordinary ring map
τ (bit) = X z:zt=1 Xiz. (4.2)

Lemma 4.1 (Two-row interpolation). [Lean] For any common row width N ≥ 0, let U i,i′ consist of Booleanity, same-row exclusions, and the two row-sum equations for distinct rows i, i′. For a polynomial R supported on these rows and of degree at most d,

R −X z,w R(ez, ew)XizXi′w ∈ I max{ d,2}(U i,i′).

Here ez, ew are the corresponding one-hot assignments. Column exclusions are not used in this
interpolation.
Proof. Reduce powers and same-row collisions. The remainder is a linear combination of 1, individual
cells of the two rows, and products containing one cell from each row. This reduction costs at most
d. Replace the constant by ρiρi′, using
1 − ρiρi′ = (1 − ρi) + ρi(1 − ρi′),
and replace each remaining single cell by its product with the other row sum. These changes have
certificates of degree at most two. The result is bilinear, and its coefficient at XizXi′w is its value at
(ez, ew), namely R(ez, ew).
Lemma 4.2 (A polynomial left inverse for the decoder). [Lean] For every m, ℓ ≥ 0, the decoder τ is
injective and preserves ordinary total degree.

Proof. Define a linear substitution λ on unary variables by sending Xi,et to bit, where et is the unit bit label, and all other unary variables to zero. The unit labels are distinct and λτ (bit) = bit, so λτ is the identity on polynomials. Both substitutions have degree at most one; applying the degree inequality in both directions proves equality, as well as injectivity. Lemma 4.3 (Degree-preserving old-base transfer). [Lean] For m ≥ 0, ℓ ≥ 2, and every B ≥ 0,

q ∈ C B(Q m,ℓ) =⇒ τ q ∈ C B(F

fun m,n).

Proof. Bit Booleanity has a degree-two image certificate:

τ (b2 it − bit) = X z:zt=1 (X2 iz − Xiz).

At a two-row one-hot assignment (ez, ew), τ (Eii′) is one exactly when z = w. Lemma 4.1 therefore gives

τ (Eii′) −X z XizXi′z ∈ I ℓ(U i,i′). The remaining terms are column exclusions of degree two. Thus every axiom image has a certificate through its original degree. Replay the source proof using Lemma 2.3 with T = 1, w = 1. Only axioms actually admitted by the source degree ceiling must be replayed; there is no additional assumption B ≥ ℓ. Let L k be the space spanned by monomials of degree at most k containing at most one bit variable from each row. Lemma 4.4 (Row-linear dimension). [Lean] Over any field, for all m, ℓ, k ≥ 0,

dim L k =X

k j=0 m j! ℓ j. (4.3)

Every nonzero polynomial in this space has a nonzero monomial coefficient of degree equal to its
total degree.
Proof. Ordinary monomials form a basis. To choose a row-linear monomial of degree j, choose its j
rows and one of ℓ coordinates in each. Terms with j > m contribute zero. The last assertion follows
by choosing a maximal-degree element of the finite nonempty support.
Lemma 4.5 (Binary cube degree drop). [Lean] Partition some source variables into t indexed groups.
For each ϵ ∈ F t 2, substitute scalars depending only on ϵi for variables in group i, and fixed affine
target polynomials for all remaining variables. Write ϕϵ for this substitution and ∆p =
P ϵ ϕϵ(p). Then deg ∆p ≤ max{deg p − t, 0} , deg p < t =⇒ ∆p = 0.
If every source generator F has a cube-independent image rF which is zero or a target generator,
then

∆I B(F) ⊆ I max{ B− t,0}(G).

The variable sets may be arbitrary; only the cube index set must be finite.

Proof. A monomial missing one group has equal evaluations in pairs obtained by flipping that cube
coordinate, so its sum is zero. A surviving monomial uses at least t selected variables, which become
scalars; the remaining factors have total degree at most its original degree minus t. For a legal
multiple qF, cube independence gives ∆(qF) = (∆q)rF . If rF = 0 it vanishes; otherwise it is one
target generator multiple, whose degree is at most B − t when B ≥ t. When B < t, it is zero.
Extend by linearity.
Lemma 4.6 (Row-cube restriction and coefficient isolation). [Lean: pair packing · restriction ·
coefficient isolation] Choose t distinct rows and, for each, two labels differing only in one prescribed
bit. If these pairs are disjoint, the one-hot substitutions on the selected rows, together with deletion
of their 2t columns on other rows, give

∆I B(F fun m,n) ⊆ I max{ B− t,0}(F

fun m− t,n−2t). For a row-linear f of degree at most t, this cube applied to τf is the constant coefficient of the monomial selecting those rows and prescribed bits. Such disjoint pairs can be chosen whenever t ≥ 1 and 4(t − 1) < 2 ℓ. More generally, the coefficient-isolation identity holds for arbitrary cube independent polynomial images of the unselected bits, provided each selected bit has its prescribed base value plus its selected cube coordinate, and the other bits in that row stay constant. Proof. On a selected row, each substitution is a one-hot assignment; on every other row, deleted columns become zero and surviving variables are relabeled. Booleanity, row exclusions and column exclusions consequently map to zero or the corresponding residual generator. Disjointness prevents a collision between selected rows or between selected and residual rows. A selected row-sum equation maps to zero, and every other row-sum equation maps to its residual counterpart. Lemma 4.5 applies. A row-linear monomial missing a selected row cancels by a cube flip. If it uses all t selected rows, the degree bound forces it to use exactly one variable in each and none outside. The two-value sum in each row is one for the prescribed bit and zero for every other bit. This isolates exactly the claimed coefficient, independently of the images outside the selected rows. Finally, after selecting j pairs, their 2j vertices forbid at most 2j of the 2 ℓ−1 pairs in any specified direction. The strict packing bound permits the next choice. Theorem 4.7 (Row-linear separation through a larger PC degree). [Lean] Let m ≥ 0, ℓ ≥ 2, n = 2 ℓ, and suppose 1 ≤ k ≤ B, 4(k − 1) < n, and 2B − 1 ≤ n. For every nonzero f ∈ L k, there is a linear functional µ on unary polynomials through degree B such that

µ(C B(F

fun m,n)) = 0, µ(τf) = 1. It can be chosen with µ(1) = 0 if deg f > 0, and µ(1) = 1 if deg f = 0. Consequently

τf /∈ C B(F

fun m,n), f /∈ C B(Q m,ℓ). Proof. A nonzero constant over F2 is one, so that case follows from a normalized matching functional. Otherwise put t = deg f and choose a nonzero degree-t coefficient. Lemma 4.6 supplies its coordinate pairs and residual operator ∆, with ∆τf = 1. Because n is divisible by four, 4(k − 1) < n implies k ≤ n/4. Thus n − 2t ≥ 1, and

n − 2t ≥ 2(B − t) − 1.
Theorem 3.2 supplies a normalized residual annihilator λ through B − t, even if there are fewer than
B − t remaining rows. Set µ = λ ◦ ∆. The residual NS transport and Corollary 3.3 show that µ
annihilates the old unary PC space. Coefficient isolation gives µ(τf) = 1, whereas ∆1 = 0 gives
µ(1) = 0. Finally apply Lemma 4.3 for the bit consequence.
10

#### 5 Excluding one complete affine extension level

The product construction belongs to the extension-Nullstellensatz approach of Buss, Impagliazzo, Krajíček, Pudlák, Razborov, and Sgall [BIKPRS]. We use a complete one-level family and prove its required properties explicitly. An accuracy-h block has a finite tuple of old affine polynomials g1, . . . , gs, fresh coefficient variables rui, and product

## P =Y

h u=1 1 −X

## s i=1 ruigi! . (5.1)

Its complete axioms are all companions giP and all coefficient Boolean equations r2 ui − rui. The product P itself is not an axiom. Coefficients of different blocks are disjoint; every input depends only on the old variables. Rank means the dimension of the affine input span. A nonzero span is called proper if it does not contain one.

##### 5.1 Affine linear algebra and ordinary restriction

Lemma 5.1 (Affine spans and coordinates). [Lean: linear algebra · affine spans · coordinates] Over
any field K, let a finite affine system on K v have span S. Its common zero set is nonempty exactly
when 1 ∈ / S. In that case it is an affine flat of codimension r = dim S, every affine polynomial
vanishing on it belongs to S, and any basis F1, . . . , Fr of S can be completed to invertible affine
coordinates. Both coordinate substitutions preserve ordinary degree. If the zero set is empty, a
constant linear combination of the inputs is one.
Proof. Write the inputs as gi = ci + Li. If a relation among their linear parts had nonzero constant
part, their span would contain one. Otherwise all relations respect the right sides − ci; linear algebra
then solves Li(x) = − ci. Equivalently, define the consistent functional on the span of the Li and
extend it to the full dual space. When 1 ∈ / S, independence of the Fj implies independence of
their linear parts: a relation would be a constant in S, hence zero, and then all coefficients vanish.
Complete those linear parts to a basis and retain the constants of the Fj . This gives an invertible
affine coordinate change. The zero flat has first r coordinates zero, so an affine polynomial vanishing
there is a linear combination of those coordinates. Substitution and its inverse have degree at most
one, which proves degree preservation. Inconsistency is exactly the failed relation already identified,
normalized to give one.
Lemma 5.2 (Scalar cleanup and exact block degrees). [Lean: cleanup · exact degrees] Over F2,
zero-span blocks, and unit-span blocks with h ≥ 1, can be removed by constant coefficient substitutions
without increasing PC degree. More generally over any field, such a substitution works whenever
the chosen constants satisfy their Boolean equations and every eliminated companion maps to zero.
If a block has a genuine degree-one input, then deg P = 2h; each nonzero degree-one input has
companion degree 2h + 1. In particular these degree equalities hold after discarding zero inputs in a
proper nonzero block. Without these hypotheses they are only upper bounds.
Proof. For zero span set all coefficients to zero. For unit span choose

P icigi = 1, use these constants in the first coefficient row, and use zero in the other rows. The product and companions become zero; over F2, every coefficient satisfies c2 i = ci. Apply the substitution lemma with degree multiplier one to the remaining axioms. For the degree assertion, a genuine linear part contributes a nonzero degree-two term to each factor, since its coefficient variables are distinct. The polynomial ring is a domain, so degrees add in the product and on multiplication by a degree-one input. 11

Lemma 5.3 (Ordinary restriction dimension and ideal membership). [Lean: dimension · ideal
membership] Over any field, an affine substitution into d variables maps a space of polynomials of
degree at most k to a space of dimension at most d+k
k . Suppose the common zero flat of a finite
affine system gi is nonempty. If the ordinary polynomial restriction of f, of degree at most k, to
that flat is zero, then for k ≥ 1

f =X i aigi, deg ai ≤ k − 1. (5.2)

Here restriction means substitution into affine free coordinates, not merely evaluation at field points.
Proof. Substitution does not increase degree. The target monomials of degree at most k, counted
by d+k
k , span the image. For ideal membership use the coordinates of Lemma 5.1. A polynomial
whose restriction at F1 = · · · = Fr = 0 is literally zero has each monomial divisible by at least one
Fj . Assign each monomial to one such factor and remove it. The resulting cofactors have degree at
most k − 1. Pull back the affine coordinate change and express each Fj as a constant combination
of the original inputs.
Lemma 5.4 (A common ordinary restriction kernel). [Lean: parameter bounds · common kernel] Let
m > 0, ℓ ≥ 1, h = 3ℓ, M, k ≥ 1, k ≤ m, and
m ln(4M) ≤ k2.
In a finite family of affine blocks in v = mℓ bits, suppose at most M blocks are proper and have rank
greater than h(k + 1). There is a nonzero f ∈ L k such that every block above that rank threshold
either has one in its input span or admits (5.2). In each proper high-rank block, the ordinary
restriction of f to its zero flat is zero.
Proof. Put r∗ = 3ℓ(k + 1) + 1. If r∗ > v, no proper high-rank block exists and choose f = 1.
Otherwise its restriction uses at most d = v− r∗ free coordinates. The checked dimension comparison
uses
k! d + k k !≤ (d + k) k, k! m k!≥ (m − k + 1) k.
Moreover d + k ≤ ℓ(m − 2k) ≤ ℓ(m − k + 1)(1 − k/m). The first inequality follows by inserting
d = mℓ − 3ℓ(k + 1) − 1 and using ℓ ≥ 1; the second follows by expansion and k ≤ m. Thus
d+k
k
m
k
ℓk ≤ 1 −

k m

k

≤ e− k2/m.

Consequently the sum of the restriction-image dimensions is at most
Me− k2/m m k! ℓ k ≤ 1 4 m k! ℓ k < dim L k.
The joint restriction map has a nonzero kernel. Apply Lemma 5.3 to each proper high-rank block;
unit-span blocks need no restriction condition.
Corollary 5.5 (A convenient kernel parameter). [Lean: parameter bounds · common kernel] For
m, M ≥ 1, the choice k = ⌈p m ln(4M)⌉ is positive and satisfies the square condition of Lemma 5.4. Thus that lemma applies whenever additionally k ≤ m.
Proof. The radicand is positive; square the inequality defining the ceiling.
12
5.2 One simultaneous weighted substitution
Lemma 5.6 (Low-rank packing without a retained core). [Lean] For affine inputs over F2 of span
rank r ≤ h(k + 1), with h, k ≥ 0, there are coefficient polynomials of degree at most k substituting
the block product to

## Z =Y

r j=1

(1 − Fj ),
where Fj is a basis of the input span. This polynomial has degree at most r, is the Boolean indicator
of the common zero set, and giZ ∈ I r+1(BOOL) for every input. No properness assumption is
needed.
Proof. Partition the basis into h ordered bins of size at most k + 1. For each bin J, use
1 −Y j∈ J (1 − Fj ) = X j∈ J Fj Y t∈ J, t  0, ℓ ≥ 2, n = 2 ℓ, h = 3ℓ, and let a finite complete old-affine family be adjoined to Q m,ℓ. Suppose M, k ≥ 1, at most M blocks are proper and of rank greater than h(k + 1), and, with B = k(D + 1), m ln(4M) ≤ k2, k ≤ m, D ≥ 2h + 1, 2B − 1 ≤ n, 4(k − 1) < n. (5.3)

Then the augmented system has no ordinary-PC refutation through degree D.
Proof. The common-kernel lemma supplies nonzero f ∈ L k. Weighted removal would derive f from
the old base through B, contrary to Theorem 4.7. Zero and unit spans are already covered by
removal, so no preliminary change of the family is needed.
Lemma 5.9 (Uniform eventual parameter room). [Lean] Fix natural numbers a, A, d. Put n = 2 ℓ,
t = ℓ + 1, q =√2, and k = ⌈ tq ℓ ⌉. For every sufficiently large ℓ, simultaneously
ℓ ≥ 2, 1 ≤ k ≤ n + 1, (n + 1) ln 4(A2 aℓ + 1) ≤ k2,
4(k − 1) < n, 2k A(ℓ + 1) d + 1 − 1 ≤ n.
The threshold depends only on a, A, d.
Proof. The ceiling gives tq ℓ
≤ k ≤ 2tq ℓ. Set C = ln(4(A+1)). Since ln 2 ≤ 1, ln(4(A2 aℓ+1)) ≤ C+aℓ.
For sufficiently large ℓ, 2(C + aℓ) ≤ t2. Together with n + 1 ≤ 2n and q2ℓ = n, this proves the
square condition. For every fixed natural e, t e/q ℓ
−→ 0: its successive ratio tends to 1/q < 1, so its
tail is dominated by a geometric sequence. Applying this to e = d + 1 gives eventually
4k(At d + 1) ≤ 8(A + 1)t d+1q ℓ < n.

This implies the remaining degree and packing bounds, and also k ≤ n + 1. Corollary 5.10 (Polynomial inventory and polylogarithmic degree). [Lean] Fix natural a, A, d. For all sufficiently large ℓ, every finite complete accuracy-3ℓ affine family over Q2 ℓ+1,ℓ with at most A2 aℓ + 1 proper blocks has no PC refutation of degree D ≤ A(ℓ + 1) d. Proof. Raise the proposed degree ceiling to D′ = max{ D, 6ℓ + 1}. It is at most (A + 7)(ℓ + 1) d+1. Apply Lemma 5.9 with constants a, A + 7, d + 1, and use its k and the upper inventory bound in Theorem 5.8. All required inequalities hold uniformly over the actual families.

#### 6 A direct PC simulation of the proof DAG

Unless stated otherwise, h ≥ 1 and there are finitely many old variables, say v. Represent a linear clause by its affine true-indicators: C =_ i (gC,i = 1), Z(C) = { b : gC,i(b) = 0 for all i} . An equation a(b) = α has true-indicator 1 + a(b) + α. The set Z(C) is an affine subspace or empty. Assign to each nonempty clause a fresh complete accuracy-h block, and write its product as PC. Set P∅ = 1, using no block for the empty clause. [Lean] Fix the whole block family before following the proof DAG. Clause values PC = 0 will be derived; they are not included among its axioms.

Lemma 6.1 (General product telescoping). [Lean] In any commutative ring, for a finite input index set and h ≥ 0, put

Pv = v Y

−1 u=0 1 −X i ruigi! , Uh,i = h

X

−1
v=0

rviPv.

Then 1 − Ph =
P i Uh,igi. For ordinary polynomials over any commutative coefficient ring, if deg gi ≤ δ, deg rvi ≤ 1, and h ≥ 1, then
deg Ph ≤ h(δ + 1), deg Uh,i ≤ 1 + (h − 1)(δ + 1), deg(giPh) ≤ deg gi + h(δ + 1).
No freshness or nonvanishing assumption is needed for these upper bounds.
Proof. The identity holds at h = 0. Writing sh =

P

irhigi, the recurrences Ph+1 = Ph(1 − sh) and

Uh+1,i = Uh,i + rhiPh give

1 − Ph+1 = 1 − Ph + Phsh =X i Uh+1,igi. Each factor has degree at most δ + 1, and each summand of Uh,i has degree at most 1 + (h−1)(δ + 1). The sum and product degree inequalities prove the three bounds, including over rings with zero divisors. At h = 0, P0 = 1 and U0,i = 0. Corollary 6.2 (Affine-clause prefix identity). [Lean] Every accuracy-h clause block, h ≥ 1, has coefficients satisfying

1 − PC =X i UC,igC,i, deg PC ≤ 2h, deg UC,i ≤ 2h − 1. (6.1)

Its companions have degree at most 2h + 1.
Proof. Apply Lemma 6.1 with δ = 1, reindexing coefficient rows from zero-based to one-based.
Exact companion degrees require the additional hypotheses in Lemma 5.2; a loose input-degree
bound alone would not justify equality.
Lemma 6.3 (Complementary-parity resolution). [Lean] Suppose A = (
W i(ai = 1)) ∨ (u = 1) and B = (
W j(bj = 1)) ∨ (1 − u = 1), with u affine. Let T have the union of the context inputs ai, bj . If PA, PB have PC derivations through degree K, then PT has a derivation in the same fixed block system through max{ K, 4h + 1}.
Proof. The context companions aiPT , bjPT are axioms of the conclusion block; a repeated input
may use the same axiom. The prefix identities yield

RA = PT − UA,uuPT = PAPT +X i UA,i(aiPT ), (6.2) RB = PT − UB,1− u(1 − u)PT = PBPT +X j UB,j (bjPT ). (6.3)

Lemma 2.1 derives these through max{ K, 4h}. In particular it multiplies the completed lines PA, PB,
not their entire earlier derivations.
For an affine u = c +

P

tctbt, the identity u2 − u =X t ct(b2 t − bt)

has a degree-two proof. Therefore
(1 − u)RA − UA,uPT (u2
− u) = (1 − u)PT (6.4)
is derivable through max{ K, 4h + 1}. The right side is a completed line of degree at most 2h + 1.
Multiply it by UB,1− u, costing at most 4h, and add (6.3). The result is PT . All multiplications
expand into primitive PC steps by Lemma 2.1.
Lemma 6.4 (Semantic weakening and tautologies). [Lean] If C |= D and PC has a degree-K
derivation, then PD is derivable through max{ K, 4h}. A tautological D has a direct value derivation
through 2h + 1.
Proof. If Z(D) is nonempty, then Z(D) ⊆ Z(C). Each gC,i vanishes on Z(D), so affine linear
algebra gives constants λij with

gC,i =X j λijgD,j . To see this directly, choose affine coordinates beginning with a basis of the equations defining Z(D). An affine polynomial vanishing when these coordinates are zero has only those coordinate terms. Consequently gC,iPD is a constant linear combination of conclusion companions. Now use PD = PCPD +X i UC,i(gC,iPD) and Lemma 2.1, with ceiling max{ K, 4h}. If Z(D) is empty, its affine equations are inconsistent, and their span contains one. The same constant combination of their companions gives PD, through 2h + 1. If the conclusion is empty, its value is one; the preceding formulas still apply with no conclusion block. In the nonempty-zero-set case, an implication to the empty clause forces all premise indicators to be identically zero, so the already derived premise value is one. Lemma 6.5 (Binary affine separator). [Lean] Let V be any vector space over F2, and A, B, D finite clauses of affine true-indicators. Suppose A ∧ B |= D, but neither A |= D nor B |= D. There is an indicator u already in A, taking both values on W = Z(D), such that W ∩ Z(A) = { x ∈ W : u(x) = 0} , W ∩ Z(B) = { x ∈ W : u(x) = 1} . No finite-dimensional assumption is required. Proof. Choose a ∈ W satisfying A and b ∈ W satisfying B. Soundness forces a ∈ Z(B) and b ∈ Z(A). Choose indicators u ∈ A, v ∈ B with u(a) = v(b) = 1; then u(b) = v(a) = 0. Soundness also gives W ⊆ Z(A)∪ Z(B). If x ∈ W ∩ Z(B) had u(x) = 0, the point a− b+x would belong to W and satisfy both u = v = 1, a contradiction. Here we used only the affine identity g(a− b+x) = g(a)− g(b)+g(x). Thus u = 1 on W ∩ Z(B), while u = 0 on W ∩ Z(A). The covering inclusion gives the two reverse implications and hence the fiber equalities. The witnesses a, b give both values. Lemma 6.6 (Two-premise semantic inference). [Lean] Over any F2-vector space, every sound inference A ∧ B |= D between finite affine clauses admits a derivation using at most three semantic weakening or complementary-parity resolution steps, introducing at most two auxiliary clauses. It is either a one-premise weakening or has the form

A |=

## 评论（1/1）

> **Sath52** · 2026-09-15T19:25:04.000Z　
> I really wish you hadn’t.

## 导航

- 项目页：[[10-项目/Show-HN-I-solved-a-12yr-math-problem-using-AI-(f_fa95a008]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
