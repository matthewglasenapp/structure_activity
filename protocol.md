# Structure Lab Exercise

## Part 1: Setup
Create a new directory (folder) on your desktop and name it “structure_activity”. Please use the underscore, do not include any spaces. 

Download STRUCTURE (Pritchard et al., 2000) from the following url: https://web.stanford.edu/group/pritchardlab/structure_software/release_versions/v2.3.4/html/structure.html 

Try downloading the package with the graphical front end. If this works for you and you can open the STRUCTURE application, then you can stop reading this document and go to the lab activity document. 

If you have a newer computer, you likely won't be able to install the graphics-based version of the program successfully. If this is the case, please download the package without front end. Rename the downloaded folder as "structure" and move it inside of the “structure_activity” folder that you created earlier on your desktop. Ensure that the program was installed correctly by opening the terminal app (Mac) or Cygwin (Windows) and using the cd and ls commands to change directories until you're in the directory containing the structure program. The cd command stands for change directory and changes your working directory. The ls command lists all directories and files in the current working directory. 

```
cd ~/desktop/structure_activity/structure/
ls
```

If you are a Windows user and do not have Cygwin installed, refer to the installing_cygwin_onlyWindowsUsers_v3.pdf file. 

To run structure, type: 

```
./structure
```

and press enter. You should see the following message printed to your screen:

----------------------------------------------------
STRUCTURE by Pritchard, Stephens and Donnelly (2000)
     and Falush, Stephens and Pritchard (2003)
       Code by Pritchard, Falush and Hubisz
             Version 2.3.4 (Jul 2012)
----------------------------------------------------

If you see an error message below this message, don't worry. It was because we did not give the structure program an input file. That is okay, we just wanted to see that the program installed properly. 

If you get a security message, such as "cannot be opened because the developer cannot be verified," you will have to go into your security settings and allow the package/file to be opened. For mac users, this can be done by going to System Preferences -> Security & Privacy.

Download turtles.txt from Canvas and place this file inside the directory containing the structure program. 

While in the structure directory, open the “mainparams” file with a text editor. Find the following line: 

```
#define MARKERNAMES  1  // (B) data file contains row of marker names
```

Change the 1 to a 0 and save the file! Our data file (turtles.txt) does not have a header line, so we must tell structure this.

While in the structure directory, open the “extraparams” file with a text editor. Find the following line: 

```
#define POPALPHAS   0 // (B) Individual alpha for each population
```

Change the 0 to a 1 and save the file! Our data file (turtles.txt) does not have a header line, so we must tell structure this. We want ALPHA to vary between populations, since we believe that each populations is likely to mix with other populations to a different degree.

Download distruct (https://rosenberglab.stanford.edu/distructDownload.html). This is the program that visualizes the output of structure analyses in nice color figures. Rename the downloaded folder as “distruct" and place it within the structure_activity folder on your desktop. Navigate to the distruct directory on the command line interface.

```
cd desktop/structure_activity/distruct/
ls
```

You will need to add executable permissions using the command: 

```
chmod +x [insert name of the distruct executable file]
```

Trying running distruct by typing:

```
./[insert name of the distruct executable file]
```

Note: Do not include the brackets [ ] in your command!

If you have a newer Mac, you will likely get the following error message: 

```
Bad CPU type in executable
```

You may need to try installing more than one version. The executable in the distruct 1.1 download did not work for me. I had to download the 2016 distruct executable file and move it into the previously downloaded distruct folder.

Once the new executable is in the distruct folder, you should rename the executable as "distruct". You will again need to add executable permissions by typing: 

```
chmod +x distruct
```

Check that is installed properly by navigating to the folder containing the program and typing 

```
./distruct
```

Go to the distruct directory and delete all the files except for the drawparams file. These files are sample data that we do not need and might confuse us. You will need to create a new text file called "turtles.names" in the distruct directory with the following information:
1 Northern CA
2 San Bernardino and Monterey
3 Southern CA
4 San Joaquin
5 Santa Barbara

This is just the information on the number and name of the five pre-defined populations in the turtles.txt file. 

## Part 2: Analysis

We will now run structure and distruct to create structure plots for K=2,3,4,5,6. 

You can run structure on the turtle data with K=2 using the following command (make sure you are in the directory containing the structure executable):

```
cd ~/desktop/structure_activity/structure/
./structure -m mainparams -e extraparams -K 2 -L 6 -N 43 -i turtles.txt -o turtles_2.txt
```

The structure command line interface options can be found in the structure manual:
<img width="468" alt="image" src="https://user-images.githubusercontent.com/60276545/225783081-e5671280-e45b-49d8-a7bb-a9387b762112.png">

Running this code will create a file called turtles_2.txt_f with the results for k=2. Open this file with a text editor and look for the following line:

```
Estimated Ln Prob of Data: ____
```

This value represents the natural logarithm of the probability of the data given the model. We will compare these values from runs with different k values to determine the optimal K for our data.

To visualize the results, we will run the distruct program. To do so, you will need to cut two data matrices from the structure results file and paste them into new text files. The first matrix is the population Q-matrix and the second is the individual Q-matrix. 

From my k=2 run, the population Q-matrix was: 

```
  1:     0.119  0.881              23
  2:     0.190  0.810               2
  3:     0.984  0.016               6
  4:     0.958  0.042               9
  5:     0.883  0.117               3
```

You should cut and paste the population Q-matrix from your own results into a new text file called turtles_2.popq and save it within the folder containing the distruct executable. Do not include any headers in the file. 

From my k=2 run, the individual Q-matrix was:

```
 1 0001_Merce    (0)    4 :  0.965 0.035 
  2 0002_Merce    (0)    4 :  0.944 0.056 
  3 0227_Kern    (0)    4 :  0.964 0.036 
  4 0331_San_D    (0)    3 :  0.989 0.011 
  5 0669_SLO    (0)    1 :  0.436 0.564 
  6  0833_OR    (0)    1 :  0.014 0.986 
  7 1165_Trini    (0)    1 :  0.024 0.976 
  8 1698_Tular    (0)    4 :  0.974 0.026 
  9 1705_Tular   (16)    4 :  0.966 0.034 
 10 1734_Kern    (0)    4 :  0.960 0.040 
 11 1775_Fresn    (0)    4 :  0.946 0.054 
 12 1776_Fresn    (0)    4 :  0.963 0.037 
 13 1788_Mader    (0)    1 :  0.019 0.981 
 14 1925_San_D    (0)    3 :  0.986 0.014 
 15 1929_San_D    (0)    3 :  0.986 0.014 
 16 1933_Ventu    (0)    5 :  0.921 0.079 
 17 1955_BCN    (0)    3 :  0.989 0.011 
 18 1959_BCN    (0)    3 :  0.989 0.011 
 19  2178_SB    (0)    5 :  0.799 0.201 
 20  2185_SB    (0)    5 :  0.929 0.071 
 21 2239_Tuolo    (0)    1 :  0.017 0.983 
 22 2272_Yuba    (0)    1 :  0.019 0.981 
 23 2291_Shast    (0)    1 :  0.019 0.981 
 24  2293_NV    (0)    1 :  0.023 0.977 
 25 2311_Napa    (0)    1 :  0.022 0.978 
 26 2334_Trini   (16)    1 :  0.016 0.984 
 27 2337_Humbo    (0)    1 :  0.016 0.984 
 28 2375_Napa    (0)    1 :  0.455 0.545 
 29 2498_Monte    (0)    2 :  0.348 0.652 
 30 2938_Marip    (0)    1 :  0.538 0.462 
 31 2972_San_B    (0)    2 :  0.032 0.968 
 32 3253_Mader    (0)    1 :  0.033 0.967 
 33 3259_Mader   (16)    1 :  0.061 0.939 
 34 3275_San_B    (0)    3 :  0.963 0.037 
 35 3293_SLO    (0)    1 :  0.784 0.216 
 36  3305_WA    (0)    1 :  0.014 0.986 
 37 3358_Kern    (0)    4 :  0.943 0.057 
 38  3781_OR    (0)    1 :  0.026 0.974 
 39  3826_OR   (16)    1 :  0.015 0.985 
 40  3960_OR    (0)    1 :  0.019 0.981 
 41    74_WA   (33)    1 :  0.129 0.871 
 42    78_WA    (0)    1 :  0.025 0.975 
 43 SFRC4_Yuba   (16)    1 :  0.023 0.977 
```

You should cut and paste the individual Q-matrix from your results into a new text file called turtles_2.indivq and save it to the folder containing the distruct executable. Do not include any headers in the file. 

You can now run distruct with the following command (make sure you are in the directory containing the distruct executable): 

```
cd ~/desktop/structure_activity/distruct/
./distruct -K 2 -M 5 -N 43 -p turtles_2.popq -i turtles_2.indivq -b turtles.names -o turtles_2_figure
```

Find the turtles_2_figure file to see the final figure! Scroll down to the bottom of the file to see the figure. 

Wow, that was a lot of work! It would be frustrating to have to repeat that process manually for many different k values. Luckily, Matt has written a custom python script that will automate this entire process for you. All you have to do is download the create_structure_figures.py file and install python (https://www.python.org/downloads/).

First, download the create_structure_plots.py file from canvas and place it in the structure_activity folder on your desktop.

Navigate to the structure_activity directory on your desktop:

```
cd ~/desktop/structure_activity/
```

Run create_structure_plots.py with the following command:

```
python3 create_structure_plots.py
```

This program will run structure for k=2,3,4,5,6 and record the results in a directory called "structure_results." It will then use the structure results as input to distruct to visualize the results. Figures for k=2,3,4,5,6 will be placed in a directory called "structure_plots." Explore these directories and files!
