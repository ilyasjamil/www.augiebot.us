FROM rasa/rasa-sdk:3.0.4

WORKDIR /app
COPY requirements.txt requirements.txt
USER root
RUN pip install --verbose -r requirements.txt
RUN apt-get update && apt-get install -y gnupg
RUN apt-get install -y wget xvfb unzip
ARG DEBIAN_FRONTEND=noninteractive
# RUN apt-get update && apt-get install -y gnupg
# RUN apt-get install -y wget xvfb unzip
# # Set up the Chrome PPA
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
# # Update the package list and install chrome
# RUN apt-get update -y
# RUN apt-get install -y google-chrome-stable
# # Set up Chromedriver Environment variables
# ENV CHROMEDRIVER_VERSION 2.19
# ENV CHROMEDRIVER_DIR /chromedriver
# RUN mkdir $CHROMEDRIVER_DIR
# # Download and install Chromedriver
# RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
# RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR
# # Put Chromedriver into the PATH
# ENV PATH $CHROMEDRIVER_DIR:$PATH
# EXPOSE 5055
# USER 1001

# # Adding trusting keys to apt for repositories
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# # Adding Google Chrome to the repositories
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# # Updating apt to see and install Google Chrome
# RUN apt-get -y update
# # Magic happens
# RUN apt-get install -y google-chrome-stable
# # Installing Unzip
# RUN apt-get install -yqq unzip
# # Download the Chrome Driver
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# # Unzip the Chrome Driver into /usr/local/bin directory
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

#approach 2

RUN apt-get update && \
    apt-get install -y gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    CHROME_VERSION=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION") && \
    wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

EXPOSE 5055
USER 1001