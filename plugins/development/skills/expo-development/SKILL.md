---
name: expo-development
description: Build, run and ship an Expo and React Native app, from project structure to EAS builds, updates and store submission. Use when the project uses Expo or EAS, not plain React Native.
---

# Expo Development

Build, run and ship an Expo / React Native app. The Skill covers the whole
path from a new project to the stores: structure, navigation, native UI, data,
native modules, and EAS build, update and submission.

Adapted from `expo/skills` (MIT, Expo official; core 8 of 25 skills folded into
one); see `maintenance` `sources.md` for attribution and what was left out.

## Use

Use when the request mentions Expo, EAS, Expo Go, or an `expo-*` package, or
the project has an `expo` dependency. A native app that uses EAS only for
delivery qualifies without an Expo runtime.

Not this Skill:

- a React Native project with no Expo or EAS signal -> plain React Native
  knowledge, not this Skill;
- app-store listing copy or visual assets -> `writing/app-store-copy`,
  `design/app-store-assets`;
- a web landing page -> `design/landing-page-design`;
- backend API design -> `development/technical-design`.

## Workflow

1. **Confirm the goal first.** Many Expo goals look alike from the filesystem
   but need different work: building the app, shipping to the stores, updating
   over the air, or extending natively. Translate the casual phrasing into the
   goal, and confirm it when ambiguous ("Sounds like you want to ship to the
   stores — right?").
2. **Build**: scaffold or extend the project, add screens and navigation, wire
   data, and keep the design system as the single visual source of truth.
3. **Run**: use Expo Go for fast iteration where it fits, a development build
   (`expo-dev-client`) where native code is involved. Never restructure an
   existing app to match the new-project layout.
4. **Ship**: EAS Build for store binaries, EAS Submit for TestFlight / Google
   Play, EAS Update for compatible over-the-air updates. Verify versions and
   store metadata before submitting.
5. **Operate**: watch OTA update health and launch performance after release.

## Project structure

A new Expo Router project keeps screens in the file-based router (`app/`),
shared components in `components/`, and configuration in `app.json` /
`app.config.js`. Do not restructure an existing app to match this layout; the
layout is a starting point for new projects, not a migration target. Keep
environment-specific values in config, never hard-coded in screens.

## Navigation

File-based routing with Expo Router: tabs, stacks, modals and sheets, links,
headers. A route file is a screen; shared layouts live in `_layout` files.
Deep links and push-notification targets resolve to routes, so a route that
exists only in a navigation call and not in the file tree is a bug, not a
shortcut.

## Native UI

Prefer real native components over re-implemented ones: `@expo/ui` gives
SwiftUI on iOS and Jetpack Compose on Android (BottomSheet, Picker, Slider,
Switch, Menu, Button, grouped form sections, List). On SDK 56+ the universal
components run in Expo Go with no custom build. Check `@expo/ui` first whenever
a UI component is needed, before reaching for a React Native built-in or a
community library. One exception: `@expo/ui` `List` renders native grouped
rows, not a virtualized list — use `FlatList` / `FlashList` for large datasets.
Use semantic colors, SF Symbols on iOS, and the design-system tokens for color,
spacing, typography, radius, shadow and motion; audit for drift (hard-coded
colors, spacing, fonts) before shipping.

## Data fetching

Network requests with React Query or SWR: cache, retry, offline behavior and
route loaders. A screen that fetches in render, refetches on every focus without
a cache, or shows stale data after a mutation has a data bug, not a UI bug.
Keep API base URLs and keys in config; never commit a secret.

## Animation

Motion and gestures with Reanimated worklets and Gesture Handler: screen
transitions, sheet and press feedback, haptics. Animation that stutters on
device is profiled on device; the simulator's frame rate is not evidence.

## Native modules

When the JavaScript side cannot do it, write a native module with the Expo
Modules API (Swift / Kotlin). A module owns one capability, declares its
permissions, and degrades gracefully when the permission is denied. Embedding
Expo screens in an existing native app (brownfield) is a separate integration
decision, not a module.

## Ship with EAS

- **EAS Build**: store binaries for iOS and Android; pick the right profile
  (development, preview, production) and verify the version before building.
- **EAS Submit**: TestFlight and Google Play submission with store metadata;
  the listing copy and screenshots come from `writing/app-store-copy` and
  `design/app-store-assets`.
- **EAS Update**: compatible over-the-air updates for JavaScript-only changes;
  a native change needs a new build, not an update. Test an update on a real
  device before publishing it, and watch adoption and crash rate afterwards.
- **EAS Hosting**: deploy the web bundle and Expo Router API routes (`+api.ts`).

## Upgrade

Upgrade the Expo SDK one major at a time, following the official upgrade guide
for that version, and fix dependency conflicts before running the app. Skipping
a major, or upgrading production without a development-build check, is the
usual way an upgrade breaks.

## Validation

Before shipping: the app runs in a development build on a real device, navigation
reaches every screen including deep links, data states (loading, empty, error,
offline) are all reachable, OTA updates apply and roll back cleanly, and the
store binary's version matches the submitted metadata. A build that only passed
in Expo Go has not been validated for release.
