FROM openjdk:8

MAINTAINER Joey Hou <z9hou@ucsd.edu>

RUN \
    echo "===> install g++" && \
    apt-get update && apt-get install -y --force-yes g++

RUN \
    echo "===> install vim" && \
    apt-get update && apt-get install vim -y --force-yes

RUN \
    echo "===> install make, curl, perl" && \
    apt-get update && apt-get install -y --force-yes make curl perl python3-pip

RUN \
    echo "===> install python packages" && \
    pip3 install pandas numpy seaborn scipy tqdm matplotlib

ARG repo
ARG branch
ADD "${repo}/archive/${branch}.zip" /

##### Unziping project file from github #####
RUN \
    unzip ${branch} && \
    rm ${branch}.zip && \
    mv DSC180A_Replication-${branch} autophrase

##### Preparing resources #####
RUN \
    echo "===> downloading resources..." &&\
    bash /autophrase/src/setup/docker_resources.sh &&\
    chmod 755 /autophrase/src/setup/*.sh

##### Compiling #####
#RUN \
#    echo "===> compile" &&\
#    cp /autophrase/src/setup/compile.sh /autophrase/ &&\
#    cp /autophrase/resources/Makefile /autophrase/ &&\
#    bash /autophrase/compile.sh &&\
#    chmod 755 tools/treetagger/bin/tree-tagger


##### Cleaning up #####
RUN \
    echo "===> clean up..."  && \
    apt-get purge -y --force-yes make && \
    apt-get autoremove -y --purge make && \
    rm -rf /var/cache/oracle-jdk8-installer  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV COMPILE 0

WORKDIR /autophrase
