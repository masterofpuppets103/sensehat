import web
import sys
from sense_hat import SenseHat  

sense = SenseHat()

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
		temp =  float("{0:.2f}".format(sense.get_temperature()))
		humin = sense.get_humidity()
		pressure = sense.get_pressure()
		greeting = "Temperatur: %d\nLuftfeuchtigkeit: %d \nLuftdruck: %d" % (temp, humin, pressure) 	
	        return greeting

if __name__ == "__main__":
    app.run()


