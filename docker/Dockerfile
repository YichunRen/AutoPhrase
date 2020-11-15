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
    apt-get update && apt-get install -y --force-yes make curl perl

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
    echo "===> downloading resources" &&\
    cd /autophrase && bash resources.sh

##### Compiling #####
RUN \
    echo "===> compile" &&\
    cd /autophrase && bash compile.sh &&\
    chmod 755 tools/treetagger/bin/tree-tagger && \
    mv data default_data && \
    mv models default_models

##### Cleaning up #####
RUN \
    echo "===> clean up..."  && \
    apt-get purge -y --force-yes make && \
    apt-get autoremove -y --purge make && \
    rm -rf /var/cache/oracle-jdk8-installer  && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV COMPILE 0

WORKDIR /autophrase_dsc180
