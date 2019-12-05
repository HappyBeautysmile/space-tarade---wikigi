cd ~/TradeSpace/tradespace_backend &&
git fetch &&
git checkout master &&
git pull &&
source .env/bin/activate &&
pip install -r requirements.txt &&
printf "killing old server processes\n" &&
sudo ./kill_old_server.sh &&
sudo ./.env/bin/gunicorn \
    --bind 0.0.0.0:443 /
    --certfile /etc/letsencrypt/live/tradespace.store/fullchain.pem /
    --keyfile /etc/letsencrypt/live/tradespace.store/privkey.pem /
    --access-logfile instance/gunicorn-access.log
    --error-logfile instance/gunicorn-error.log
    wsgi /
    --daemon &&
printf "deploy successful!\n"
