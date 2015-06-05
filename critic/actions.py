"""
Actions of the `critic` app
"""

from django.core.mail import mail_admins

from critic import signals


def create_app_links():
    """
    Creates links of the `critic` app
    """
    signals.app_link_ready.send(
        sender=None,  # not specified
        base_pattern=r'^critic/',
        url_name='critic:review',
        text='Go to Review form'
    )
    # Inner navigation
    signals.sub_link_ready.send(
        sender=None,  # not specified
        url_name='critic:review',
        text='Back to Review form',
        alias='critic_review'
    )
    signals.sub_button_ready.send(
        sender=None,  # not specified
        button_type='submit',
        text='Send',
        alias='critic_send'
    )


def send_review(book_name, review_text):
    """
    Sends an email with review for a specified book
    """
    if book_name and review_text:
        mail_admins(
            subject='Book "{0}" was reviewed'.format(book_name),
            message='{0}\n---\n{1}\n'.format(book_name, review_text)
        )
    else:
        # TODO: Add logging for this case
        print("Book and/or text of review aren't specified")
