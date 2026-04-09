1 sudo systemctl start redis запустить бд
2 uvicorn main:app --reload для запуска бекенда и базы данных
3 открываем index.html

chmod +666 sudo chmod 666 /var/run/docker.sock
docker build -t todo app . запустить сборку
docker run -d -p 8000:8000 --name todo-container todo-app запуск


