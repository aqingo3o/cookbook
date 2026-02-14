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
1.
```
cd /usr/local/texlive
```
確認這個資料夾存在！ **/texlive** 這個資料夾就是下載 MacTex 會自動附上的，超肥。  
cd 進去應該可以看見 **/2025** 和 **/texmf-local** 這倆東西，這邊就是本地編譯器的本體所在，不可以刪掉喔。  
2.
```
which xelatex
>> /Library/TeX/texbin/xelatex
which pdflatex
>> /Library/TeX/texbin/pdflatex
```
注意，/Library/TeX/texbin/ 這個路徑下本身不含 compiler，這是一個 symlink，compiler 的本體是在 /usr/local/texlive 這邊。  
我也不知道為什麼會這樣，但是你試試看這個，像這樣「->」的輸出就代表該目錄指向另一個目錄。  
```
ls -l /Library/TeX/texbin/        
>> lrwxr-xr-x  1 root  wheel  39 Jul 27  2025 /Library/TeX/texbin/ -> ../.DefaultTeX/Contents/Programs/texbin
```
有點複雜但沒關係，不用管他也可以完成 Latex 的部署。

當安裝完成之後，可以用終端指令進行對 .tex 檔的編譯。  
