from botocore.exceptions import ClientError
from sns.notifications.notification import Notification
from typing import Set

import boto3
import json
import logging

logger = logging.getLogger(__name__)


class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self):
        self.client = boto3.client('sns')

    def publish_notification(
            self,
            target_arn: str,
            notification: Notification,
            default: str = '',
            providers: Set[str] = None):
        """Publishes a push notification, to a target.

        Parameters
        ----------
        target_arn
            The target ARN

        notification
            The notification to be published
            
        default
            The default message to be used if a message is not present for one of the notification platforms
            
        providers
            Set of providers for which specific message should be generated
        """
        if not providers:
            providers = ['GCM', 'APNS', 'APNS_SANDBOX']

        message = {
            'default': default
        }

        for provider in providers:
            provider_config = getattr(notification, provider.lower(), None)

            if not provider_config:
                logger.exception(f'Unable to construct message for {provider} provider.')
                raise

            message[provider] = json.dumps(provider_config)

        try:
            self.client.publish(
                TargetArn=target_arn,
                MessageStructure='json',
                Message=json.dumps(message),
                MessageAttributes={
                    'AWS.SNS.MOBILE.APNS.TTL': {
                        'DataType': 'String',
                        'StringValue': str(notification.ttl),
                    },
                    'AWS.SNS.MOBILE.APNS_SANDBOX.TTL': {
                        'DataType': 'String',
                        'StringValue': str(notification.ttl),
                    },
                    'AWS.SNS.MOBILE.GCM.TTL': {
                        'DataType': 'String',
                        'StringValue': str(notification.ttl),
                    },
                }
            )
        except ClientError:
            logger.exception(f'Unable to publish message to target {target_arn}.')
            raise
        else:
            return
        # try:
        #     att_dict = {}
        #     for key, value in attributes.items():
        #         if isinstance(value, str):
        #             att_dict[key] = {'DataType': 'String', 'StringValue': value}
        #         elif isinstance(value, bytes):
        #             att_dict[key] = {'DataType': 'Binary', 'BinaryValue': value}
        #     response = topic.publish(Message=message, MessageAttributes=att_dict)
        #     message_id = response['MessageId']
        #     logger.info(
        #         "Published message with attributes %s to topic %s.", attributes,
        #         topic.arn)
        # except ClientError:
        #     logger.exception("Couldn't publish message to topic %s.", topic.arn)
        #     raise
        # else:
        #     return
