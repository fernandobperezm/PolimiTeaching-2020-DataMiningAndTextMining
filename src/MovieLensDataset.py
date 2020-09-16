import pandas as pd
import numpy as np


class MovieLensDataset(object):
    def __init__(self):

        ratings: pd.DataFrame = pd.read_csv(filepath_or_buffer="./data/ml-100k",
                                            sep="|",
                                            names=["user_id", "item_id", "rating", ],
                                            )

    def item(self):
        """
        Information about the items (movies); this is a tab separated
          list of
          movie id | movie title | release date | video release date |
          IMDb URL | unknown | Action | Adventure | Animation |
          Children's | Comedy | Crime | Documentary | Drama | Fantasy |
          Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
          Thriller | War | Western |
          The last 19 fields are the genres, a 1 indicates the movie
          is of that genre, a 0 indicates it is not; movies can be in
          several genres at once.
          The movie ids are the ones used in the u.data data set.

        :return:
        """
        self.items