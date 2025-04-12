To run timeweb within its docker container, follow these instructions 
1. Download "Dockerfile" and ".profile" and place it in the folder you would like to run the container from
2. Run the command "docker pull joegroetken/timeweb"
3. Run the command "docker build -t joegroetken/timeweb ."
4. Then run the command "docker run -it --rm --name [ReplaceWithContainerName] -dp [RealPort]:[DockerPort] -e GITHUB_USER=[ReplaceWithYourUsername] -e GITHUB_EMAIL=[ReplaceWithYourEmail] -e GITHUB_TOKEN=[YourGithubToken] joegroetken/timeweb", replacing the bracketed values with the information you want there
5. Run the command "docker exec -it [ContainerName] bash", replacing the brackets with the container name
6. cd into the timeweb folder
7. use the "make run" command
8. Open a your browser and input your ip address (or local host, which is 127.0.0.1) and the port number into your browser, such as "http:127.0.0.1:5000"

Now You can tell the time without having to look down at your watch.
