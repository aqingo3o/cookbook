# Edittina and Compiling .tex in Local Environment
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
<div style="color: #000000; background-color: #cceeff;"><strong>Texshop</strong> or <strong>vscode + Latex Workshop</strong> </div>
&darr;
<p style="color: #000000; background-color: #cceeff;">Call the Compiler</p>   
&darr;
<p style="color: #000000; background-color: #cceeff;"><strong>MacTex</strong> or <strong>Tex Live</strong> </p>  
&darr;
<p style="color: #333; background-color: #cceeff;">PDF #</p>  


## Local LaTeX Compiler
不管怎樣，都會需要**編譯器**本體，這邊採用的範例是 **MacTex**。  
到 [MacTex 官網](https://www.tug.org/mactex/mactex-download.html) 下載 **MacTex.pkg**，下載成功之後，進行以下兩個檢查已確認安裝。（或是可以在下載之前先看看電腦對這倆指令有沒有反應，搞不好有預先安裝呢？）  
1. 確認此目錄存在
```
cd /usr/local/texlive
```
**/texlive** 這個資料夾就是下載 MacTex 會自動附上的，超肥。  
cd 進去應該可以看見 **/2025** 和 **/texmf-local** 這倆東西，這邊就是本地編譯器的本體所在，不可以刪掉喔。 

2. 檢查編譯器路徑
```
which xelatex
>> /Library/TeX/texbin/xelatex
which pdflatex
>> /Library/TeX/texbin/pdflatex
```
注意，`/Library/TeX/texbin/` 這個路徑下本身不含 compiler，這是一個 symlink，compiler 的本體是在 `/usr/local/texlive` 這邊。  

我也不知道為什麼會這樣，但是你試試看這個，像這樣「->」的輸出就代表該目錄指向另一個目錄。  
```
ls -l /Library/TeX/texbin/        
>> lrwxr-xr-x  1 root  wheel  39 Jul 27  2025 /Library/TeX/texbin/ -> ../.DefaultTeX/Contents/Programs/texbin
```
有點複雜但沒關係，不用管他也可以完成 Latex 的部署。

當安裝完成之後，我們可以先建立一個 .tex 檔以進行接下來的編譯測試。  
用下面這個終端指令、vscode或是任何已知方式建立一個 .tex 檔。   
```
touch ~/text.tex
```
接著，在 `text.tex` 中寫入這些內容。  
```
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