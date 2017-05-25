# -*- coding:utf-8 -*-

import datetime
from haystack import indexes
from shareapp.models import article


class articleIndex(indexes.SearchIndex, indexes.Indexable):
    articleid = indexes.IntegerField(model_attr='articleid')
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')


    def get_model(self):
        return article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()