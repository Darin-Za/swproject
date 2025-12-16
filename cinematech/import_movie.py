import pandas as pd
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinematech.settings")
django.setup()

from movie.models import Movie

df = pd.read_excel("movies.xlsx")
df['release_year'] = pd.to_datetime(df['release_year']).dt.date

for _, row in df.iterrows():
    Movie.objects.create(
        title=row['title'],
        description=row['Description'],
        release_year = row['release_year'].year,
        rating=row['Rating'],
        poster=f"poster/{row['  Posters']}"
    )

