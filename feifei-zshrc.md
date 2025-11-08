# RT
放在 `~/.zshrc` 裡面的舒適設置  
哪天 feifei 爆炸了我還能用這些東西快速獲得設置好的電腦  
希望不要啦哈哈

## Switch `conda` in different arch
真的被 fortran 狠狠操了  
今天唯一的好事就是在 .zshrc 裡面加了這個:  
```
ARCH=$(uname -m)
if [ "$ARCH" = "arm64" ]; then
    CONDA_PATH="$HOME/miniconda3_arm"
else
    CONDA_PATH="$HOME/miniconda3_x86"
fi
# conda 裝好的時候會附的東西，稍微改一下路徑
__conda_setup="$("$CONDA_PATH/bin/conda" 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$CONDA_PATH/etc/profile.d/conda.sh" ]; then
        . "$CONDA_PATH/etc/profile.d/conda.sh"
    else
        export PATH="$CONDA_PATH/bin:$PATH"
    fi
fi
unset __conda_setup
```
這樣用不同架構的時候一樣打
```
conda activate
```
就可以召喚出當前架構對應的 conda 辣  
是的我有兩種 conda，因為我現在有點想要試試已經編譯成功的arm-64 pyradex 能不能用  
所以先這樣，就是跟大家分享一下  
>
## Terminal appearance
提示字元和使用者名稱的顏色改改指令，美麗的工作環境保護身心健康。  
也是在 .zshrc 裡面加這個  
```
autoload -U colors && colors
export PS1="%F{blue}%n@%m%f %~ %F{blue}$%f "
```
不排除任何人有更高級的美商，但依然提供湯底。

----
下次會寫 alias 切換架構
