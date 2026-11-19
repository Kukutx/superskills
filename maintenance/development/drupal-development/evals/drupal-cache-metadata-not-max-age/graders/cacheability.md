---
type: llm
---

The block shows per-user data that changes when bookings are saved. The right fix is cacheability metadata, not disabling the cache.

PASS if the main fix the reply gives adds BOTH of these to the block (in the `#cache` of `build()` or through `getCacheContexts()` and `getCacheTags()`):
- a per-user cache context (`user`), so each account gets its own copy; and
- cache tags that are invalidated when bookings change, such as the booking entity type's list tag (`booking_list`) or a custom per-user tag that the code invalidates when a booking is saved.
The reply must also say that `max-age: 0` is not the right fix, or only a last resort, because it makes the block uncacheable instead of correct. Offering a lazy builder placeholder in addition is fine.

FAIL if the reply accepts `max-age: 0`, the page cache kill switch or disabling caching as the main fix; if it adds the `user` context but nothing that makes the count update when a new booking is saved; or if its main advice is to clear caches more often.
