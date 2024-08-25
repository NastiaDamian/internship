from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "my-new-experience",
        "image": "IT.jpg",
        "author": "Nastia",
        "date": date(2023, 8, 12),
        "title": "New Experience",
        "excerpt": """Experience is the accumulation of knowledge, skills, and impressions gained through life or 
        professional
         activities. It is an integral part of personal development, shaping one's 
         worldview and professional competence.""",
        "content": """Experience is a valuable teacher that shapes our understanding and skills over time. Through
         various
            encounters and challenges, we gain insights that no textbook can provide. Each experience, whether positive
            or negative, contributes to our growth and helps us navigate future situations with greater wisdom.
            Embracing new experiences allows us to adapt, learn, and evolve, making us more resilient and insightful
            individuals.
            
            Experience is a valuable teacher that shapes our understanding and skills over time. Through various
            encounters and challenges, we gain insights that no textbook can provide. Each experience, whether positive
            or negative, contributes to our growth and helps us navigate future situations with greater wisdom.
            Embracing new experiences allows us to adapt, learn, and evolve, making us more resilient and insightful
            individuals.
            
            Experience is a valuable teacher that shapes our understanding and skills over time. Through various
            encounters and challenges, we gain insights that no textbook can provide. Each experience, whether positive
            or negative, contributes to our growth and helps us navigate future situations with greater wisdom.
            Embracing new experiences allows us to adapt, learn, and evolve, making us more resilient and insightful
            individuals."""
    },
    {
        "slug": "programming-is-fun",
        "image": "computer.jpg",
        "author": "Nastia",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what"
                   " happened to me yesterday...",
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
        "image": "girl.jpg",
        "author": "Nastia",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
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


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-post.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
