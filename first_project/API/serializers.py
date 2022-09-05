from rest_framework import serializers
from blog.models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date_posted'] = instance.date_posted.strftime('%d-%m-%Y %H:%M:%S')

        return representation
