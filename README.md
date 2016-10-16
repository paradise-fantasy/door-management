#### Door Unlocker

## How to run
'python unlock.py'

## Renewal of SSL certificate
Added crontab to renew SSL certificate when close to experation date:

'16 06,22 * * * /home/<user>/letsencrypt/certbot-auto renew'
