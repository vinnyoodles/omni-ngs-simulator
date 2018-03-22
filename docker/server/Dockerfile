FROM ubuntu:xenial

# Install os level dependencies
RUN apt-get update && apt-get install -y \
    libz-dev \
    curl \
    wget \
    git-core \
    perlbrew \
    python2.7 \
    python-pip \
    python-tk

WORKDIR /app

# Install python dependencies for python 2.7
# NOTE: Running two commands of pip install because of an issue with "cogent" module
COPY . /app
RUN python2.7 -m pip install -r /app/requirements.txt
    # python2.7 -m pip install numpy && \
    # python2.7 -m pip install -r /app/requirements.txt

# uclust is a dependency of qiime
# RUN curl http://www.drive5.com/uclust/uclustq1.2.22_i86linux64 > uclustq1.2.22_i86linux64 && \
#     ln -s uclustq1.2.22_i86linux64 /usr/bin/uclust

# # Install perl dependencies
# RUN perlbrew install-cpanm && /root/perl5/perlbrew/bin/cpanm Bio::Perl

# RUN git clone https://github.com/MG-RAST/DRISEE.git

# COPY dependencies/cdbfasta.tar.gz /home/cdbfasta.tar.gz
# RUN tar -xvf /home/cdbfasta.tar.gz && \
#     make -C /cdbfasta && \
#     ln -s /cdbfasta/cdbfasta /usr/bin/cdbfasta && \
#     ln -s /cdbfasta/cdbyank /usr/bin/cdbyank

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--reload"]