# Institutional Architecture

**UNLESS · Foundation Document · v1.0**

Design. Anything. Everything. Better.

Technology. Society. Economics. Infrastructure. Institutions. Environment.

This is the fifth domain, made explicit: **Institutions.** Every organization — a company, an agency, a nonprofit, a cooperative, a family trust — is a designed system whether anyone designed it on purpose or not. Most weren't. They accreted. This document is how UNLESS designs them instead.

---

## 1. What an institution is, for this purpose

An institution is a system that turns purpose into outcomes through repeated decisions, and either learns from what happens or doesn't.

That's the whole claim. Everything below is instrumentation for it.

Two institutions with identical org charts can behave completely differently depending on whether the decision layer is wired to the outcome layer. Most aren't. A hospital collects mortality data for a decade without changing triage protocol. A city council commissions the same traffic study three times. The architecture failed, not the people in it — nobody built the loop that would have let the institution notice and correct itself. Institutional architecture is the discipline of building that loop on purpose, and then keeping it honest as the institution grows past the point where anyone can hold the whole thing in their head.

## 2. The spine

One causal chain. Everything in this document is a view onto it — never a competing model.

```
Purpose → Capability → Decision → Resource → Outcome → Learning → Evolution
```

Read it as a sentence: an institution's **purpose** requires **capabilities**; capabilities, resourced properly, enable **decisions**; decisions consume **resources** and produce **outcomes**; outcomes generate **learning**; learning either changes capability or it was never really learning — it was just a report nobody acted on. That last link is where most institutions quietly break.

## 3. The canonical entity model

Earlier drafts of this framework defined the entity model three separate times — once as individual YAML files per entity, once as an ontology document, once as a graph schema — and the three copies had already begun to disagree with each other on relationship verbs before anyone noticed. That's not a paperwork problem. An institution that can't agree with itself about what "capability" means is the exact failure mode this framework exists to prevent, and it isn't allowed to happen inside the framework's own definition of itself.

So: one table. This supersedes prior scattered definitions. Nothing below is aspirational — every relationship maps directly onto the spine in Section 2.

| Entity | Definition | Key relationships |
|---|---|---|
| **Institution** | The bounded system being modeled | contains Capability · depends_on Resource · evolves_through Transformation |
| **Purpose** | The reason the institution exists, stated so specifically that someone could tell if it stopped being true | requires Capability |
| **Actor** | A person, team, or system that makes decisions inside the institution | makes Decision |
| **Capability** | An institutional ability that reliably creates value, regardless of who currently holds it | enables Decision · depends_on Resource · evolves_into Capability |
| **Resource** | Anything capability consumes to operate — money, time, data, trust, authority | enables Capability |
| **Decision** | A choice an actor makes, using specific evidence, that consumes resource and produces outcome | informed_by Knowledge · enabled_by Capability · produces Outcome |
| **Outcome** | What actually happened, measured, not what was intended | informs Learning |
| **Knowledge** | Validated information available to inform a decision | validated_by Evidence |
| **Evidence** | The specific data or observation that makes a piece of knowledge trustworthy | validates Knowledge |
| **Learning** | What the institution concludes from an outcome — and is obligated to act on | improves Capability |
| **Pattern** | A recurring structure of decision-and-outcome, observed across more than one institution | informs Transformation |
| **Transformation** | A deliberate, sequenced change to one or more capabilities | evolves Capability |

Twelve entities. No fewer would tell the truth about how institutions actually run; no more would be earning its keep.

## 4. Maturity — five levels, one measure

An institution's maturity is not how sophisticated its org chart looks. It's how far the loop closes.

1. **Initial** — decisions get made; nobody wrote down why.
2. **Structured** — capabilities and decisions are named and owned, but outcomes aren't systematically fed back.
3. **Managed** — outcomes are measured against intent. Someone reads the report.
4. **Adaptive** — learning routinely changes capability. The report changes what happens next time.
5. **Intelligent** — the institution predicts where its own capability will need to change before the outcome data forces the question.

Most institutions Travis has assessed sit at level 2, believe they're at level 3, and would be embarrassed to see level 4 written down next to what they actually do with a quarterly report.

## 5. Practice — how this gets used on a real institution

Five phases, each producing an artifact that feeds the next. This is the delivery layer; Section 3 is what it's built on.

- **Discover** — Interview the actors who hold the purpose, not just the ones who hold the title. Output: a purpose statement specific enough to falsify.
- **Model** — Populate the entity table in Section 3 with this institution's actual capabilities, resources, and decision points. Output: an institution instance.
- **Assess** — Score each capability against the five maturity levels in Section 4. Output: a scored capability map, with the gaps named plainly rather than softened into "opportunities."
- **Recommend** — Identify which capability, if changed first, unlocks the most downstream outcome improvement. Not every gap deserves a project.
- **Transform** — Execute the change, and route the resulting outcome data back into Learning. If nothing routes back, the institution didn't transform — it just spent money.

## 6. Governance — sized to what actually exists

A framework this young doesn't need a certification authority yet. It needs one person who can change the entity model in Section 3 without three files drifting out of sync, and a changelog that says why.

- **Steward** — owns Section 3. Any change to an entity or relationship goes through one person until there's a real reason to need more.
- **Contribution** — new patterns (Section 3's Pattern entity) get added when they've shown up in at least two independent institution instances, not on the strength of a single engagement.
- **Versioning** — this document is v1.0 because it's the first version built to be used on something real, not the first version that existed. Earlier scaffolding stays in the repo as `/gps-metamodel` and `/models` for lineage; this file is what a practitioner should actually open.

Formal councils, a research body, a public certification track — those get built when there's a second contributor to govern, not before.

---

*Institutions are the fifth domain. You are the Designer.*

**—UNLESS**
