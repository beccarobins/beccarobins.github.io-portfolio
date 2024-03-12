---
layout: post
title: The content stack
published: true
subtitle: > 
    Part 1: markup languages
# cover-img: /assets/img/path.jpg
# thumbnail-img: /assets/img/thumb.png
share-img: /images/social-share-logo.png
gh-repo: beccarobins/beccarobins.github.io
# gh-badge: [star, fork, follow]
gh-badge: [follow]
tags: [content stack, markup languages, Markdown, HTML]
---

Although you may consider yourself a writer first and foremost, venturing into writing for the web requires much more than grammar skills alone. You'll most likely find yourself needing to "mark up" your writing to format it appropriately for your site and enhance its readability for your audience. And the tool to do this is a **markup language**.

## Markup languages

A markup language is essentially a systematic way of formatting digital text. Any text that you see on a website, in an email, or even just in a Word doc, that has been bolded, italicized, or just changed size has been "marked up". In an email or Word, the markup happens behind the scenes&mdash;you highlight a bit of text and then click a button labeled **B** and viola! Bold! However, if you're working with an [authoring tool](../coming-soon) that doesn't have this level of abstraction, you'll need to learn markup language. Importantly, you'll need to learn which language (or languages) you need because it's not a one-size-fits-all situation.

This blog is written in a combination of Markdown and HTML. I use both because _most_ of what I write has pretty simple formatting and Markdown is a lot less work than HTML. However, HTML is much more flexible and I can customize things (like images) with HTML that I can't with Markdown. I'll go over those two in a _little_ bit more detail, however, it's important to note that I'm really only scratching the surface.

### Markdown

A _markup_ language called _markdown_? What? Yes, yes you read that correctly. While that may be a head-scratcher, the language itself is anything but; Markdown is an exceedingly simple markup language that anyone can learn _and use_ in just minutes (I swear). The drawback of having such a simple markup language is just that&mdash;compared to other markup languages, it can only do simple things. If you want to do anything beyond pretty basic formatting, you'll have to learn at least a little bit of another markup language.

#### Markdown examples

Here is what the header and first sentence of this section looks like in Markdown:

```
### Markdown

A _markup_ language called _markdown_?
```

Here is an example image formatted in Markdown using the following syntax: 

```
![Becca's cat Oscar playing with a bath towel.](../images/oscar_towel.jpg)
```

![cat pic](../images/oscar_towel.jpg)

This syntax is super simple but lacks versatility. If you rely on Markdown in your organization, you'll need to either edit, size, and format your images before importing them into your content, which trust me, is a lot less easy than it sounds, or your engineering team will likely need to develop a Markdown extension that enables more advanced functionality.

Even if you're not a content creator, learning Markdown is helpful in many fields. The [Markdown guide][Markdown guide] is an **excellent** resource for Markdown, whether you're an absolute beginner and you're looking for more flexible ways to markup your content.

### HTML

Even if you've never used HTML, you've probably heard of it. I first used it 20+ years ago in a class I believe was called "Keyboarding", where I created the dullest static webpage known to man. These days, there are hundreds of tools to help you create webpages without learning a line of code, but behind it all is the lifeblood of front-end engineering: HTML. If you're working in content, it's very unlikely you'll need the skills of a front-end developer, but knowing a few bits and bobs can take your content to the next level.

#### HTML examples

Here is the header and the first sentence from the previous section in HTML for comparison:

```
<H3>Markdown</H3>
<p>A <i>markup</i> language called <i>markdown</i>?
```

What was three hashtags and four underscores is now seven HTML "tags" with multiple characters each. You'll also notice that the tags preceding the formatted content are slightly different from the ones following the formatted content. This is because HTML requires both opening and closing tags. Forgetting to close a tag or simply an error in the closing tag syntax will result in the formatting "spilling" over and formatting things you don't want to be formatted. I think it's easy to see why I prefer using Markdown for text-heavy posts.

Now here is the same image from before, but using some image attributes in HTML:

<div>
<img src="../images/oscar_towel.jpg" alt="Becca's cat Oscar playing with a bath towel." width="50%" height="50%" class="center">
<br>
</div>

```
<div>
<img src="../images/oscar_towel.jpg" 
     alt="Becca's cat Oscar playing with a bath towel." 
     width="50%" 
     height="50%" 
     class="center">
</div>
```

While the formatting is substantially more effort than the Markdown version, it's also much more visually pleasing and versatile. However, there are ways to make formatting in HTML slightly easier. For example, the style parameters used to center this image are _not_ included in the above syntax but rather result from functionality in HTML (and many other languages) called "inheritance". Inheritance here refers to the fact that I have a separate file that dictates style parameters that all HTML content in my blog should adhere to. So, when I formatted this image by calling `class`, it pulled in those parameters, or "inherited" them.

I'm no expert on HTML and besides the tag for bold formatting (which oddly enough is `<strong>` not `<bold>`), I can _never_ remember the syntax correctly. My favorite resource for HTML is by far [W3][W3 HTML]. It gets straight to the point, shows you the syntax, and provides a sandbox for you to test it out. I can't recommend W3 enough.

### Other markup languages

There are tons of other markup languages out there&mdash;and there are also "flavors" of some of these. 

- **LaTeX** is probably something you'll only encounter if you're working in STEM or possibly Finance. It's typically used to format mathematical equations.
- **XML** or eXtensible Markup Language is a "meta" markup language as its purpose is for storing and transmitting data (see: [What Are Markup Languages?][What Are Markup Languages? Semrush]).
- **GitHub-flavored Markdown** - is an extension of standard Markdown built specifically for use on <github.com> (where this blog is hosted). It supports more advanced functionality, such as creating functional checklists or bitly-style short links to reference pull requests or issues.

If you need to learn about another markup language, Wikipedia has a [list of markup languages][List of markup langauges], which links to even more specific lists of markup languages (I told you there were tons). 

## Summary

Knowing the ins and outs of your markup language _will_ make you a better content creator. You will be able to direct your readers as needed and communicate your message much more effectively when you can style your text appropriately. However, markup may only touch the surface of programming languages you may need. In fact, while I mentioned that I use Markdown and HTML for markup, this post actually also includes [unicode][Unicode] for special characters and [YAML][YAML] for configuration. I will touch a bit on YAML in a future post about metadata, but you'll need to wait on that one.

Stay tuned for the next part of the content stack series, which will cover [authoring tools](../coming-soon)&mdash;the program where you'll use all your markup skills.

[Markdown guide]: https://www.markdownguide.org/

[Markup language]: https://en.wikipedia.org/wiki/Markup_language

[What Are Markup Languages? Semrush]: https://www.semrush.com/blog/markup-language/

[What is a Markup Language?]: https://www.howtogeek.com/721685/what-is-a-markup-language/

[List of markup langauges]: https://en.wikipedia.org/wiki/List_of_markup_languages

[W3 HTML]: https://www.w3schools.com/html/

[Unicode]: https://home.unicode.org/

[YAML]: https://geekflare.com/yaml-introduction/
