
# Multilang_site

It's a little django project in which I display in a single page a list of some posts. In addition, I translate all static elements of this web page in two languages : English and french. Despite, I haven't implemented a chatbot in my project even if I did some research.


## Tech Stack

**Tech:** python, html and CSS




## Step by step :

**Step 1 :** I started my project by creating a new django project named "Multilang_site" and a new application "main". Before That, I created a virtual environment. In this step, I had two folders. First, my virtual environment and the project folder. Inside the project folder, I had two other folders : main and multilang_site. Inside my main folder, I made two other folders : templates and static. That's, in this moment, all of my project's organization.

**Step 2 :** Next, I create my database in the models.py
```
class blog_article(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=6000)
    publication_date = models.DateField()
```
After that, I created my view in views.py but as I needed a template, I created an html file. Then I finally wrote my url in urls.py.
To see if every elements displayed on my web page, I decided to test my code in writing this command in my terminal :

```
py manage.Py runserver
```

Then, I saw all my elements.  First step is finished.

**Step 2 :** Now, it's one of the most difficult project's part because I never did it : translate all static elements of my site. First, I read django's doc, next I do some research on the web about internationalization. I saw little tuto so I tried to follow each steps but I saw in my terminal an error that my past didn't exist. I took 2 hours to resolve my error. After searching into website, forum and chat GPT but my path exists so I tried to use not my terminal in VS code but with my computer's terminal and it's worked. After that I copied the code founded in django's doc to translate my elements. Then I worked but it's a form and I want to have button. So I read and tried to understand the code. Next, I deleted the form and create button with href. After took some times to make button, and some hours more to create a correct style, I succeed. Then, I create elements in my database.

**Step 3 :** I started to do some research about LLM, chat bot and in particular, How can I implement a chat bot in a django's project. But at this moment, it's too late, and too complex to start now. So I do some finition about this project like the readme and depoyement.
## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    