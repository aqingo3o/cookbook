# Editting and Compiling .tex in Local Environment
(( 雖然是 latex 教學但竟然是用 markdown 寫的！ 叛徒！ )) 

真的是被 Overleaf 的介面醜到了，如果不用共編的話，在本地編輯才是最理想的吧！

以下部署方式在 feifei (macOS Sequoia) 上成功過，但不確定適用範圍到哪兒。    

雖然常說有不懂的就推 issue 吧，但這邊我真的有點無能為力...  
有不懂的請使用萬能的網路吧!

這邊分成了:  
1. Local LaTeX Compiler
2. Editting LaTeX (.tex) in vscode

## 前情提要
根據不可靠來源，LaTeX 的 local compiler 有 `MacTex` 和 `TexLive`。在 mac 上，呼叫編譯器的手段可以透過 `Texshop` 或是 `vscode + Latex Workshop` (<- an vscode extension)。  

流程像是這樣的:  
<mark><strong>Texshop</strong></mark> or <mark><strong>vscode + Latex Workshop</strong></mark>  
&darr;  
<mark>Call the Compiler</mark>   
&darr;  
<mark><strong>MacTex</strong></mark> or <mark><strong>Tex Live</strong></mark>  
&darr;  
<mark>PDF #</mark>  

## Local LaTeX Compiler
不管怎樣，都會需要**編譯器**本體，這邊採用的範例是 **MacTex**。  
到 [MacTex 官網](https://www.tug.org/mactex/mactex-download.html) 下載 **MacTex.pkg**，下載成功之後，進行以下兩個檢查已確認安裝。（或是可以在下載之前先看看電腦對這倆指令有沒有反應，搞不好有預先安裝呢？）  
1. 確認此目錄存在
```Shell
cd /usr/local/texlive
```
**/texlive** 這個資料夾就是下載 MacTex 會自動附上的，超肥。  
cd 進去應該可以看見 **/2025** 和 **/texmf-local** 這倆東西，這邊就是本地編譯器的本體所在，不可以刪掉喔。 

2. 檢查編譯器路徑
```Shell
which xelatex
>> /Library/TeX/texbin/xelatex
which pdflatex
>> /Library/TeX/texbin/pdflatex
```
注意，`/Library/TeX/texbin/` 這個路徑下本身不含 compiler，這是一個 symlink，compiler 的本體是在 `/usr/local/texlive` 這邊。  

我也不知道為什麼會這樣，但是你試試看這個，像這樣「->」的輸出就代表該目錄指向另一個目錄。  
```Shell
ls -l /Library/TeX/texbin/        
>> lrwxr-xr-x  1 root  wheel  39 Jul 27  2025 /Library/TeX/texbin/ -> ../.DefaultTeX/Contents/Programs/texbin
```
有點複雜但沒關係，不用管他也可以完成 Latex 的部署。  

接下來，需要把 `/Library/TeX/texbin` 加到環境變數(PATH) 中。  
使用這個終端命令，以 nano (或其他的文字編輯器，但在這個場合我喜歡 nano) 打開 zsh 設定檔。
```Shell
nano ~/.zshrc
```
進到設定檔之後，在裡面寫入這行。
```Shell
export PATH="/Library/TeX/texbin:$PATH"
```
接著按 <kbd>ctrl</kbd> + O 寫入（存檔的概念），<kbd>Enter</kbd> 確認寫入，然後按 <kbd>ctrl</kbd> + X 退出 nano。  
以上有關 nano 操作都可以在 nano 介面的下方找到。  
最後，在終端輸入這個更新 zsh 設定檔，使變更失效。
```Shell
source ~/.zshrc
```

當安裝完成之後，我們可以先建立一個 .tex 檔以進行接下來的編譯測試。  
用下面這個終端指令、vscode或是任何已知方式建立一個 .tex 檔。   
```Shell
touch ~/text.tex
```
接著，在 `text.tex` 中寫入這些內容。  
```LaTeX
\documentclass{article}
\usepackage{xeCJK}
\setCJKmainfont{PingFang TC}

\begin{document}
使用這個酷方程，在量物獲得些許分數。
\[
i\hbar \frac{\partial \Psi}{\partial t}=\frac{-\hbar^2}{2m} \frac{\partial ^2 \Psi}{\partial x^2}+V(x)
\]
\end{document}
```
編譯的方法就是在終端輸入這個：
```
xelatex ~/text.tex
```
`xelatex` 就是指定使用編譯器種類，整個指令的概念類似於在終端使用 `python3 testtt.py` 可以執行該 .py 檔。  
應該會在與 `text.tex` 相同的目錄之下出現 `text.pdf`，點進去看看是不是如你所願！  

p.s.  
LaTeX 的編譯起有很多變種，像是上面用的 xelatex 就是一種，還有 pdflatex, luna latex...等等，每種的「開頭語法」會略有不同。  
比如說上面那個 test.tex 用 pdflatex 編譯的話， `\setCJKmainfont{PingFang TC}` 這行沒辦法正確編譯，會直接顯示在成品 pdf 裡面。  

因為根據不可靠來源，**xelatex** 在中文（中日韓）字型的表現比 pdflatex 好，所以在接下來的設定中，我會在 vscode 中將 **xelatex** 設定成預設編譯器。  

## Editting LaTeX (.tex) in vscode
因為 vscode 是窩用得順手的文字編輯器，所以提供了這個教程。  

0. 確定 vscode存在並且可用。  
1. 打開 vscode，在左邊工具欄點 <kbd>Extensions</kbd>，或是 <kbd>Shift</kbd> + <kbd>cmd</kbd> + X。

2. 在這裡搜尋 `LaTeX Workshop` 並下載（要選作者是 James Yu 的那款）。
3. 截至現在，可以先進行一些簡單的嘗試。在 vscode 中開啟剛剛做的那個 test.tex，並按畫面右上角的綠色箭頭進行編譯。
4. 可能會編譯失敗，並且出現一坨紅字，以及產生一桶副檔名怪異的檔案。  
如果出現這些問題請不要擔心，這些可以通過修改 vscode 的設定檔(setting.json) 解決。  
5. 編寫 vscode 的設定檔(setting.json)  
承第4步，直接裝直接用的話很大機率會出現編譯錯誤，原因很可能是是因為 LaTeX Workshop 的預設編譯器不是 xelatex。  
6. 在 vscode 左下角的那個齒輪中找到 **Setting** 並打開（或是在英文輸入法下按 <kbd>cmd</kbd> + , 快捷地打開 setting ）  
7. 在上方 search settings 的欄位中輸入 `latex-workshop.latex.toolchain`，並在下方找到任意一個 `Edit in setting.json`，點它。  
（其實用任意方法找到並打開 vscode 的 setting.json 都行，這邊只是提供其中一個方法。）
8. 點進去之後，會看到一個用 javascript 寫的東東，像是這樣（大致），小心不要動到他的一堆大括號和縮排。
```js
{
    "workbench.colorTheme": "Default Dark+",
    "editor.tokenColorCustomizations":{
        "comments": "#ff5858",
        "functions": "#dba0db",
        "keywords": "#fcc642",
        "strings": "#a5cf27",
        "variables": "#ffffff",
        "numbers": "#cee6fe"
    },
    "python.defaultInterpreterPath": "/Users/aqing/miniconda3_arm/envs/eltha_py310/bin/python",
    "workbench.settings.applyToAllProfiles": [],
    "github.copilot.nextEditSuggestions.enabled": true,
}
```
應該可以看到設定檔裡面已經有一些 LaTeX 相關的內容， 不裹因為的不順手，所以在階下來的不揍中我會將他們都副蓋掉。  

這邊分享我在設定檔裡寫了什麼，當然您也可以上網找別人寫的設定檔或是 AI 生成一個設定檔。  
請將雙引號開頭的東西 (`"latex-workshop.intellisense.biblatexJSON.replace"`, `"latex-workshop.intellisense.package.enabled"` 這類的) 與既有的雙引號 (`"python.defaultInterpreterPath"`, `"github.copilot.nextEditSuggestions.enabled"` 等等) 對齊。
```js
    "latex-workshop.intellisense.biblatexJSON.replace": {},
    "latex-workshop.intellisense.package.enabled": true,
    "latex-workshop.latex.tools": [
        {
            "name": "xelatex",
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOCFILE%"
            ]
        },
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOCFILE%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "xeLaTeX",
            "tools": ["xelatex"]
        },
        {
            "name": "PDFLaTeX",
            "tools": ["pdflatex"]
        },
        {
            "name": "LaTeXmk",
            "tools": ["latexmk"]
        },
        {
            "name": "xelatex -> bibtex -> xelatex*2",
            "tools": [
                "xelatex",
                "bibtex",
                "xelatex",
                "xelatex"
            ]
        },
        {
            "name": "pdflatex -> bibtex -> pdflatex * 2",
            "tools": [
                "pdflatex",
                "bibtex",
                "pdflatex",
                "pdflatex"
            ]
        }
    ],
    "latex-workshop.latex.clean.fileTypes": [
        "*.aux",
        "*.bbl",
        "*.blg",
        "*.idx",
        "*.ind",
        "*.lof",
        "*.lot",
        "*.out",
        "*.toc",
        "*.acn",
        "*.acr",
        "*.alg",
        "*.glg",
        "*.glo",
        "*.gls",
        "*.ist",
        "*.fls",
        "*.log",
        "*.fdb_latexmk"
    ],
    "latex-workshop.latex.autoClean.run": "onFailed",
    "latex-workshop.latex.recipe.default": "xelatex",
    "latex-workshop.latex.autoBuild.run": "onFileChange",
    "latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click",
    "editor.unicodeHighlight.allowedLocales": {
        "zh-hans": false,
        "zh-hant": true
    },
    "[latex]": {
        "editor.defaultFormatter": "James-Yu.latex-workshop"
    }
```
### 我提供的設定檔的一些解釋
有些沒寫就是我不知道哈哈。  

- "latex-workshop.intellisense.package.enabled: true"   
 intelliSense 會自動補全 LaTeX 套件和命令，啊 true 就是允許他自動提示 \usepackage{} 或 command。

- "latex-workshop.latex.tools:[...]"  
    工具，定義「可以被執行的命令」。  
    這裡的東西應該是裝了 LaTeX Workshop 之後就會自動出現在 setting.json 了，可以自己更改的地方只有 `"name": "the tool's name"` 這些部分。  
    概念就是，有一個工具叫 **the tool's name-1**，使用這個工具的話實際上是在執行名為 **the command1**  的命令。 
    ```js
    "latex-workshop.latex.tools": [
        {
            "name": "the tool's name-1",
            "command": "the command1",
            "args": [ arguments ]
        },
        {
            "name": "the tool's name-2",
            "command": "the command2",
            "args": [ arguments ]
        }
    ]
    ```

- "latex-workshop.latex.recipes:[...]"  
    食譜，它定義的是要用哪些 tool 以及列出的順序。所以這邊的 `"tools": []` 裡面填入的工具名稱要是在 `latex-workshop.latex.tools` 那邊定義過的 （因為有可能會自己修改 tool 的名字，那邊改了這邊也要改。）  
    這邊的 name 就比較隨便了，隨便取，自己認得出來就好。  
    ```js
    "latex-workshop.latex.recipes": [
        {
            "name": "tool_ONE",
            "tools": ["the tool's name-1"]
        },
        {
            "name": "tool_TWO",
            "tools": ["the tool's name-2"]
        }
    ]
    ```

- "latex-workshop.latex.recipe.default": "xelatex"  
    設定預設的編譯器為 `xelatex`，這樣按右上角的綠色小箭頭就會直接用 `xelatex` 進行編譯。當然您可以設定成任何用的習慣的東西！不過這邊設定的編譯器名稱必須在 `latex-workshop.latex.recipes` 那邊存在。

- "latex-workshop.latex.clean.fileTypes:[...]"  
    在嘗試的環節，可以已經發現在編譯 .tex 的時候會連帶的產生一桶副檔名怪異的檔案，這行的功能就是自動清理這些編譯垃圾。在清楚情況的前提下，您可以增減這邊的設定讓自己的工作環境變得更加舒適。  

- "latex-workshop.latex.autoClean.run": "onFailed"  
    如同你所讀到的字面意思，這行的設定就是當編譯失敗時會自動清理上面那些檔案。  
    也可以寫 "onBuilt"(編譯成功時清理), 或是 "never"(不清理，但就是會有一坨大便出現在資料夾中)。

- "latex-workshop.latex.autoBuild.run": "onFileChange"  
    這行是用來控制自動編譯 pdf 的，這邊填 "onFileChange" 代表在每次存檔時，自動編譯生成 pdf。  
    也可以填 "never"（存檔時不會自動編譯）。

- "latex-workshop.view.pdf.viewer": "tab"  
    在 vscode 編輯 .tex 檔時，可以在另個視窗(tab)同時查看編譯後的 pdf。  
    也可以寫 "external"(用 macPreview 開啟), "browser"(以瀏覽器開啟) 之類的，但我覺得 tab 會最方便。   

- "latex-workshop.view.pdf.internal.synctex.keybinding": "double-click"  
    如同你所讀到的字面意思，這行的設定就是讓你可以 double click on pdf，看 pdf 的哪行對應到 .tex 檔裡的哪行。  

- "editor.unicodeHighlight.allowedLocales" 
    簡單來說，這個設定是讓 vscode 不要警告中文字符
    - unicodeHighlight 會檢測文件裡的特殊字元，例如 emoji、希臘字母、全形字、非本地語言字元）。
    - allowedLocales 允許哪些語言不被標記為「異常字元」。  
    在我的例子： "zh-hans": false 代表簡體中文會被標紅或標記; "zh-hant": true 則是代表繁體中文不會被標紅或標記。（真的很羨慕母語是英文的人）  

- "[latex]": {"editor.defaultFormatter": "James-Yu.latex-workshop"}  
    - [latex] 表示只對 **.tex** 檔生效。  
    - editor.defaultFormatter 是用來指定 vscode 使用哪個工具自動格式化檔案，這邊填 "James-Yu.latex-workshop"，因為這就是 LaTeX Workshop 提供的格式化工具。
