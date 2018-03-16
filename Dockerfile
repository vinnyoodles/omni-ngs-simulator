FROM ubuntu:xenial

# Install os level dependencies
RUN apt-get update && apt-get install -y \
    libz-dev \
    curl \
    git-core \
    perlbrew \
    python2.7 \
    python-pip \
    python-tk


# Install python dependencies for python 2.7
# NOTE: Running two commands of pip install because of an issue with "cogent" module
COPY requirements.txt /home/requirements.txt
RUN pip install --upgrade pip && \
    python2.7 -m pip install numpy && \
    python2.7 -m pip install -r /home/requirements.txt

# uclust is a dependency of qiime
RUN curl http://www.drive5.com/uclust/uclustq1.2.22_i86linux64 > uclustq1.2.22_i86linux64 && \
    ln -s uclustq1.2.22_i86linux64 /usr/bin/uclust

# Install perl dependencies
RUN perlbrew install-cpanm && /root/perl5/perlbrew/bin/cpanm Bio::Perl

RUN git clone https://github.com/MG-RAST/DRISEE.git
ENV PATH="${PATH}:/DRISEE"

COPY dependencies/cdbfasta.tar.gz /home/cdbfasta.tar.gz
RUN tar -xvf /home/cdbfasta.tar.gz && \
    make -C /cdbfasta && \
    ln -s /cdbfasta/cdbfasta /usr/bin/cdbfasta