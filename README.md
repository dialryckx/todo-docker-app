FullStack application with Frontend(HTML/JS), Backend(FastAPI, Redis), Containerization Docker. 
This project is made for the purpose of developing containerization skills.
#### Requirements:
You need to have Docker on your PC. If you use Linux, be sure that you have permission to use docker's commands (or just use "sudo")
### For installing application:
1. `git clone https://github.com/dialryckx/todo-docker-app`
2. `cd todo-docker-app/`
#### For launch the application:
##### 1 Build an image:
In your terminal open the directory with the application and enter the command:
``` bash
docker build -t todo-app .
```
##### 2 Launching container:
Launch the image:
``` bash
docker run -d -p 8000:8000 --name my-todo-app todo-app
```
##### 3 Using:
Open your browser and go to:
`http://localhost:8000`

### Helpful commands
##### Stop the application:
``` bash
docker stop my-todo-app
```

##### Remove container:
``` bash
docker rm -f my-todo-app
```

##### View the logs (if something doesnt work)
``` bash
docker logs my-todo-app
```




