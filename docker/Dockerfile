# FROM debian:jessie

# RUN \
#    echo "===> add webupd8 repository..."  && \
#    echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee /etc/apt/sources.list.d/webupd8team-java.list  && \
#    echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  && \
#    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  && \
#    apt-get update  && \
#    \
#    \
#    echo "===> install Java"  && \
#    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
#    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
#    DEBIAN_FRONTEND=noninteractive  apt-get install -y --force-yes oracle-java8-installer oracle-java8-set-default

# The above is the original version, but the Oracle Java installation doesn't seem to work anymore.  The container cloned below has Java
# pre-installed.  The full JDK (as opposed to the JRE) isn't necessary, but this is the easiest way to get things up and running.


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
    mv DSC180A_Replication-${branch} autophrase_dsc180

##### Preparing resources #####
RUN \
    echo "===> downloading resources" &&\
    cd autophrase_dsc180 && bash resources.sh

##### Compiling #####
RUN \
    for entry in "./*"
    do
      echo "$entry"
    done
    echo "===> compile" &&\
    bash compile.sh &&\
    chmod 755 resources/AutoPhrase/tools/treetagger/bin/tree-tagger && \
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
