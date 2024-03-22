---
layout: post
title: Accessibility improvements
published: true
# subtitle: Excerpt from Soulshaping by Jeff Brown
# cover-img: /assets/img/path.jpg
thumbnail-img: ../images/22.png
share-img: /images/social-share-logo.png
gh-repo: beccarobins/beccarobins.github.io-portfolio
# gh-badge: [star, fork, follow]
gh-badge: [follow]
tags: [Microsoft, Accessibility, Python]
---

This project started out as a quick fix that morphed into a week-long hackathon project at one of Microsoft's "Fix Hack Learn" weeks where employees get to work on a project that interests them. ​​​​​​​From an earlier project I'd completed, I noticed that the vast majority of the alternative text within my team's portfolio was not accessible. Instead, there was filler text, such as "image" or no alternative text at all. Images accounted for the majority of media assets within our portfolio, so fixing alt text was a high impact opportunity to improve accessibility.

The aforementioned "quick fix" was a Jupyter notebook I created to update Markdown syntax for images; our platform developers created Markdown extensions to allow writers more flexibility than standard Markdown allows, including some additions to image functionality. This is especially important because my team doesn't have access to update HTML, which means we can't modify HTML attributes such as "alt" or "aria-labelledby". This project built upon that Jupyter notebook by focusing on alternative text.

## Process
I coded this project from scratch in Python, starting in a Jupyter notebook and eventually moving onto a standalone desktop executable. The original code identified the string pattern that represented Markdown images using regular expressions, extracted the alt text (when available) and the file path, and rearranged the text into the new syntax. I created this notebook because the new syntax was a bit finicky and verbose—I kept messing it up when I updated it manually.

```
import re
import pyperclip

# Copy text to clipboard
original_string = pyperclip.paste()

pic_path = re.findall(r'(?<=]\()[^\)]*',original_string)
alt_text = re.findall(r'(?<=!\()[^\)]*',original_string)

if len(pic_path) == 0:
  pic_path = re.findall(r'(?<=source="[^"]*)',original_string)
  alt_text = re.findall(r'((?<=alt-text="[^"]*)',original_string)

# New image syntax using internal Microsoft code
new_string = ######

pyperclip.copy(new_string)
pyperclip.paste()
```
<figcaption  class="caption">Clip of script from original Jupyter Notebook that focused on updating image syntax.</figcaption>

## Moving from notebook to app
Not all my colleagues are familiar with Python or Jupyter Notebooks, so I decided to turn the script into a simple-to-use app that could be run by anyone. I've never been on the coding end of app development, so I started in shallow waters with the PySimpleGUI package that helps build, well, simple GUIs. It's not the prettiest thing, but customers aren't seeing it, so I'm okay with it.

<a class = "center" href="https://www.youtube.com/watch?v=8aE4JO4ld4g" target="_blank"><img src="../images/Smart%20Alternative%20prototype%20FHL%20page%20-%20thumbnail.jpg" alt="HTML tutorial"></a>

<figcaption  class="caption">An iteration of the app, "Smart Alternative". The UI text for the toggle features follows the content patten {verb){image/feature}. The radio button text uses terms familiar to the intended users: simple image, complex image, and icon. The output message shows the user the new syntax as well as an analysis that checks the alternative text against content guidelines.</figcaption>

## Controversial guidelines
In addition to meeting user needs, our images needed to follow the platform's accessibility guidelines. Some of the platform guidelines are standard, for example, images used only for decoration actually shouldn't have alternative text. However, one guideline is a bit controversial, as it states that all alternative text should start by stating the type of image. This is a bit controversial because screen readers already state "image" when reading alt text and stating the image type can lead to unnecessary verbosity and a subpar experience. Ultimately, I implemented the business logic of these guidelines into the app, which provided the user with an analysis of the text in addition to the new syntax with the checked features.

## Outcome
I was able to build the app within the hackathon, and while it may not be pretty, it's very usable. I ended up using this app to update hundreds of images across our portfolio (~160 modules on learn.microsoft.com).

## Takeaway
While I would have preferred creating a web app over a desktop app, it did the job it needed to do and I've used it many times. There are still many improvements that could be made: ideally, it would be an extension in Visual Studio Code (where most of my team's authoring is done), and it would be owned by the same team that creates our accessibility guidelines—shortly after this app launched, the guidelines that I "snapped to", were changed and my app was already out-of-date, so any meaningful updates would (in an ideal world) ship with changes to guidelines.
