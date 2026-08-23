# NASA PART CATALOGING SYSTEM (NPCS)

This is an open-source application created by a high school NASA intern, designed to eliminate the need to manually enter part numbers and other words from a part label into a spreadsheet. This tool is intended to automate cataloging so people can focus on building circuits rather than spending hours looking for the parts. 

The program uses OpenCV to scan and process the part label, PaddleOCR to extract the text, built-in logic, Mouser's free API to extract information from the part number, and Tkinter to display everything. 

The program was intended to be used as fast as possible and to put the user's ease of use first. 

Please don't mind the outdated GUI. 

This is supposed to be a Windows-only application, but if you need it on Linux, you must run it from the terminal. If needed on a Mac, the graphics may not work, but can probably be run from an IDE/terminal (using the NPCS.py file instead). 

## How to Install

### The General Gist:

NO LIBRARIES NEED TO BE INSTALLED—Just use the Windows .exe file. Easy!

* Get a free API key from Mouser Electronics. (Has a limit of 1000 free scans per day)

* Save that key and title it exactly "MOUSER_API_KEY" (no quotes) as an environment variable through the terminal.

* Download the NPCS_setup.exe file and proceed with installation; please be patient, as things do load even without progress bars.

* The application should launch on its own; just be patient; it may take as long as a minute or two (with no loading screen). 

## How to Install, Specifics:

* [Click on this link](https://www.mouser.com/en/api-search/) and follow the instructions there, and copy your API key.

* This is highly secretive, so take the necessary precautions to keep it safe.

* Press the Windows key and type, ```CMD``` and then hit Enter. Use the following command to save it as an environment variable.

```

setx MOUSER_API_KEY "YOURAPIKEYGOESHEREINSIDETHEQUOTES"

```

Here is another example using a fake made-up API key (make sure you include the quotes):

```

setx MOUSER_API_KEY "ogaeoruegpoiuhp845hpgq9peiurbggfdfak"

```

* Close the terminal, go back to GitHub, and download the NPCS_setup.exe file from the releases tab on the right side. [Or click here if you can't find it](https://github.com/azaheer28-Asdad/Official-NASA-Part-Cataloging-System_NPCS/releases/tag/V7.1)

#### Warning

* I do not own an expensive Windows developer license, so you will have to trust the file either in your browser or in File Explorer before you are able to run it.

### How To Trust the File For Different Browsers:

* ### Google Chrome:

* Chrome will not flag the file, but Windows will. Go to File Explorer right after the file finishes the download, and right-click on the file, select "Properties," and under the "Security" section at the bottom, check the box that says "unblock" → apply → ok → double-click the file to launch it and wait. After installation, it will auto-launch; just give it 1 - 2 minutes, and it will be ready to go. (The first-time launch takes a bit longer.) 

* ### Microsoft Edge:
* NASA Personnel - please do not use Edge to download, as it may block the download.
* Edge will flag the file. It will say that you don't often install files from here or something like that. Hover over the file with the error (you just downloaded) → keep → click the down arrow next to the delete button. Keep Anyway → Click the file in the browser once to launch or, alternatively, double-click the file in File Explorer and wait. After installation, it will The first time, just give it 1 - 2 more seconds, and it will be ready to go. (The first-time launch takes a bit longer.)

 

* ### Mozilla Firefox:

* Same as Chrome.

## How to Use the Software:

* This is the fun part.

* After the live camera feed comes up, click the actual feed and then bring up the label for the camera.

* To take a photo, you can use both hands to hold the label, and it will automatically capture it when the image is still enough. Alternatively, press the space bar to take a photo and give it a couple of seconds to process. 

* Now you should see the GUI, and you want to click on the first time with the correct part number, unless it was clear enough that the software found it, and will auto-upload the one that it found, unless you click the "Edit" text box.

* If you click the "Edit" text box, it will auto-populate the last option given, unless you click the option that is closest to the actual part number and then click "Edit"—it will edit that option. 

* After clicking "Edit" if needed, press the Enter / Return key to register what you wrote; if you didn't, that's okay; it will auto-pull whatever is in the text box.

* You can also click "none," and it will leave that box of the spreadsheet blank.

* Finally, you can click the "Etch into Sheet" button to make a new entry, or you can click the "Save and quit" button to make an entry and kill the process gracefully.

* Alternatively, if you forget to press "save and quit," then you could also just close the camera window, and it will serve the same function.

* You will hear a nice sound if there are no errors.

* You will see a pop-up for sorting purposes. We are sorting them here at NASA by type and package. Please note that package data is not available for many of the scans; you could use an LLM at the end to fix this by uploading your .csv file and asking it to look up these parts and fill in the blanks.

* After quitting, you can find the .csv file under the new folder you created in the installation process, under your username, inside the Documents tab.

* Double-click the .csv to open it, and if you have Excel or another spreadsheet program, it will prompt you to format; click "NO." This will not remove the leading zeros. Also, if your spreadsheet program shows a different pop-up (like in LibreOffice Calc), make sure you click "separate by comma," not "separate by spaces."

*Please rename the spreadsheet before running the program again, unless you want all of your next scans to write to that file. 

## Warnings:

* Please double-check part numbers. PaddleOCR AI sometimes confuses characters, so skimming it isn't a bad idea.

* If you do not rename the spreadsheet, then your next entries will be appended to that spreadsheet. 

* Unfortunately, the API and the system part number decoder will not catch everything, and depending on where your parts are coming from, the level of success may vary (but only by a little bit; the algorithm is pretty foolproof, so that even if the part isn't in Mouser's inventory, it will try to decode the part number itself). I had to use a free API to make this more widely available, but paid-for ones like "Silicon Expert" are aggregators and will likely know every part.

* You can try using a different API, but I'm not sure what the format of those may be, so they probably won't work.

#### AI Transparency:

Google's Gemini was used to debug and write small portions of the code. 
