FROM ubuntu:xenial

# Install os level dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git-core \
    perlbrew \
    python2.7 \
    python-pip \
    python-tk

RUN pip install --upgrade pip

# Install python dependencies for python 2.7
RUN python2.7 -m pip install numpy biopython
RUN python2.7 -m pip install qiime

# uclust is a dependency of qiime
RUN curl http://www.drive5.com/uclust/uclustq1.2.22_i86linux64 > uclustq1.2.22_i86linux64
RUN ln -s uclustq1.2.22_i86linux64 /usr/bin/uclust

# Install cpanm to install perl dependencies
RUN perlbrew install-cpanm

# Install perl dependencies
RUN /root/perl5/perlbrew/bin/cpanm Bio::Perl