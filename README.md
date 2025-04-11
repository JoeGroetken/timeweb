To run timeweb within its docker container, follow these instructions 
1. Download "Dockerfile" and ".profile" and place it in the folder you would like to run the container from
2. Run the command "docker build -t joegroetken/timeweb ."
3. Then run the command "docker run -it --rm -e GITHUB_USER=[ReplaceWithYourUsername] -e GITHUB_EMAIL=[ReplaceWithYourEmail] joegroetken/timeweb", replacing the bracketed values with your username and email
4. cd into the timeweb folder
5. use the make run command
6. This should now work (It doesn't and shouldn't)
