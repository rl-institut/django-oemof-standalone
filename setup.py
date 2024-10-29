def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'django_oemof',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'dos',
                'USER': 'dosuser',
                'PASSWORD': 'dosdos',
                'HOST': '127.0.0.1',
                'PORT': '5432',
            }
        },
        MEDIA_ROOT="media",
    )
    django.setup()
