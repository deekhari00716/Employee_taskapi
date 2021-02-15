# Employee_taskapi
# To signup:
curl -X "POST" http://127.0.0.1:8000/api/signup/ -H 'Content-Type: application/json' -d '{"username":"<username>","password":"<password>"}'

# To login:
curl -X "POST" http://127.0.0.1:8000/api/login/ -H 'Content-Type: application/json' -d '{"username":"<username>","password":"<password>"}'
