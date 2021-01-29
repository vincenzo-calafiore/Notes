# CODECs

The main purpose of a compression is to stream the video into a device (cloud streaming as such). It is not possible to transmit the original file because it contains too much information.



Video compression minimize redundancy in the video data in different ways.

Spatial Compression (Intraframe): is applied only to individual frames (jpg). more the image is complicated more artefacts will have.



Temporal Compression (Interframe): (mpeg)  basically frames that stays the same for more time will be compressed, those who change often are less compress. There are 3 types all frames

I frames: decides the important frames

B frames: skipped frames

P frames: prediction frames



A CODEC is an encoding tool that process video and stores the bytes stream. THey are basically algorithms that resize the audio and video.

Bitrate is the amount of data loaded every second.

Video compression is a balance between quality and file size.

Youtube and other streaming platforms have different types of compression.



Codecs algorithms like H264 needs a container to store it (like MP4, MOV, AVI). they are useful to stream the video on different devices. 



## Resume

RAW (High Hand Files)

Film -> Colouring/Editing

BRAW, R3D



INTRAFRAME

Intermediate codecs used for Editing

Codecs: DNXHR, DNXHD ----> Container: MXF

Codecs: ProRes, CineForm -----> Container: MOV

(the best solution for 3d is to compress per frame so to have less copression per frame)



INTERFRAME

Codecs :

H264-> UP to HD

H265 -> HD and UHD 4K

Containers -> Delivery -> MP4, JPG

Platform compression -> YouTube

(Keeps all the information in I frames)



For 3D as an export format is better **EXR** , **EXR MULTILAYER** 




