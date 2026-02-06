# Formatting Skill
內容不好說但我的 README 要美美的啊
## Pretty Block in Markdown
就是像這樣，大於符號加裡面帶驚嘆號的中括號。這個美麗格式只在 github 生效。  
```
> [!NOTE]
> This is note
```
將 **NOTE** 換成其他單字（要全大寫）就可以獲得顏色不同的框框。  
Demo:  
> [!NOTE]
> This is note

> [!TIP]
> This is TIP

> [!IMPORTANT]
> This is important

> [!WARNING]
> This is warning

> [!CAUTION]
> This is caution

## HTML + md
### 標題與置中
```
<div align="center"> <h1>標題置中</h1> </div>
```
還可以加上副標題，包在 `<div> </div>` 裡面的都會一起置中。
```
<div align="center"> <h1>標題置中</h1> <p>副標題</p> </div>
```
Demo:  
<div align="center"> <h1>標題置中</h1> <p>副標題</p></div>  

### 按鈕圖樣
```
<kbd>長得像是按扭的東西</kbd>
```
Demo:  
<kbd>長得像是按扭的東西</kbd>

### 折疊內容
```
<details> 
  
被折疊的內容
</details>
```
或是更近一步，加上折疊的標籤。
```
<details> 
<summary>點擊此處查看被折疊的內容</summary> 被折疊的內容
</details> 
```
Demo:  
<details> 
<summary>點擊此處查看被折疊的內容</summary> 被折疊的內容
</details> 
還可以加上假按鈕 ;P  
<details> 
<summary>點擊 <kbd>此處</kbd> 查看被折疊的內容</summary> 超好笑按鈕並不是特殊功能，只是長得像而已？
</details> 
