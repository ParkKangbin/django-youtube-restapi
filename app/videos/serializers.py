from rest_framework.serializers import ModelSerializer
from .models import Video
from users.serializers import UserInfoSerializer
from reactions.models import Reaction
from rest_framework import serializers

class VideoListSerializers(ModelSerializer):
    user = UserInfoSerializer(read_only=True)
    class Meta:
        model = Video
        fields = '__all__'

        # depth = 1

from comments.serializers import CommentSerializer
class VideoDetailSerializer(ModelSerializer):
    user = UserInfoSerializer(read_only=True)

    comment_set = CommentSerializer(many=True, read_only=True)

    reaction = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'

    def get_reaction(self, video):
        return Reaction.get_video_reactions(video) 