# AI Visibility

Read when the question is whether AI assistants mention, cite or recommend the business. Every platform figure in this field is a dated snapshot from vendor or practitioner studies; none is stated here, and any the user brings is labelled with its date and source.

## Five levels, reported separately

1. **Retrieved**: the page is fetched.
2. **Cited**: the page appears among the sources. This follows from the usefulness of the content.
3. **Mentioned**: the brand name appears in the answer.
4. **Recommended**: the brand is on the shortlist the answer gives a buyer. This follows mostly from what the rest of the web says: reviews, forums, analysts, press, video. What the company's own site says matters little here.
5. **Recommended against**: named, with a warning.

Report the ladder and the wording of each mention (positive, neutral, qualified, negative), not one "AI visibility" number. Citations rising while recommendations stay flat means the site is useful and the wider web does not yet back it. The test question: if a model ignored everything on our own domain, would the rest of the web still put us on the shortlist?

## Self-ranked "best of" lists

A list that ranks its own publisher first is read by a model as a source about the category: it takes the competitors' names and the criteria, then recommends by wider consensus, which can mean recommending the competitors. A category leader wins both ways; a newer brand may earn citations and shape the framing without reaching the shortlist. The answer is not "never write one": write a few useful guides, name the leader honestly and say where the user's product goes further, and shift effort towards review platforms, communities, analysts and press.

## Measuring

- Merge differently worded versions of the same intent into one core prompt and spend the budget on repeated runs, each in a new session.
- Report a hit rate with its sample ("3 of 5"). Compare rates over time: 4 of 5 becoming 3 of 5 is noise; 4 of 5 becoming 0 of 5 for a month is a signal.
- Before explaining why the business is not cited, sort the cause: technical (cannot be fetched or parsed), understanding (described vaguely or wrongly), or trust (understood but not chosen).
- Most visits prompted by an assistant do not arrive labelled as such; they come as brand searches and direct visits. Three instruments together: tracked prompts, a "how did you hear about us" question with an assistant option and a follow-up asking what was typed, and what prospects say on sales calls. Brand search rising with no campaign behind it is an indirect sign.

## Agent readiness

- **Access**: core content is in the initial HTML, since many agents do not run JavaScript; what the firewall or content network actually does to each user agent has been checked, because many sites block by default without anyone having decided it; status codes are correct and canonicals stable.
- **Discovery**: robots.txt states a position for each kind of AI crawler (training, search retrieval, fetching at a user's request); the sitemap parses. Take the current crawler names, and whether each honours robots.txt, from each vendor's documentation.
- **Parseable**: structured data with real content, one main heading, subheadings that answer the sub-questions, and the highest-intent actions (signup, pricing, booking, contact) not locked inside script-only flows, with labelled form fields.

Newer conventions such as an AI text file, a full-content companion file or Markdown versions of pages are emerging and are not confirmed signals; build them only on request and only from confirmed facts. Assistants draw on different search indexes, so check inclusion in the other major search engines' webmaster tools as well as Google's.

## What moves, and what does not

Which formats and which third-party sites assistants cite changes from one model release to the next. Do not justify producing list or comparison pages at scale by a snapshot of citations, and do not concentrate the effort on one third-party platform. The company's own product pages, documentation, pricing page and original research are the base no platform can remove. Reading the search queries an assistant actually runs for the category shows which third-party profiles deserve attention first; turning every such query into a new article is the scaled content abuse search policies name.

## Consistency off the site

The description of the business (segment, category, difference) on review sites, directories, professional networks and partner listings matches the "about" page, and free profiles are filled in. Before a repositioning or rename: record a baseline of prompts for the old and new segment, change the off-site signals first, then the site in stages, and keep the pages that still win the old prompts until tracking shows the new association. A weakness that models keep repeating is answered publicly and specifically ("implementation takes four to eight weeks", on the implementation page), not by asking anyone to remove a criticism. Invented awards and a company-run "review" site posing as independent are declined; fake or undisclosed reviews are also a consumer-protection matter.

## Other surfaces

- A model does not watch a video; it reads the text layer: transcript, captions, title, chapters, description. Say the key answer as a complete sentence and say the key names aloud.
- A full article reposted on a professional network competes with the original; publish on the site first and post a rewritten summary that links back.
