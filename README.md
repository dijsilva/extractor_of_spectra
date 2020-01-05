<h1>Spectra Extractor built using Python 3.7</h1>


<h2>Overview</h2>
This is a algorithm with GUI for specta extraction obtained by TEXAS (TIDA) and Eco-ATR (Bruker) spectrometers. This algorithm was created using Python 3.7 and the GUI built using Tkinter library.

<h2>How to use</h2>
For use, download the file of executable (available for Windows and Ubuntu) or clone this respository and run the main.py script. Make sure that all dependencies were installed.

When the window of GUI open, choose the type of file that the algorithm (required) should read and select which files will be read. Next step is select the name and path of output file. This algorithm can save the output in .xslx or .csv formats.

There are two options that can chosen by user: the creation of a log file (a file that contains informations about the process, like time of execution and/or error that can be occurred) and to use comma as decimal separator (default is point).

<img align="center" width="800" src="https://github.com/dijsilva/extractor_of_spectra/blob/master/images_readme/initial.png">

After select the files to be read and the output file, just click in RUN and wait process to complete. The progress bar will be complete and the extraction of spectra is done.

<img align="center" width="800" src="https://github.com/dijsilva/extractor_of_spectra/blob/master/images_readme/end.png">