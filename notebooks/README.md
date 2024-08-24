# Code Explaination

So don't mind my language i am not used to writing readme documents on my projects, i guess this would be great opportunity to learn that too. but till then try to fill my words and antisipate, what i mean by your own words.

On this notebook i have worked on Solar Radiation Measurement.

## Main

The main function is the central function that deines the paths to the data files which we have recived on the project challenge.
The main Function also loops over each region's data, performing the analysis using the evaluate_region function which is imported from the script folder.
On its evaluation it stores the average GHI(Global Horizontal Irradiance) from each region and identifies the region with the highest solar potential.

Then finally after evaluation and analysis it prints out the region with the highest solar potential, which is the key output of the analysis. It prints it on the console it doesnt plot it so make sure you check your output section or terminal.

## Output

The script will output the following:

- Plots showing daily average GHI trends for each region.
- A printed statement indicating the region with the highest average GHI, i.e., the best candidate for solar energy installations.
