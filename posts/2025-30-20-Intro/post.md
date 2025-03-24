---
title: "Introducing: Katnip! «Initial Release»"
excerpt: "Introducing Katnip, a Transpiled, text-based version of Scratch for the web!"
coverImage: "./assets/cover.png"
date: "2025-03-20T23:10:00.000-05:00"
author:
  name: B1j2754
  picture: "https://avatars.rotur.dev/b1j2754"
ogImage:
  url: "./assets/cover.png"
---

# Introducing Katnip: A Transpiled, Text-Based Version of Scratch for the Web!

We are excited to announce the **initial release of Katnip**, cool new project aimed at providing a link between Scratch and real-world programming languages!

## ❔ What is Katnip?

Katnip is a programming language designed to give users the ability to create interactive projects just like Scratch, but with the flexibility and power of text-based code. Unlike the traditional Scratch block-based interface, Katnip allows for more precise control and scalability, ideal for users who want to write code without worrying about the visual (and **tedious** 😭) structure of blocks.

![Katnip Cover](.\assets\cover.png)

### 🗝️ Key Features:
- **Text-Based Syntax**: Instead of blocks, users write code in a simple, human-readable syntax.
- **Compiling for Web**: Katnip projects are transpiled to sb3, which can be run directly either in Scratch or through Katnip's project vm.
- **Easy to Learn**: Designed to be beginner-friendly but powerful enough for advanced projects.
- **Large Skill Ceiling**: Though beginner-friendly, don't let it fool you. Katnip is very powerful!!
- **Extension and Library support**: Following in Python's footsteps, custom Katnip libraries and extensions are availible, expanding the possibilities even futher
- **Custom Transpiled Blocks**: Ever needed a resuable block that takes 100s of blocks? Write it instead once with a script that compiles at runtime!

## 🔨 How It Works

Katnip works by taking user-created scripts and compiling them into executable sb3 file. The compiler then produces a file that can be embedded or shared via the web.

This is a huge step forward for the Scratch community, allowing for even more flexibility and creativity when building projects.

Large collaborative efforts upon projects, now can be done fully in text, using code editors with GIT or similar to provide project management like never before!

## 👀 A Sneak Peek at Katnip's Syntax

Here’s a quick example of how a simple Katnip program might look:

>func: greet(warp=true, name[str]){\
&nbsp;&nbsp;&nbsp;&nbsp;looks.say("Hello, " + a.name)\
}\
events.onflag(){\
&nbsp;&nbsp;&nbsp;&nbsp;fn.greet(name: "Katnip")\
}
