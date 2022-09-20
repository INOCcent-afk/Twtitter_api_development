from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    i_follow = serializers.SerializerMethodField(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)
    following = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'email', 'username',
            'nickname', 'password',
            'bio',
            'date_joined',
            'followers', 'following', 'i_follow'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_followers(self, obj):
        return obj.followed.count()

    def get_following(self, obj):
        return obj.following.count()

    def get_i_follow(self, obj):
        current_user = self.context.get('request').user
        return True if current_user in obj.followed.all() else False

    def validate(self, data):
        if len(data.get("password")) <= 6:
            raise serializers.ValidationError(
                {'error': 'Passwords must be larger than 6 letters !'})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
