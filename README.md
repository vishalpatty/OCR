# OCR
Built an OCR using Lenet

<B>Dataset Generation:</B>
<P>The data was generated using the various Scanned PDF documents available to me.
The document has one single image per page which contains all the information regarding content.
At first, Extraction of images from the document was done.
Which was followed by the binarization of image.
After which, OpenCV was used to extract the images of various characters(including punctuations) using connected components.
THe data was collected in 14 various Fonts.

<B>Data Engineering:</B>
<P>After getting the small images of characters, the main challenge was to resize all the images in a single dimension, without loosing the pixel information.
Used projections to predict the area of characters and cut the characters accordingly to resize it.

<B>Training and Testing:</B>
<P>Model was trained using Lenet Adam Optimization Technique.

<B>Results:</B>
<P>The accuracy was found to be 98.55%

<B>Real-time Testing:</B>
<P>A PDF document was passed and the letters were extracted and labelled accordingly as per prediction. The pitching of word and Character spaces were used to determine a word.
