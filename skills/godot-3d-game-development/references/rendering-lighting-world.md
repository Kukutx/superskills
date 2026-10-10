# Rendering, Lighting and World Reference

Use for 3D materials, lights, WorldEnvironment, GI, transparency, shadows, world rendering, LOD/occlusion/instancing and measured 3D performance.

## 1. Renderer and target first

Before recommending a 3D rendering feature, identify the project's actual renderer and target hardware/platform. Forward+, Mobile and Compatibility do not expose identical rendering features or costs.

For version-sensitive renderer capabilities, verify the project's exact Godot documentation rather than storing a permanent feature matrix here.

## 2. Build the look from the cheapest correct layer

Prefer the existing/project-native stack:

```text
mesh + StandardMaterial3D/material setup
-> basic lights/environment
-> shadows only where useful
-> GI/reflections when the scene needs them
-> custom spatial shaders/post effects only for a real visual requirement
```

Do not start with advanced GI, screen effects or custom shaders merely because the project is 3D.

## 3. Materials

Use `StandardMaterial3D`/the project's existing PBR workflow for ordinary surfaces. Use `ShaderMaterial` when a custom effect genuinely requires shader logic.

Check:

- albedo/base color;
- roughness/metallic expectations;
- normal/ORM/AO textures when supplied;
- transparency mode and sorting implications;
- material/resource sharing when one object needs a unique runtime parameter.

Do not duplicate a shared material unintentionally for every object, but also do not mutate one shared resource when only one instance should change.

## 4. Lighting and environment

Separate responsibilities:

```text
DirectionalLight3D -> broad directional source
Omni/Spot/other local lights -> local illumination
WorldEnvironment -> sky/ambient/tonemap/fog/post environment
```

Shadows, many visible local lights and advanced environmental effects can be expensive. Add them according to visual need and target performance, not a universal light-count rule.

## 5. Global illumination and reflections

Choose GI/reflection techniques based on:

```text
static vs dynamic world
scene size
lighting-change requirements
renderer support
target hardware
bake/iteration cost
measured visual benefit
```

Do not encode "realistic = use X" as a permanent rule. A stylized scene may need no dynamic GI; a mostly static scene may benefit from baked approaches; a dynamic world has different constraints.

## 6. Transparency and overdraw

Transparent materials can create sorting and fill-rate problems. Prefer opaque/cutout-style solutions when they match the art, and inspect large overlapping transparent surfaces, particles, foliage and full-screen effects when GPU cost rises.

Do not fix transparency artifacts by arbitrarily disabling depth/shadows everywhere.

## 7. World construction

Keep render geometry separate from gameplay metadata/collision/navigation.

Godot-native level authoring, GridMap, CSG/prototyping or imported DCC scenes are all viable when they match the project's source-of-truth workflow. Do not maintain the same room/world layout manually in both Blender and Godot without a clear ownership boundary.

Prototype geometry may be replaced later; avoid binding gameplay IDs to fragile mesh names/transforms without a stable convention.

## 8. LOD, visibility and occlusion

Use LOD, visibility ranges, occlusion culling and instancing when the scene scale/content makes them valuable.

Typical decision order:

```text
measure real scene
-> identify draw/geometry/shadow/overdraw bottleneck
-> remove unnecessary work
-> use import/mesh LOD or visibility strategy
-> add occlusion/instancing when scene structure benefits
-> re-measure same scenario
```

Do not add every optimization feature to a small room or prototype.

## 9. Repeated geometry

`MultiMeshInstance3D` can be useful for large numbers of repeated meshes, but it changes per-instance interaction/customization tradeoffs. Use it for a demonstrated repeated-rendering problem, not as a default entity architecture.

## 10. 3D performance diagnosis

Classify first:

- CPU/script/physics/navigation;
- draw calls/scene complexity;
- shadows/lights;
- shader/GPU cost;
- transparency/particles/overdraw;
- texture/mesh memory;
- asset loading/import/stutter.

Compare the same representative scene and camera path before/after. "Looks simpler" or "node count went down" is not performance evidence by itself.

## 11. Validation

Check the relevant target(s):

- correct renderer and project settings;
- materials/normal maps/lighting look correct in motion;
- shadows and transparent surfaces have no obvious artifacts;
- day/night or dynamic-light changes if supported;
- representative worst scene/camera path;
- LOD/occlusion transitions do not visibly break gameplay readability;
- performance measurement before/after any optimization;
- low-end/mobile/web target only when that platform is actually supported.
