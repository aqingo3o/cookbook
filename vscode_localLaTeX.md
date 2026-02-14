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
<p style="color: #000000; background-color: #cceeff;">Call Compiler</p>   
&darr;
<p style="color: #000000; background-color: #cceeff;"><strong>MacTex</strong> or <strong>Tex Live</strong> </p>  
&darr;
<p style="color: #333; background-color: #cceeff;">PDF #</p>  


## Local LaTeX Compiler
不管怎樣，都會需要**編譯器**本體，這邊採用的範例是 **MacTex**。  
