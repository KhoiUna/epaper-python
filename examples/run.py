#!/usr/bin/python
# -*- coding:utf-8 -*-
from waveshare_epd import epd7in5_V2
import sys
import time
import requests
import datetime
import logging
from PIL import Image, ImageDraw, ImageFont
from canvas import get_assignments
import os
picdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(
    os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)


logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()

    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    medium = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    title = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 28)

    logging.info("Displaying data...")
    Display = Image.new('1', (epd.width, epd.height), 255)
    qr = Image.open(os.path.join(picdir, 'qr.bmp'))
    logo = Image.open(os.path.join(picdir, 'logo.bmp'))

    # Header
    draw = ImageDraw.Draw(Display)
    draw.text(
        (10, 0), 'Information Systems in Organizations: CIS-236-01', font=title, fill=0)
    draw.text((10, 50), 'Professor J. Matt Colburn | Office hours: Today - by appointment',
              font=medium, fill=0)
    draw.text((10, 80), 'Email: jmcolburn@una.edu  |  Phone number: (256)-765-4955',
              font=font18, fill=0)
    draw.text((10, 110), 'Class starts: 8h  -  Class ends: 9h45 ',
              font=font18, fill=0)
    # draw.line((10, 130, 500, 80), fill = 0) #horizontal
    draw.line((0, 148, 642, 148), fill=0)
    Display.paste(logo, (650, 0))

    # Body
    draw.text((5, 153), 'Assignments:', font=title, fill=0)
    draw.text((10, 190), get_assignments(), font=medium, fill=0)
    #draw.text((10, 190), '- Content: Chapter 1 - 4', font=medium, fill=0)
    #draw.text((10, 215), '- Date: ' + datetime.date.today().isoformat(), font=medium, fill=0)

    # Footer
    file = open('weather.env.txt', 'r')
    API_key = file.read()
    file.close()
    url = "https://api.openweathermap.org/data/2.5/weather?appid=" + \
        API_key + "&zip=35632&units=imperial"
    temp = requests.get(url).json()['main']['temp']

    draw.line((0, 400, 800, 400), fill=0)
    draw.text((5, 410), 'Max occupancy: 10 people', font=title, fill=0)
    draw.text((5, 440), 'Temperature: ' + str(temp) +
              u'\u00b0F', font=title, fill=0)
    draw.text((280, 453), '(Temperature updated at ' +
              time.strftime('%H:%M') + ')', font=font18, fill=0)
    draw.text((595, 438), "Scan QR for \ncourse info ->", font=font18, fill=0)
    Display.paste(qr, (710, 390))

    epd.display(epd.getbuffer(Display))
    time.sleep(2)

    # logging.info("Clear...")
    # epd.init()
    # epd.Clear()

    logging.info("Go to sleep...")
    epd.sleep()
    time.sleep(3)

    epd.Dev_exit()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
