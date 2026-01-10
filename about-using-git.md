# git and Github
一些相關的東西，雖然老子最早用的是純粹醜醜的 git branch  
但 Github/vscode 實在美麗...

## In vscode
紅魚會用的東西，從 vscode 直接推東西上 Github  

### steps
在 vscode 裡總而言之找到這個按鈕  
**[ Clone Github Repository ]**  
憑直觀操作，會在本機獲得一個與 repo 同名的資料夾  

在 vscode 中打開這個資料夾，然後該改動該新增該怎樣怎樣。  

完成一次 commit 需要的操作之後，在左邊工具列選中
**[ Source Control ]**  
的符號，就是很 git 的一個樹狀的東西。

在 change 的部分把所以東西都 **[ add to change ]**  
代表說，累計的改動有這麼多，這次像要 commit 其中哪些  

然後選擇按鈕  
**[ commit & push ]**  
輸入 commit message 然後按右下的藍色 **[ commit ]** 按鈕   

完成！

## FAQ
### Unidentified
第一次在本地使用 git 系列工具，可能在 **[ commit & push ]** 這步會遇到**個人資料還未完善**的問題。  
我們將在終端解決這些障礙。即使估以很香但終端一直有種原始的美感...  

先進到剛從 github 抓下來的那個與 repo 同名的本地資料夾中
```
cd ~/(PATHtoREPO)
```

以下是 git 系列的命令  
```
git config user.name "Liv"
git config user.email "universe5961@gmail.com"
```
使用與 github primary email 一樣的郵箱地址可以讓你的 github 頭像出現在 vscode 的 graph 中  
git 認的是**郵件地址**，而不是顯示的名字。

如果你很確定一生就叫這名字了，可以用含有 global 的指令  
（但我才不要）  
```
git config --global user.name "Liv"
git config --global user.email "universe5961@gmail.com"
```
題外話，這些資料會存在 `.git/congig` 中  
可以這樣查看（或修改）
```
cd ~/(PATHtoREPO)
ls -a  # show hidden folders
nano .git/config
```

### Didn't see change on Github?
就是 commit 成功，但沒有 push 成功  

事情是這樣的：  
本機的主分支叫做 main  
Github 上的主分支叫做 original/main
commit 是 commit 到 main, push 是推上 Github  
大概是這樣

在 vscode 左邊的 **[ Source Control ]** 中找到 **[ Sync Change ]**  
點它  

如果還不惜的話應該是 Github 的 original/main 和本地的 main 有前有後的  
常見在多人共用的 repo 上  
解法就是先把 Github 上的東西 pull 下來，再將已經 commit 到 main 的東西 push 上去。  

一樣使用原始力量 terminal  
先把 GitHub 上的 commit 接回來
```
cd ~/(PATHtoREPO)
git pull --rebase origin main
```
應該會顯示 Successfully rebased and updated refs/heads/main  

然後再把本地 main 的東西推上去
```
git push origin main
```
#### still not clear
這邊好像是遇到衝突的時候應該決定 merge or rebase  
我並不是很清楚，但總之就是小心操作啦...
