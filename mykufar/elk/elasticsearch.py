# from elasticsearch import Elasticsearch
# from django_elasticsearch_dsl import Index, Document, Text, Keyword, Integer
#
# from .documents import UserDocument, CategoryDocument, ItemDocument
#
# es = Elasticsearch(['elasticsearch:9200'])
#
# users_index = Index('users')
# users_index.document(UserDocument)
# users_index.create(using=es)
#
# categories_index = Index('categories')
# categories_index.document(CategoryDocument)
# categories_index.create(using=es)
#
# items_index = Index('items')
# items_index.document(ItemDocument)
# items_index.create(using=es)