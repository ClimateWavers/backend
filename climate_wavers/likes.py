# likes.py

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@async_to_sync
async def send_like_notification(user_id, post_id):
    # Logic to send a like notification to the user with ID user_id
    # Usage
    notification_message = {
        'type': 'post_like_notification',
        'message': f'Your post (ID: {post_id}) has been liked by another user.',
    }
    user_channel_name = f"user_{user_id}"
    await channel_layer.send(user_channel_name, notification_message)

