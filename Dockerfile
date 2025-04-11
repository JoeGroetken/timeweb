FROM ubuntu:latest

# Install neccessary software for development
RUN apt-get update && apt-get install -y \
	vim curl git sudo gcc g++ \
	python3 python3-pip python3-venv python3-dev \
	build-essential libffi-dev libc-dev


#Setup a dev user that is not root
RUN useradd -m developer && echo "developer ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/developer

USER developer
WORKDIR /home/developer

# Git config
COPY .profile .profile
RUN echo "\n. .profile\n" >> .bashrc
RUN git clone https://github.com/JoeGroetken/timeweb
RUN (cd timeweb && make setup)


CMD ["/bin/bash"]
