---
title: "Directional bike lights"
date: 2023-10-04T21:31:30+02:00
slug: bike
draft: true
image: /images/IMG_2445.jpg
---


If you are a biker, you may have faced the challenge of indicating the direction you want to turn in poor light conditions. I had experienced this situation often while biking, especially during wintertime. Because of that, I decided to develop, from scratch, a set of directional lights for my own bicycle. To develop this project, I combined an Arduino micro, RGB-LED stripe and other electronic components. My main idea was to use the Arduino to read and interpret the signal sent from buttons mounted on the handlebar and control the RGB-LED stripe (e.g. colour, blink frequency, intensity, etc). Below is a picture of the initial bench test I did while prototyping the electronics and developing the Arduino code.


{{< img src="/images/bench.jpg" alt="" width="70% q75" >}}


When the software and the electronics were ready, I started building the hardware and the housing for the electronics. For housing for the RGB stripes, I used PVC tubes for electrical installations. I made some cuts to the tubes to make the RGB stripe visible and then coated the external and internal parts of the tube with black and white paint. The building result can be seen in the picture below.


{{< img src="/images/lights.jpg" alt="" width="100% q75" >}}


I used a multi-purpose plastic box to house the Arduino and the additional electronic board. I am using this additional board to interface the Arduino and the other components (push buttons and RGB-LED stripes). The board receives the input signal and translates it into a signal that can be understood by the Arduino; it also gets the Arduino response and sends it to the RGB-LED stripes. The picture below shows the assembly of the additional board (fig A) and the mounting of the different components within the housing box (fig B, C). The light activation and switching between different modes is done by pressing the push buttons I installed on the handlebar (fig D). 


{{< img src="/images/components.jpg" alt="" width="100% q75" >}}


Finally, when all the parts were ready, it was time to mount them on the bike. The first test after the mounting is visible in the heading picture and in the following short video. Soon, I will build the rear light set.

{{< youtube glTSB_6MoPY >}}
