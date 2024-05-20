conda create -n ChatDev_conda_env python=3.9 -y
conda activate ChatDev_conda_env

cd ChatDev
pip3 install -r requirements.txt

set OPENAI_API_KEY=key

$env:OPENAI_API_KEY="key"

python run.py --task "make a trading bot for forex" --name "trading-bot"

python run.py --task "make a tiktok toe game" --name "tiktok toe game"

python run.py --task "make a weather app" --name "weather-app2"


python3 run.py --task "describe your modification or query here" --config "Human"

python run.py --task "change color of submit button to red" --config "incremental" --path ".\WareHouse\BMI Calculator_DefaultOrganization_20230918110521"


docker run -it -p 8000:8000 -e OPENAI_API_KEY=key chatdev:latest

docker build -t chatdev:latest .

docker run -it -p 8000:8000 -e OPENAI_API_KEY=YOUR_OPENAI_KEY  chatdev:latest

docker run -it -p 8000:8000 -e OPENAI_API_KEY=key chatdev:latest


python run.py --task "make a messaging app" --name "messaging app"


docker exec chatdev-main-app-1 ls /app

docker exec chatdev-main-app-1 python --version


to run in detuched mode
docker exec -d chatdev-main-app-1 python run.py --task "make a weather app" --name "weather-app2"

to run directly
docker exec chatdev-main-app-1 python run.py --task "make a kids game app" --name "kids-game-app2"



docker exec -d chatdev-main-app-1 python run.py --task "make a weather app" --name "weather-app2" > /app/logs/weather-app.log 2>&1


working------ make container up
docker compose up -d

working------ enter the container
docker exec -it chatdev-main-app-1 bash

working------ test log command
docker exec -d chatdev-main-app-1 python run.py --task "ls -al" > /app/logs/weather-app.log 2>&1

working------ to setup log folder
docker exec chatdev_container sh -c 'mkdir -p /app/logs && chmod 777 /app/logs'

working------ to create a project
docker exec -d chatdev_container sh -c 'mkdir -p /app/logs && python run.py --task "make a kids game app" --name "kids-game-app2" > /app/logs/kids-game-app2.log 2>&1'

working------ to update a project
docker exec -d chatdev_container sh -c 'mkdir -p /app/logs && python run.py --task "change color of submit button to red" --config "incremental" --path "./WareHouse/BMI Calculator_DefaultOrganization_20230918110521" > /app/logs/task-output.log 2>&1'


docker exec -d chatdev-main-app-1 sh -c 'mkdir -p /app/logs && ls -al > /app/logs/output.log 2>&1'


