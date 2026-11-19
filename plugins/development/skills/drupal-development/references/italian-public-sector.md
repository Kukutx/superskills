# Italian public-sector sites

Read on the official pages on 2026-11-19 unless another date is given. Criteria, versions and deadlines change; re-open the source before quoting one to a client.

## What applies

- **Comuni** follow the Designers Italia comuni model: a site model ("cittadino informato") and a digital services model ("cittadino attivo"), with an information architecture document, HTML templates, CMS themes for WordPress and Drupal, and conformity criteria. Other PA sites follow the Designers Italia design guidelines (`designers.italia.it/normativa/linee-guida-di-design/`).
- **Accessibility** binds every PA site: Legge 4/2004 and the AgID guidelines.
- **PNRR measure 1.4.1** ("Esperienza del cittadino nei servizi pubblici") funded comuni to adopt the model; meeting the conformity criteria is the condition for the funds ("il rispetto dei criteri di conformità è requisito necessario al rilascio degli incentivi").

## Stack

- **Bootstrap Italia** (`italia/bootstrap-italia`): latest stable v2.18.3 (4 August 2026); v3.0.0 is in beta (beta.8, 5 November 2026). Production uses the stable line; criterion C.SI.1.2 asks for Bootstrap Italia 2.0 or later.
- **Drupal theme `bootstrap_italia`** (drupal.org project, mirrored at `italia/design-drupal-theme`): 2.17.7 of 2 September 2026, compatible with `^10.5 || ^11.3`, covered by security advisories. Install it with Composer (it needs `drupal/components`), copy the `italiagov` starter kit from the theme's `var/starter_kits/` into the custom themes folder, set `hidden: false` in its `.info.yml` and make it the default theme. The library comes from a release zip, an npm build inside the sub-theme or a CDN; components are managed through UI Patterns.
- The theme presents itself as a base for Italian public digital services; the model's pages mention CMS themes for Drupal and WordPress without naming them. For criterion C.SI.1.4 ("tema CMS del modello", 1.0 or later, if one is used), confirm on designers.italia.it which Drupal theme the model recognises before claiming it.

## The validator

- The official checker is `italia/pa-website-validator-ng`, a Lighthouse-based CLI (Node 18+, Chrome, about 16 GB RAM): `pa-website-validator-ng --type municipality --destination <dir> --report <name> --website <url> --scope online --accuracy suggested`, or `--scope local` for a development site. The older `italia/pa-website-validator` is archived (December 2024); `pa-website-validator-gui` is the desktop variant.
- It recognises the model through `data-element="…"` attributes in the HTML, for example `main-navigation`, `breadcrumb`, `service-link`, `accessibility-link`, `privacy-policy-link`, `legal-notes`, `faq`, `report-inefficiency`, `feedback` and `metatag`. The model's templates and CMS themes include them where possible; checking that they are in place stays with the site. For links it also checks that the `href` is not empty and, in some cases, that it is HTTPS and loads.
- So every Twig override, Views template or custom block that replaces a model component copies the base template's `data-element` attributes along with the markup. A page that looks right but lost them fails the check.

## Conformity criteria for the comuni site (design-comuni-docs 5.1)

Each criterion is graded Successo, Tolleranza or Fallimento.

| Area | Criteria |
| --- | --- |
| User experience | C.SI.1.1 model fonts (Titillium Web, Lora, Roboto Mono); 1.2 Bootstrap Italia 2.0+; 1.3 service pages carry the mandatory items in the model's order; 1.4 model CMS theme 1.0+ if used; 1.5 topics from the model's controlled vocabulary or EuroVoc; 1.6 mandatory first-level menu items in the right order; 1.7 second-level page titles from the model's vocabulary |
| Functions | C.SI.2.1 appointment booking with the responsible office without requiring digital identity; 2.2 the responsible office's contacts on every service page; 2.3 FAQ linked from the footer; 2.4 disservice reporting linked from the footer; 2.5 and 2.6 clarity rating on every first- and second-level page and every service page |
| Law | C.SI.3.1 technical cookies only, compliant, on the comune's domain; 3.2 accessibility declaration linked from the footer; 3.3 privacy notice linked from the footer on valid HTTPS; 3.4 legal notes declaring the CC-BY 4.0 licence |
| Performance | C.SI.4.1 Lighthouse mobile performance of at least 50, or a "Piano di miglioramento del sito" linked from the footer |
| Security | C.SI.5.1 valid, current HTTPS certificate (AgID TLS recommendations); 5.2 institutional `comune.` domain from the allowed list |

The digital services model (5.2) adds C.SE criteria: digital-identity access, receipt confirmation, a data summary, once-only reuse of known data, drafts, request status and maximum time, payment, booking, the same legal footer items, response speed, and a services subdomain as the model documents.

PNRR-funded work also shows the EU emblem with "Finanziato dall'Unione Europea - NextGenerationEU" (art. 34, Reg. UE 2021/241).

## Practices the asseverazione checks (5.3)

- The informative site and the services area share the same header and footer, and menu items lead to the same pages.
- Every page sits in the most coherent section of the tree, with breadcrumbs that match it; service pages show at least Home > Servizi > the service.
- Menu items and titles are not entirely in capitals or italics unless they are acronyms; bold, italics and capitals are used sparingly.
- These content types exist as dedicated pages with their required attributes: **Ufficio** (description; competences or services; main address; contacts), **Documento** (description; the document, downloadable or linked; responsible office or document type), **Luogo** (description; address; access information; contacts), **Evento** (description; date and time; place; cost; contacts), **Persona** (role; organisation; contacts, which may be the office's), **Notizia** (full text; date; author office).

In Drupal terms: one bundle per type with those fields required and ordered in the form and the template; vocabularies loaded from the model's lists; the mandatory menu tree and vocabularies shipped with a deploy hook or migration, because menu links and terms are content, not config (see `modules-and-hooks.md`). A Views listing or Paragraph that replaces a model component keeps its `data-element` attributes.

## Accessibility obligations

- The AgID guidelines require WCAG 2.1 level AA, which they define as equivalent to points 9.1 to 9.4 and the conformity requirements of 9.5 of UNI EN 301549:2018. When the EU adopts a newer EN 301 549, the guidelines' technical references update automatically, so check which version is in force before quoting one.
- **Dichiarazione di accessibilità**: one per site and app, filed only through `form.agid.gov.it` (only the administration's RTD can log in), reviewed and updated every year by 23 September; for a new site the platform generates a link that goes in the footer. Not publishing it is a breach under art. 9 of Legge 4/2004 (AgID news, 16 September 2026). The developer supplies the evidence: the WCAG self-assessment (Allegato 2 model), the list of non-accessible content and why, and the feedback mechanism.
- **Obiettivi di accessibilità**: published by 31 March each year, also through `form.agid.gov.it` (AgID accessibility page).
- Testing combines automated tools with manual checks (keyboard only, a screen reader, 400% zoom reflow, text and non-text contrast, form labels and errors); automated checks find only part of the failures, and documents editors upload are in scope too.

## PNRR timing

Deadlines and asseverazione status are set per avviso on PA digitale 2026 (`padigitale2026.gov.it`) and in its decrees; the current deadlines and any extension were not verified here. Ask which avviso and deadline a comune is under before promising anything about funding, and treat the conformity criteria as the acceptance checklist either way.
