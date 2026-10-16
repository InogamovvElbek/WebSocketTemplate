from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from apps.models import Category
from apps.serializers import CategoryModelSerializer


@receiver(post_save, sender=Category)
def order_saved(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    categories = Category.objects.all()
    data = CategoryModelSerializer(instance=categories , many=True).data
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "notify_message",  # -> maps to notify_message() in consumer
            "message": data,
        },
    )


