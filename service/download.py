from config import FILE_PATH

import os
import re
import shutil

def get_all_files():
    files = os.listdir(FILE_PATH)
    return files

def is_git(url):
    re_git = re.compile(".*?github.com.*/(.*?).git")
    name = re.findall(re_git, url)
    if name != []:
        return name[0]
    return False

def is_compress_file(url): #git 发布的 压缩文件
    if url.startswith("https://github.com/") and \
        ( url.endswith(".zip") or url.endswith(".tar.gz")):
        return True
    return False


def zipFile(name):
    commad = 'zip -r ' + name +'.zip ' + name
    status = os.system(commad)
    if status is 0:
        shutil.rmtree(name)
        return True


def gitClone(url):
    name = is_git(url)
    os.chdir(FILE_PATH)
    if name:
        commad = "git clone " + url
        status = os.system(commad)
        if status is 0:
            statu = zipFile(name)
            if statu:
                return True
    elif is_compress_file(url):
        commad = "wget " + url
        status = os.system(commad)
        if status is 0:
            return True
if __name__ == '__main__':
    url = 'https://github.com/protocolbuffers/protobuf.git'
    url2 = 'https://github.com/EECS-PKU-XSB/Shared-learning-materials.git'
    url3 = 'https://github.com/geeeeeeeeek/electronic-wechat/releases/download/V2.0/linux-x64.tar.gz'
    #gitClone(url)
    print(is_compress_file(url3))
