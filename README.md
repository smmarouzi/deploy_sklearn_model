bash deploy.sh

docker exec -it sonova-api pytest --ignore=tests/ --cov=app tests/ --cov-config=.coveragerc
