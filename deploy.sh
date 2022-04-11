docker build -t sonova-test-app:new .
docker run -d -p 8080:8080 --name sonova-api sonova-test-app:new