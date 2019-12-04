git fetch &&
git checkout master &&
git pull &&
source .env/bin/activate &&
pip install -r requirements.txt &&
printf "killing old server processes\n" &&
sudo ./kill_old_server.sh &&
sudo ./.env/bin/gunicorn -b 0.0.0.0:443 --certfile /etc/letsencrypt/live/tradespace.store/fullchain.pem --keyfile /etc/letsencrypt/live/tradespace.store/privkey.pem wsgi --daemon &&
printf "deploy successful!\n"
