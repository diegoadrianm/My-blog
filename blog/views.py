from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-moutains",
        "image": "mountains.jpg",
        "author": "Diego",
        "date": date(2024, 12, 16),
        "title": "Mountain Hiking",
        "excerpt": """There is nothing quite like the view of a mountain, 
        I was not ready for what happened!""",
        "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Deleniti aut tempora adipisci dignissimos voluptatem eveniet minima vero voluptates 
            eum delectus maiores veritatis repudiandae fugit 
            labore quidem eos, deserunt doloribus aliquid?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Deleniti aut tempora adipisci dignissimos voluptatem eveniet minima vero voluptates 
            eum delectus maiores veritatis repudiandae fugit 
            labore quidem eos, deserunt doloribus aliquid?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Deleniti aut tempora adipisci dignissimos voluptatem eveniet minima vero voluptates 
            eum delectus maiores veritatis repudiandae fugit 
            labore quidem eos, deserunt doloribus aliquid?
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Deleniti aut tempora adipisci dignissimos voluptatem eveniet minima vero voluptates 
            eum delectus maiores veritatis repudiandae fugit 
            labore quidem eos, deserunt doloribus aliquid?"""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Diego",
        "date": date(2024, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": """Did you ever spend hours searching that one error in your code?
          Yep - that's what happened to me yesterday...""",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Diego",
        "date": date(2024, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": """Nature is amazing! 
        The amount of inspiration I get when walking in nature is incredible!""",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def index(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_details(request, slug):
    desired_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": desired_post
    })
