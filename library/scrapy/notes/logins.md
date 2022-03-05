# logins
option 1)
get csrf value from network tab after a login attempt
from scrapy import FormRequest
csrf_token = response.xpath("//*[@name='csrf_token']/@value").get()
yield FormRequest.from_response(response, formdata, callback)

option 2)
look for form inputs and populate formdata from there (essentially consolidates the two steps from option 1 into 1 step)

option 3) 
use def start_requests and return the populated FormRequest object

