# cube2Sphere--Blender-Addon-Example

Cube2Sphere Addon
A deterministic Blender addon for bidirectional shape conversion.

Overview
Cube2Sphere is a custom Blender Python addon that converts a selected cube into a smooth sphere — and reverses the process by converting a sphere back into a cube. The addon was created through iterative prompt‑driven development, debugging, and feature expansion.

This project demonstrates tool development, troubleshooting, UI integration, and clean pipeline design.

Features
Cube → Sphere conversion

Sphere → Cube conversion

Smooth shading + Subdivision Surface modifier

Deterministic object‑difference tracking

No StructRNA or ghost‑object errors

Undo‑safe operators

Clean N‑Panel UI integration

Fully self‑contained single‑file addon

Installation
Download cube2Sphere.py

Open Blender → Edit → Preferences → Add-ons

Click Install…

Select the cube2Sphere.py file

Enable the addon

Open the N‑Panel → Cube2Sphere tab

Usage
Cube → Sphere
Select a cube

Open the N‑Panel → Cube2Sphere

Click Cube → Sphere

The cube is replaced with a smooth, subdivided sphere

Sphere → Cube
Select a sphere

Click Sphere → Cube

The sphere is replaced with a clean cube

Both operations are:

deterministic

ghost‑proof

undo‑friendly

Development Process
This addon was created through an iterative, prompt‑driven workflow. The project evolved from a simple script into a fully‑featured Blender addon with expanded functionality.

1. Initial Script
The project began with a basic Python script that:

detected the active cube

created a sphere at the same location

deleted the original cube

produced a clear, visible transformation

This provided a testable foundation.

2. Debugging and Troubleshooting
Early versions triggered Blender’s StructRNA errors due to invalid object references.
To fix this, I:

analyzed Blender’s operator behavior

identified ghost‑object creation

implemented deterministic object‑difference tracking

avoided accessing deleted RNA blocks

ensured safe deletion and selection handling

This eliminated all errors and produced a stable pipeline.

3. Converting the Script Into an Addon
Once stable, the script was packaged into a full Blender addon with:

proper registration

undo‑safe operators

a custom N‑Panel UI

clean, modular code structure

This transformed the script into a reusable tool.

4. Expanding Functionality
After the addon was stable, I added a second operator:

Sphere → Cube (reverse transformation)

This mirrored the original pipeline and demonstrated extensibility and clean architectural design.

5. Prompt‑Driven Development
Throughout the project, I used iterative prompt engineering to:

refine logic

debug errors

improve structure

expand features

document the tool

This demonstrates the ability to use AI as a collaborative engineering assistant.

Technical Architecture
Deterministic Object Tracking
Blender operators sometimes create temporary objects or leave behind invalid references.
To avoid this, the addon uses a before/after object‑difference method:

Capture all objects before creation

Run the operator

Capture all objects after creation

The difference = the newly created object

This prevents:

StructRNA errors

ghost objects

invalid pointer access

unpredictable behavior

Safe Deletion
Objects are deleted only after:

deselecting everything

selecting the original object by name

verifying it still exists

This ensures Blender never attempts to access a removed RNA block.

UI Integration
The addon adds a custom panel:

Code
View3D → N‑Panel → Cube2Sphere
With two operators:

object.c2s_convert (Cube → Sphere)

object.c2s_reverse (Sphere → Cube)


Why This Project Matters
This addon demonstrates:

Blender Python scripting

debugging complex API behavior

deterministic pipeline design

UI and operator integration

clean, modular code structure

feature expansion (reverse operator)

practical tool‑building for artists and pipelines

It represents a complete arc:

Script → Debugging → Production Pipeline → Addon → Feature Expansion

