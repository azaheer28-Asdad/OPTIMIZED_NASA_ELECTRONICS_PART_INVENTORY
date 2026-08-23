# **NOTE**:  

The follower names are simply different versions of the same project: NASA_PARTS_SOFTWARE, Electronic_Components_Inventory_NASA, Electronic Components Inventory NASA, NASA_INVENTORY_OPTIMIZED, Official-NASA-Part-Cataloging-System_NPCS, and OPTIMIZED_NASA_ELECTRONICS_PART_INVENTORY.   

 

Also, this project works without an API key but may not cover as many part labels. 

  

# Project Goal:  

The NASA Part Cataloging System is a project designed to simplify part cataloging. As a high school intern at NASA Goddard Space Flight Center, I was tasked with cataloging thousands of electronic components. The first thing I thought of was that I must create something to make my job a lot easier, and so NPCS were born. Even today, many people at NASA use this project because it saves a lot of time and money and lets engineers focus on engineering rather than finding parts. The goal was simple: since the parts did not have any bar codes, the computer would have to read the words off the label, transcribe them, and write them into a row of a spreadsheet.  

  

# Phase 1, Setup:  

The very first version of this project was a terminal prototype, and it was very limited in what it could do. I received a lot of encouragement from my mentor and other people, so I decided to pursue it. One of my mentors decided to set a list of requirements for me, so that I can make the best possible app. I know Python very well, and since it's such a simple and popular language, there should be plenty of libraries and resources available. I learned OpenCV, PaddleOCR, and more to get this project started.   

  

# Phase 2, Feature Implementation:  

As I received more feedback, I integrated more features. The first thing I did was get the basics down: OpenCV to capture and process the image, PaddleOCR to read the text, and Pandas to write it to the spreadsheet. I eventually settled on the pieces of information needed: box ID, part number, alternate part number, type, description, package (part size), date code, quantity, and, later, manufacturer. Each of these fields was a hurdle in and of itself. I got all the fields from the label except type, description, and package, so I need to find a way to get these pieces of information as well, and do it for free. I finally found a free API from Mouser Electronics, and using API calls, I was able to extract these last pieces of information. After that, it was up to me to make the user experience as good as possible. I added an auto-capture feature that requires the user to hold the part label still for a few seconds until it's stable enough, then OpenCV captures the photo. This solved the problem of blurry photos and made it a lot easier to take photos.  

  

# Phase 3, Key Challenges:  

One of the biggest challenges I faced was at the beginning, when I realized that all part labels look different. The manufacturer decides how the part label looks, and they may structure it differently from another manufacturer. And so, I didn't know how to associate the label and the value. For example, if I am trying to read the part number off a label, I would look for the word part number and read what it says right next to it, but computers don't work that way. I have come up with so many solutions, but only one of them really worked. The first solution I had was to draw imaginary lines between the label and the value, and since PaddleOCR draws bounding boxes around each word, I could just see which lines intersect with which boxes. This was perfect, except the labels are structured differently, and some may have the label above the value. Also, the bounding boxes weren't very consistent. So I decided to add a GUI. 

By implementing REGEX in the back-end, the computer could now sift through everything that looks like a part number and display the most likely option for each. Now the user can just click a button to select the correct part number, and if they find an error, they can simply edit that one character. The second-biggest problem was packaging the entire application into an .exe file. The problem was that PaddleOCR is a neural network, and for some reason, Pyinstaller was not picking up all the .dll files. So, I worked with Gemini to write a build script that would gather all the files and compile them so that Inno Setup could package them into a nice installer GUI. After about a week of trial and error, I finally got a perfect .exe setup file. Then I used virtual machines to test this software and ensure it works not only on my machine but on any Windows machine.  

 

# Conclusion: 

After spending a lot of time learning, building, and testing the code, I was finally able to create a working app that other people would use and benefit from. As for myself, I learned a lot of libraries and useful Python skills that I would not have otherwise learned, and most importantly, I lose my brain to solve difficult problems, and that's how people get smarter. 
