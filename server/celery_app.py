from celery import Celery
from celery.schedules import crontab
from server.app import create_app
from server.config import Config



def make_celery(app):
    """Factory function to create a Celery instance."""
    celery = Celery(
        app.import_name,
        backend=Config.CELERY_RESULT_BACKEND,
        broker=Config.CELERY_BROKER_URL,
    )
    celery.conf.update(app.config)
    celery.autodiscover_tasks(['server.tasks'])  # Ensure tasks are discovered automatically
    return celery


# Create Flask app and initialize Celery
app = create_app()
celery = make_celery(app)

celery.autodiscover_tasks(['server.tasks'])

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """Configure periodic tasks using Celery beat."""
    # Task: Fetch stock data for 'AAPL' every 5 minutes
    sender.add_periodic_task(
        crontab(minute='*/5'),  # Every 5 minutes
        fetch_stock_data_task.s('AAPL'),
        name='Fetch AAPL stock data every 5 minutes'
    )

    # Task: Fetch Arxiv papers for a sample author daily at midnight
    sender.add_periodic_task(
        crontab(hour=0, minute=0),  # Midnight daily
        fetch_arxiv_data_task.s('John Doe'),
        name='Fetch papers for John Doe daily'
    )


# Add any additional periodic tasks below as needed