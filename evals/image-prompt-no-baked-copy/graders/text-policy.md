---
type: llm
---

The same base image must serve both Chinese and English markets, so headline/slogan copy should not be rendered into the artwork.

PASS if the main prompt does not ask the image generator to render any specific headline, slogan, tagline or marketing sentence (in Chinese or English) inside the image, AND the reply states a text policy such as no text in the image, or leaving clean space for copy to be added later per language. Generic placeholder UI inside a phone screen (bars, a pie chart, small unreadable numbers) does not count as marketing copy.
FAIL if the main prompt tells the generator to render a specific slogan or headline in the image (for example quoted text like "轻松记账，掌控每一分钱" or "Track every penny"), or if the reply gives no instruction at all about text in the image.
