# How to Publish a Blog?

Follow this file hierarchy:

```plaintext
katnip-blog/
│
├── posts/
│   ├── 2024-06-30-Release/
│   │   ├── assets/
│   │   │   ├── cover.png
│   │   │   ├── example-image1.png
│   │   │   └── example-image2.png
│   │   └── post.md
│   │
│   ├── YYYY-MM-DD-name/
│   │   ├── assets/
│   │   │   ├── cover.png
│   │   │   └── feature-image.png
│   │   └── post.md
│   │
│   └── YYYY-MM-DD-name/
│       ├── assets/
│       │   ├── cover.png
│       │   └── update-image.png
│       └── post.md
```

## How to Format Your Post?

* Create a folder in `/posts/` in the format: `YYYY-MM-DD-Name_Here_In_Snakecase`
* The post should be in Markdown format.
* The post should have a cover image.
* Any additional images should be placed in the `/posts/[postName]/assets` folder.
* The post should begin with metadata in the following format:

```yaml
---
title: "Title"
excerpt: "This is a post"
coverImage: "./assets/cover.png"
date: "2025-03-20T23:10:00.000-HH:MM"
lastUpdated: "YYY-MM-DDTHH:MM:SS.SSS-HH:MM"
author:
  name: Name
  picture: "/avatars/avatar.jpg"
ogImage:
  url: "./assets/cover.png"
---
```

* The date and time should be adjusted to UTC time. So if you are in EST, you should add `-05:00` to your time of posting.
* The author picture should be placed in the `/avatars` folder. If you don't have a picture, add an avatar for youself in the `/avatars` folder inside of your post commit. Feel free to also just use a link to your avatar hosted on another websitem, such as `"https://avatars.rotur.dev/b1j2754"`; The `https://` part is very imporant, as it is how a link to an image is recognized.
* ogImage is the display image for a thumbnail. I usually just set this to the cover image, but its perosnal choice

