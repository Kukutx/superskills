# Auditing

Start with the balance sheet. If it does not balance, quantify the difference per period and trace where it first appears; nothing else matters until it is found.

Then, in order of how often each is the cause:

1. a typed number overwriting a formula, the leading source of silent errors;
2. a formula that differs from its neighbours in the same row;
3. a sign convention applied the wrong way;
4. a sum that misses the first or last row;
5. a unit mismatch: thousands against millions, a percentage stored as a whole number;
6. a broken or circular reference, a hidden row or sheet.

Arithmetic worth re-deriving rather than copying from a source: a growth rate (end value = start value × (1 + rate)^years, with years counted as the difference between the two dates) and a multiple (value ÷ the metric, over the same period). A result more than a few percent away from the quoted one usually means a different base year or a different definition, such as trailing against forward. When several sources size a market, show the range across them and take the growth rate from the middle of the cluster, not the extremes. Format by meaning: money as money, counts without a currency sign, ratios as percentages, years as text so they are not shown with a thousands separator.

Plausibility flags: growth above 100% with no explanation, a margin outside anything the industry shows, gross margin below net margin, a late "hockey stick", a value compounding to an absurd level by the final year, and a model that breaks at zero or negative growth.

When the model is being checked before it supports a deck or report, compare the documents too: the same metric must show the same value everywhere once units and rounding are normalized, totals and growth rates must agree with their end points, every figure is labelled with its period, and the wording of a trend matches the direction of its chart.
