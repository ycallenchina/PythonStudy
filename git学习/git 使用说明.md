# git 使用说明

git init `初始化git 创建.git文件`

git add 文件名`缓冲区加载`

git log `查看git 缓冲区目录`

git commit 文件名 `确认git追踪`

git commit -m"标注" `确认git追踪`

git diff 文件名 文件名 `对比git 内容`

git diff staged `对比 缓冲区 和git 更新的对比`

git status `查看目前git状态 branch add commit`

# github 使用说明

**加载github路径**
    git remote add origin git文件地址  `加载文件地址`
    git remote -v `查看所有已加载的文件地址`

**上传本地git log的更新文件**
    git push -u origin master `上传git`


**克隆文件**
    git clone git文件地址 `克隆下载文件`
    两个本人实例地址
    https://github.com/ycallenchina/PyTry.git
    https://github.com/ycallenchina/PythonStudy.git

**分支branch**
    git branch `查询`
    git branch 分支名 `创立分支`
    git checkout -b branch1 `创建并切换至新分支`
    git checkout branch1 `切换分支`

**合并分支**
    git merge 分支名 分支名 `若合并冲突,就先去合并文件里面修改好了后,在commit下`

**同步到本地**
	git pull origin master

**删除文件**
    通过git的方式删除
    首先我们将整个仓库clone到本地
    git clone https://github.com/***

    在clone下来的本地仓库里初始化
    git init

    选择删除文件或者文件夹
    git rm FILE  ***删除文件***
    git rm -r ***删除文件夹***

    当然这里也可以有对应的增加操作（具体参考另一篇博客）

    提交上述操作
    git commit -m "log message"

    推送所有文件到远程仓库
    git push origin master
