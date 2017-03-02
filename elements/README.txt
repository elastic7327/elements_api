
_____ _                           _
| ____| | ___ _ __ ___   ___ _ __ | |_ ___
|  _| | |/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
| |___| |  __/ | | | | |  __/ | | | |_\__ \
|_____|_|\___|_| |_| |_|\___|_| |_|\__|___/


____  _____ ____ _____ __       _      _    ____ ___
|  _ \| ____/ ___|_   _/ _|_   _| |    / \  |  _ \_ _|
| |_) |  _| \___ \ | || |_| | | | |   / _ \ | |_) | |
|  _ <| |___ ___) || ||  _| |_| | |  / ___ \|  __/| |
|_| \_\_____|____/ |_||_|  \__,_|_| /_/   \_\_|  |___|




1.Requirements can be divided into three parts

>base.txt  =>  development.txt  >>  prodution.txt
>    |—————————|
>    | ——————————————————|  -   -   -  -  - - |
>    | ———————————————————————----------————— |







2 .django module setting can be divided into four parts

>base.py >>   development.py   >> testing.py >> prodution.py
>    |—————————|
>    | ——————————————————|  -   -     - |
>    | ——————————————————|--------------|-------------------- |
>    | ———————————————————————————--------------------------— |





3.how to approach
>I have focused on managing user's own csv files in any environment by putting them on a server(with RESTful CURD).
>and focuses on reading and writing the csv file.
>It looks like it's very similar to the IT support project that I've worked on to help other teams in the past.
>Users can transfer the csv file to the server several times.
>The server automatically reads and re-organizes (RDMBS way) the file and shows it to the user(with RESTful CURD).
>It also informs to user that there is a problem with the file user sent to server .
>Pass the header issue, or file extension problems, of the csv file.
>To help with the understanding of the front-end development,
I chose django-restframework and django-rest-swagger.
>The reason why I use those two framework is because it can be developed fast and I can reduce the number of code.
>n particular, I focuses on reading and writing the csv file.
>I used pandas package to read and write cvs files, and ORM_bulk_insert
>Users won't use mobile application to move large volumes of csv files [almost 50M ~ ]
>this time No asynchronous use ..
>If the user uploads large csv file frequently ....I will use rabbitmq & celery, To prevent requests time-out

4.how it works
>Users can upload a csv to the server via a particular url.
>Once you have uploaded the csv file, you must check the archived and error messages at the csvs table
>If archived is true, then the corresponding csv file will be generated and saved to the contents table (if there is no problem).
>(Of course, all of the data on the content model can be accessed from a specific url (RESTful CURD).)
>If the error_status is zero(0), it is normal.(you can check error_status on csvs table)
>elif the status is 100, it is csv fileformat or extension error.
>else the status is 200, it is csv header error.
>when storing the contents objects in an RDB , the performance was raised using bulk_insert(please check csv__to_db.py

>Through uwsgi and nginx, we will create a large number of cluster and allow them to serve in AWS
>and Please check /elements/settins/config


After finishing.....
>
>the approach to the problem is, suppose to be with . . .
>with the meetings, the project managers, the collaborators and the colleagues of the faculty.
>We have to decide after discussion.
>and also I believe that good code is not something that is made from individual skills, but it is made by collaborating with others.
>It believes that the code is becoming more beautiful and more powerful through review.
>That's why I like code-reviews.
>I'm very quick to learn something new, to be humble, to respect others python-code.
>
>Lastly, thank you for giving me a good chance.
>
>-Daniel Kim-
