# Manual to use this script
You need to clone the hwole **folder** to make everything work.  
Because `C++` may require a same named folder so the 編譯/上傳 of the `.ino` file can be 成功.  

應該連同資料夾一起抓下來，因為 c++ 的特性吧，總之 `.ino` 得要放在一個**與它同名的**資料夾裡面才能成功編譯/上傳  

## Introduction
實驗物理學的作業，一個可以判斷哪邊光亮就往哪邊走的小車，可以稱他為追光小車或是正趨光性小車。  
請用，我將像這個世界開源我的垃圾 :D

## In this folder
- `manual.md`: ur here :)   
- `2ldr_lightFollower.ino`: 應該灌到板子里的程式，已經測試過能相容的 Arduino 請參見**Arduino Board and IC**  
- `Circuit.png`: 電路圖，要接出東西最主要還是電路圖吧，使用了樸實無的麵包板，和我精湛（並無）的理線技術。

## Arduino board and IC
- Arduino UNO
- Arduuino nano
- Arduino nano every
- L298N

(Any Arduino of them and a L298N can work,  
I mean, just pick **one** Arduino board, you won't need three even if you plan to add 6 LDRs on the car.)
