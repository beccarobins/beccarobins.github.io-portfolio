---
layout: post
title: The content stack
published: true
subtitle: >
    Part 2: authoring tools
# cover-img: /assets/img/path.jpg
# thumbnail-img: /assets/img/thumb.png
share-img: /images/social-share-logo.png
gh-repo: beccarobins/beccarobins.github.io
# gh-badge: [star, fork, follow]
gh-badge: [follow]
tags: [content stack, authoring tools, editorial tools]
---

In the first post of the this series, I wrote about markup languages. To show how those markup languages shape your text, you need an _authoring tool_, otherwise your text will \_just\_ look \*\*crazy\*\* and you won't know what you've actually done to it. Here we'll dive into some of the different types of authoring tools (also known as editors) and look at some widely used tools.

## Built-in authoring tools

If you use a proprietary [content management system](../coming-soon) like WordPress, you're using their built-in authoring tool. In this case, chances are you're _not_ dealing with markup languages, but rather a toolbar with formatting options, much like those found in Word or Google Docs. The main advantage of these tools is their ease of use; most people have used similar tools, so adoption is a piece of cake. A disadvantage, however, is that these tools might have limited functionality, and the flexibility you can achieve with markup languages, such as customizing images, may not be available. 

Let's take a look at one exception, the WordPress block editor, which gives non-technical users the power of a frontend engineer.

### WordPress block editor

WordPress' authoring tool, the block editor, can do **a lot**. The editor's vast feature set and flexibility is a large reason it's the market leader in the content management space, constituting a whopping 43% of **all** websites on the internet ([WordPress Statistics: How Many Websites Use WordPress in 2023?][WordPress Statistics: How Many Websites Use WordPress in 2023?]). Content creators love the block editor not only for it's power, but also for its convenience: it's an all-in-one tool where you can add and update [metadata][Coming soon], visit your live URL, customize the post's landing page appearance, and even tag for SEO.

![The block editor][Welcome to the Gutenberg Editor]

Also known as the Gutenberg editor (named after the inventor of the printing press, Johannes Gutenberg), the editor includes your standard formatting options: bold, italics, etc. But what really makes it pack a punch is the wealth of "blocks" available. Blocks lets users create highly customized web pages with the click of a button. Behind the scenes, blocks are modular chunks of code that pull in bits of information tagged throughout WordPress.

<div>
<img src="https://wordpress.org/documentation/files/2022/10/Screen-Shot-2022-10-24-at-4.24.56-PM.png" alt="Block editor options dialog box." width="40%" height="40%" class="center">
<br>
</div>

For example, the `Post Author` block pulls in data from the "Users" section of your WordPress instance. It grabs the author name, avatar (i.e. image), and user bio and wraps it in a neatly formatted container. Using a `Post Author` block means you can easily add consistently-formatted author information to all of your posts, regardless of author, without copying and pasting or rewriting a thing.

If you want to learn how to use the block editor, but don't want to go through the hassle of setting up a WordPress website, you can [use this handy WordPress sandbox][How to start using WordPress Playground], which runs an entire WordPress instance in an iframe. If you've never used WordPress before, open the sandbox and follow these steps to get to the block editor:
1. Select **My WordPress Website**.
1. Scroll down to **Posts**.
1. Click the **Add New** button to create a new post.
1. Follow the "Welcome to the block editor" prompt.

## Internal authoring tools

You might be using an _internal_ authoring tool, meaning one built just for your company. In that case, I can't describe much because I don't know your business (professional or personal). That said, if you _are_ using an internal tool, make sure you _really_ get to know it. The good, the bad, and the ugly. If it's relatively new, there are bound to be unexpected kinks. If you're already familiar with other authoring tools or markup languages, identifying these kinks will not only potentially save a lot of people some trouble in the future, but it will set you up as the go-to authoring tool guru. And if it's not new, then learning the ins and outs of the tool will let you focus on writing your content.

## elearning authoring tools

Learning & development professionals have slightly different needs than other content creators. In addition to educating their audience, they usually have to _test_ them as well. This means going beyond static webpages (like this one) and adding dynamic features that receive input from learners, assess them, and return the results. As such, elearning authoring tools have very specific features and content types, like **branched scenarios**, where the subsequent content seen by the user is dependent on their previous input. If you've used a product simulation before, with prompts and button clicks and dropdowns, that was probably built using a branched scenario.

I won't dive in too deep here because elearning authoring tools are really their own field and I simply can't do them justice. However, if you're interested in learning more, here is a list of a few popular authoring tools along with links to some learning resources.

- [Articulate][Elearning Heroes]
- [Adobe Captivate][Adobe Captivate tutorials]
- [iSpring][iSpring]

## Other authoring tools

Believe or not, we've only touched the surface of authoring tool technology. There are many more tools out there that can be used to create content, including those appropriated from software development and those that _only_ support formatting content.

### Integrated Development Environments

For this blog, I've been using Visual Studio Code as an authoring tool. Visual Studio Code is an integrated development environment (IDE) for writing and editing source code. I use it partly because I've gotten comfortable with it (I use it at work too) and partly because it's free. But another advantage of using an IDE is taking advantage of the terminal, or the area where you can use commands to run different programs and utilities to support your work.

My blog is hosted on **Git**Hub, so every time I work on it, I use **git** commands, the version control system on which GitHub is built. Using a version control system like git means that if I mess something up and need to back track, I can easily do that. While it takes a bit of knowledge to use git, it's a lot easier to learn a few bits of code than to recreate an entire post from memory.

<div>
<img src="../images/mick-vs-code.jpg" alt="Becca's cat Mick supervising her authoring work in Visual Studio Code]" width="70%" height="70%" class="center">
</div>
<figcaption class="center"> Here, my cat Mick, is monitoring my post progress in Visual Studio Code.</figcaption>

In addition to git, IDEs let you use pretty much any coding language you can think of. Something I've more recently begun using (just for this blog) is Ruby, which GitHub Pages are based on. Using some very simple Ruby "gems", I can launch this website on a local server to test out how things are looking before pushing it live, essentially playing the part of a [staging environment][Coming soon].

### WYSIWYGs

A WYSIWYG, which is pronounced "wizzy wig", stands for "what you see is what you get". A WYSIWYG is a very straightforward tool: you add marked up content, you see rendered content. The beauty of a WYSIWYG is that you see the rendered content _as_ you're writing it. If you're learning a new markup language, this is an excellent tool as you can correct your mistakes immediately and learn correct syntax right off the bat. The downside of using a WYSIWYG is that, while you get to see rendered content, it might not render the same way your site does. Your site may have some specific style parameters it brings in, so what you see in the WYSIWYG editor might be what you _sort of_ get.

I haven't used a WYSIWYG in awhile, but I did _all the time_ when I was a Content Developer at DataCamp. We provided the instructors we worked with feedback in GitHub issues and sometimes it would take HOURS to write up that feedback. If you wrote your feedback directly in a GitHub issue and accidentally navigated away from the page...oh man, hours of work GONE. It only took that happening once for me to seek out a Markdown editor. While some of my colleagues swore by [Dillinger][Dillinger], I landed on [StackEdit][StackEdit].

You can try out StackEdit yourself below. If you aren't familiar with Markdown, scroll through the text and compare the raw markup on the left with the rendered output on the right.

<iframe src="https://stackedit.io/app#" title="StackEdit editor" height="500" width="800"></iframe>

## Summary

If you've learned anything from this post, I hope it's this: there isn't a single "best authoring tool" out there, there is only the right authoring tool for the job. The tool you use depends on your needs, your skill set, and the other tools in your stack. And if you're a content person like me, you'll probably use many different authoring tools through the course of your career.

Next up in the content stack series is [metadata](../coming-soon)&mdash;data about data.

Need to catch up? Check out [part 1: markup languages](../content-stack-markup)

[How to start using WordPress Playground]: https://developer.wordpress.org/playground/
[WordPress Statistics: How Many Websites Use WordPress in 2023?]: https://colorlib.com/wp/wordpress-statistics/
[Block editor options]: https://wordpress.org/documentation/files/2022/10/Screen-Shot-2022-10-24-at-4.24.56-PM.png
[Welcome to the Gutenberg Editor]: https://wordpress.org/documentation/files/2022/10/Screen-Shot-2022-10-24-at-4.20.49-PM-1-1024x666.png
[Coming soon]: ../coming-soon
[Block list]: https://wordpress.org/documentation/article/blocks-list/#:~:text=Below%20is%20a%20list%20of%20the%20blocks%20that,types%3A%20Text%2C%20Media%2C%20Design%2C%20Widgets%2C%20Theme%20and%20Embeds.
[StackEdit]: https://stackedit.io/
[WYSIWYGs]: https://en.wikipedia.org/wiki/WYSIWYG
[Dillinger]: https://dillinger.io/
[Elearning Heroes]: https://community.articulate.com/
[Adobe Captivate tutorials]: https://elearning.adobe.com/adobe-captivate-tutorials-2/
[iSpring]: https://www.ispringsolutions.com/guides
