FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

WORKDIR /pythoncode

COPY nesting4_pizza.py/ .

CMD [ "python3" , "./nesting4_pizza.py" ]
