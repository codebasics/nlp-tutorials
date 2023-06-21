from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import random
import ssl
import uvicorn

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']

    intent_handler_dict = {
        'course.price': handle_course_price,
        'eligibility.age': handle_eligibiliy_age,
        'eligibility.background': handle_eligibility_background
    }

    return intent_handler_dict[intent](parameters)


def handle_course_price(parameters: dict):
    course_name = parameters["course-name"]
    country = parameters["geo-country"]

    price_dict = {
        "SQL": 900,
        "Power BI": 2400,
        "Python": 800,
        "Excel": 700,
        "Data Analytics Bootcamp": 4800
    }

    course_price = price_dict.get(course_name)

    response = {
        "fulfillmentText": f"The course price for {course_name} is : {course_price}"
    }

    return JSONResponse(content=response)

def handle_eligibiliy_age(parameters: dict):
    course_name = parameters["course-name"]
    age = parameters["age"]["amount"]

    if age>30:
        answer = random.choice([
            '''There are many folks who have learned necessary data analyst skills at a later age
            and successfully transitioned into a data analyst role. I know one person who made this transition
            at the age of 51 and his past background was physical therapist. I've a video on my YouTube channel 
            that has few such stories highlighted, please watch that to get 
            some tips: https://www.youtube.com/watch?v=nkvInnpuic8 
            In short: we believe it is possible to learn data analytics at this age 
            ''',
            '''
            Hey, It is a common perception that at a later age it is hard to learn new things and switch your career 
            but to be honest I personally know many folks who learned data analytics, data science at 40+ age and made 
            this transition. One other person I know was a physical therapist till age 51 and now he is a data 
            analyst working in a healthcare company. Watch this video to know about few such 
            stories: https://www.youtube.com/watch?v=nkvInnpuic8
            In short, it is 100% possible, if you have an eagerness to learn and a commitment 
            towards making this career switch. 
            Also one great thing about data analyst career is it requires very less coding so it will not 
            be very difficult for you! So yes, you can learn data analysis at your age.
            '''
        ])

    else:
        answer ="Your age is less than 30 and you are too young to learn anything. Just do it my friend."

    if course_name:
        answer += " And yes you are eligible for " + "".join(course_name)

    return JSONResponse(content={
        "fulfillmentText": answer
    })


def handle_eligibility_background(parameters: dict):
    course_name = parameters["course-name"]
    background = parameters["degree-or-situation"]

    if background:
        if background == "Mechanical Engineer":
            answer = '''I know many Mechanical Engineers who have successfully become data analysts. Watch these videos 
            for these success stories: (1) https://www.youtube.com/watch?v=4BLxapDqrlA (2) https://www.youtube.com/watch?v=yKB6EUbGamo
            Transition from mechanical engineering to data analyst is definitely possible. You need to learn necessary skills
            such as Excel, Power BI, SQL etc.  
            '''
        elif background == "B.COM":
            answer = '''There are many B.COM graduates who have transitioned into data analytics industry. For example watch 
            Suryanshu's story here: https://www.youtube.com/watch?v=in3IB45YEgY
            or How Hitesh is now working at Accenture with B.Com background: https://www.youtube.com/watch?v=lqEzYDuTnvU
            Let your past not define what you can do in the future. The transition is definitely possible.
            '''
        elif background == "HR":
            answer = '''If you are an HR trying to transition to data industry then I would suggest you leverage your past
            experience. Meaning you already know HR domain, now you can learn necessary skills such as SQL, Excel, Power BI
            and become an HR data analyst. This person Ankur Sharma was an HR and now he is working as a people analyst 
            in an MNC: https://www.linkedin.com/in/ankur-sharma-b57266185/
            '''
        else:
            answer = '''There are many folks who have breaked into a data analyst career despite irrelavant degree, 
            work experience or an older age. So the transition to data analyst career, no matter what your past background
            is possible for sure. Here is the playlist link with all such amazing transition stories to get some motivation:
            https://www.youtube.com/playlist?list=PLeo1K3hjS3us2Ko99XX9V5phkf5_2CJpQ
            If they can do it, you can do it too. 
            '''
        if course_name:
            answer += " And yes you are eligible for " + "".join(course_name)
    else:
        answer = f"To understand if you are eligible for {course_name} or not, you can take this survey. It will" \
                 f"tell you if you have natural abilities in the field of data analytics or not. Survey link: https://codebasics.io/find-your-match-da"

    response = {
        "fulfillmentText": answer
    }

    return JSONResponse(content=response)
