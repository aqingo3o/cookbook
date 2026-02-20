# Formatting Skill
內容不好說但我的 README 要美美的啊
## Code Blocks in Markdown
眾所周知，一對模板字串(``)可以在 github 的 md 渲染中產生單字灰底的效果(i.e. `fromattingSkill.md`)，而把三個 template literals 算一片麵包做成的夾心則可以產生引用程式碼的效果，並且右邊還會出現可以單擊複製的按鈕。  
```
效果展示
import numpy as np
```
是非常之好用的功能。  
不過當你引用一大坨程式碼但沒有語法高亮的時候，是否會有面對一坨大便的感覺呢（抱歉這個人的中文有點退化了）  
現在有另一個超簡易超聰明感嘆科技發展有你真好的東西出現了！
只要在地衣片「吐司」的後面加上中間包的程式語言的種類，就可以自動產生語法高亮。
````
```python
import numpy as np
for i in range(10):
    print(i)
```

```shell
export PATH="/opt/homebrew/bin:$PATH"
alias casa=/Applications/CASA.app/Contents/MacOS/casa
nano ~/.zshrc
```
````
###### p.s. 雙層引用程式法就是把最外面那層「吐司」改成 4 個 template literals.  

用出來的話是像這樣
```python
import numpy as np
for i in range(10):
    print(i)
```

```shell
export PATH="/opt/homebrew/bin:$PATH"
alias casa=/Applications/CASA.app/Contents/MacOS/casa
nano ~/.zshrc
```
像是 `python`, `javascript`(can be shorted to `js`), `shell`(俗稱的一般終端命令), `json`(寫設定檔的時候用的一堆大括號語言)... 等等都可以喔。

## Pretty Blocks in Markdown
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

### Font color
(inline CSS) 但這東西好像在 github 渲不出來...?  
```
<p style="color:blue">Blue inline CSS font</p>
```
Demo:  
<p style="color:blue">Blue inline CSS font</p>
