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

1. The post should be in Markdown format.
2. The post should have a cover image.
3. Any additional images should be placed in the `/assets` folder.
4. The post should begin with metadata in the following format:

```yaml
---
title: "Title"
excerpt: "This is a post"
coverImage: "/assets/cover.png"
date: "2025-03-20T23:10:00.000-05:00"
author:
  name: Name
  picture: "/avatars/avatar.jpg"
ogImage:
  url: "/assets/cover.png"
---
```

5. The date and time should be adjusted to UTC time. So if you are in EST, you should add `-05:00` to your time of posting.
6. The author picture should be placed in the `/avatars` folder. If you don't have a picture, add an avatar for youself in the `/avatars` folder inside of your post commit. Feel free to also just use a link to your avatar hosted on another websitem, such as `"https://avatars.rotur.dev/b1j2754"`

