import hashlib
import os
import zipfile
Asset = {"assets": {}}

def test_file_md5(file_path):
    test = hashlib.md5()
    if os.path.isfile(file_path):
        with open(file_path, "rb") as f:
            while True:
                data = f.read(8096)
                if not data:
                    break
                else:
                    test.update(data)
                    ret = test.hexdigest()
                    Asset["assets"][file_path] = {}
                    Asset["assets"][file_path]["md5"] = ret
                    Asset["assets"][file_path]["compressed"] = False
                    MyzipFile(os.path.abspath(file_path), os.path.abspath(file_path) + ".zip")

def test_dir_md5(file_path):
    test_abs_path = os.path.abspath(file_path)
    # print(test_abs_path)
    os.chdir(test_abs_path)
    for mfile in os.listdir(os.getcwd()):
        if os.path.isfile(mfile):
            test_file_md5(os.path.abspath(mfile))
        elif os.path.isdir(mfile):
            test_dir_md5(os.path.abspath(mfile))
        else:
            pass


def MyzipFile(file_path, des_file_path):
    zip = zipfile.ZipFile(des_file_path, "w", zipfile.ZIP_DEFLATED)
    # zip.write(file_path) 全压缩路径
    file_path = os.path.basename(file_path)  # 压缩路径只有当前文件
    zip.write(file_path)
    zip.close()
