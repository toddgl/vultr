# .env

# Environment setting to determine which setty configurations to use
PROJECT_ENVIRONMENT='prod'

# Should robots.txt allow everything to be crawled?
ALLOW_ROBOTS=False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY='{{ django_secret_key }}'

# Database connection: keep the database connection credentials used in production secret!
DATABASE_NAME='fairsystem_db'
DATABASE_USER='admin'
DATABASE_PASS='{{ database_password }}'

# A list of all the people who get code error notifications.
ADMIN_LIST="[('Glenn Todd', 'g.todd@internet.co.nz')]"

# A list of all the people who should get broken link notifications.
MANAGERS="Glenn Todd <g.todd@internet.co.nz"

# By default, Django will send system email from root@localhost.
# However, some mail providers reject all email from this address.
SERVER_EMAIL='convener@martinboroughfair.org.nz'

# Stripe setup Test
STRIPE_PUBLISHABLE_KEY_TEST='{{ stripe_publishable_key_test }}'
STRIPE_SECRET_KEY_TEST= '{{ stripe_secret_key_test }}'
STRIPE_WEBHOOK_SECRET_TEST= '{{stripe_webhook_secret_test }}'

# Stripe setup Production
STRIPE_PUBLISHABLE_KEY= '{{ stripe_publishable_key }}'
STRIPE_SECRET_KEY= '{{ stripe_secret_key }}'
STRIPE_WEBHOOK_SECRET= '{{ stripe_webhook_secret }}'

# Mailgun setup Production
MAILGUN_API_KEY='{{ mailgun_api_key }}'
