# Static file in Django

How do you "serve" files like images,videos,css and javascript?

- [Docs] (https://docs.djangoproject.com/en/3.0/howto/static-files/)
- [Django Storage](https://django-storage.readthedocs.io/en/latest/)

1.self -Hosted
   - Static Files Server (your own via NGINX not Django)
   - Whitenoise (on Heroku; not-recommended)
   - AWS S3 / Google Cloud Storage

2. CDN
   - Use Public cdn files
   - Create our own CDN
      - AWS cloudfront
      - Google Cloud CDN
      - CloudFlare
      - Stackpath   