# Gamma
A user interface engine for parsing and rendering content from M3L and GSS files.

Olympus

## WARNING

This protocol is currently under active development and is subject to change. Please do not use it for any production or real-world applications until an official release is available. The official release will be identified by a version ending in .01 or higher.
Versioning is based on the date the version was finalized. At the time this document was written, the current version is 2025.05.10.00, indicating a pre-release version finalized on August 10, 2025.
Please also note that this README is incomplete—additional widgets and content will be included as development progresses and changes are made.


## Built With

-Python 3.11.3

-Kivy

-Python 3.11.3

-Kivy

## Overview
The Gamma project serves as a renderer for M3L (Multi-Media Markup Language) and GSS (Global Style Sheets), designed to deliver a consistent UI experience across various applications. It achieves this by defining the UI structure using M3L and styling it through a GSS file. This system is also integrated within UndChain, a decentralized, cloud-based blockchain platform, where it functions as the UI layer.

Although Gamma is the initial renderer developed for M3L and GSS, it is not intended to be the sole implementation. We currently utilize Python as the main programming language and rely on QT6 for the UI foundation. However, the protocol is flexible enough to be implemented with other UI frameworks—or even game engines, if desired.

The M3L and GSS standards are maintained by me, but they are intended to remain open and evolve over time. Below, you’ll find a list of keywords used in M3L, along with example syntax. Both M3L and GSS adopt a TOML-inspired formatting style.

## Modes
Within M3L and GSS, multiple modes are supported to adapt the UI to different input methods or user contexts—such as transitioning from mouse & keyboard to a game controller or a touchscreen device. Each mode presents a unique layout and interaction model tailored to its environment. The available modes include:

- **Application Mode:** This is the classic windowed mode, resembling a traditional desktop application. It includes standard UI elements like a title bar, minimize/maximize buttons, and menu bars. It’s ideal for desktop usage with mouse and keyboard.
- **Dashboard Mode:** Designed for fullscreen usage within the UI engine, this mode provides a fixed viewport—meaning the user cannot scroll the entire window (though individual widgets may still support scrolling). It’s best suited for presenting dashboards or visual summaries, and it's the default mode when using a game controller. Dashboard Mode is intentionally limited in terms of complex inputs like text fields, favoring simple, navigable layouts that are controller-friendly.
- **Web Mode:** Created to mimic the behavior and structure of a typical website, Web Mode offers vertical scrolling only. Elements can be defined as static, ensuring they stay pinned in place while the rest of the content scrolls. This makes it ideal for document-style pages or information-driven layouts.
- **Desktop Mode:** Tailored for wide-screen desktops, this mode supports horizontal scrolling. Like Web Mode, you can define static elements that remain fixed on the screen, but Desktop Mode also supports parallax scrolling—allowing certain elements to move at different speeds during scroll events, adding depth and motion to the user experience.

## Elements
In Gamma, an Element represents a UI structure composed of multiple widgets, designed to work together to fulfill a specific user-facing function. Below is a list of the core elements supported by the M3L/GSS system, along with a breakdown of their intended usage:

#### Video Element
Designed to embed video content in the UI. This element typically includes a video widget and may also incorporate the following:

- Reactions
- Goal bar
- Voting
- Quizzes
- Comments/Chat (for live streams)
- Pop-ups (tooltip-style overlays used for emphasis or interactivity)
- Closed Captioning (manual for now; future versions may support AI-based generation)
- Ratings (to suggest target audience)
- Video suggestions

Empty fields in M3L (like missing video suggestions) should be gracefully handled by GSS to maintain layout consistency.

#### Video Catalog
Enables users to browse and explore multiple video entries. Similar to an item selector, but without checkout functionality.

#### Map
Displays a 2D map or image annotated with interactive tooltips (landmarks). Supports:

- Custom landmarks via marker widgets
- Reaction widgets and links within each marker
- Ideal for highlighting points of interest on static images

#### Background Audio
Plays ambient audio with no user controls except mute (accessible via settings). Controlled entirely through GSS, not defined in M3L. By default, background audio should mute when other media is active, though final behavior is GSS/user defined.

#### Spreadsheet
A structured element for handling tabular data. Includes:

- One or more table widgets
- Tab widget
- Scroll widget
- Graph widget
- Special text areas (size-limited)

#### Social Media
Mimics a social feed layout. Contains:

- Messaging widget
- Reaction widget
- Rating widget
- Mute widget

#### Text Editor
Simulates a code editing environment with:

- Line numbering (label widget)
- Syntax-aware text area
- File explorer (tree widget)
- Status bar
- Search widget

#### Word Processor
Similar to a text editor, but geared toward writing:

- Includes spellcheck and formatting tools
- Replaces line number widget with text modifier for rich editing (via press-and-hold options)

#### GSS Emulator
- Used to preview pages under different GSS themes for compatibility testing. Not intended for building theme-inconsistent pages.

#### Markdown
- Renders .md content as styled HTML-like views for readable formatting.

#### Tiles
- Displays a collection of card/poster widgets as a visual selection grid. Can be paired with a filter widget for sorting/searching.

#### Notification (Toast)
Displays temporary on-screen alerts. Three types:

- Information
- Warning
- Error

#### Gallery
- Displays large sets of images. Each image can have a title and subtitle as part of its description.

#### Menu Bar
Top-level navigation container. Includes:

- Icon and button widgets
- Sliders, dropdowns, dividers
- Tabs and full-screen page slides

Note: Only one menu bar is allowed per application.

#### Image Editor
Built for basic image manipulation. Includes:

- Canvas
- Image viewer
- Color picker
- Layer manager (tree widget)

Node Graph
Used for visualizing relationships or idea mapping. Contains:

#### Grid widget

- Shapes and arrows
- Color picker

Should use Obsidian’s open file format for node data.

#### Hero Section
A promotional UI block, mainly for web view but usable elsewhere. Should include:

- Header and sub-header (max 256 characters)
- Call to action (button)
- Optional image/icon and secondary action

#### Article
For long-form content. Contains:

- Header widget (titles)
- Section headers
- Paragraph widgets

May be expanded into a Book Element with chapters in the future.

#### Documentation
Similar to Article, but adds:

- Hyperlink widgets
- Table of contents
- Embedded media (images, video, maps)

#### Custom
A fully user-defined element. Requires:

- Widget declarations
- Resizing logic
- State definitions for undo/redo or revision control

Note: Use with care—intended for unique needs, not for bypassing UI standards.
