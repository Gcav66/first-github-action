FROM python:3.8.15
RUN git clone https://github.com/Gcav66/first-github-action.git
WORKDIR /first-github-action
RUN pip install -r requirements.txt
#RUN python app.py
EXPOSE 5000
CMD ["python", "app.py"]
